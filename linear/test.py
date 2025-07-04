import numpy as np
import matplotlib.pyplot as plt


#update to not store the result current residual somewre class :)
def correlation_matrix(data, expected, batch_size):
    curr = np.empty((5, 5), dtype=float)
    for row in data:
        curr = np.vstack([curr, row])
        if (len(curr) == batch_size):
            corr = np.corrcoef(curr, rowvar=False)
            curr = np.empty((5, 5), dtype=float)


data = [[]]
expected = 20
batch_size = 5
correlation_matrix(data, expected, batch_size)

class linear_equation():
    def __init__(self, factor_len): 
        self.len = factor_len
        self.curr_batch = []
        self.expected = 0
        self.prev_batch = []
        for i in range(5):
            self.prev_batch.append(5)
        self.prev_expected = 0
        self.curr_factors_value = 0
        self.residual = None

    def clear_batch(self):
        self.prev_batch = self.curr_batch
        print(f'this is the test batch{self.curr_batch}')
        print(self.prev_batch)
        self.curr_batch.clear()
        
    def update_curr_factor_values(self):
        print(self.prev_batch)
        for i in range(len(self.curr_batch)):
            self.curr_factors_value =  (self.curr_batch[i] * self.prev_batch[i]) +  self.curr_factors_value
        print(self.curr_factors_value)

    def measure_residual(self):
        self.residual = self.expected - self.curr_batch[3]

    def complete_equation(self, value):
        if self.residual != None:
            self.expected = (self.curr_factors_value * value) 
            self.expected = self.expected + self.measure_residual()
            print(self.expected)
        else:
            self.residual = value 
    
    def get_correlation(self):
        #corr = residual & factor want to equal zero
        #&corr = residual & current residual measured(measures accuracy) also want to equal zero
        #done iteratively in correlation matrix in training
        #because bi1 = factor exposure measured by the correlation
        #and by adjusting and properly setting the exposure(bi1) you can make the residual zero or close to it
        pass

#takes in each individual layer or batch as a list than computes using there object


test_example_values = [
    [20, 25, 30, 35, 40],
    [40, 45, 50, 55, 60], 
    [60, 65, 70, 75, 80]]

"""
the measuring of the correlation 
"""

def run(data):
    LEN = 5
    temp = linear_equation(LEN)
    for i in range(0, len(data)):
        print(f'curr value in first loop {data[i]}')
        temp.curr_batch = data[i]
        print(temp.curr_batch)
        temp.update_curr_factor_values()
        temp.measure_residual()
        temp.clear_batch()
            