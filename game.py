import cmd, textwrap, sys, os, time, random, string
import player
import game_map # the semi-extensible game map
import ship # animation???
screen_width = 79 # for text wrapping & stuff

# setup classes
zonemap = game_map.level_1 # we could go to level_2 in the future...
character = player.player() # init player, save game with this object
text_wrapper = textwrap.TextWrapper(width=screen_width-4)

### Text utilites
def speak(words, speed = 0.01, wait=0.25):
    # typewriter like effect
    words = text_wrapper.fill(words)
    for character in words:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)
    print("\n")
    if(wait > 0):
        time.sleep(wait)    

def block_type(text):
    # prints text with # around it #
    text = "  " + text + "  "
    print(text.center(screen_width, "#"))

def centered(text):
    # prints centered text
    lines = textwrap.wrap(text, screen_width)  
    final = "\n".join(line.center(screen_width) for line in lines)
    print(final)

def print_row():
    # print a horizontal rule
    left = "•._.••´¯``•.¸¸.•`"
    right = "`•.¸¸.•´´¯`••._.•"
    spacer_length = screen_width - (len(left) + len(right))
    print(left + (" "*spacer_length) + right)

def show_exits():
    # display room exits
    sides = ["SIDE_UP", "SIDE_DOWN", "SIDE_LEFT", "SIDE_RIGHT"]
    centered(" EXITS: ")
    for side in sides:
        if(zonemap[character.location][side] != False):
            dest = zonemap[character.location][side]
            go_text = side.replace("SIDE_", "") #+ " " + dest
            if(zonemap[dest]["room_type"] != 'hall'):
                go_text += " (" + zonemap[dest]["name"] + ")"
            else:
                go_text += " (Hallway)"
            centered(go_text)

### Title screen choices
def title_screen_selections():
    
    print("\n"*4)
    print("\n")
    print_row()
    print("\n")
    block_type("Type a command to begin:")
    centered("play")
    centered("help")
    centered("quit")
    print("\n")
    print_row()
    
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("skip"):
        os.system("cls")
        enter_location()

    while option.lower() not in ['play', 'help', 'quit']:
        centered("Please enter a valid command")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit() # cold quit
        elif option.lower() == ("skip"):
            os.system("cls")
            enter_location()

### Actual title graphic
def title_screen():
    os.system('mode con: cols='+str(screen_width)+' lines=40')
    print(
r'''
              ____ _____ ___     ____      _____ ____    _____ _ ___
             / __//____//__ \   /__  \    /____//__  \  /____//_X__/
            ( (    __   __| |   ___) /     __   ___) / ____  ___ 
             \ \  / / ,/,/| |  /   _/     / /  /   _/ / __/ / _ \        
          ____) )/ /,/ /__| | / /\ \     / /  / /\ \ / /__ / / \ \   
         /_____//_//________|/_/ /_/    /_/  /_/ /_//____//_/   \_\  
   ___      _          _    ___     __   _       _  _  __  ___    __
    |  |_| |_    |\ | |_ \/  |     | _  |_ |\ | |_ |_)   |  |  | |  | |\ |
    |  | | |_    | \| |_ /\  |     |__| |_ | \| |_ | \ /_|  |  | |__| | \|

'''
)
    time.sleep(0.5)
    centered(" ¸,ø¤º°`°º¤ø,¸¸,ø¤º° RIKER'S EROTIC QUIZ LABYRINTH °º¤ø,¸¸,ø¤º°`°º¤ø,¸ ")
    time.sleep(1)
    centered("version 0.1")
    centered("Programming - jp00p")
    centered("Quality Assurance - Kimmi")
    
    centered(" (a work of satire made in good humor with no purpose) ")

    title_screen_selections()

def help_menu():
    print("\n")
    
    block_type(" HELP MENU ")
    centered(" Type \"move\" to move ")
    centered(" You can move in these directions: ")
    centered(" [U]p - [D]own - [R]ight - [L]eft ")
    centered(" You can use cardinal directions as well (N,S,E,W) ")
    centered(" Type \"look\" to investigate more closely ")
    centered(" Sometimes you have to \"look\" more than once!\" ") 
    centered(" Type [i]nventory to see your list of items ")
    centered(" Type status to see your score ")
    centered(" Making a map on paper is highly recommended! ")
    print("\n")
    title_screen_selections()





