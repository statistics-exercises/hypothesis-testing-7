import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_statistic(self) :
        self.assertTrue( np.abs( sum(data) - statistic(data) ) <1e-7, "your statistic has not been calculated correctly" )
        
    def test_criticalRange(self) : 
        l = scipy.stats.binom.ppf(0.05,10,0.5 )
        u = scipy.stats.binom.ppf(0.95,10,0.5 )
        lll, uuu = criticalRange( 0.5, len(data) )
        self.assertTrue( np.abs(l-lll)<1e-4, "the lower boundary for the critical region has not been computed correctly")
        self.assertTrue( np.abs(u-uuu)<1e-4, "the higher boundary for the critical region has not been computed correctly")
        
    def test_hypothesisTest(self) : 
        hhh = hypothesisTest( data, 0.5 ) 
        self.assertTrue( hhh=="the null hypothesis is rejected in favour of the alternative", "The string returned from your hypothesis test code is incorrect.  This code should return the string the null hypothesis is rejected in favour of the alternative as the sample mean is within the critical region." )
        self.assertTrue( inspect.getsource(hypothesisTest).find("if")>0, "your hypothesisTest function does not contain an if statement" )
        self.assertTrue( inspect.getsource(hypothesisTest).find("there is insufficient evidence to reject the null hypothesis")>0, "The hypothesis test function does not contain the string there is insufficient evidence to reject the null hypothesis.  This string should be present and output when the sample mean falls outside the critical region." ) 
