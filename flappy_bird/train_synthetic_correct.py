"""
Synthetic correct training data - no simulation needed
"""

import numpy as np
from src.ai.ai_game_runner import EnhancedGameSensor
from src.ai.neural_net import NeuralNetwork

print("Generating Synthetic Training Data with Correct Labels")
print("="*70)

X_data = []
y_data = []

# Generate many game scenarios
np.random.seed(42)

# For each gap position
for gap_pos in range(5, 15):  # Gap can be at positions 5-14
    gap_center = gap_pos + 1.5
    
    # For each character position
    for char_pos in range(2, 23):  # Character can be at 2-22
        # Generate multiple feature variations
        for pipe_dist in np.linspace(5, 70, 10):  # Pipes at different distances
            for prev_pos in [char_pos - 1, char_pos, char_pos + 1]:  # Different velocities
                # Create feature state
                state = EnhancedGameSensor.get_enhanced_state(char_pos, 15, int(pipe_dist), gap_pos, prev_pos)
                
                # CORRECT LOGIC: Jump if below gap center
                action = 1 if char_pos > gap_center else 0
                
                X_data.append(state)
                y_data.append(action)

print(f"Generated {len(X_data)} synthetic examples")

X_train = np.array(X_data, dtype=np.float32)
y_train = np.array(y_data, dtype=np.float32).reshape(-1, 1)

jump_count = np.sum(y_train)
fall_count = len(y_train) - jump_count
print(f"Jump (1): {int(jump_count)} ({100*jump_count/len(y_train):.1f}%)")
print(f"Fall (0): {int(fall_count)} ({100*fall_count/len(y_train):.1f}%)")

print("\n" + "="*70)
print("Training Network...")

nn = NeuralNetwork(input_size=12, hidden_size=32, output_size=2, learning_rate=0.01)
num_epochs = 200
batch_size = 64

best_accuracy = 0

for epoch in range(num_epochs):
    indices = np.random.permutation(len(X_train))
    X_shuffled = X_train[indices]
    y_shuffled = y_train[indices]
    
    epoch_loss = 0
    num_batches = 0
    
    for i in range(0, len(X_train), batch_size):
        X_batch = X_shuffled[i:i+batch_size]
        y_batch = y_shuffled[i:i+batch_size]
        
        y_batch_onehot = np.zeros((len(y_batch), 2))
        y_batch_onehot[np.arange(len(y_batch)), y_batch.astype(int).flatten()] = 1
        
        output = nn.forward(X_batch)
        loss = -np.mean(y_batch_onehot * np.log(output + 1e-8))
        epoch_loss += loss
        num_batches += 1
        
        nn.backward(X_batch, y_batch_onehot, output)
    
    avg_loss = epoch_loss / num_batches
    
    if (epoch + 1) % 50 == 0:
        pred, _ = nn.predict(X_train)
        correct = np.sum(pred == y_train.flatten())
        accuracy = correct / len(y_train)
        print(f"Epoch {epoch+1:3d}: Loss={avg_loss:.4f}, Accuracy={accuracy:.1%}")
        best_accuracy = max(best_accuracy, accuracy)

print("\n" + "="*70)
pred, _ = nn.predict(X_train)
correct = np.sum(pred == y_train.flatten())
final_accuracy = correct / len(y_train)
print(f"Final Accuracy: {final_accuracy:.1%}")

np.save('models/learned_synthetic_corrected.npy', {'W1': nn.W1, 'b1': nn.b1, 'W2': nn.W2, 'b2': nn.b2}, allow_pickle=True)
print("Saved to: models/learned_synthetic_corrected.npy")
