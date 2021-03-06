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

level_1 = {
    's1': {
        "name": "Riker's Band Practice Auditorium",
        "description": "Somehow, you never noticed this room before.",
		"info": "Amongst the scattered drums, bass guitars, and discarded evidence of previous sexual conquests, you spy a shiny -- yet dry -- trombone.",
		"puzzle": "As you reach for the 'bone, your hand is deflected by a force field!\nNobody touches Riker's 'bone!\nThe computer speaks:\n\"PLEASE STATE COMMANDER RIKER'S RANK TO ACCESS THE BONE\"",
        "response": "\"ACKNOWLEDGED. BONE ACCESS GRANTED.\"\nYou grab the 'bone firmly, and notice that it could use some lubing up.",
        "room_type": "quiz_room",
        "answer": "commander",
        "wrong": "\"ERROR - INCORRECT. PLEASE STEP AWAY FROM THE BONE.\"",
		"solved": "This room has seen some action, but you've already extracted the 'bone.",
        "given_item": "trombone",
        "required_item": False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "b1",
        "trigger": False,
    },
    's2': {
        "name": "Riker's Storage Closet",
        "description": "A mysterious room you never noticed before.",
		"info": "As you step into the closet, a shadowy figure touches your shoulder from the darkness.",
		"puzzle": "\"Please... tell me... who is in Sector A1...?\"",
        "response": "\"I knew it! Nobody is mourning me! They're all having fun and I'm stuck in this penalty box!\" The shadowy figure sobs, and begins to slump away, dejected.\nFrom behind you would almost swear it looks like Tasha Yarr...\nWhere they once stood, you see a brand new bottle of BONE OIL on the shelf and snag it.",
        "room_type": "quiz_room",
        "answer": "geordi",
        "wrong": "\"Hmm... I think you're lying to me.\" the shadowy figure hisses.  You can see a bottle of something behind them...",
		"solved": "\"This room is full of unspeakable things, but nothing that looks useful to you right now.\"",
        "given_item": "bone oil",
        "required_item": False,
		"SIDE_UP": False,
		"SIDE_DOWN": "a5",
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        "trigger": False,
    },
    'TL': {
        "name": "Turbolift",
        "description": "The only way out of this den of hedonistic debauchery",
		"info": "Fresh air blows out from the open doors, sweet relief after hours in these musky hallways.",
		"puzzle": "",
        "response": "",
        "room_type": "exit",
        "answer": "",
        "wrong": "",
		"solved": False,
        "given_item": "",
        "required_item": False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "c8",
		"SIDE_RIGHT": False,
        "trigger": False,
    },
	'a1': {
        "name": "The Holodeck",
		"description": "A room where all your fantasies can come true, just make sure the safety protocols are always on.",
		"info": "As you step through the holodeck doors, Geordi spins around and screams \"Computer, end program now!\" The room goes black, but not before you catch a glimpse of ...something personal.",
		"puzzle": "\"Uh... I thought I locked that door. I was just doing some research on...\nPlasmonic reactions...\nAnyway, I was supposed to feed Data's cat but I got distracted.  \nWhat is that cat's name anyway?\"",
        "response": "\"Yeah, Spot! You wouldn't mind feeding him for me would you? Thanks pal.\"",
        "room_type": "quiz_room",
        "answer": "spot",
        "wrong": "\"No... it was something like Fido or Rover.  Well, I should get back to this... research.\n Come back if you remember that cat's name!\"",
		"solved": "Geordi has locked the door.",
        "given_item": "cat food",
        "required_item": False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "a2",
        "trigger": False,
	},
    'a2': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": "b2",
        "SIDE_LEFT": "a1",
        "SIDE_RIGHT": "a3"
    }, 
	'a3': {
        "name": "Picard's Ready Room",
		"description": "A stately state room for a man of his station",
		"info": "Picard is frantically searching through his room, there are drawers upturned and priceless artifacts tossed aside.",
		"item_request": "\"Where the devil is my little flute!?\" Picard seems on the verge of tears.", 
        "response": "\"Oh thank heavens! You found my tiny flute!\"",
		"room_type": "item_room",
        "answer": False,
        "wrong": "\"I know I had it when I left on that last away mission, which Riker doesn't know about.\"",
		"solved": "Picard is sitting in the wreckage of his ready room, playing a solemn tune on his itty bitty flutey.",
        "given_item": "",
        "required_item": "flute",
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": 'a2',
		"SIDE_RIGHT": False,
        "trigger": False,
	},
    'a4': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": 'b4',
        "SIDE_LEFT": False,
        "SIDE_RIGHT": 'a5'
    },
    'a5': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": False,
        "SIDE_LEFT": 'a4',
        "SIDE_RIGHT": 'a6'
    },
    'a6': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": 'b6',
        "SIDE_LEFT": 'a5',
        "SIDE_RIGHT": 'a7'
    },
    'a7': {
        # bat'leth lirpa Teral'n
        "name": "Worf's Quarters",
		"description": "Every wall is decked out with enough bladed weapons to fill an entire kiosk in a mall.",
		"info": "Worf has been afflicted by some weird space beams that make him act drunk.  He's in a good mood, luckily, but can't figure out which weapon to play with.",
		"puzzle": "Giggling, Worf confides in you that he can't remember which one is the most honorable.\n\"Should I use the Lirpa, the Bat'Leth or the Teral'n?\"\n\n\t1. Give him the Lirpa\n2. Give him the Bat'Leth\n3. Give him the Teral'n\n", 
        "response": "\"Of course! A warrior's weapon.\"\nAs you make your retreat to a safe distance, you see a fresh glass of prune juice on the nightstand.\nA warrior's drink.",
        "wrong": "Worf tries the weapon. \"This doesn't feel right. You have dishonored me.\"",
		"room_type": "quiz_room",
        "answer": "2",
		"solved": "Worf is drunk and dangerously swinging around his Bat'Leth, while humming that old Betazoid Jazz standard: \"Night Bird.\"",
        "given_item": "prune juice",
        "required_item": False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "a6",
		"SIDE_RIGHT": False,
        "trigger": False,
	},
    'a8': {
        "name": "Ten Forward",
		"description": "A bustling bar and lounge, managed by Guinan",
		"info": "Guinan is behind the bar, cleaning a glass with a dirty rag.  She beckons you over.",
		"puzzle": "\"We all know Counselor Troi's favorite food and only interest is chocolate, but do you know Worf's favorite beverage?\"", 
        "response": "\"That's it!  I can't believe it either.  Klingons are stranger than Mark Twain!\nHere, take this chocolate, you might need it if Troi attempts to interact with you.\"",
		"room_type": "quiz_room",
        "answer": "prune juice",
		"solved": "Guinan gives you a knowing wink.",
        "given_item": "chocolate",
        "required_item": False,
        "wrong": "\"Quit playin' with me! You know what it is!\"",
		"SIDE_UP": False,
		"SIDE_DOWN": 'b8',
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        "trigger": False,
	},
    'b1': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": "c1",
        "SIDE_LEFT": False,
        "SIDE_RIGHT": "b2"
    },
    'b2': {
        "room_type": "hall",
        "SIDE_UP": "a2",
        "SIDE_DOWN": "c2",
        "SIDE_LEFT": "b1",
        "SIDE_RIGHT": "b3"
    },
    'b3': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": False,
        "SIDE_LEFT": "b2",
        "SIDE_RIGHT": "b4"
    },
    'b4': {
        "room_type": "hall",
        "SIDE_UP": "a4",
        "SIDE_DOWN": "c4",
        "SIDE_LEFT": "b3",
        "SIDE_RIGHT": "b5"
    },
    'b5': {
        "name": 'Data\'s Room',
		"description": "Art supplies and cat toys litter the floor.",
		"info": "Data is busy painting, listening to 12 classical compositions, and reading 2 different PADDs.  You would have to scream to be heard over the noise.",
		"item_request": "Data's cat rubs against your leg.  She looks hungry!",
        "response": "Spot purrs happily at you before shoveling the food into her face.\nData still hasn't noticed you, but you notice he's painting a picture of a trombone that's... sweaty?",
        "wrong": "There's nothing you can do here at the moment.  That cat needs food!",
		"room_type": "item_room",
        "answer": "",
		"solved": "Data is hard at work painting a ...sweaty trombone?!",
        "given_item": "",
        "required_item": "cat food",
        "trigger": True,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "b4",
		"SIDE_RIGHT": False,
	},
    'b6': {
        "room_type": "hall",
        "SIDE_UP": "a6",
        "SIDE_DOWN": "c6",
        "SIDE_LEFT": False,
        "SIDE_RIGHT": "b7"
    },
    'b7': {
        "room_type": "hall",
        "SIDE_UP": False,
        "SIDE_DOWN": False,
        "SIDE_LEFT": "b6",
        "SIDE_RIGHT": "b8"
    },
    'b8': {
        "room_type": "hall",
        "SIDE_UP": "a8",
        "SIDE_DOWN": "c8",
        "SIDE_LEFT": "b7",
        "SIDE_RIGHT": False
    },
    'c1': {
        "name": "Barclay's Room",
		"description": "A small, disorderly room where Brocolli resides",
		"info": "Reg looks worried, as usual. He's pacing back and forth, occasionally biting his knuckle.",
		"item_request": "\"I... I was going to ask Deanna on a d-date tonight, but I can't work up the nerve.  If only I could just ...smell her...\"", 
        "response": "\"T-T-Thank you..?\" Barclay grabs the leotard and resumes his pacing. \"God I wish Geordi wasn't hogging the holodeck!\nIf I still had my super brain powers I'd show him!\"",
		"room_type": "item_room",
        "wrong": "\"I just need ...something of hers so I can think clearly.\"",
        "answer": "1",
		"solved": "Brocolli has resumed pacing back and forth, this time occasionally huffing Troi's leotard.",
        "given_item": "",
        "required_item": "leotard",
        "trigger": True,
		"SIDE_UP": 'b1',
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
	},
    'c2': {
        "room_type": "hall",
        "SIDE_UP": "a2",
        "SIDE_DOWN": False,
        "SIDE_LEFT": False,
        "SIDE_RIGHT": "c3"
    },
    'c3': {
        "name": "Transporter Room",
		"description": "O'Brian stands at attention for weeks at a time in here.",
		"info": "O'Brian is in here, grumbling about Keiko and fidgeting with a small flute.",
		"puzzle": "O'Brian says to you: \"Ken yer believe she wants ter name 'er Keiko Jr.? 'Elp me a choose a better name, ken ya?!\"\nWhat would YOU name the baby?",
        "solved": "O'Brian is standing at the control panel, staring straight ahead and grumbling to himself.",
        "response": "O'Brian says: \"Molly... Aye, I reckon Molly'r do ...fer now\" in one of the most offensively stereotypical accents you've ever read.\nHe hands you the flute and returns to his default position.",
		"room_type": "quiz_room",
        "wrong": "\"I really donnae think Keiko would approve o' that name\"",
        "given_item": "flute",
        "answer": "molly",
        "required_item": False,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": "c2",
		"SIDE_RIGHT": False,
        "trigger": False,
	},
    'c4': {
        "name": 'Wesleys Room',
		"description": "Half child's playpen, half science lab.",
		"info": "A small, terrified child is cowering in the corner -- Oh, it's the boy! Ensign Wesley!",
		"puzzle": "Wesley, decked out in a cool rainbow jumpsuit, asks you why people do drugs and what makes them feel good and are they bad and he won't stop going on about it...\nYou've got to silence this kid somehow",
        "response": "You tell Wesley to shut up and knock him over with barely any effort, effectively silencing him. While he returns to his corner, you start rifling through his personal belongings.",
        "wrong": "Wesley is unrelenting.  He starts showing off his many science projects and asking about what happens on Risa and wondering where Spot is and asking for his mother and saying he will be a captain someday and telling you about his crush and...",
        "solved": "Wesley is cowering in the corner, afraid and annoying.",
		"room_type": "quiz_room",
        "answer": "shut up wesley",
        "given_item": "",
        "required_item": False,
		"SIDE_UP": "b4",
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": False,
        "trigger": False,
	},
    'c5': {
        "name": "Counselor Troi's Office",
		"description": "You are in Counselor Troi's office.",
		"info": "Troi looks as bored as a cardboard cutout.  She can sense you judging her from across the room.",
		"item_request": "Troi demands you leave unless you brought her favorite food.", 
        "response": "Troi violently snatches the chocolate from your hands and begins eating it in an inapropriately erotic manner.\nWhile she's distracted, you grab her ridiculous workout leotard from her nighstand like a creep.",
        "wrong": "You don't need to be an empath to know Troi is angry you don't have chocolate.",
		"room_type": "item_room",
        "answer": "",
		"solved": "Troi is busy slowly eating every layer of her chocolate.",
        "given_item": "leotard",
        "required_item": "chocolate",
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "c6",
        "trigger": False,
	},
    'c6': {
        "room_type": "hall",
        "SIDE_UP": "b6",
        "SIDE_DOWN": False,
        "SIDE_LEFT": "c5",
        "SIDE_RIGHT": False
    },
    'c7': {
        "name": "Riker's Boudoir",
		"description": "A powerful musk eminates from the doorway",
		"info": "You enter Riker's room, and pass through a thick haze of romantic incense.\nThe lights are low and Riker stands before you in a silk robe.\n",
		"puzzle": "Riker eyes you up and down and sadly shakes his head.\n\"I don't think so.  I'm looking for someone with a little more ...experience.\"",
        "puzzle_2": "Riker eyes you up and down and smirks softly.\n\"If only I had my 'bone, I'd get this party started.\" Great. Riker's 'bone could be ANYWHERE.",
        "puzzle_3": "Riker eyes you up and down, his jaw drops.\n\"I dream of a galaxy where your eyes are the stars and the universe worships the night.\"\nHe tries to serenade you, but he can barely move the shaft of his 'bone.\n\"This 'bone is way too dry. Be a dear and find me some bone oil, would you?\"",
        "response": "\"Actually, on second thought, Rikey likey\" he purrs, licking his moustache. \"You're looking up to par for this one on one...\"",
        "response_2": "\"Mmm... now we're talking.  But this 'bone seems to be bone dry!\"",
        "response_3": "\"Great. Let me just lube up this 'bone and we'll be in business.\"",
        "final_response": "Riker hesitates, says \"Ha. I'll show you.\" He squints at you, then raises the 'bone to his mouth and starts to blow.\nIt's obvious he hasn't mastered this one yet, but in an effort to impress you\n...he keeps trying.  It sounds awful.\nWhile he's distracted, you punch the button that unlocks the Turbolift.",
        "wrong": "Riker needs someone who knows a little more about the way things work.",
        "wrong_2": "\"Can I help you Ensign? Go grab my 'bone!\"",
        "wrong_3": "\"Ensign, I am waiting to put that oil on my 'bone!\"",
		"room_type": "end",
        "step": 0,
        "answer": "nightbird",
		"solved": "Riker is busy desperately trying to figure out how to play Night Bird.",
        "given_item": "",
        "required_item": "trombone",
        "required_item_2": "bone oil",
        "trigger": True,
		"SIDE_UP": False,
		"SIDE_DOWN": False,
		"SIDE_LEFT": False,
		"SIDE_RIGHT": "c8",
        "trigger": False,
	},
    'c8': {
        "room_type": "hall",
        "SIDE_UP": "b8",
        "SIDE_DOWN": False,
        "SIDE_LEFT": "c7",
        "SIDE_RIGHT": False
    }
}