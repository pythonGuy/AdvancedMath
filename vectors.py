#!/home/allen/local/bin/python

from math import *

def km2miles (km):
    return km * .62137119224

def distance (*points):
    pLen = len(points)
    if pLen == 1:
        orig   = [0 for i in range(len(points[0]))]
        pts    = points[0]
        points = [orig, pts]
    elif pLen != 2:
        print "Error, two points are required"
        return
    elif len(points[0]) != len(points[1]):
        print "Error, vectors not the same length"
        return
    pSum = 0
    for i in range(len(points[0])):
        pSum += (points[1][i]-points[0][i])**2
    return sqrt(pSum)

def add (p1, p2):
    if len(p1) != len(p2):
        print "Error, vectors not the same length"
        return
    rSum = []
    for i in range(len(p1)):
        rSum.append(p1[i] + p2[i])
    return rSum

def dotProdMA (P, Q, angle):
    prod = P*Q*cos(radians(angle))
    if prod < .000001:
        prod = 0
    return prod

def dotProd (P, Q):
    if len(P) != len(Q):
        print "Error, vectors not the same length"
        return
    prod = 0
    for i in range(len(P)):
        prod += P[i] * Q[i]
    return prod

def angle (P, Q):
    if len(P) != len(Q):
        print "Error, vectors not the same length"
        return
    p1 = 0
    p2 = 0
    num = dotProd(P,Q)
    for i in range(len(P)):
        p1 += P[i]**2
        p2 += Q[i]**2
    den = sqrt(p1)*sqrt(p2)
    return degrees(acos(num/den))

def mag (P):
    origin = [0 for i in range(len(P))]
    return distance( origin, P )

def crossProd (A, B):
    if len(A) != 3 and len(B) != 3:
        print "Error, crossProd only support for 3d vectors"
        return
    return mag(A)*mag(B)*sin(radians(angle(A,B)))

def vectorProd (A, B):
    return crossProd(A, B)

def LatorLog2rads(d, m, compass):
    d = float(d)
    m = float(m)
    if compass == "S" or compass == "W":
        d = d*(-1.0)
        m = m*(-1.0)

    rads = (d*pi)/180.0
    rads += ((m/60.0)*pi)/180.0
    return rads

def cAngle (LL1, LL2):
    p1LatR = LatorLog2rads( LL1[0], LL1[1], LL1[2])
    p1LogR = LatorLog2rads( LL1[3], LL1[4], LL1[5])
    p2LatR = LatorLog2rads( LL2[0], LL2[1], LL2[2])
    p2LogR = LatorLog2rads( LL2[3], LL2[4], LL2[5])
    t1 = sin((p2LatR-p1LatR)/2.0)**2
    e1 = cos(p1LatR)*cos(p2LatR)
    e2 = sin((p2LogR-p1LogR)/2.0)**2
    t2 = e1 * e2
    cAngle = 2*asin(sqrt(t1+t2))
    return cAngle

def arcLen (radius, centralAngle):
    return radius * centralAngle

def earthDist (LL1, LL2, units):
    centralAngle = cAngle(LL1, LL2)
    kms          = arcLen(6371, centralAngle)
    miles        = km2miles (kms)
    if units == 'm':
        retValue = miles
    else:
        retValue = kms
    return retValue
