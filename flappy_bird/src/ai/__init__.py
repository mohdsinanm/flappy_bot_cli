"""
AI module for flappy_bot_cli.

Provides:
- NeuralNetwork: Binary classification neural network using NumPy
- GameSensor: Feature extraction from game state
- EnhancedGameSensor: Enhanced feature extraction with 12 features
"""

from src.ai.neural_net import NeuralNetwork
from src.ai.game_sensor import GameSensor
from src.ai.ai_game_runner import EnhancedGameSensor

__all__ = ['NeuralNetwork', 'GameSensor', 'EnhancedGameSensor']
