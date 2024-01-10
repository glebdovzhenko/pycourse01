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

    def __init__(self, 
                 methodName: str = "runTest") -> None:
        super().__init__(methodName)

    @classmethod
    def setUpClass(cls):
        cls._report = importlib.import_module(cls._report_name)
    
    @property
    def report(self):
        return self._report.__dict__


DEFAULT_TEMPLATE = os.path.join(
    os.path.dirname(__file__), 
    "report_template_2.html"
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

    def addSuccess(self, test) -> None:
        cls_key = test.__doc__
        case_key = test._testMethodDoc
        if cls_key not in self._jinja_context['results'].keys():
            self._jinja_context['results'][cls_key] = dict()
            self._jinja_context['summaries'] = ''
        self._jinja_context['results'][cls_key][case_key] = self.SUCCESS
        return super().addSuccess(test)

    def addFailure(self, test: unittest.case.TestCase, err) -> None:
        cls_key = test.__doc__
        case_key = test._testMethodDoc
        if cls_key not in self._jinja_context['results'].keys():
            self._jinja_context['results'][cls_key] = dict()
            self._jinja_context['summaries'] = ''
        self._jinja_context['results'][cls_key][case_key] = self.FAILURE

        return super().addFailure(test, err)

    def addSubTest(self, test, subtest, err) -> None:
        print(test.__doc__)
        print(subtest.__doc__)
        return super().addSubTest(test, subtest, err)

    def generate_report(self, extra_context=dict(), report=None):
        if report is None:
            with open(DEFAULT_REPORT, 'w') as f:
                f.write(
                    self._jinja_template.render(
                        **self._jinja_context, **extra_context)
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



