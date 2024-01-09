from boilerplate import setUpModule, TestStudentReport
import numpy as np


class TestTask01(TestStudentReport):
    _report_name = 'task01'
    
    def test_a(self):
        self.assertTrue(
            np.all(np.isclose(
                self.report['a'],
                np.array([1, 2, 3])
            ))
        )

    def test_b(self):
        self.assertTrue(
            self.report['b']
        )
    
    def test_c(self):
        self.assertDictEqual(
            self.report['c'],
            {1: 2, 3: 4}
        )
