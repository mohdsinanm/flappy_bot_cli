import subprocess, time, emoji
import keyboard
from ..common.Start import SetupGame, SetupCharacter
from ..common.Physics import GamePhysics
from ..utils.spwaners import *
from ..utils.detecters import *
from ..ai.game_sensor import GameSensor
from ..ai.ai_game_runner import EnhancedGameSensor
from ..ai.neural_net import NeuralNetwork
import numpy as np

character = SetupCharacter()

c = character.i
d = character.j #Coordinates of playable character
kill = character.kill
hit_sprite = character.hit_sprite
count = character.count #score
hit = character.hit #life
a = 0  # view window position
b = 0  # gap position

def flappy_main():
    """
    Main game loop for a text-based game that simulates a character navigating through obstacles.

    This function initializes the game setup, manages the game loop, and handles the rendering of the game state.
    It continuously updates the game state based on player interactions and physics, checks for collisions,
    and manages scoring and lives. The game runs until the player loses all lives or reaches a defined boundary.

    The game features:
    - A view window that moves to simulate scrolling.
    - Obstacles represented by chains and a playable character represented by an alien monster emoji.
    - Life and score mechanics that affect gameplay.
    - Collision detection with obstacles and boundaries.
    - A speed control mechanism that adjusts the game speed based on the player's score.

    Global variables used:
        - c: Current vertical position of the playable character.
        - d: Current horizontal position of the playable character.
        - hit: Number of hits taken by the player.
        - hit_sprite: Boolean flag indicating if a collision has occurred.
        - kill: Boolean flag indicating if the game should end.

    Returns:
        bool: True if the game ends due to a loss of life or boundary collision, False otherwise.

    Note:
        The function uses the `emoji` library for rendering emojis and `subprocess` for clearing the console.
        The game speed is controlled by a multiplier that decreases as the score increases.
    """

    global c,d,hit,hit_sprite, kill, a, b
    multip = 0.1 # this will controls the speed of the game , if increased the speed will reduce
    while True:
        game_setup = SetupGame()
        a = game_setup.view_window_length  #this variable controls the visibility (view window) decrease to shorten the window,together with second fore loop
        b = game_setup.passage_space # var for producing the passage

        x_window = game_setup.x_window
        y_window = game_setup.y_window

        l_c = game_setup.life_coordinate #this random choice determine the coordinate of life
        life = game_setup.life

        s_c = game_setup.score_coordinate #this random choice determine the coordinates of multiplier cross
        score = game_setup.score

        clear_cmd = game_setup.clear_cmd

        
        
        while True:     
            global count  
            for i in range(x_window):
                print()
                for j in range(y_window):#for the collision object
                    if j == a or j == a+5:
                        if i == b:
                            continue
                        elif i == b+1:
                            continue
                        elif i == b+2:
                            continue
                        elif i == b+3:
                            continue
                        print(emoji.emojize(":chains:"), end="")

                    else:
                        if i == (x_window-2):#when the i (the vertical componant) hit 23 the lower boundary is printed,else evry time space is printed
                            print('_',end='')
                        else:
                            print(" ", end="")

                    
                    if life_spawner(life, i , j, l_c, a, c, d ):
                        hit += 1
                        life = False

                    if muliplier_spawner(score, i, j , s_c, a, c, d):
                        count *= 2 
                        score = False

                    if i == c and j == d:#printing the playable object
                        print(emoji.emojize(":alien_monster:"), end="")
                    if hit_sprite:
                        if i == c and j == d:
                            print(emoji.emojize(":collision:"), end="")
                            
                            hit_sprite= False
            #physics
            physics = GamePhysics()
            c += physics.gravity_increment #added physics(gravity 1 block per iteration) and removed the up navigation

            if a == d:#collision identifier  and hiting monitering
                if c in {b, b+1, b+2,b+3}:#if the position of a ( the position of the pipe) = the position of bird (d) check if the c cordinate is in the predicted random cordinate b,b+1,b+2
                    pass
                else:# if else mark a hit
                    hit -=1
                    hit_sprite = True

            # life detction
            if hit_detection(hit, count):
                kill = True
                a = 0
                break

            # lower boundary detection
            if lower_boundary_detection(c, count):

                kill = True
                a = 0
                break

            # upper  boundary detection
            if upper_boundary_detection(c, count):
                kill = True
                a = 0
                break

            #execution
            if kill: 
                break    
                
                    
            # window speed       
            a -= 1
            if count%1 == 0 and count != 0:#it will increase the speed by decreaseing the delay according to the score
                if a == a-1:
                    multip *= .99
                
            time.sleep(multip)
            print("Score [ {} ]".format(count)+(emoji.emojize(":red_heart:"*hit)), end="")
            

            
            subprocess.run(clear_cmd, shell =True)
            if a <= 0:break
        
        count += 1
        if kill: 
            break
    return kill


