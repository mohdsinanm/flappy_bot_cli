import random


class SetupCharacter:

    def __init__(self):
        self.i = 5 #i Coordinates of playable character
        self.j = 15 #j Coordinates of playable character
        self.kill = False
        self.hit_sprite = False
        self.count = 0 #score
        self.hit = 3 #life
        

class SetupGame:

    def __init__(self):
        self.view_window_length = 70 #this variable controls the visibility (view window) decrease to shorten the window,together with second for loop
        self.passage_space = random.randint(5,15)# var for producing the passage

        self.life_coordinate = random.randint(5,10) #this random choice determine the cordinate of life
        self.life = random.choice([False,False,False,False,False,True,False,False,False,False,False])

        self.score_coordinate = random.randint(5,10) #this random choice determine the cordinates of multiplier cross
        self.score = random.choice([False,False,False,False,False,True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False])
        