import answers
import unittest
from HtmlTestRunner import HTMLTestRunner


if __name__ == '__main__':
    runner = HTMLTestRunner(
        template='test_engine/report_template.html',
        combine_reports=True
    )
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(answers)
    print(suite)
    runner.run(suite)
