# flappy_bot_cli

## Description
The Flappy bot Game is a fun and engaging text-based game inspired by the classic Flappy Bird. Players control an bot character as it navigates through obstacles, collecting extra lives and score multipliers. The objective is to survive as long as possible while achieving the highest score.
![Capture](https://github.com/user-attachments/assets/df57a264-d740-4150-b655-8acfe08e9e5e)

## Features
- **Playable Character**: Control a bot represented by an emoji.
- **Collectibles**: Gather extra lives (❤️) and score multipliers (❌) to enhance your gameplay.
- **Simple Controls**: Use the keyboard to jump and stop the game.
- **Game Over Conditions**: The game ends when the player runs out of lives or collides with obstacles or boundaries.
- **Score Tracking**: Keep track of your score as you collect items.

## AI Implementation

This project includes an AI-powered bot that can play the Flappy Bird game autonomously using machine learning. The AI is implemented using a neural network trained on synthetic data to make optimal jump decisions.

### AI Architecture

The AI system consists of three main components:

1. **Game Sensor** (`src/ai/game_sensor.py` and `src/ai/ai_game_runner.py`)
   - Extracts 12 features from the current game state
   - Features include: distance to pipe, gap position, character position, velocity, distances to boundaries, and predictive features

2. **Neural Network** (`src/ai/neural_net.py`)
   - Simple feedforward neural network with one hidden layer
   - Input layer: 12 neurons (game state features)
   - Hidden layer: 32 neurons with ReLU activation
   - Output layer: 2 neurons with softmax (jump/no-jump decision)

3. **AI Game Runner** (`src/core/flappy_core.py`)
   - Integrates the trained model into the game loop
   - Makes real-time decisions during gameplay
   - Replaces keyboard input with AI predictions

### Training Process

The AI is trained using synthetic data generation rather than actual gameplay experience:

1. **Data Generation** (`train_synthetic_correct.py`)
   - Generates thousands of game scenarios with varying pipe positions, character positions, and velocities
   - Uses perfect knowledge of the game mechanics to label correct actions
   - Correct logic: Jump if the character is below the gap center, otherwise fall

2. **Training Algorithm**
   - Uses backpropagation with cross-entropy loss
   - Xavier weight initialization for better convergence
   - Batch training with 64 samples per batch
   - 200 epochs of training
   - Learning rate: 0.01

3. **Model Persistence**
   - Trained weights saved to `models/learned_synthetic_corrected.npy`
   - Model achieves near-perfect accuracy on training data

### Feature Extraction

The AI extracts 12 normalized features from the game state:

- Distance to next pipe (normalized 0-1)
- Gap center position (normalized -1 to 1)
- Character vertical position (normalized -1 to 1)
- Character velocity (change in position)
- Distance to top boundary
- Distance to bottom boundary
- Distance to gap center
- Binary flags for above/below gap
- Predicted next position distance to gap
- Flag for if next position would be too low
- Velocity direction indicator

All features are clipped to the range [-1, 1] for neural network input.

### Running the AI

To run the game with AI:

```bash
python flappy_bird/__main__.py
```

When prompted, enter 'AI' to start AI mode. The AI will automatically control the character and attempt to navigate through the pipes indefinitely.

### AI Performance

- The trained AI can achieve very high scores by making optimal jump decisions
- Uses perfect game knowledge encoded in the training data
- Makes decisions in real-time with minimal latency
- Provides detailed logging of decisions and game state during play

### Future Improvements

Potential enhancements to the AI system:

- Train on actual gameplay data instead of synthetic data
- Implement reinforcement learning (Q-learning, PPO)
- Add convolutional layers for processing raw game screen
- Multi-objective optimization (score + survival time)
- Hyperparameter tuning and model architecture search

## Installation
- To run the game, you need to have Python installed on your machine. 
- For Windows use the following commands

   ```
   git clone https://github.com/mohdsinanm/flappy_bot_cli
   cd flappy_bot_cli

   pip install -r requirements.txt

   python flappy_bird/__main__.py

   ```

- On Linux, the keyboard module may require superuser privileges. To run your script with the necessary permissions, use the following command

   ```
   git clone https://github.com/mohdsinanm/flappy_bot_cli
   cd flappy_bot_cli

   pip install -r requirements.txt

   sudo python flappy_bird/__main__.py

   ```
