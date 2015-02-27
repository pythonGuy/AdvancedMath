#!/home/allen/local/bin/python

from math import *

def eval_f (poly, *argv, **kargs):
    """Computes the value of a polynomial at the given the various
       value for variables in the polynomial
    
    Args:
      poly    (str): The polynomial to evaluate
      *argv   (float or int): Up to 3 values representing
                              x, y, and z in the polynomial
      **kargs (float or int): Any number of named variables in
                              the polynomial

    Examples:
      eval_f ("3*x**4 - 7*y**3", 3, 2)
      187
      eval_f ("3*x**4 - (7*y**3)*cos(d) + sin(z) - 4*a + 3*b**2 - 5.1*c1",
              2.77, 2, pi*3, a=-3.17, b=3.2, c1=4, d=2*pi)
      143.62018322999938
    """
    defaultVars = ['x', 'y', 'z']
    if len(argv) > 3:
        print "Too many unamed variable values, only supply unamed values for x, y and z"
        return
    for arg in argv:
        poly = poly.replace(defaultVars.pop(0), str(arg))
    for var, value in kargs.iteritems():
        poly = poly.replace(str(var), str(value))
    return eval(poly)

def differentiate (poly, atX):
    """Differentiate a polynomial with respect to 'x'

    Args:
      poly (str): The polynomial to differentiate
      atX (float or int): Value for 'x'

    Example:
      differentiate ( "(5/2)*x**2", 4.7 )

      dy/dx: 19.0 (4.7 to 4.8)
      dy/dx: 18.82 (4.7 to 4.71)
      dy/dx: 18.802 (4.7 to 4.701)
      dy/dx: 18.8001999999 (4.7 to 4.7001)
      19.0
      """

    retList = []
    base  = eval_f(poly, atX)
    incr  = .1
    endv  = eval_f(poly, atX+incr)
    retList.append(endv)
    #
    incr  /= 10.0
    endv  = eval_f(poly, atX+incr)
    retList.append(endv)
    #
    incr  /= 10.0
    endv  = eval_f(poly, atX+incr)
    retList.append(endv)
    #
    incr  /= 10.0
    endv  = eval_f(poly, atX+incr)
    retList.append(endv)
    #
    incr  /= 10.0
    endv  = eval_f(poly, atX+incr)
    retList.append(endv)
    #
    return retList
