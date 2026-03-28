"""
AI Game Runner - Run the flappy bird game with an AI agent.

This module provides functions to run the game with an AI player
instead of keyboard input.
"""

import subprocess
import time
import emoji
import numpy as np
from src.common.Start import SetupGame, SetupCharacter
from src.common.Physics import GamePhysics
from src.utils.spwaners import *
from src.utils.detecters import *


# Enhanced sensor with 12 features (for learned model)
class EnhancedGameSensor:
    """Enhanced feature extraction for better learning."""
    
    MAX_HEIGHT = 25
    MAX_WIDTH = 80
    
    @staticmethod
    def get_enhanced_state(c, d, a, b, prev_c=None):
        """Extract 12 enhanced features."""
        gap_center = b + 1.5
        distance_to_pipe = (a - d) / EnhancedGameSensor.MAX_WIDTH
        gap_center_norm = ((gap_center - 12.5) / 12.5)
        char_position = ((c - 12.5) / 12.5)
        
        velocity = 0 if prev_c is None else ((c - prev_c) / EnhancedGameSensor.MAX_HEIGHT)
        distance_to_top = c / EnhancedGameSensor.MAX_HEIGHT
        distance_to_bottom = (EnhancedGameSensor.MAX_HEIGHT - c) / EnhancedGameSensor.MAX_HEIGHT
        
        distance_to_gap_center = (c - gap_center) / EnhancedGameSensor.MAX_HEIGHT
        above_gap = 1.0 if c < gap_center - 0.5 else 0.0
        below_gap = 1.0 if c > gap_center + 1.5 else 0.0
        
        predicted_c = c + 1
        predicted_distance = (predicted_c - gap_center) / EnhancedGameSensor.MAX_HEIGHT
        
        will_be_too_low = 1.0 if predicted_c > gap_center + 2 else 0.0
        
        features = np.array([
            distance_to_pipe,
            gap_center_norm,
            char_position,
            velocity,
            distance_to_top,
            distance_to_bottom,
            distance_to_gap_center,
            above_gap,
            below_gap,
            predicted_distance,
            will_be_too_low,
            1.0 if velocity > 0 else 0.0,
        ], dtype=np.float32)
        
        return np.clip(features, -1.0, 1.0)
