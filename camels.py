from enum import Enum
NUM_CAMELS = 5
DICE_MAX = 3

counts = [0] * NUM_CAMELS

class DICE_COLORS(Enum):
    WHITE = 0
    YELLOW = 1
    ORANGE = 2
    GREEN = 3
    BLUE = 4

available_dice = [i for i in DICE_COLORS]

#an input of camelstacks is a list of lists. the position of the camel stack is the index
#camels at the back of the list are considered on top.
exampleStack = [[0,1,2],[2,3]]

def simulate(camelStacks, available_dice):
    for dice_color in available_dice:    
        for dice_result in DICE_MAX:
            
    