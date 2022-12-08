import unittest
from gradescope_utils.autograder_utils.decorators import weight,partial_credit

class TestExtraCredit(unittest.TestCase):
    @partial_credit(2)
    def test1(self,set_score=None):
        f"""Extra Credit: +0.4 per day"""
        from datetime import date
        set_score(min(2,0.4*(date(2022,12,4)-date.today()).days))
