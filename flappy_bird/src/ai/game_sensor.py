import numpy as np


class GameSensor:
    """
    Extracts game state features for the neural network input.
    
    Features extracted:
    1. Distance to next pipe (normalized)
    2. Vertical gap position (normalized)
    3. Character vertical position (normalized)
    4. Character vertical velocity (normalized)
    5. Distance to top boundary (normalized)
    6. Distance to bottom boundary (normalized)
    """
    
    # Game constants
    MAX_HEIGHT = 25  # Maximum vertical position
    MAX_WIDTH = 80   # Maximum horizontal position
    
    @staticmethod
    def get_state(c, d, a, b, previous_c=None):
        """
        Extract normalized features from game state.
        
        Parameters:
            c (int): Character vertical position (0-25)
            d (int): Character horizontal position (15)
            a (int): Pipe horizontal position (scrolls left)
            b (int): Passage space (gap between pipes, ~5-15)
            previous_c (int): Previous vertical position for velocity calculation
            
        Returns:
            numpy array of shape (6,) with normalized features in range [-1, 1]
        """
        
        # Feature 1: Distance to next pipe (normalized)
        # Positive means pipe is approaching
        distance_to_pipe = (a - d) / GameSensor.MAX_WIDTH
        
        # Feature 2: Vertical gap center position (normalized)
        gap_center = (b + 2) / GameSensor.MAX_HEIGHT  # Center of the passage
        gap_center_normalized = (gap_center - 0.5) * 2  # Scale to [-1, 1]
        
        # Feature 3: Character vertical position (normalized)
        char_position = (c / GameSensor.MAX_HEIGHT - 0.5) * 2  # Scale to [-1, 1]
        
        # Feature 4: Character vertical velocity (normalized)
        if previous_c is not None:
            velocity = (c - previous_c) / GameSensor.MAX_HEIGHT
        else:
            velocity = 0.0
        
        # Feature 5: Distance to top boundary (normalized)
        distance_to_top = c / GameSensor.MAX_HEIGHT
        
        # Feature 6: Distance to bottom boundary (normalized)
        distance_to_bottom = (GameSensor.MAX_HEIGHT - c) / GameSensor.MAX_HEIGHT
        
        # Combine all features
        features = np.array([
            distance_to_pipe,
            gap_center_normalized,
            char_position,
            velocity,
            distance_to_top,
            distance_to_bottom
        ], dtype=np.float32)
        
        return features
    
    @staticmethod
    def normalize_features(features):
        """
        Ensure all features are in valid range [-1, 1].
        
        Parameters:
            features: numpy array of features
            
        Returns:
            Clipped features in range [-1, 1]
        """
        return np.clip(features, -1.0, 1.0)
