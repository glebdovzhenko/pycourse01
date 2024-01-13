import sys
import os
import importlib
import unittest
from .jup import NotebookFinder

from jinja2 import Template


def setUpModule():
    sys.meta_path.append(NotebookFinder())


class TestStudentReport(unittest.TestCase):
    _report_name = ''
    _varlist = ()

    def __init__(self,
                 methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.longMessage = False

    @classmethod
    def setUpClass(cls):
        cls._report = importlib.import_module(cls._report_name)

    @property
    def report(self):
        return self._report.__dict__

    # strange name so that it always runs first
    def test0_variables(self):
        """
        Определены все переменные.
        """
        not_in_list = []
        for v_name in self._varlist:
            if v_name not in self.report:
                not_in_list.append(v_name)

        if not_in_list:
            self.assertIn(
                not_in_list[0], self.report,
                msg='Переменные %s не определены' % ', '.join(not_in_list)
            )


DEFAULT_TEMPLATE = os.path.join(
    os.path.dirname(__file__),
    '..',
    'templates',
    'report_template_2.html'
)


DEFAULT_REPORT = os.path.join(
    os.path.dirname(__file__),
    '..',
    'reports',
    'report.html'
)


class JinjaTestResult(unittest.TestResult):
    """
    TestCase header is class docstring.
    test name is method docstring.
    """
    (SUCCESS, FAILURE, ERROR, SKIP) = range(4)
    status_tags = ('success', 'danger', 'warning', 'info')

    def __init__(self, stream=None, descriptions=None, verbosity=None):
        super().__init__(stream, descriptions, verbosity)

        self._jinja_context = {
            'results': dict(),
            'tr_object': self,
            'summaries': dict()
        }
        self._jinja_template = None

        self._load_template()

    def add_test_result(self, test, result, msg='') -> None:
        cls_key = test.__doc__.replace('\n', '')
        case_key = test._testMethodDoc.replace('\n', '')
        if cls_key not in self._jinja_context['results'].keys():
            self._jinja_context['results'][cls_key] = dict()
            self._jinja_context['summaries'][cls_key] = ''
        self._jinja_context['results'][cls_key][case_key] = (result, msg)

    def addSuccess(self, test) -> None:
        self.add_test_result(test, self.SUCCESS)
        return super().addSuccess(test)

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        self.add_test_result(test, self.FAILURE, err[1])
        return super().addFailure(test, err)

    def addError(self, test, err) -> None:
        self.add_test_result(test, self.ERROR, err[1])
        return super().addError(test, err)

    def addSkip(self, test, reason) -> None:
        self.add_test_result(test, self.SKIP)
        return super().addSkip(test, reason)

    def generate_report(self, extra_context=dict(), report=None):
        for cls_key in self._jinja_context['results']:
            self._jinja_context['summaries'][cls_key] = all(
                (cs[0] == self.SUCCESS) for (_, cs) in self._jinja_context['results'][cls_key].items()
            )

        if report is None:
            with open(DEFAULT_REPORT, 'w') as f:
                f.write(
                    self._jinja_template.render(
                        **self._jinja_context,
                        **extra_context
                    )
                )
        else:
            raise NotImplementedError()

    def _load_template(self, template=None):
        if template is None:
            self._jinja_template = Template(
                open(DEFAULT_TEMPLATE, 'r').read()
            )
        else:
            raise NotImplementedError()


class JinjaTestRunner(unittest.TextTestRunner):
    resultclass = JinjaTestResult

    def __init__(self, **kwargs) -> None:
        self.extra_context = kwargs.pop('extra_context', dict())
        super().__init__(**kwargs)

    def run(self, test):
        result = super().run(test)
        if hasattr(result, 'generate_report'):
            result.generate_report(
                extra_context=self.extra_context
            )
        return result
