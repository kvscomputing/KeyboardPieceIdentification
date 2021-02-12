
import cPickle
import gzip
import numpy as np

class Network(object):

    def __init__(self, sizes):
        self.layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def output(self, input):
        for bias, weight in zip(self.biases, self.weights):
            output = sigmoid(np.dot(weight, output) + bias)
        return output

    def gradient_descent(self, training_data, epoch, batch_size, learning_rate, test_data=None):
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

    def learn(self, batch, learning_rate):
        gradient_bias = [np.zeros(b.shape) for b in self.biases]
        gradient_weight = [np.zeros(w.shape) for w in self.weights]
        for i, j in batch:
            delta_gradient_bias, delta_gradient_weight = self.backpropagation(i, j)
            gradient_bias = [a + b for a, b in zip(gradient_bias, delta_gradient_bias)]
            gradient_weight = [a + b for a, b in zip(gradient_weight, delta_gradient_weight)]
        self.biases = [a - b*(learning_rate/len(batch)) for a, b in zip(self.biases, gradient_bias)]
        self.weights = [a - b*(learning_rate/len(batch)) for a, b in zip(self.weights, gradient_weight)]

    def backpropagation(self, bias, weight):
        gradient_bias = [np.zeros(b.shape) for b in self.biases]
        gradient_weight = [np.zeros(w.shape) for w in self.weights]
        cur = bias
        activations = [bias]
        z_vector = []
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation) + b
            z_vector.append(z)
            activation = sigmoid(z)
            activations.append(z)
        delta = self.derivative(activations[-1], weight) * \ sigmoid_deriv(z_vector[-1])
        gradient_bias[-1] = delta
        gradient_weight[-1] = np.dot(delta, activations[-2].transpose())
        for i in range(2, self.layers):
            z = z_vector[-i]
            s = sigmoid_deriv(z)
            delta = np.dot(self.weight[-i+1].transpose(), delta) * s
            gradient_bias[-i] = delta
            gradient_weight[-1] = np.dot(delta, activations[-i-1].transpose())
        return gradient_bias, gradient_weight

    def evaluate(self, test_data):
        result = [(np.argmax(self.output(x)), y) for (x,y) in test_data]
        return sum(int(x == y) for x, y in result)

    def derivative(self, activations, weight):
        return (activations-weight)

def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))

def sigmoid_deriv(x):
    return sigmoid(x) * (1-sigmoid(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
