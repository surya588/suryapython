# -*- coding: utf-8 -*-
"""
Created on Thu Dec 01 05:40:04 2016

@author: suryateja
"""

a= True
while(a):
    print ("1.windows\n2.linux\n3.mac\n4.quit")
    r=raw_input("enter your option")
    if (r=='1'):
        print ("windows selected")
    elif (r=='2'):
        print ("linux selected")
    elif (r=='3'):
        print ("mac selected")
    elif (r=='4'):
        break
    else:
        print ("choose correct option")