### Interactivity

def enter_location():
    print_row()
    centered("Sector " + character.location.upper())
    if(zonemap[character.location]["room_type"] != "hall"):
        #enter a room
        centered(zonemap[character.location]["name"])
        centered(" ----- ")
        centered(zonemap[character.location]["description"])
    else:
        #enter a hall
        #todo: rando the dialog
        speak(" You are in a hallway...\n")
    show_exits()
    prompt()

def display_inventory():
    print_row()
    block_type(" Current Items: ")
    for item in character.inventory:
        centered(item)
    #centered(" You can't \"use\" items yet, so save your typing ")
    print("\n")
    print_row()
    prompt()

def prompt():
    print_row()
    block_type('What would you like to do? (move, look, inventory, status, quit)')
    action = input("> ")
    acceptable_actions = ['status', 'teleport', 'inventory', 'items', 'i', 'move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    parsed_action = action.lower()
    compound_action = parsed_action.split()
      
        
    while parsed_action not in acceptable_actions and compound_action[0] not in acceptable_actions:
        print("\n Unknown action")
        action = input("> ")
        parsed_action = action.lower()
        compound_action = parsed_action.split()
    
    if(len(compound_action) > 1 and compound_action[0] == "move"):
        if(compound_action[0] in ['move', 'go', 'travel', 'walk'] and compound_action[1] in ['up','down','left','right']):
            destination = zonemap[character.location]["SIDE_" + compound_action[1].upper()]
            movement_handler(destination)

    if parsed_action == 'quit':
        sys.exit()
    if parsed_action in ['inventory', 'items', 'i']:
        print_row()
        display_inventory()
    if parsed_action == 'status':
        print_row()
        print("Score: " + str(character.solves))
        prompt()
    if parsed_action in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    if parsed_action == 'teleport':
        dest = input("Where to? > ")
        movement_handler(dest)
    elif parsed_action in ['examine', 'inspect', 'interact', 'look']:
        player_examine()
    prompt()

def player_move(action):
    centered("Which direction would you like to " + action.lower() + " to?")
    show_exits()
    dest = input("> ").lower()
    os.system("cls")
    if dest in ['up', 'north', 'u', 'n']:
        destination = zonemap[character.location]["SIDE_UP"]
        movement_handler(destination)
    elif dest in ['down', 'south', 'd', 's']:
        destination = zonemap[character.location]["SIDE_DOWN"]
        movement_handler(destination)
    elif dest in ['left', 'west', 'l', 'w']:
        destination = zonemap[character.location]["SIDE_LEFT"]
        movement_handler(destination)
    elif dest in ['right', 'east', 'r', 'e']:
        destination = zonemap[character.location]["SIDE_RIGHT"]
        movement_handler(destination)
    else:
        centered(" Invalid direction ")
        player_move("move")
    prompt()

def movement_handler(dest):
    if dest == '' or dest == False:
        print("You can't walk through walls... yet.")
        prompt()
    else:
        #current room check...
        move_text = " "
        if(zonemap[character.location]["room_type"] != 'hall'): 
            move_text += "You leave " + zonemap[character.location]["name"] + "\n"

        character.location = dest # update location

        if(zonemap[character.location]["room_type"] == 'hall'):
            move_text += "You enter a hallway\n"
        else:
            move_text += "You enter " + zonemap[character.location]["name"] + "\n"
        speak(move_text)
        enter_location()


# Runs when a player 'looks'
def player_examine():
    if character.room_solved[character.location]:
        # puzzle already solved
        centered(zonemap[character.location]["solved"])
    else:
        # end of game
        if(zonemap[character.location]["room_type"] == "exit"):
            os.system("cls")
            speak(" You instruct the Turbolift to take you anywhere else! ")
            speak(" Nearly overcome with love, lust and confusion, you slump against the floor and begin laughing. ")
            speak(" Your mad laughter slowly turns to sobs of longing for Riker. ", 0.01)
            speak(" The Turbolift hums... ")
            speak(" ..... ", 0.03)
            speak(" The doors open... ")
            speak(" ..... ", 0.03)
            speak(" You hear glasses clinking together, and the general bustle of people. ")
            speak(" A dim, dusty light shines in... ")
            speak(" a hand reaches in to help you to your feet... ")
            speak(" and you see a friendly, youthful face, which says... ")
            time.sleep(2)
            speak(" \"Welcome to Deep Space Nine.\" ")
            time.sleep(1)
            speak(" \"I'm Doctor Julian Bashir.\"", 0.03)
            time.sleep(3)
            print("\n")
            print_row()
            centered(" THE END ")
            print_row()
            time.sleep(1)
            speak(" ...or is it...? ", 0.6)
            time.sleep(5)
            sys.exit()
            
        
        # quiz room look
        if(zonemap[character.location]["room_type"] == "quiz_room"):
            speak(" "+zonemap[character.location]["info"]) # intro
            speak(" "+zonemap[character.location]["puzzle"]) # question
            puzzle_answer = input("?> ")
            check_puzzle(puzzle_answer)
        # item room look
        elif(zonemap[character.location]["room_type"] == "item_room"):
            speak(" "+zonemap[character.location]["info"]) # intro
            check_puzzle()
        # end room look
        elif(zonemap[character.location]["room_type"] == "end"):
            if(zonemap[character.location]["step"] == 0):
                speak(" "+zonemap[character.location]["info"]) # intro
                speak(" "+zonemap[character.location]["puzzle"]) # step 1
            elif(zonemap[character.location]["step"] == 1):
                speak(" "+zonemap[character.location]["info"]) # intro
                speak(" "+zonemap[character.location]["puzzle_2"]) # step 2
            elif(zonemap[character.location]["step"] == 2):
                speak(" "+zonemap[character.location]["info"]) # intro
                speak(" "+zonemap[character.location]["puzzle_3"]) # step 3
            elif(zonemap[character.location]["step"] == 3):
                speak(" \"Now... What song should I play?\"")
                puzzle_answer = input("?> ")
                check_puzzle(puzzle_answer)
            check_puzzle() # fallback to checking empty answer
        else:
            speak("Not much to see in this hallway.")
            show_exits()
    prompt()


def trigger(room):
    if(room == 'b5'):
        zonemap['a4']['SIDE_UP'] = 's2'
        speak("\n"*4)
        speak(" You hear something change somewhere nearby... ")
        speak("\n"*4)
        zonemap['a4']["trigger"] = False
    if(room == 'c7'):
        if(zonemap['c7']["step"] == 4):
            zonemap['c8']['SIDE_RIGHT'] = 'TL'
            speak("\n"*4)
            speak(" The Turbolift is unlocked! It's just outside of Riker's Boudoir. ")
            speak("\n"*4)
            zonemap['c7']["trigger"] = False
    if(room == 'c1'):
        zonemap['b1']['SIDE_LEFT'] = 's1'
        speak("\n"*4)
        speak(" You hear something change somewhere nearby... ")
        speak("\n"*4)
        zonemap['c1']["trigger"] = False
        


### Handles logic of trying to solving all room types
def check_puzzle(answer=''):  
    if(answer != ''):
        # strip punctuation and trailing whitespace and make lowercase
        answer = answer.translate(str.maketrans('', '', string.punctuation)).lower().strip()

    # endgame
    if(zonemap[character.location]["room_type"] == 'end'):
        end_step = zonemap[character.location]["step"]
        #print("Step " + str(end_step))
        if(end_step == 0):
            # requires 7 solved rooms
            if(character.solves < 7):
                speak(" "+zonemap[character.location]["wrong"])
            else:
                # increase step
                speak(" "+zonemap[character.location]["response"])
                zonemap[character.location]["step"] = 1
        elif(end_step == 1):   
            # requires trombone 
            if(zonemap[character.location]["required_item"] in character.inventory):
                character.inventory.remove(zonemap[character.location]["required_item"])
                speak(" You hand Riker the bone.")
                speak(" "+zonemap[character.location]["response_2"])
                zonemap[character.location]["step"] = 2
            else:
                speak(" "+zonemap[character.location]["wrong_2"])
        elif(end_step == 2):
            # requires bone oil
            if(zonemap[character.location]["required_item_2"] in character.inventory):
                character.inventory.remove(zonemap[character.location]["required_item_2"])
                speak(" You slide Riker the 'bone oil.")
                speak(" "+zonemap[character.location]["response_3"])
                zonemap[character.location]["step"] = 3
            else:
                speak(zonemap[character.location]["wrong_3"])
        elif(end_step == 3):
            if(answer == zonemap[character.location]["answer"] or answer == "night bird"):
                character.room_solved[character.location] = True
                zonemap[character.location]["step"] = 4
                speak(" "+zonemap[character.location]["final_response"])
                trigger('c7')
            else:
                speak(" Riker plays that song with ease, and finishes quickly.\nStill, you feel your pulse racing and the blood rushing to your face.\n\"Come on, don't you know something more... appropriate for this 'bone?\"")

    # quiz_room
    if(zonemap[character.location]["room_type"] == 'quiz_room'):
        # correct answer quiz_room
        # print(" answer debug: " + answer)
        if(answer != zonemap[character.location]["answer"]):
            speak(" "+zonemap[character.location]["wrong"])
            block_type("Wrong answer. Look again or move on.")
            prompt()
        else:
            character.room_solved[character.location] = True
            character.solves += 1
            speak(zonemap[character.location]["response"])
            # if they have an item to give you
            if(zonemap[character.location]["given_item"] != ""):
                character.inventory.append(zonemap[character.location]["given_item"])
                speak(" You receive " + zonemap[character.location]["given_item"])
            block_type("You have solved this room. Onwards!")
            block_type("Rooms solved: " + str(character.solves))
    
    if(zonemap[character.location]["room_type"] == 'item_room'): # item room handling
        speak(zonemap[character.location]["item_request"]) # item demand
        if zonemap[character.location]["required_item"] in character.inventory:
            # give item
            character.inventory.remove(zonemap[character.location]["required_item"])
            speak(" You hand over the " + zonemap[character.location]["required_item"])
            speak(zonemap[character.location]["response"])
            # if they have an item to give you
            if(zonemap[character.location]["given_item"] != ""):
                character.inventory.append(zonemap[character.location]["given_item"])
                speak(" You receive " + zonemap[character.location]["given_item"])
            character.room_solved[character.location] = True
            character.solves += 1
            block_type("You have solved this room. Onwards!")
            block_type("Rooms solved: " + str(character.solves))
        else: # player doesnt have the item
            speak(" "+zonemap[character.location]["wrong"])
            print_row()
            block_type("You don't have the required item! Find the " + zonemap[character.location]["required_item"] + "!")

    # if the room has a trigger when solved, run it
    if(character.room_solved[character.location] == True and zonemap[character.location]["trigger"] == True):
        trigger(character.location)

    prompt()    

### Main Game/loop functionality
def game_loop():
    #basically pointless for now, game loops in enter_location and there's no death state
    while character.solves < 12:
        prompt()
    block_type("Game over sucka")
    sys.exit()
    
def setup_game():
    os.system("cls")

    slow = 0.036
    speak(" ENSIGN'S LOG:", slow)
    speak(" Stardate ... 97901.18", slow)
    speak(" The Enterprise has been taken over by Riker.", slow)
    speak(" By using his charm, wit, and sexy chest hair, he has gained the willful consent of every crew member on board.", slow)
    speak(" ...Except me.", 0.075)
    speak(" The only way out is the turbolift near his quarters, which he has locked...", slow)
    speak(" Until he can have a \"one on one\" with me.", slow)
    speak(" My mission is to survive this meeting and escape with my decency intact.", slow)
    time.sleep(2)
    '''
    stars = [" ", ".", " ", " ", " ", " "]
    for x in range(31):
        starline = ''
        for y in range(screen_width-4):
            starline += random.choice(stars)
        speak(starline, 0.00025, 0)
    print("\n")
    '''
    os.system("cls")
    animation = ship.frames
    for i in range(len(animation)):
        print(animation[i])
        time.sleep(0.25)
        os.system("cls")

    speak("==== MAKE IT SO! ====>".center(screen_width), 0.03)
    time.sleep(2)
    os.system("cls")
    enter_location()
    game_loop() # probably won't reach this 


os.system("cls") # clear the screen
title_screen() # boot the game