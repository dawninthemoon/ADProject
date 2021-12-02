import unittest

from GMPtoCJU import GMPtoCJU
from CJUtoGMP import CJUtoGMP
import mainWindow as mw

class TestAirline(unittest.TestCase):
    def setUp(self):
        self.g1 = GMPtoCJU(2021, 12, 12)
        self.c1 = CJUtoGMP(2021, 12, 12)
        self.Gairline = self.g1.airline
        self.Cairline = self.c1.airline

    def tearDown(self):
        pass


    def test_GMPtoCJU_keys_len(self):
        keys_len = len(self.g1.keys)
        keys2_len = len(self.g1.keys2)//2
        keys3_len = len(self.g1.keys3)
        self.assertEqual(keys_len, keys2_len)
        #self.assertEqual(keys2_len, keys3_len)

    def test_CJUtoGMP_keys_len(self):
        keys_len = len(self.c1.keys)
        keys2_len = len(self.c1.keys2)//2
        keys3_len = len(self.c1.keys3)
        self.assertEqual(keys_len, keys2_len)
        #self.assertEqual(keys2_len, keys3_len)

    def test_GMPtoCJU_sort_money_low_to_high(self):
        self.g1.sortMoneyLowToHigh()
        for i in range(len(self.g1.keys) - 1):
            self.assertTrue(self.g1.getAirlineCost(i) <= self.g1.getAirlineCost(i+1))

    def test_CJUtoGMP_sort_money_low_to_high(self):
        self.c1.sortMoneyLowToHigh()
        #print(self.c1.airline)
        #print(self.Cairline)
        for i in range(len(self.c1.keys) - 1):
            self.assertTrue(self.c1.getAirlineCost(i) <= self.c1.getAirlineCost(i+1))
            
    def test_GMPtoCJU_sort_money_high_to_low(self):
        self.g1.sortMoneyHightToLow()
        #print(self.Gairline)
        for i in range(len(self.g1.keys) - 1):
            self.assertTrue(self.g1.getAirlineCost(i) >= self.g1.getAirlineCost(i+1))

    def test_CJUtoGMP_sort_money_high_to_low(self):
        self.c1.sortMoneyHightToLow()
        for i in range(len(self.c1.keys) - 1):
            self.assertTrue(self.c1.getAirlineCost(i) >= self.c1.getAirlineCost(i+1))

    def test_GMPtoCJU_sort_start_time(self):
        self.g1.sortStartTime()
        for i in range(len(self.c1.keys) - 1):
            t1 = self.g1.getAirlineStartTime(i)
            h1, m1 = map(int, t1.split(':'))
            minute_time1 = m1 + 60 * h1

            t2 = self.g1.getAirlineStartTime(i+1)
            h2, m2 = map(int, t2.split(':'))
            minute_time2 = m2 + 60 * h2

            self.assertTrue(minute_time1 <= minute_time2)

    def test_CJUtoGMP_sort_start_time(self):
        self.c1.sortStartTime()
        for i in range(len(self.c1.keys) - 1):
            t1 = self.c1.getAirlineStartTime(i)
            h1, m1 = map(int, t1.split(':'))
            minute_time1 = m1 + 60 * h1

            t2 = self.c1.getAirlineStartTime(i+1)
            h2, m2 = map(int, t2.split(':'))
            minute_time2 = m2 + 60 * h2

            self.assertTrue(minute_time1 <= minute_time2)

    def test_month(self):
        days = [0, 31, 28, 31, 28, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(1, 13):
            for j in range(1, days[i]):
                self.assertTrue(mw.isDateValid(i, j))

        for i in range(1, 13):
            self.assertFalse(mw.isDateValid(i, 32))
            self.assertFalse(mw.isDateValid(i, 0))
            self.assertFalse(mw.isDateValid(i, -1))







if __name__ == "__main__":
    unittest.main()