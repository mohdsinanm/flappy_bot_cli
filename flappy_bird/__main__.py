from src.core.flappy_core import flappy_main, key, ai_key
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


def main_ai():
    """
    Run the game with AI player using the corrected neural network model.
    The main game loop runs in one thread, and the AI input provider runs in another.
    """
    t1 = threading.Thread(target=flappy_main)  # Thread for the main game loop
    t2 = threading.Thread(target=ai_key)        # Thread for AI input instead of keyboard
    t2.start()                                   # Start the AI input thread
    t1.start()                                   # Start the main game loop thread
    t2.join()                                    # Wait for AI input thread to finish
    t1.join()                                    # Wait for main loop to finish


def startup_screen():
    return f"""
    Player           :     {emoji.emojize(":alien_monster:")} , This is your playable character
    Extra life       :     {emoji.emojize(":red_heart:")} , Collect this for extra life
    Score multiplier :     {emoji.emojize(":cross_mark:")} , Collect this for 2x score

    Use 'W' key to jump
    Use 'X' to stop the game
                                
                                Please expand your window to maximum size
    """

if __name__ == '__main__':
    print(startup_screen())
    choice = str(input('Ready to play ? [Y/N/AI] : ')).upper()
    if choice == 'Y':
        main()  # Execute the main function if the script is run directly
    elif choice == 'AI':
        print("\n🤖 Starting AI Game Mode...\n")
        main_ai()  # Run with AI
    else:
        print("Thank you , Try next time")