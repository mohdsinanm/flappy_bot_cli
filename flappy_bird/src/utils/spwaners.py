
import emoji

def life_spawner(life : bool,i_coordinate:int, j_coordinate:int , life_coordinate:int, view_window : int, character_i: int, character_j : int ):
        global hit
        i = i_coordinate
        j = j_coordinate


        if life:#life multiplier
            # there is a 1 in 10 chances of getting life multilier
            #if life is true when j reaches a-20 it will print a heart 
            if j == view_window - 20 and i == life_coordinate:
                print(emoji.emojize(":red_heart:"), end="")
                if ({character_i-1, character_j } == {j,life_coordinate}) or ({ character_i+1, character_j} == {j,life_coordinate}) or ({character_i,character_j} == {j,life_coordinate}):#this check the coordinate of bird is equal to the coordinale of heart
                    hit +=1 #give one heart
                    life = False #then make it invisible
