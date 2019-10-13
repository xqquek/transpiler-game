#!/usr/bin/env python
# coding: utf-8


import numpy as np


iden = np.array([[1,0],[0,1]])
swap = np.array([[1,0,0,0],[0,0,1,0],[0,1,0,0],[0,0,0,1]])
cx = np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])
cx01 = np.kron(cx, np.kron(iden,iden))
cx12 = np.kron(iden, np.kron(cx, iden))
cx23 = np.kron(np.kron(iden,iden), cx)
swap01 = np.kron(swap,np.kron(iden,iden))
swap12 = np.kron(iden, np.kron(swap,iden))
swap23 = np.kron(np.kron(iden,iden), cx)

def cir_is_equal(x,y):
    """
    x is a matrix, y is integer specifying the subproblem of the circuit (i.e. time step)
    """
    l = [np.kron(np.kron(iden,iden),cx),
         np.kron(np.kron(swap,iden),iden)@np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx),
        np.kron(np.kron(iden,swap),iden)@np.kron(np.kron(iden,iden),cx)]
    if np.all(x == l[y]):
        return True
    else:
        return False


def build_gate(x):
    if x == 0:
        return cx01
    elif x == 1:
        return cx12
    elif x == 2:
        return cx23
    elif x == 3:
        return swap01
    elif x == 4:
        return swap12
    else:
        return swap23




def tot_oper(x):
    """
    x is the list of user inputs from the card stack
    """
    total = np.kron(np.kron(iden,iden),np.kron(iden,iden))
    for i in x:
        print(total.shape)
        print(build_gate(i).shape)
        total = total@build_gate(i)
    return total




