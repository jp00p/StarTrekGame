#############
# Map Setup	#
#############
"""		     ____
             |s2|
    --------------------------
    |a1|a2|a3|a4|a5|a6|a7|a8|
 -----------------------------
 |s1|b1|b2|b3|b4|b5|b6|b7|b8|
 -------------------------------
    |c1|c2|c3|c4|c5|c6|c7|c8|TL|
    ----------------------------

trigger s rooms:
if character.location == x
    u hear somethin
    change zonemap entry for x to unlock s room

riker endgame
    find s1: bone
    find s2: bone oil
    enter c7 with both items and answer the question 
    night bird

"""

#Sets up constant variables for rooms
NAME = 'Name' # name of room
DESCRIPTION = 'description' # upon entering
INFO = 'info' # upon 'looking'
ITEM_REQUEST = 'ask' # when they ask for an item
PUZZLE = 'puzzle' # question
PUZZLE_2 = 'puzzle two'
PUZZLE_3 = 'puzzle tree'
ANSWER = 'answer' # answer
SOLVED = "This room has been solved" # text for when its solved
#"SIDE_UP" = 'x1' # which room each direction will take you
#"SIDE_DOWN" = False # false means you cant go that way
#"SIDE_LEFT" = 'x3'
#"SIDE_RIGHT" = 'x4'
GIVEN_ITEM = "chocolate", "undies", "cat food"  # gives u this upon solving
REQUIRED_ITEM = "item1", "item2" # requires this to solve
REQUIRED_ITEM_2 = "ri1", "ri2"
RESPONSE = 'thanks' # when you complete the room
WRONG = 'wrong answer dummy' # wrong answer 
ROOM_TYPE = 'quiz_room', 'item_room', 'hall', 'end', 'exit'
TRIGGER = False
STEP = 0
WRONG_2 = "wrong two"
WRONG_3 = "wrong three"
RESPONSE_2 = "res two"
RESPONSE_3 = "res three"
FINAL_RESPONSE = "res four"
# quiz_room has a quiz (might give u an item too)
# item_room requires an item to clear
# hall is just a hall with no interaction yet
# end room has special requirements to finish

