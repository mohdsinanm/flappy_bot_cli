import subprocess
from src.common.Start import SetupGame

game_obj = SetupGame()
clear_cmd = game_obj.clear_cmd

def hit_detection(hit: int, count: int) -> bool:
    """
    Checks if the player has lost all lives in the game.

    This function evaluates the number of hits the player has taken. If the number of hits
    reaches zero, it clears the console, displays a "GAME OVER" message along with the final score,
    and returns True to indicate that the game should end.

    Parameters:
        hit (int): The current number of lives remaining for the player.
        count (int): The current score of the player.

    Returns:
        bool: True if the game is over (when hit is 0), False otherwise.
    """
    
    if hit == 0:
        subprocess.run(clear_cmd, shell=True)
        print("GAME OVER")
        print("SCORE = [ {} ]\n\n".format(count))
        return True
    return False

def lower_boundary_detection(lower_boundary_limit: int, count: int) -> bool:
    """
    Checks if the playable character has fallen below the lower boundary of the game.

    This function evaluates the vertical position of the character against a defined lower boundary limit.
    If the character's position exceeds this limit, it clears the console, displays a "GAME OVER" message
    along with the final score, and returns True to indicate that the game should end.

    Parameters:
        lower_boundary_limit (int): The current vertical position of the playable character.
        count (int): The current score of the player.

    Returns:
        bool: True if the game is over (when the character exceeds the lower boundary), False otherwise.
    """
    
    if lower_boundary_limit >= 25:  # 25 is the defined lower boundary limit
        subprocess.run(clear_cmd, shell=True)
        print("GAME OVER")
        print("SCORE = [ {} ]\n\n".format(count))
        return True
    return False
    
def upper_boundary_detection(upper_boundary_limit: int, count: int) -> bool:
    """
    Checks if the playable character has exceeded the upper boundary of the game.

    This function evaluates the vertical position of the character against a defined upper boundary limit.
    If the character's position falls below this limit, it clears the console, displays a "GAME OVER" message
    along with the final score, and returns True to indicate that the game should end.

    Parameters:
        upper_boundary_limit (int): The current vertical position of the playable character.
        count (int): The current score of the player.

    Returns:
        bool: True if the game is over (when the character exceeds the upper boundary), False otherwise.
    """
    
    if upper_boundary_limit <= 0:  # 0 is the defined upper boundary limit
        subprocess.run(clear_cmd, shell=True)
        print("GAME OVER")
        print("SCORE = [ {} ]\n\n".format(count))
        return True
    return False