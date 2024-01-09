import sys
import importlib
import unittest
from .jup import NotebookFinder


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
