from src.core.flappy_core import flappy_main, key
import threading
import emoji

def main():
    """
    Entry point for the game that initializes and starts the main game loop and keyboard input handling.

    This function creates two threads:
    - One thread runs the main game loop (`flappy_main`), which handles the game logic and rendering.
    - The second thread monitors keyboard input (`key`), allowing the player to control the character.

    The function starts both threads and waits for them to complete using `join()`. The game will continue
    running until the player loses all lives or chooses to exit the game.

    Note:
        This function requires the `threading` module to run the game and input handling concurrently.
        The `flappy_main` function is expected to contain the main game logic, while the `key` function
        handles user input for controlling the game.

    Example:
        To run the game, simply call `main()` when the script is executed.
    """
    
    t1 = threading.Thread(target=flappy_main)  # Thread for the main game loop
    t2 = threading.Thread(target=key)           # Thread for handling keyboard input
    t2.start()                                   # Start the input handling thread
    t1.start()                                   # Start the main game loop thread
    t2.join()                                    # Wait for the input handling thread to finish
    t1.join()                                    # Wait for the main game loop thread to finish


def startup_screen():
    return f"""
    Player           :     {emoji.emojize(":alien_monster:")} , This is your playable character
    Extra life       :     {emoji.emojize(":red_heart:")} , Collect this for extra life
    Score multiplier :     {emoji.emojize(":cross_mark:")} , Collect this for 2x score

    Use 'W' key to jump
    Use 'X' to stop the game
    """

if __name__ == '__main__':
    print(startup_screen())
    if  'Y' == str(input('Ready to play ? [Y/N] : ')).upper():
        main()  # Execute the main function if the script is run directly
    else:
        print("Thank you , Try next time")