level_1 = {
    's1': {
        NAME: "Riker's Band Practice Auditorium",
        DESCRIPTION: "Somehow, you never noticed this room before.",
		INFO: "Amongst the scattered drums, bass guitars, and discarded evidence of previous sexual conquests, you spy a shiny -- yet dry -- trombone.",
		PUZZLE: "As you reach for the 'bone, your hand is deflected by a force field!\nNobody touches Riker's 'bone!\nThe computer speaks:\n\"PLEASE STATE COMMANDER RIKER'S RANK TO ACCESS THE BONE\"",
        RESPONSE: "\"ACKNOWLEDGED. BONE ACCESS GRANTED.\"\nYou grab the 'bone firmly, and notice that it could use some lubing up.",
        ROOM_TYPE: "quiz_room",
        ANSWER: "commander",
        WRONG: "\"ERROR - INCORRECT. PLEASE STEP AWAY FROM THE BONE.\"",
		SOLVED: "This room has seen some action, but you've already extracted the 'bone.",
        GIVEN_ITEM: "trombone",
        REQUIRED_ITEM: False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "b1",
        TRIGGER: False,
    },
    's2': {
        NAME: "Riker's Storage Closet",
        DESCRIPTION: "A mysterious room you never noticed before.",
		INFO: "As you step into the closet, a shadowy figure touches your shoulder from the darkness.",
		PUZZLE: "\"Please... tell me... who is in Sector A1...?\"",
        RESPONSE: "\"I knew it! Nobody is mourning me! They're all having fun and I'm stuck in this penalty box!\" The shadowy figure sobs, and begins to slump away, dejected.\nFrom behind you would almost swear it looks like Tasha Yarr...\nWhere they once stood, you see a brand new bottle of BONE OIL on the shelf and snag it.",
        ROOM_TYPE: "quiz_room",
        ANSWER: "geordi",
        WRONG: "\"Hmm... I think you're lying to me.\" the shadowy figure hisses.  You can see a bottle of something behind them...",
		SOLVED: "\"This room is full of unspeakable things, but nothing that looks useful to you right now.\"",
        GIVEN_ITEM: "bone oil",
        REQUIRED_ITEM: False,
		"SIDE_UP": False,
		"SIDE_DOWN": "a5",
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        TRIGGER: False,
    },
    'TL': {
        NAME: "Turbolift",
        DESCRIPTION: "The only way out of this den of hedonistic debauchery",
		INFO: "Fresh air blows out from the open doors, sweet relief after hours in these musky hallways.",
		PUZZLE: "",
        RESPONSE: "",
        ROOM_TYPE: "exit",
        ANSWER: "",
        WRONG: "",
		SOLVED: False,
        GIVEN_ITEM: False,
        REQUIRED_ITEM: False,
		"SIDE_UP": False,
		"SIDE_DOWN": "a5",
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        TRIGGER: False,
    },
	'a1': {
        NAME: "The Holodeck",
		DESCRIPTION: "A room where all your fantasies can come true, just make sure the safety protocols are always on.",
		INFO: "As you step through the holodeck doors, Geordi spins around and screams \"Computer, end program now!\" The room goes black, but not before you catch a glimpse of ...something personal.",
		PUZZLE: "\"Uh... I thought I locked that door. I was just doing some research on...\nPlasmonic reactions...\nAnyway, I was supposed to feed Data's cat but I got distracted.  \nWhat is that cat's name anyway?\"",
        RESPONSE: "\"Yeah, Spot! You wouldn't mind feeding him for me would you? Thanks pal.\"",
        ROOM_TYPE: "quiz_room",
        ANSWER: "spot",
        WRONG: "\"No... it was something like Fido or Rover.  Well, I should get back to this... research.\n Come back if you remember that cat's name!\"",
		SOLVED: "Geordi has locked the door.",
        GIVEN_ITEM: "cat food",
        REQUIRED_ITEM: False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "a2",
        TRIGGER: False,
	},
    'a2': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": "b2",
        "SIDE_LEFT": "a1",
        "SIDE_RIGHT": "a3"
    }, 
	'a3': {
        NAME: "Picard's Ready Room",
		DESCRIPTION: "A stately state room for a man of his station",
		INFO: "Picard is frantically searching through his room, there are drawers upturned and priceless artifacts tossed aside .",
		ITEM_REQUEST: "\"Where the devil is my little flute!?\" Picard seems on the verge of tears.", 
        RESPONSE: "\"Oh thank heavens! You found my tiny flute!\"",
		ROOM_TYPE: "item_room",
        ANSWER: False,
        WRONG: "\"I know I had it when I left on that last away mission, which Riker doesn't know about.\"",
		SOLVED: "Picard is sitting in the wreckage of his ready room, playing a solemn tune on his itty bitty flutey.",
        GIVEN_ITEM: False,
        REQUIRED_ITEM: "flute",
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": 'a2',
		"SIDE_RIGHT": False,
        TRIGGER: False,
	},
    'a4': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": 'b4',
        "SIDE_LEFT": False,
        "SIDE_RIGHT": 'a5'
    },
    'a5': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": False,
        "SIDE_LEFT": 'a4',
        "SIDE_RIGHT": 'a6'
    },
    'a6': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": 'b6',
        "SIDE_LEFT": 'a5',
        "SIDE_RIGHT": 'a7'
    },
    'a7': {
        # bat'leth lirpa Teral'n
        NAME: "Worf's Quarters",
		DESCRIPTION: "Every wall is decked out with enough bladed weapons to fill an entire kiosk in a mall.",
		INFO: "Worf has been afflicted by some weird space beams that make him act drunk.  He's in a good mood, luckily, but can't figure out which weapon to play with.",
		PUZZLE: "Giggling, Worf confides in you that he can't remember which one is the most honorable.\n\"Should I use the Lirpa, the Bat'Leth or the Teral'n?\"\n\n1. Give him the Lirpa\n2. Give him the Bat'Leth\n3. Give him the Teral'n\n", 
        RESPONSE: "\"Of course! A warrior's weapon.\"\nAs you make your retreat to a safe distance, you see a fresh glass of prune juice on the nightstand.\nA warrior's drink.",
        WRONG: "Worf tries the weapon. \"This doesn't feel right. You have dishonored me.\"",
		ROOM_TYPE: "quiz_room",
        ANSWER: "2",
		SOLVED: "Worf is drunk and dangerously swinging around his Bat'Leth, while humming that old Betazoid Jazz standard: \"Night Bird.\"",
        GIVEN_ITEM: "prune juice",
        REQUIRED_ITEM: False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "a6",
		"SIDE_RIGHT": False,
        TRIGGER: False,
	},
    'a8': {
        NAME: "Ten Forward",
		DESCRIPTION: "A bustling bar and lounge, managed by Guinan",
		INFO: "Guinan is behind the bar, cleaning a glass with a dirty rag.  She beckons you over.",
		PUZZLE: "\"We all know Counselor Troi's favorite food and only interest is chocolate, but do you know Worf's favorite beverage?\"", 
        RESPONSE: "\"That's it!  I can't believe it either.  Klingons are stranger than Mark Twain!\nHere, take this chocolate, you might need it if Troi attempts to interact with you.\"",
		ROOM_TYPE: "quiz_room",
        ANSWER: "prune juice",
		SOLVED: "Guinan gives you a knowing wink.",
        GIVEN_ITEM: "chocolate",
        REQUIRED_ITEM: False,
        WRONG: "\"Quit playin' with me! You know what it is!\"",
		"SIDE_UP": False,
		"SIDE_DOWN": 'b8',
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        TRIGGER: False,
	},
    'b1': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": "c1",
        "SIDE_LEFT": False,
        "SIDE_RIGHT": "b2"
    },
    'b2': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "a2",
        "SIDE_DOWN": "c2",
        "SIDE_LEFT": "b1",
        "SIDE_RIGHT": "b3"
    },
    'b3': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": False,
        "SIDE_LEFT": "b2",
        "SIDE_RIGHT": "b4"
    },
    'b4': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "a4",
        "SIDE_DOWN": "c4",
        "SIDE_LEFT": "b3",
        "SIDE_RIGHT": "b5"
    },
    'b5': {
        NAME: 'Data\'s Room',
		DESCRIPTION: "Art supplies and cat toys litter the floor.",
		INFO: "Data is busy painting, listening to 12 classical compositions, and reading 2 different PADDs.  You would have to scream to be heard over the noise.",
		ITEM_REQUEST: "Data's cat rubs against your leg.  She looks hungry!",
        RESPONSE: "Spot purrs happily at you before shoveling the food into her face.\nData still hasn't noticed you, but you notice he's painting a picture of a trombone that's... sweaty?",
        WRONG: "There's nothing you can do here at the moment.  That cat needs food!",
		ROOM_TYPE: "item_room",
        ANSWER: "",
		SOLVED: "Data is hard at work painting a ...sweaty trombone?!",
        GIVEN_ITEM: False,
        REQUIRED_ITEM: "cat food",
        TRIGGER: True,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "b4",
		"SIDE_RIGHT": False,
	},
    'b6': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "a6",
        "SIDE_DOWN": "c6",
        "SIDE_LEFT": False,
        "SIDE_RIGHT": "b7"
    },
    'b7': {
        ROOM_TYPE: "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": False,
        "SIDE_LEFT": "b6",
        "SIDE_RIGHT": "b8"
    },
    'b8': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "a8",
        "SIDE_DOWN": "c8",
        "SIDE_LEFT": "b7",
        "SIDE_RIGHT": False
    },
    'c1': {
        NAME: "Barclay's Room",
		DESCRIPTION: "A small, disorderly room where Brocolli resides",
		INFO: "Reg looks worried, as usual. He's pacing back and forth, occasionally biting his knuckle.",
		ITEM_REQUEST: "\"I... I was going to ask Deanna on a d-date tonight, but I can't work up the nerve.  If only I could just ...smell her...\"", 
        RESPONSE: "\"T-T-Thank you..?\" Barclay grabs the leotard and resumes his pacing. \"God I wish Geordi wasn't hogging the holodeck!\nIf I still had my super brain powers I'd show him!\"",
		ROOM_TYPE: "item_room",
        WRONG: "\"I just need ...something of hers so I can think clearly.\"",
        ANSWER: "1",
		SOLVED: "Brocolli has resumed pacing back and forth, this time occasionally huffing Troi's leotard.",
        GIVEN_ITEM: False,
        REQUIRED_ITEM: "leotard",
        TRIGGER: True,
		"SIDE_UP": 'b1',
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
	},
    'c2': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "a2",
        "SIDE_DOWN": False,
        "SIDE_LEFT": False,
        "SIDE_RIGHT": "c3"
    },
    'c3': {
        NAME: "Transporter Room",
		DESCRIPTION: "O'Brian stands at attention for weeks at a time in here.",
		INFO: "O'Brian is in here, grumbling about Keiko and fidgeting with a small flute.",
		PUZZLE: "O'Brian says to you: \"Ken yer believe she wants ter name 'er Keiko Jr.? 'Elp me a choose a better name, ken ya?!\"\nWhat would YOU name the baby?",
        SOLVED: "O'Brian is standing at the control panel, staring straight ahead and grumbling to himself.",
        RESPONSE: "O'Brian says: \"Molly... Aye, I reckon Molly'r do ...fer now\" in one of the most offensively stereotypical accents you've ever read.\nHe hands you the flute and returns to his default position.",
		ROOM_TYPE: "quiz_room",
        WRONG: "\"I really donnae think Keiko would approve o' that name\"",
        GIVEN_ITEM: "flute",
        ANSWER: "molly",
        REQUIRED_ITEM: False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "c2",
		"SIDE_RIGHT": False,
        TRIGGER: False,
	},
    'c4': {
        NAME: 'Wesleys Room',
		DESCRIPTION: "Half child's playpen, half science lab.",
		INFO: "A small, terrified child is cowering in the corner -- Oh, it's the boy! Ensign Wesley!",
		PUZZLE: "Wesley, decked out in a cool rainbow jumpsuit, asks you why people do drugs and what makes them feel good and are they bad and he won't stop going on about it...\nYou've got to silence this kid somehow",
        RESPONSE: "You tell Wesley to shut up and knock him over with barely any effort, effectively silencing him. While he returns to his corner, you start rifling through his personal belongings.",
        WRONG: "Wesley is unrelenting.  He starts showing off his many science projects and asking about what happens on Risa and wondering where Spot is and asking for his mother and saying he will be a captain someday and telling you about his crush and...",
        SOLVED: "Wesley is cowering in the corner, afraid and annoying.",
		ROOM_TYPE: "quiz_room",
        ANSWER: "shut up wesley",
        GIVEN_ITEM: False,
        REQUIRED_ITEM: False,
		"SIDE_UP": "b4",
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        TRIGGER: False,
	},
    'c5': {
        NAME: "Counselor Troi's Office",
		DESCRIPTION: "You are in Counselor Troi's office.",
		INFO: "Troi looks as bored as a cardboard cutout.  She can sense you judging her from across the room.",
		ITEM_REQUEST: "Troi demands you leave unless you brought her favorite food.", 
        RESPONSE: "Troi violently snatches the chocolate from your hands and begins eating it in an inapropriately erotic manner.\nWhile she's distracted, you grab her ridiculous workout leotard from her nighstand like a creep.",
        WRONG: "You don't need to be an empath to know Troi is angry you don't have chocolate.",
		ROOM_TYPE: "item_room",
        ANSWER: "",
		SOLVED: False,
        GIVEN_ITEM: "leotard",
        REQUIRED_ITEM: "chocolate",
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "c6",
        TRIGGER: False,
	},
    'c6': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "b6",
        "SIDE_DOWN": False,
        "SIDE_LEFT": "c5",
        "SIDE_RIGHT": False
    },
    'c7': {
        NAME: "Riker's Boudoir",
		DESCRIPTION: "A powerful musk eminates from the doorway",
		INFO: "You enter Riker's room, and pass through a thick haze of romantic incense.\nThe lights are low and Riker stands before you in a silk robe.\n",
		PUZZLE: "Riker eyes you up and down and sadly shakes his head.\n\"I don't think so.  I'm looking for someone with a little more ...experience.\"",
        PUZZLE_2: "Riker eyes you up and down and smirks softly.\n\"If only I had my 'bone, I'd get this party started.\" Great. Riker's 'bone could be ANYWHERE.",
        PUZZLE_3: "Riker eyes you up and down, his jaw drops.\n\"I dream of a galaxy where your eyes are the stars and the universe worships the night.\"\nHe tries to serenade you, but he can barely move the shaft of his 'bone.\n\"This 'bone is way too dry. Be a dear and find me some bone oil, would you?\"",
        RESPONSE: "\"On second thought, Rikey likey\" he purrs, licking his moustache. \"You're looking up to par for this one on one...\"",
        RESPONSE_2: "\"Mmm... now we're talking.  But this 'bone seems to be bone dry!\"",
        RESPONSE_3: "\"Great. Let me just lube up this 'bone and we'll be in business.\"",
        FINAL_RESPONSE: "Riker hesitates, says \"Ha. I'll show you.\" He squints at you, then raises the 'bone to his mouth and starts to blow.\nIt's obvious he hasn't mastered this one yet, but in an effort to impress you\n...he keeps trying.  It sounds awful.\nWhile he's distracted, you punch the button that unlocks the Turbolift.",
        WRONG: "Riker needs someone who knows a little more about the way things work.",
        WRONG_2: "\"Can I help you Ensign? Go grab my 'bone!\"",
        WRONG_3: "\"Ensign, I am waiting to put that oil on my 'bone!\"",
		ROOM_TYPE: "end",
        STEP: 0,
        ANSWER: "nightbird",
		SOLVED: "Riker is busy trying to figure out how to play Night Bird.",
        GIVEN_ITEM: False,
        REQUIRED_ITEM: "trombone",
        REQUIRED_ITEM_2: "bone oil",
        TRIGGER: True,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "c8",
        TRIGGER: False,
	},
    'c8': {
        ROOM_TYPE: "hall",
        "SIDE_UP": "b8",
        "SIDE_DOWN": False,
        "SIDE_LEFT": "c7",
        "SIDE_RIGHT": False
    }
}