import numpy as np




class linear_equation():
    def __init__(self, factor_len): 
        self.len = factor_len
        self.curr_batch = []
        self.expected = 0
        self.prev_batch = [0, 0, 0, 0, 0] # saved by index samea as curr
        self.prev_expected = 0
        self.curr_factors_value = 0
        self.residual = None

    def clear_batch(self):
        self.prev_batch = self.curr_batch
        print(f'this is the test batch{self.curr_batch}')
        self.curr_batch.clear()
        
    def update_curr_factor_values(self):
        print(self.curr_batch)
        temp = self.curr_batch[0]
        for i in range(len(self.curr_batch)):
            print(f"this is test value{self.prev_batch}")
            self.curr_factors_value =  (self.curr_batch[i] * self.prev_batch[i]) +  self.curr_factors_value

    def measure_residual(self):
        self.residual = self.expected - self.curr_batch[3]

    def complete_equation(self, value):
        if self.residual != None:
            self.expected = (self.curr_factors_value * value) 
            self.expected = self.expected + self.measure_residual()
            print(self.expected)
        else:
            self.residual = value 

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
        print('iteration ran')
        #needs prev append in an object
        if len(temp.curr_batch) > 0:
            temp.curr_batch.append(data[i])
        else:
            temp.curr_batch = [data[i]]
        if i* 5 % 2 == 0:
            temp.update_curr_factor_values()
            temp.measure_residual()
            temp.clear_batch()
            
run(test_example_values)