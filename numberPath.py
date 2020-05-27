# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:17:57 2020

@author: Liam
"""
import random
import matplotlib.pyplot as plt

def numberPathv1(numberAim):
    probList=[1,0.5] # The probability of starting on number 1 is 1, and landing on 2 is 0.5.
    for i in range(2,numberAim):
        probList.append(0.5*probList[i-2]+0.5*probList[i-1]) 
    return probList    # The model reduces to a fairly straight-forward recursion formula. 
    
def plotProbs(numberAim):
    random.seed(1)
    xaxis=[]
    y=numberPathv1(numberAim)
    for i in range(0,numberAim):
        xaxis.append(i+1)
    plt.plot(xaxis,y)
    plt.show()
    plt.savefig("ProbDistribution.png")
def main():
    numberaim=100        # Choose a larger number than 25 to obtain a substantial probability distribution. 
    plotProbs(numberaim) # Note the probabiliy for 25 will be presented correctly, as it is in actuality deterministic.


main()