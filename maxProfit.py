# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:32:11 2022

@author: MANCHALA VAISHNAVI
"""

def maxProfit(n):
    theatre=1500
    pub=1000
    commercialPark=3000
    tUnits=n
    pUnits=n
    cUnits=n
    res1=0
    res2=0
    res3=0
    P=0
    T=0
    C=0
    if n<4:
        print("T:0 P:0 C:0")
        return 
    elif n>=4 and n<6:
        print("T:0 P:"+str((n-4))+" C:0")
        return 
    while pUnits>4:
        diff=pUnits-4
        total=diff*pub
        res1=res1+total
        P+=1
        pUnits=pUnits-4
    while tUnits>5:
        diff=tUnits-5
        total=diff*theatre
        res2=res2+total
        T=T+1
        tUnits=tUnits-5
    while cUnits>10:
        diff=cUnits-10
        total=diff*commercialPark
        res3=res3+total
        C=C+1
        cUnits=cUnits-10

    
    if res1>=res2 and res1>=res3:
        print("T:0 P:"+str(P)+"C:0")
        return 
    elif res2>=res1 and res2>=res3:
        print("T:"+str(T)+" P:0 C:0")
    else:
        print("T:0 P:0 C:"+str(C))
        
    
    return

n=int(input())
maxProfit(n)