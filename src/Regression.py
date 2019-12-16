import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

class LinearRegression:

    def __init__(self, x, y):
        
        self.x = np.array([np.ones(len(x)), x]).T
        self.y = np.array([y]).T
        self.weights = 0
        self.__calculate_weights()

    def __calculate_weights(self):
        x = self.x
        y =  self.y
        xt = x.T
        inverse = np.linalg.inv(xt@x)
        inverse_xt = inverse@xt
        final_result = inverse_xt@y

        self.weights = final_result 

    def graph_original_data(self):
        plt.scatter(self.x[0], self.y[0], label="original data")
        plt.xlabel('x label')
        plt.ylabel('y label')
        plt.title('original graph')
        plt.legend()
        plt.show()

    def graph_estimated_data(self, x, y):
        plt.scatter(x, y, label="estimated data")
        plt.xlabel('x label')
        plt.ylabel('y label')
        plt.title('estimated graph')
        plt.legend()
        plt.show()

    def compare_graphs(self, x, y):
        plt.scatter(self.x[:, 1], self.y[:], alpha=0.5, label="original") #original data
        plt.plot(x, y, 'g', label="estimated") #estimated data
        plt.xlabel('x label')
        plt.ylabel('y label')
        plt.title('compare graph')
        plt.legend()
        plt.show()

    def estimate_values(self, x):
        w = self.weights
        o0, o1 = w[0][0],w[1][0]
        values = [o1*i + o0 for i in x]
        return values 
