import random


class SetupCharacter:
    """
    Class to initialize and manage the state of the playable character in the game.

    Attributes:
        i (int): The vertical coordinate of the playable character.
        j (int): The horizontal coordinate of the playable character.
        kill (bool): A flag indicating whether the game should end (True if the character is dead).
        hit_sprite (bool): A flag indicating if the character has collided with an obstacle.
        count (int): The score of the player, initialized to 0.
        hit (int): The number of lives the character has, initialized to 3.

    Methods:
        __init__: Initializes the character's position, score, and life attributes.
    """
    
    def __init__(self):
        self.i = 5  # i Coordinates of playable character
        self.j = 15  # j Coordinates of playable character
        self.kill = False
        self.hit_sprite = False
        self.count = 0  # score
        self.hit = 3  # life


class SetupGame:
    """
    Class to initialize and manage the game setup parameters.

    Attributes:
        view_window_length (int): The length of the view window, controlling the visibility of the game area.
        passage_space (int): A random integer determining the space between obstacles in the game.
        life_coordinate (int): A random integer determining the vertical coordinate for life pickups.
        life (bool): A flag indicating whether a life pickup is available (True) or not (False).
        score_coordinate (int): A random integer determining the vertical coordinate for score multipliers.
        score (bool): A flag indicating whether a score multiplier is available (True) or not (False).

    Methods:
        __init__: Initializes the game parameters, including view window length, passage space, and life/score coordinates.
    """
    
    def __init__(self):
        self.view_window_length = 70  # Controls the visibility (view window)
        self.passage_space = random.randint(5, 15)  # Space for producing the passage

        self.life_coordinate = random.randint(5, 10)  # Coordinate for life pickups
        self.life = random.choice([False ] * 10 + [True]  * 1)  # Randomly determine if a life is available

        self.score_coordinate = random.randint(5, 10)  # Coordinate for score multipliers
        self.score = random.choice([False]  * 30 + [True] * 1)  # Randomly determine if a score multiplier is available