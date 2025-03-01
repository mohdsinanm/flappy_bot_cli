
class GamePhysics:
    """
    Class to manage the physics-related properties of the game.

    Attributes:
        gravity_increment (int): The amount by which the vertical position of the playable character
        is affected by gravity in each iteration of the game loop. Initialized to 1, representing
        a constant downward force.

    Methods:
        __init__: Initializes the gravity increment for the game.
    """
    
    def __init__(self):
        self.gravity_increment = 1  # The amount of gravity applied to the character each iteration