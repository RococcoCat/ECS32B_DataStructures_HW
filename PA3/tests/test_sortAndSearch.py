import unittest
from gradescope_utils.autograder_utils.decorators import weight
import csv, sys, ast, time, json
from sortAndSearch import main
csv.field_size_limit(2147483647)


class TestSortAndSearch(unittest.TestCase):
    def setUp(self):
        self.data = {}
        with open('data.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data[row['Date']] = row['Price']

        with open("queries.json",'r') as f:
            self.queries = json.load(f)

        main()
        self.output = {}
        with open('output.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.output[row['Name']] = {'Time': float(row['Time']),
                                            'Output': ast.literal_eval(row['Output'])}


    @weight(3)
    def test_case0(self):
        """03 Sort and Search: Correct format (also see setUp)"""
        for k in ['Linear Search', 'Bubble Sort', 'Other Sort', 'Other Search']:
            self.assertTrue(k in self.output.keys())
        print("First test case (sort and search): Completed")

    @weight(1.5)
    def test_case1(self):
        """03 Sort and Search: Checking linear search"""
        self.assertTrue(self.output['Linear Search']['Time']>1.)
        self.assertTrue(self.output['Linear Search']['Time']<15.)
        for i,(date,price) in enumerate(self.output['Linear Search']['Output']):
            self.assertEqual(self.data[date], price)
            self.assertEqual(self.queries[i], price)
        self.assertTrue(len(self.output['Linear Search']['Output']), len(self.queries))
        print("Second test case (sort and search): Completed")


    @weight(1.5)
    def test_case2(self):
        """03 Sort and Search: Checking bubble sort"""
        self.assertTrue(self.output['Bubble Sort']['Time']>1.)
        self.assertTrue(self.output['Bubble Sort']['Time']<15.)
        for (date0,price0),(date1,price1) in zip(self.output['Bubble Sort']['Output'],
                                                 self.output['Bubble Sort']['Output'][1:]):
            self.assertTrue(price0<=price1)
            self.assertEqual(self.data[date0], price0)
            self.assertEqual(self.data[date1], price1)
        print("Third test case (sort and search): Completed")


    @weight(1.5)
    def test_case3(self):
        """03 Sort and Search: Checking other sort"""
        self.assertTrue(self.output['Other Sort']['Time']>0.)
        self.assertTrue(self.output['Other Sort']['Time']<self.output['Bubble Sort']['Time'])
        for (date0,price0),(date1,price1) in zip(self.output['Other Sort']['Output'],
                                                 self.output['Other Sort']['Output'][1:]):
            self.assertTrue(price0<=price1)
            self.assertEqual(self.data[date0], price0)
            self.assertEqual(self.data[date1], price1)
        print("Fourth test case (sort and search): Completed")


    @weight(1.5)
    def test_case4(self):
        """03 Sort and Search: Checking other search"""
        self.assertTrue(self.output['Other Search']['Time']>0.)
        self.assertTrue(self.output['Other Search']['Time']<self.output['Linear Search']['Time'])
        for i,(date,price) in enumerate(self.output['Other Search']['Output']):
            self.assertEqual(self.data[date], price)
            self.assertEqual(self.queries[i], price)
        self.assertTrue(len(self.output['Other Search']['Output']), len(self.queries))
        print("Last test case (sort and search): Completed")





