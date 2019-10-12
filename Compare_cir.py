#!/usr/bin/env python
# coding: utf-8


import numpy as np


iden = [[1,0],[0,1]]
swap = [[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]]
cx = [[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]]
cx01 = np.kron(cx, np.kron(iden,iden))
cx12 = np.kron(iden, np.kron(cx, iden))
cx23 = np.kron(np.kron(iden,iden), cx)
swap01 = np.kron(swap,np.kron(iden,iden))
swap12 = np.kron(iden, np.kron(swap,iden))
swap23 = np.kron(np.kron(iden,iden), cx)

def cir_is_equal(x,y):
    l = [np.kron(np.kron(iden,iden),cx),
         np.kron(np.kron(swap,iden,iden))@np.kron(np.kron(iden,swap,iden))@np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,iden,cx)),
        np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx)]
    if x[y] == l[y]:
        return True
    else:
        return False


def build_gate(x):
    if x == 1:
        return cx01
    elif x == 2:
        return cx12
    elif x == 3:
        return cx23
    elif x == 4:
        return swap01
    elif x == 5:
        return swap12
    else:
        return swap23




def tot_oper(x):
    tot = iden
    for i in x:
        total = total@build_gate(i)





