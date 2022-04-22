import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value = 5)
        self.MockClass1 = self.patcher1.start()
        self.addCleanup(self.patcher1.stop)

    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)# will execute the add
        self.assertEqual(calculate('1',6,3), 5) # will call the mock

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',9,3), 9)

    def test_DividByZerrorEx1(self):
        with self.assertRaises(ValueError):
             calculate('4','3','w')
    
    def test_DividByZerrorEx2(self):
        with self.assertRaises(ValueError):
             calculate('3','10','w')

    def test_DividByZerrorEx3(self):
        with self.assertRaises(ValueError):
             calculate('4','0','w')
    ##OR

    def test_DividByZerrorEx2(self):
        self.assertRaises(ValueError, calculate, '4','3','w') 

    def test_DividByZerrorEx5(self):
        self.assertRaises(ValueError, calculate, '12','0','w') 

    def test_DividByZerrorEx7(self):
        self.assertRaises(ValueError, calculate, '0','0','w') 

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')


    
    def test_DividByZerrorEx8(self):
        with self.assertRaises(ValueError):
             calculate('3','50','w')


    
    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 6)

    def test_AddPassWithMockEx9(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 10)

    @mock.patch('calculatorApp.add', return_value = 4)
    def test_AddPassWithMockEx2(self, mock_check):
        result = calculate('1',3,2)
        self.assertEqual(result, 4)

    @mock.patch('calculatorApp.add', return_value = 4)
    def test_AddPassWithMockEx3(self, mock_check):
        result = calculate('1',10,5)
        self.assertEqual(result, 4)

    @mock.patch('calculatorApp.add', return_value = 60)
    def test_AddPassWithMockEx3(self, mock_check):
        result = calculate('1',3,5)
        self.assertEqual(result, 4)

    @mock.patch('calculatorApp.add', return_value = 4)
    def test_AddPassWithMockEx4(self, mock_check):
        result = calculate('1',100,6)
        self.assertEqual(result, 4)




    def test_AddPassWithMocEx3(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',2,6), 5)
        
    def test_AddPassWithMocEx4(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',1000,6), 6)

    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


class TestCalculateWithoutMock(unittest.TestCase):
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(calculate('1',6,3), 9)

if __name__ == '__main__':
	unittest.main()
