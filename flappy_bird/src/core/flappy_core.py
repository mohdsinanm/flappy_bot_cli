import subprocess, random, time, threading, emoji
import keyboard
from src.utils.Start import SetupGame, SetupCharacter
from src.utils.spwaners import life_spawner
character = SetupCharacter()

c = character.i
d = character.j #Coordinates of playable character
kill = character.kill
hit_sprite = character.hit_sprite
count = character.count #score
hit = character.hit #life

def main():

    global c,d,hit,hit_sprite, kill
    multip = 0.1 # this will controls the speed of the game , if increased the speed will reduce
    while True:
        game_setup = SetupGame()
        a = game_setup.view_window_length  #this variable controls the visibility (view window) decrease to shorten the window,together with second fore loop
        b = game_setup.passage_space # var for producing the passage

        l_c = game_setup.life_coordinate #this random choice determine the coordinate of life
        life = game_setup.life

        s_c = game_setup.score_coordinate #this random choice determine the coordinates of multiplier cross
        score = game_setup.score
        
        while True:     
            global count  
            for i in range(25):
                print()
                for j in range(80):#for the collision object
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
                        if i == 23:#when the i (the vertical componant) hit 23 the lower boundary is printed,else evry time space is printed
                            print('_',end='')
                        else:
                            print(" ", end="")

                    life_spawner(life, i , j, l_c, a, c, d  )
                    if life:#life multiplier
                        # there is a 1 in 10 chances of getting life multilier
                        #if life is true when j reaches a-20 it will print a heart 
                        if j == a-20 and i == l_c:
                            print(emoji.emojize(":red_heart:"), end="")
                            if ({c-1,d} == {j,l_c}) or ({c+1,d} == {j,l_c}) or ({c,d} == {j,l_c}):#this check the coordinate of bird is equal to the coordinale of heart
                                hit +=1 #give one heart
                                life = False #then make it invisible

                    if score:#score multiplier
                        # there is a 1 in 20 chances of getting score multilier
                        #if score is true when j reaches a-20 it will print a cross mark
                        if j == a-20 and i == s_c:
                            print(emoji.emojize(":cross_mark:"), end="")
                            if({c-1,d} == {j,l_c}) or ({c+1,d} == {j,l_c}) or ({c,d} == {j,l_c}):#this check the coordinate of bird is equal to the coordinale of cross mark
                                count *= 2 #doubles the scores
                                score = False #then make it invisible

                            

                    if i == c and j == d:#printing the playable object
                        print(emoji.emojize(":alien_monster:"), end="")
                    if hit_sprite:
                        if i == c and j == d:
                            print(emoji.emojize(":collision:"), end="")
                            
                            hit_sprite= False
            #physics
            c += 1 #added physics(gravity 1 block per iteration) and removed the up navigation

            if a == d:#collision identifier  and hiting monitering
                if c in {b, b+1, b+2,b+3}:#if the position of a ( the position of the pipe) = the position of bird (d) check if the c cordinate is in the predicted random cordinate b,b+1,b+2
                    pass
                else:# if else mark a hit
                    hit -=1
                    hit_sprite = True

            # life detction
            if hit == 0:
                subprocess.run("cls", shell =True)
                print("GAME OVER")
                print("SCORE = [ {} ]\n\n".format(count))

                kill = True
                a = 0
                break
            
            # lower boundary detection
            if c >= 25: # 21 because max hieght of the window is 20 ( first for loop)
                subprocess.run("cls", shell =True)
                print("GAME OVER")
                print("SCORE = [ {} ]\n\n".format(count))


                kill = True
                a = 0
                break
            # upper  boundary detection
            if c <= 0:
                subprocess.run("cls", shell =True)
                print("GAME OVER")
                print("SCORE = [ {} ]\n\n".format(count))


                kill = True
                a = 0
                break
            #execution
            if kill: 
                break    
                
                    
            # window speed       
            a -= 1
            if count%1 == 0 and count != 0:#it will increase the speed by decreaseing the delay according to the score
                if a == 69:
                    multip *= .99
                
            time.sleep(multip)
                    
           
            print("Score [ {} ]".format(count)+(emoji.emojize(":red_heart:"*hit)), end="")
            

            
            subprocess.run("cls", shell =True)
            if a <= 0:break
        
        count += 1
        if kill: 
            break
    return kill


def key():
    
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


