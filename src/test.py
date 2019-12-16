from Regression import LinearRegression
import numpy as np
import math

def test_function():
    x = [ i for i in range(100) ]
    y = [math.pow(i, 3) for i in x]
    return [x,y]

def estimated_data():
    x = [i for i in range(100)] 
    y = linear_regression.estimate_values(x)
    return [x,y]

def graph(x, y):
    #graph original and estimated data to see how much relation exist between them.
    linear_regression.compare_graphs(x, y)

if __name__=="__main__":

    x,y = test_function() #original data
    linear_regression = LinearRegression(x, y)
    
    test_x, test_y = estimated_data()
    graph(test_x, test_y)
