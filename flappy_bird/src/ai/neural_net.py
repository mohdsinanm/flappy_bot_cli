import numpy as np


class NeuralNetwork:
    """
    A simple feedforward neural network for binary classification using NumPy.
    
    Architecture:
    - Input Layer: 6 features (game state)
    - Hidden Layer: 16 neurons with ReLU activation
    - Output Layer: 2 neurons with softmax (jump or no-jump)
    
    This network learns to make jump/no-jump decisions based on surrounding game values.
    """
    
    def __init__(self, input_size=6, hidden_size=16, output_size=2, learning_rate=0.01):
        """
        Initialize the neural network with random weights and biases.
        
        Parameters:
            input_size (int): Number of input features (default: 6)
            hidden_size (int): Number of neurons in hidden layer (default: 16)
            output_size (int): Number of output classes (default: 2 for binary)
            learning_rate (float): Learning rate for weight updates (default: 0.01)
        """
        self.learning_rate = learning_rate
        
        # Initialize weights with Xavier initialization
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(1.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(1.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))
        
        # Store activations for backpropagation
        self.cache = {}
    
    def relu(self, z):
        """ReLU activation function"""
        return np.maximum(0, z)
    
    def relu_derivative(self, z):
        """Derivative of ReLU for backpropagation"""
        return (z > 0).astype(float)
    
    def softmax(self, z):
        """Softmax activation for output layer"""
        exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # For numerical stability
        return exp_z / np.sum(exp_z, axis=1, keepdims=True)
    
    def forward(self, X):
        """
        Forward pass through the network.
        
        Parameters:
            X: Input features of shape (batch_size, input_size)
            
        Returns:
            Output probabilities of shape (batch_size, 2)
        """
        # Hidden layer
        Z1 = np.dot(X, self.W1) + self.b1
        A1 = self.relu(Z1)
        
        # Output layer
        Z2 = np.dot(A1, self.W2) + self.b2
        A2 = self.softmax(Z2)
        
        # Cache for backpropagation
        self.cache = {'Z1': Z1, 'A1': A1, 'Z2': Z2, 'A2': A2, 'X': X}
        
        return A2
    
    def backward(self, X, y, output):
        """
        Backward pass (backpropagation) to compute gradients.
        
        Parameters:
            X: Input features
            y: True labels (one-hot encoded)
            output: Predicted output from forward pass
        """
        m = X.shape[0]
        
        # Output layer gradient
        dZ2 = output - y
        dW2 = np.dot(self.cache['A1'].T, dZ2) / m
        db2 = np.sum(dZ2, axis=0, keepdims=True) / m
        
        # Hidden layer gradient
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * self.relu_derivative(self.cache['Z1'])
        dW1 = np.dot(X.T, dZ1) / m
        db1 = np.sum(dZ1, axis=0, keepdims=True) / m
        
        # Update weights and biases
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
    
    def train(self, X, y, epochs=100):
        """
        Train the neural network.
        
        Parameters:
            X: Training features of shape (num_samples, 6)
            y: Training labels (one-hot encoded) of shape (num_samples, 2)
            epochs (int): Number of training iterations
        """
        losses = []
        
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X)
            
            # Backward pass
            self.backward(X, y, output)
            
            # Calculate loss (cross-entropy)
            loss = -np.mean(y * np.log(output + 1e-8))
            losses.append(loss)
            
            if (epoch + 1) % 10 == 0:
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")
        
        return losses
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Parameters:
            X: Input features of shape (batch_size, 6) or (6,)
            
        Returns:
            Predicted class (0 or 1) and probabilities
        """
        # Handle single sample
        if X.ndim == 1:
            X = X.reshape(1, -1)
        
        output = self.forward(X)
        predictions = np.argmax(output, axis=1)
        
        return predictions, output
    
    def save(self, filepath):
        """Save network weights to a file"""
        np.save(filepath, {
            'W1': self.W1,
            'b1': self.b1,
            'W2': self.W2,
            'b2': self.b2,
            'learning_rate': self.learning_rate
        })
        print(f"Model saved to {filepath}")
    
    def load(self, filepath):
        """Load network weights from a file"""
        data = np.load(filepath, allow_pickle=True).item()
        self.W1 = data['W1']
        self.b1 = data['b1']
        self.W2 = data['W2']
        self.b2 = data['b2']
        self.learning_rate = data['learning_rate']
        print(f"Model loaded from {filepath}")
