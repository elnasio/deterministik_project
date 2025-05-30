import numpy as np


class SimpleMLP:
    def __init__(self, input_size, output_size):
        self.W = np.random.randn(input_size, output_size) * 0.01
        self.b = np.zeros((1, output_size))

    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / exp_x.sum(axis=1, keepdims=True)

    def predict(self, X):
        X = np.array(X)
        logits = np.dot(X, self.W) + self.b
        return self.softmax(logits)

    def train(self, X, y, epochs=1000, lr=0.1):
        X = np.array(X)
        y = np.array(y)
        for _ in range(epochs):
            logits = np.dot(X, self.W) + self.b
            probs = self.softmax(logits)
            grad_logits = probs - y
            grad_W = np.dot(X.T, grad_logits) / len(X)
            grad_b = np.mean(grad_logits, axis=0, keepdims=True)
            self.W -= lr * grad_W
            self.b -= lr * grad_b

    def save(self, path):
        np.savez(path, W=self.W, b=self.b)

    def load(self, path):
        data = np.load(path)
        self.W = data["W"]
        self.b = data["b"]
