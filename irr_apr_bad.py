# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:26:40 2020

@author: wu
"""

import numpy as np

def irr_apr(rate):
    n=12
    a=10000
    f=a*rate*(n/12)/n    
    f1=0
    ff=[f1+(f-f1)/10000*k for k in range(10000)]
    for l in ff:
        b=[float(a)/n+l]*n        
        r=np.irr([-10000]+b)
        irr=(r+ 1)** 12- 1
#        print(irr-rate)
        if  abs(irr-rate)<0.0001:
            return l/10000.0,r
def macd(rate,m,n):
    r=irr_apr(rate)[0]
    pv=0
    npv=0
    for l in range(m+1)[1:-1]:
#        print(l)
        pv=pv+1.0/n/(1+r)**(l)*(l)
        npv=npv+1.0/n/(1+r)**(l)
    pv=pv+(n-m)/n/(1+r)**(m)*(m)
    npv=npv+float(n-m)/n/(1+r)**(m)
    return pv/npv
    

def loss(rate,bad,m,n):
    mad=macd(rate,m,n)
    br=bad*12/mad
    ra=rate-br
    for i in range(10):
        mad=macd(ra,m,n)
        br=bad*12/mad
#        print(br,mad)
        ra=rate-br
    return br


#
#loss(0.27,0.025,5,12)
#
#loss(0.18,0.0721,18,36)
#
#loss(0.18,0.08,18,36)
#
#
#for i in range(10):
#    print(0.07+i/100)
#    print(loss(0.18,0.07+i/100,18,36))
#    
#    
#
#loss(0.18,0.025,5,12)
#24*0.025/(6)
#loss=br*12/
#
#
#m,n=18,36
#
#def rrt(rate,m,n):
#    ll=0
#    for l in range(m):
#        ll=ll+(n-l)/n
#    ll=ll/m    
#    return 12/m*rate/ll
#
#
#
#
#
#def rrt(rate,m,n):
#    ll=0
#    for l in range(m):
#        ll=ll+(n-l)/n
#    ll=ll/m
#    return 12/m*rate/ll
#
#        
#rrt(0.07,18,36)
#loss(0.18,0.07,18,36)
#
#rrt(0.03,6,12)
#
#loss(0.24,0.03,6,12)
#
#
#
#rrt(0.03,6,12)














