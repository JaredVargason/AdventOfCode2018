NUM_PLAYERS = 416
LAST_MARBLE = 7161700

class Marble:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

scores = [0] * NUM_PLAYERS
current_marble = Marble(0)
current_marble.next = current_marble
current_marble.prev = current_marble

for i in range(1, LAST_MARBLE + 1):
    current_elf = i % NUM_PLAYERS

    if i % 23 == 0: 
        scores[current_elf] += i 
        for i in range(7):
            current_marble = current_marble.prev
            #remove marble
        first = current_marble.prev
        second = current_marble.next
         
        first.next = second
        second.prev = first
        scores[current_elf] += current_marble.value
        current_marble = second      
    
    else: #add marble to the right of next clockwise marble
        first = current_marble.next
        second = first.next 
        marble = Marble(i)
        first.next = marble
        marble.prev = first
        marble.next = second
        second.prev = marble 
        current_marble = marble
        
print(max(scores))