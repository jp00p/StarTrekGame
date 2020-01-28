class player: 
    def __init__(self): # new player
        #self.name = ''
        self.solves = 0
        self.location = 'b3'
        self.inventory = ['phaser']
        self.room_solved = {
            'a1': False, 'a2' : False, 'a3': False, 'a4': False, 'a5': False, 'a6' : False, 'a7': False, 'a8': False,
            'b1': False, 'b2' : False, 'b3': False, 'b4': False, 'b5': False, 'b6' : False, 'b7': False, 'b8': False,
            'c1': False, 'c2' : False, 'c3': False, 'c4': False, 'c5': False, 'c6' : False, 'c7': False, 'c8': False,
            's1': False, 's2' : False, 'TL': False
        }
        #self.game_over = False
        #self.astrological = ''
    def use_item(self, item):
        #placeholder for expansion
        return