import tests
from unittest import TextTestRunner, TextTestResult, TestLoader
from HtmlTestRunner import HTMLTestRunner
from test_engine import JinjaTestRunner, JinjaTestResult


DEFAULT_CONTEXT = {
    'student_name': 'Иванов Иван Иванович',
    'group_name': 'ГР-000',
    'title': 'Выполненные работы'
}


if __name__ == '__main__':
    # runner = HTMLTestRunner(
    #     template='test_engine/report_template.html',
    #     combine_reports=True
    # )
    # runner = TextTestRunner(resultclass=TextTestResult)
    runner = JinjaTestRunner(
        resultclass=JinjaTestResult,
        extra_context=DEFAULT_CONTEXT
    )
    suite = TestLoader().loadTestsFromModule(tests)
    runner.run(suite)

