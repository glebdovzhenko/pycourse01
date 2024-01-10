from boilerplate import setUpModule, TestStudentReport
import numpy as np


class TestTask01(TestStudentReport):
    """
    This is an example of how the student reports can be checked.
    
    File task01.ipynb contains some cells within which are 
    3 variable definitions: a, b, c.
    This test case compares the values of these variables against some hard-coded values.
    """
    _report_name = 'task01'
    
    def test_a(self):
        """
        a = np.array([1, 2, 3])
        """
        self.assertTrue(
            np.all(np.isclose(
                self.report['a'],
                np.array([1, 2, 3])
            ))
        )

    def test_b(self):
        """
        b = True
        """
        self.assertTrue(
            self.report['b']
        )
    
    def test_c(self):
        """
        c = {1: 2, 3: 4}
        """
        self.assertDictEqual(
            self.report['c'],
            {1: 2, 3: 4}
        )

