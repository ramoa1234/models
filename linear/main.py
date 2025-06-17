import numpy as np


class model:
    def __init__(self, start_open, start_high, start_low, start_close, start_volume):
        self.std_div = []
        self.prevs = []
        self.std_div.append(0)
        self.std_div.append(0)
        self.std_div.append(0)
        self.std_div.append(0)
        self.std_div.append(0)
        self.std_div.append(0) # 5 = std of residual
        self.prevs.append(start_open)
        self.prevs.append(start_high)
        self.prevs.append(start_low)
        self.prevs.append(start_close)
        self.prevs.append(start_volume)
        self.prevs.append(0) # = previous residual 
        self.correlations = []
        self.expected_return = 0
        self.residual = 0 # how off you were

    def linear_equation(self, curr_open, curr_high, curr_low, curr_close, curr_volume):
        #measure the correlation between the values and expected return
        self.std_div[0] = self.get_curr_std_div(self.prevs[0], curr_open)
        self.std_div[1] = self.get_curr_std_div(self.prevs[1], curr_high)
        self.std_div[2] = self.get_curr_std_div(self.prevs[2], curr_low)
        self.std_div[3] = self.get_curr_std_div(self.prevs[3], curr_close)
        self.std_div[4] = self.get_curr_std_div(self.prevs[4], curr_volume)
        




    def get_curr_std_div(self, prev, now):
        if prev > now:
            return prev - now
        elif now > prev:
            return now - prev
        
    #compare two values and update iteratively or update at each interval 
    def get_correlation(self, curr_val_index, curr_factor): 
        #index = index of the current value in the list 
        x = np.array([self.prevs[5], curr_factor])
        y = np.array([self.std_div[5], self.prevs[curr_val_index]])
        corr = np.corrcoef(x, y)
        print(corr)


    #update floats rounding(slow)
    def run(self):
        data = np.loadtxt('../data/btcusd_1-min_data.csv', delimiter=',', skiprows=1)
        depth = 5
        index = 0
        for i in range(0, len(data), 5):
            temp = []
            for i in depth(data[range]):
                pass




def test():
    test = model(1, 1, 1, 1, 1)
    test.run()

test()

#act as run and read function 

