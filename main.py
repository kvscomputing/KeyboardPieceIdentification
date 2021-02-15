# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cPickle
import gzip
import numpy as np

class CrossEntropy(object):
    @staticmethod
    def f(a,y):
        return np.sum(np.nan_to_num(-y*np.log(a) + (1-y)*np.log(1-a)))

    @staticmethod
    def delta(a,y):
        return (a-y)


class Network(object):

    def __init__(self, sizes):
        self.layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)/np.sqrt(x)
                        for x, y in zip(sizes[:-1], sizes[1:])]
        self.cost = cost

    def output(self, input):
        for bias, weight in zip(self.biases, self.weights):
            output = sigmoid(np.dot(weight, output) + bias)
        return output

    def gradient_descent(self, training_data, epoch, batch_size, learning_rate, lmb, test_data=None):
        for i in range(epoch):
            random.shuffle(training_data)
            batches = []
            for i in range(0,len(training_data),batch_size):
                batches.append(training_data[i: i+batch_size])
            for batch in batches:
                self.learn(batch, learning_rate)
            if test_data:
                print("Epoch {0}: {1}/{2}".format(j, self.evaluate(test_data), len(test_data)))
            else:
                print("Epoch {0} done".format(j))

    def learn(self, batch, learning_rate, lmb):
        gradient_bias = [np.zeros(b.shape) for b in self.biases]
        gradient_weight = [np.zeros(w.shape) for w in self.weights]
        for i, j in batch:
            delta_gradient_bias, delta_gradient_weight = self.backpropagation(i, j)
            gradient_bias = [a + b for a, b in zip(gradient_bias, delta_gradient_bias)]
            gradient_weight = [a + b for a, b in zip(gradient_weight, delta_gradient_weight)]
        self.biases = [(1-learning_rate*(lmb/n))*a - b*(learning_rate/len(batch)) for a, b in zip(self.biases, gradient_bias)]
        self.weights = [a - b*(learning_rate/len(batch)) for a, b in zip(self.weights, gradient_weight)]

    def backpropagation(self, a, b):
        gradient_bias = [np.zeros(b.shape) for b in self.biases]
        gradient_weight = [np.zeros(w.shape) for w in self.weights]
        activation = a
        activations = [a]
        z_vector = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            z_vector.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        delta = (self.cost).delta(activations[-1],y)
        gradient_bias[-1] = delta
        gradient_weight[-1] = np.dot(delta, activations[-2].transpose())
        for i in range(2, self.layers):
            z = z_vector[-i]
            s = sigmoid_deriv(z)
            delta = np.dot(self.weights[-i+1].transpose(), delta) * s
            gradient_bias[-i] = delta
            gradient_weight[-i] = np.dot(delta, activations[-i-1].transpose())
        return (gradient_bias, gradient_weight)

    def evaluate(self, test_data):
        result = [(np.argmax(self.output(x)), np.argmax(y)) for (x,y) in test_data]
        return sum(int(x == y) for x, y in result)

    def derivative(self, activations, weight):
        return (activations-weight)

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def sigmoid_deriv(x):
    return sigmoid(x) * (1-sigmoid(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
