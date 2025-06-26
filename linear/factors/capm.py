
#measures risk to return


class CAPM:
    def __init__(self, risk_free, beta, expected_return):
        self.risk_free = risk_free
        self.beta = beta
        self.expected_return = expected_return
        self.calculate()

    def calculate(self):
        self.result = self.risk_free + self.beta * (self.expected_return - self.risk_free)

