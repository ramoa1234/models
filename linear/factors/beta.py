from alpha import get_alpha

#ROR(rate of return) = mean(new - original) / original 



def get_beta(result, beta, error_term):
    alpha = get_alpha(result, beta)
    result = alpha + beta * result + error_term
    

    