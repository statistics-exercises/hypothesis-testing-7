import numpy as np
import scipy.stats

def statistic( data ) :
  #Your code to calcualte the sum of all the variables should go here
  
def criticalRange( p, n ) : 
  # Your code to calculate the critical region should go here
  lower = 
  upper = 
  return lower, upper
  
def hypothesisTest( data, p ) : 
  l, u = criticalRange( p, len(data) )
  # You need to use the l and u values that are returned from the critical range
  # function above within an if statement.  This if statement should decide whether 
  # there is sufficient evidence to reject the null hypothesis.  The code should
  # then return either the statement about the null hypothesis being rejected or
  # the statement about there being insufficient evidence to reject the null 
  # hypothesis form the flowchart.
  
  
data = np.loadtxt("games.dat")
print( hypothesisTest( data, 0.5 ) )
  
