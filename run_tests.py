import answers
from unittest import TextTestRunner, TextTestResult, TestLoader
from HtmlTestRunner import HTMLTestRunner


if __name__ == '__main__':
    # runner = HTMLTestRunner(
    #     template='test_engine/report_template.html',
    #     combine_reports=True
    # )
    runner = TextTestRunner(resultclass=TextTestResult)
    suite = TestLoader().loadTestsFromModule(answers)
    runner.run(suite)