def key():
    """
    Monitors keyboard input to control the playable character's actions in the game.

    This function runs in an infinite loop, checking for specific key presses:
    - Pressing "w" decreases the vertical position of the playable character (c) by 2,
      effectively allowing the character to jump or counteract gravity.
    - Pressing "x" sets the global variable `kill` to True, signaling that the game should end.

    The function will terminate when the `kill` variable is set to True, either by pressing "x"
    or by other game conditions that may set `kill` to True.

    Global variables used:
        - c: Current vertical position of the playable character.
        - kill: Boolean flag indicating if the game should end.

    Returns:
        bool: True if the game should end (when `kill` is set to True), False otherwise.
    
    Note:
        This function relies on the `keyboard` library to detect key presses.
        It runs indefinitely until the game is signaled to end.
    """
    
    global c
    while True:
        if keyboard.read_key() == "w":
            c -= 2 #balanced the gravity
        elif keyboard.read_key() == "x":
            global kill 
            kill= True
        if kill: 
            break
    return kill


def ai_key():
    """
    AI input provider that makes decisions based on the game state.
    Uses the corrected neural network model to decide when to jump.
    Replaces keyboard input with AI decisions.
    """
    global c, d, a, b, kill, count
    
    # Load corrected AI model
    try:
        nn = NeuralNetwork(input_size=12, hidden_size=32, output_size=2)
        data = np.load('models/learned_synthetic_corrected.npy', allow_pickle=True).item()
        nn.W1 = data['W1']
        nn.b1 = data['b1']
        nn.W2 = data['W2']
        nn.b2 = data['b2']
        print(f"[AI] Model loaded successfully. Weights shape: W1={nn.W1.shape}, W2={nn.W2.shape}")
    except Exception as e:
        print(f"[AI] Error loading model: {e}")
        import traceback
        traceback.print_exc()
        return
    
    previous_c = c
    iteration = 0
    decision_count = [0, 0]  # [fall, jump]
    
    while True:
        try:
            # Get current game state
            state = EnhancedGameSensor.get_enhanced_state(c, d, a, b, previous_c)
            pred, prob = nn.predict(state)
            action = int(pred[0])  # pred is already the argmax result
            previous_c = c
            
            # Track decisions
            decision_count[action] += 1
            
            # Execute AI action
            if action == 1:  # Jump
                c -= 2
            
            # Detailed logging every 100 iterations
            if iteration % 100 == 0:
                gap_center = b + 1.5
                print(f"\n[AI] Iter {iteration}: pos={c:.1f}, gap={gap_center:.1f}, d={d:.1f}, a={a:.1f}, prob={prob}, action={action}")
            
            iteration += 1
        except Exception as e:
            print(f"[AI] Error during prediction at iteration {iteration}: {e}")
            import traceback
            traceback.print_exc()
            break
        
        # Small delay to not overwhelm the main loop
        time.sleep(0.001)
        
        if kill:
            break
    
    print(f"[AI] Game ended. Total iterations: {iteration}, Score: {count}, Decisions: Fall={decision_count[0]}, Jump={decision_count[1]}")
    return kill
