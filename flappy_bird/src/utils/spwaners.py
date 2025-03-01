
import emoji

def life_spawner(life: bool, i_coordinate: int, j_coordinate: int, life_coordinate: int, view_window: int, character_i: int, character_j: int) -> int:
    """
    Spawns a life pickup in the game at a specified coordinate.

    This function checks if a life pickup should be displayed based on the current game state.
    If the life is available and the character's position matches the life coordinate when the
    view window reaches a certain point, it prints a heart emoji. If the character collects the life,
    the function returns 1; otherwise, it returns 0.

    Parameters:
        life (bool): A flag indicating whether a life pickup is available.
        i_coordinate (int): The vertical coordinate of the current game state.
        j_coordinate (int): The horizontal coordinate of the current game state.
        life_coordinate (int): The vertical coordinate where the life pickup is located.
        view_window (int): The current position of the view window.
        character_i (int): The vertical position of the playable character.
        character_j (int): The horizontal position of the playable character.

    Returns:
        int: 1 if the life is collected, 0 otherwise.
    """
    i = i_coordinate
    j = j_coordinate

    if life:#life multiplier
        # there is a 1 in 10 chances of getting life multilier
        #if life is true when j reaches a-20 it will print a heart 
        if j == view_window - 20 and i == life_coordinate:
            print(emoji.emojize(":red_heart:"), end="")
            if abs(character_i - life_coordinate) < 2 and (character_j == j):
                life = False #then make it invisible
                return 1
            else:
                return 0
    return 0



def muliplier_spawner(score: bool, i_coordinate: int, j_coordinate: int, score_coordinate: int, view_window: int, character_i: int, character_j: int) -> bool:
    """
    Spawns a score multiplier in the game at a specified coordinate.

    This function checks if a score multiplier should be displayed based on the current game state.
    If the score multiplier is available and the character's position matches the score coordinate
    when the view window reaches a certain point, it prints a cross mark emoji. If the character collects
    the score multiplier, the function returns True; otherwise, it returns False.

    Parameters:
        score (bool): A flag indicating whether a score multiplier is available.
        i_coordinate (int): The vertical coordinate of the current game state.
        j_coordinate (int): The horizontal coordinate of the current game state.
        score_coordinate (int): The vertical coordinate where the score multiplier is located.
        view_window (int): The current position of the view window.
        character_i (int): The vertical position of the playable character.
        character_j (int): The horizontal position of the playable character.

    Returns:
        bool: True if the score multiplier is collected, False otherwise.
    """
    i = i_coordinate
    j = j_coordinate


    if score:#life multiplier
        # there is a 1 in 10 chances of getting life multilier
        #if life is true when j reaches a-20 it will print a heart 
        if j == view_window - 20 and i == score_coordinate:
            print(emoji.emojize(":cross_mark:"), end="")

            if abs(character_i - score_coordinate) < 2 and (character_j == j):
                score = False #then make it invisible
                return True
            else:
                return False
    return False

def player_spawner(hit_sprite_: bool, i_coordinate: int, j_coordinate: int, character_i: int, character_j: int) -> bool:
    """
    Spawns the playable character in the game at the specified coordinates.

    This function checks if the playable character's position matches the given coordinates.
    If they match, it prints the character's emoji. If a collision is detected (indicated by
    the hit_sprite_ flag), it prints a collision emoji and returns False to indicate that the
    character has collided with an obstacle.

    Parameters:
        hit_sprite_ (bool): A flag indicating if a collision has occurred.
        i_coordinate (int): The vertical coordinate of the current game state.
        j_coordinate (int): The horizontal coordinate of the current game state.
        character_i (int): The vertical position of the playable character.
        character_j (int): The horizontal position of the playable character.

    Returns:
        bool: False if a collision occurs, True otherwise.
    """
    
    if i_coordinate == character_i and j_coordinate == character_j:#printing the playable object
        print(emoji.emojize(":alien_monster:"), end="")
        if hit_sprite_:
            if i_coordinate == character_i and j_coordinate == character_j:#printing the playable object
                print(emoji.emojize(":collision:"), end="")
                
                return False