import answers
from boilerplate import unittest
from HtmlTestRunner import HTMLTestRunner


if __name__ == '__main__':
    runner = HTMLTestRunner()
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(answers)
    runner.run(suite)
