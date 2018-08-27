import numpy as np

def sigmoid(data, coefficients): 
    z = np.dot(data, coefficients[1:]) + coefficients[0]
    result = 1.0 / (1.0 + np.exp(-z))  
    return result

def logistic_regression(data, labels, weights, num_epochs, learning_rate): # do not change the heading of the function
    for i in range(num_epochs):
        hx = sigmoid(data, weights)
        error = hx - labels
        gradient = data.T.dot(error)
        weights[0] -= learning_rate * error.sum()
        weights[1:] -= learning_rate * gradient

    return weights
    


    
