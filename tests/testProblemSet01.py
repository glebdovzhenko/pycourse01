from test_engine import setUpModule, TestStudentReport
import numpy as np


class TestProblemSet01(TestStudentReport):
    """
    Лабораторная работа 1: Основные типы и управляющие конструкции
    """
    _report_name = 'answers.01_pset'
    _varlist = ('a', 'b', 'c', 't1_l', 't1_d',
                't2_l', 't2_lsq', 't2_lsq_sum',
                't3_l', 't3_l_odd',
                't4_d', 't4_d_inv')

    def test1a(self):
        """
        Задание 1
        """
        a = 10
        b = 3
        c = a ** 2 + b ** 2
        self.assertEqual(a, self.report['a'])
        self.assertEqual(b, self.report['b'])
        self.assertEqual(c, self.report['c'])
        
        t1_l = []
        t1_l.append(str(a**(-b)))
        t1_l.append(float(a % b))
        self.assertListEqual(t1_l, self.report['t1_l'])

        t1_d = dict()
        t1_d[26] = 'z'
        t1_d[25] = 'y'
        t1_d[24] = 'x'
        t1_d[23] = 'w'
        t1_d[22] = 'v'
        self.assertDictEqual(t1_d, self.report['t1_d'])

    def test2a(self):
        """
        Задание 2
        """
        t2_l = [0, 1, 4, 2, 0, 2, 3, 4]
        t2_l = list(set(t2_l))
        t2_l.sort()
        self.assertListEqual(t2_l, self.report['t2_l'])

        t2_lsq = [x ** 2 for x in t2_l]
        self.assertListEqual(t2_lsq, self.report['t2_lsq'])
        t2_lsq_sum = sum(t2_lsq)
        self.assertEqual(t2_lsq_sum, self.report['t2_lsq_sum'])

    def test3a(self):
        """
        Задание 3
        """
        t3_l = []

        n = 0
        while n <= 20:
            t3_l.append(n % 5)
            n += 1
        self.assertListEqual(t3_l, self.report['t3_l'])

        t3_l_odd = [x for x in t3_l if x % 2 == 1 ]
        self.assertListEqual(t3_l_odd, self.report['t3_l_odd'])

    def test4a(self):
        """
        Задание 4
        """
        t4_d = dict()

        n = 0
        while n <= 20:
            t4_d[n] = n + 1
            n += 1
        self.assertDictEqual(t4_d, self.report['t4_d'])

        t4_d_inv = {v: k for (k, v) in t4_d.items()}
        self.assertDictEqual(t4_d_inv, self.report['t4_d_inv'])

