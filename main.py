from map import Room
from item import Item
import sys


#ascii art goes WOO
def print_game_over_ascii(text):
    for char in text:
        print(char, end="")
    print()

game_over = """

⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⠴⠶⠶⠶⠶⠶⠶⠶⠶⢤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠶⣤⡀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⡄⠀⠀⠀
⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⠀
⢰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀
⣿⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡄⠀⢹⡄
⡏⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⡇
⣿⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⢸⡇
⢹⡆⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⣾⠀
⠈⢷⡀⢸⡇⠀⢀⣠⣤⣶⣶⣶⣤⡀⠀⠀⠀⠀⠀⢀⣠⣶⣶⣶⣶⣤⣄⠀⠀⣿⠀⣼⠃⠀
⠀⠈⢷⣼⠃⠀⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⡾⠃⠀⠀
⠀⠀⠈⣿⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⠃⠀⢸⡇⠀⠀⠀
⠀⠀⠀⣿⠀⠀⠘⢿⣿⣿⣿⣿⡿⠃⠀⢠⠀⣄⠀⠀⠙⢿⣿⣿⣿⡿⠏⠀⠀⢘⡇⠀⠀⠀
⠀⠀⠀⢻⡄⠀⠀⠀⠈⠉⠉⠀⠀⠀⣴⣿⠀⣿⣷⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⢸⡇⠀⠀⠀
⠀⠀⠀⠈⠻⣄⡀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣟⠳⣦⡀⠀⠀⠀⠸⣿⡿⠀⢻⣿⡟⠀⠀⠀⠀⣤⡾⢻⡏⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⡄⢻⠻⣆⠀⠀⠀⠈⠀⠀⠀⠈⠀⠀⠀⢀⡾⢻⠁⢸⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⡇⠀⡆⢹⠒⡦⢤⠤⡤⢤⢤⡤⣤⠤⡔⡿⢁⡇⠀⡿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⡇⠀⢣⢸⠦⣧⣼⣀⡇⢸⢀⣇⣸⣠⡷⢇⢸⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣷⠀⠈⠺⣄⣇⢸⠉⡏⢹⠉⡏⢹⢀⣧⠾⠋⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠈⠉⠙⠓⠚⠚⠋⠉⠁⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠶⠦⣤⣤⣤⡤⠶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀

"""

#camera ascii
def camera_art(text):
    for char in text:
        print(char, end="")
    print()

camera_art = """                                   
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠶⣞⡩⠽⢷⣆⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⡤⢿⠀⢹⠖⠒⡛⠧⠐⠉⣧⠀⠀⠀⠀
⠀⢀⡠⠴⣲⣭⡁⠲⠇⢈⡑⢚⠪⠭⠤⠤⢄⣀⣿⠀⠀⠀⠀
⢠⠃⠤⠄⠉⠉⠀⠐⠉⣡⠞⠁⢀⡴⠞⠉⢉⣩⠿⠶⠤⣄⠀
⢸⠀⠀⠀⠀⡄⠀⠀⣰⠃⠀⢠⡞⠀⠀⡴⢋⣴⣿⣿⣷⡘⣆
⢸⠀⠀⠀⠀⡇⠀⠀⡏⠀⠀⣾⠀⠀⡜⢀⣾⣿⣤⣾⣿⡇⣿
⢨⠀⠀⠀⠀⡇⠀⠀⣇⠀⠀⡏⠀⠀⡇⢸⣿⣿⣿⣿⣿⢁⡏ 
⠈⠀⣀⠀⠀⣷⠀⠀⠘⢄⠀⢳⠀⠀⡇⠸⣿⣿⣹⡿⢃⡼⠁
⢰⡀⠛⠓⠀⢻⠀⠀⠀⠀⢙⣻⡷⠦⣼⣦⣈⣉⣡⡴⠚⠀⠀
⠀⢷⣄⡀⠀⠀⠀⢀⡠⠖⠋⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀
 ⠀⠉⠛⠓⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  
"""
#actually using the camera
camera = Item()


#map stuff - more for future reference than application here...
studyRoom = Room("Study Room")
meetingRoom = Room("Meeting Room")
storytimeRoom = Room("Storytime Room") 

studyRoom.get_linked_room("meetingRoom");
meetingRoom.get_linked_room("studyRoom");
meetingRoom.get_linked_room("storytimeRoom");
storytimeRoom.get_linked_room("meetingRoom");

studyRoom.set_description("The study room is filled with carved, dated Victorian furniture. ")
studyRoom.describe()

meetingRoom.set_description("The tables are arranged in a T shape. Waiting in the middle, is a stunning figure.")
meetingRoom.describe()

storytimeRoom.set_description("Colourful images stand out from the decrepid library. Beautifully colourful murals of children's fables are scattered across the walls in a dazzling array.")
storytimeRoom.describe()

# function to check room visits
meetingRoom.visit_room(meetingRoom)
storytimeRoom.visit_room(storytimeRoom)

#Coding the storyline, actual printed text and conversation
print("Welcome to  Nosferatu  Library!")
print("As you walk past, you read a sign saying 'quaere explorare, non enim determinat exploratio defectus excogitatoris'.")
print("Thanks to your Paranormal Studies class, you understand the Latin to  be: 'seek to explore, for the designer does not settle for lack of exploration'.")
print("As you think on the Latin phrase, you wait for the Professor  of your Paranormal Studies class.")
print("As you arrived early, you question to explore the environment!")

print("Do you  want to enter the library?")
roomChoice = input("> ")


    


#third act
def studyRoom():
    if (bookChoice == "no"):
                print("Professor Aaron stares at you from the corner of the room.")
                print("So you expect to perform well, in research, in MY department, without doing a humble line of reading!?")
                print("Professor Aaron snaps you into atomic dust!")
                print_game_over_ascii(game_over)
                sys.exit()

    if (bookChoice == "yes"):
            print("You feel the urge to make your way to the study room. ")
            print("Suddenly door open, and a mysterious force pulls you down. You are dragged through the halls to the study room!")
            print("Aaron Pho Phessor]: Ha HA HA! You've fully stumbled into my trap mere mortal?!")
            print("What do you want to say to Aaron Pro Phessor? Choose a number.")
            print("1]: Hey... You look so young for your age...")
            print("2]: You smell bad man...")
            print("3]: Hey, I know you...")
            response6 = input("> ")

            if (response6 == "2"):
                print("Aaron Pho Phessor]: How DARE YOU?! I'll have you know I have the latest range of enfernal colognes!")
                print("Aaron Pho Phessor looks at you disappointingly, and pummels you into the ground. You are library much for eternity.")
                print_game_over_ascii(game_over)
                sys.exit()

            if (response6 == "1"):
                print("Aaron Pho Phessor]: Wha- **he starts blushing** A biblical being like myself?!")
                print("What do you want to say to Aaron Pro Phessor? Choose 1 or 2.")
                print("1]: Just kidding man... you look like you knew Adam and Eve personally...")
                print("2]: Anytime bud!. Was wondering if you had a minute to spare to talk about how you were turned?")
                response11 = input("> ")


                if (response11 == "1"):
                    print("Professor Aaron stands there absolutely unbothered by your insult!")
                    print("Professor Aaron]: think your puny insults shall disturb me, mere human!")
                    print("Professor Aaron replays your most embarassing memories over for the whole of eternity.")
                    print("You recall the time you slipped on invisible stairs.")
                    print("You relive the occasion you stopped in the middle of the road, staring at maps and realising you have to turn all the way back.")
                    print("Professor Aaron even brings you back to the moment you said 'You too', when a waiter said 'Enjoy your meal'. ")
                    print("DEATH BY PSYCHOLOGICAL TORTURE (EMBARASSING!)")
                    print_game_over_ascii(game_over)   
                    sys.exit()


                if (response11 == "2"):
                    print("Professor Aaron stares at you with glinting eyes...")
                    print("A moment passes. Silence bestows across the grand library.")
                    print("Professor Aaron]:  Her name was...")
                    print("Professor Aaron]:  Josephine...")
                    print("Professor Aaron sheds a tear.")
                    print("Professor Aaron]: We were supposed to get married! ")
                    print("Professor Aaron]:  The night before the wedding...")
                    print("Professor Aaron]:  she lost her 'something blue'...")
                    print("Professor Aaron]:  I let her pet blue canary out, she never got over it.")
                    print("Professor Aaron]:  She was so upset that she cursed me!  Leaving me here... not a mirror to look in, AND without a picture of myself...")
                    print("What will you say? Choose a number")
                    print("1]: Aww... Buddy! You can still do so much in your afterlife!")
                    print("2]: Yo momma so fat...")
                    response8_1 = input("> ")

                    if (response8_1 == "2"):
                        print("Professor Aaron's face visibly saddens.")
                        print("Professor Aaron]: You think I would let to even think a sentence about MY momma, and let you get away with it?")
                        print("Professor Aaron locks eyes with you. The sheer aura, unfathomable rage from his vicinity blasts you across the study room.")
                        print("DEATH BY AURA")
                        print_game_over_ascii(game_over)
                        sys.exit()

                    if (response8_1 == "1"):
                        print("Professor Aaron]: Oh yeah?...  Like what! It's nothing but coffins, cobwebs and criminally boring books up in here!")
                        print("You ruffle through your backpack...")
                        print("What do you want to give to Professor Aaron? Type a number.")
                        print("1]: Customised Playstation, with his initials embedded on it, with a PSN subscription.")
                        print("2]: A batch of homemade cinnamon rolls.")
                        print("3]: Your camera.")
                        backpack1 = input("> ")


                        if (backpack1 == "1"):
                            print("Professor Aaron gives you a grinning look.")
                            print("No you didn't *He is now uncontrollably happy*.")
                            print("You and Professor  Aaron spend the rest of eternity in perpetual video games fixations.")
                            print("He even spends a day, phase shifting through the walls of Rockstar Games, to retrieve a GTA VI prototype!")
                            print("You form a brotherlike bond and was invited to his deathday party from then onwards!")
                            print("You feel an urge to store the memory...")
                            camera3_3 = input("> ")

                            if (camera3_3 == "camera"):
                                camera.use()
                                print(camera_art)

                                if (camera.uses == 3):
                                    if (camera3_3 is not "camera"):
                                        print("You and Professor Aaron still enjoy yourselves! But you are stuck in the library for the rest of eternity...")
                                        return  

                                    else:
                                        print("Whoops! You dropped your camera and broke it... You spend the rest of your days in the library having fun!)")


                        if (backpack1 == "2"):
                            print("Professor Aaron gives you a grinning look.")
                            print("No you didn't! *He is now uncontrollably happy*.")
                            print("You and Professor  Aaron spend the rest of eternity baking alternative forms of pastries!")
                            print("You form a brotherlike bond and was invited to his deathday party from then onwards!")
                            print("You feel the urge to capture the moment!")
                            camera3_4 = input("> ")

                            if (camera3_4 == "camera"):
                                camera.use()
                                print(camera_art)

                                if (camera.uses == 3):
                                    if (camera3_4 is not "camera"):
                                        print("You and Professor Aaron still enjoy yourselves! But you are stuck in the library for the rest of eternity...")
                                        return  

                                    else:
                                        print("Whoops! You dropped your camera and broke it... You spend the rest of your days in the library having fun!)")


                        if (backpack1 == "3"):
                            print("Professor Aaron drops the camera!")
                            print("Professor Aaron]: I- I am so sorry.")
                            print("A long silence passes. You are in shock. You signed off to have the camera...")
                            print("Professor Aaron]: So you just don't carry a case for it or anything huh?")
                            print("You shake your head.")
                            print("A painfully long winded silence passes over the two of you.")
                            print("Professor Aaron looking ashamed, waves the door open.")
                            print("You leave the library, wondering how you were going to replace such an expensive paranormal camera.")
                            print("The university campus ground opens up before you, swallowing you whole, taking you as a payment for the broken camera!")
                            print("DEATH BY UNPAID BILLS")
                            print_game_over_ascii(game_over)
                            sys.exit()


                #choosing option 3 gives them the psycho analysis or psychotortue ending.
            if (response6 == "3"):
                print("3]: You were cursed by an ancient ghost... Why would you insult a ghost of all things?!") 
                print("Aaron Pho Phessor]: You think you know me mere mortal? You don't even see the irony of your idiotic words!")
                print("Aaron Pho Phessor]: You haven't seen anything yet!")
                print("Aaron Pho Phessor begins to transform in a storm of dark matter into his final form!")
                print("To your surprise, it reveals Professor Aaron! ")
                print("Professor Aaron]: Now you shall be trapped here forevermore. Forced to serve me for eternity!")
                print("What do you say to him?! Choose 1 or 2.")
                print("1]: I would but I wouldn't wanna stare at you for all those years!")
                print("2]: Do you want to talk about... how you feel?")
                response9 = input("> ")

                #psychotorture ending
                if (response9 == "1"):
                    print("Professor Aaron stands there absolutely unbothered by your insult!")
                    print("Professor Aaron]: think your puny insults shall disturb me, mere human!")
                    print("Professor Aaron replays your most embarassing memories over for the whole of eternity.")
                    print("You recall the time you slipped on invisible stairs.")
                    print("You relive the occasion you stopped in the middle of the road, staring at maps and realising you have to turn all the way back.")
                    print("Professor Aaron even brings you back to the moment you said 'You too', when a waiter said 'Enjoy your meal'. ")
                    print("DEATH BY PSYCHOLOGICAL TORTURE (EMBARASSING!)")
                    print_game_over_ascii(game_over)
                    sys.exit()                    
                
                #psychotherapy ending
                if (response9 == "2"):
                    print("Professor Aaron stares at you with glinting eyes...")
                    print("A moment passes. Silence bestows across the grand library.")
                    print("Professor Aaron]:  Her name was...")
                    print("Professor Aaron]:  Josephine...")
                    print("Professor Aaron sheds a tear.")
                    print("Professor Aaron]: We were supposed to get married! ")
                    print("Professor Aaron]:  The night before the wedding...")
                    print("Professor Aaron]:  she lost her 'something blue'...")
                    print("Professor Aaron]:  I let her pet blue canary out, she never got over it.")
                    print("Professor Aaron]:  She was so upset that she cursed me!  Leaving me here... not a mirror to look in, AND without a picture of myself...")
                    print("What will you say? Choose a number")
                    print("1]: I mean- Would you like me to take your picture...")
                    print("2]: Wha- Then was this all for you to have a picture of yourself?!")
                    response10 = input("> ")

                    if (response10 == "1"):
                        print("Professor Aaron]: Thanks bro!")
                        print("Professor Aaron]: When I tell you, I've waited CENTURIES for this!")
                        print("Professor Aaron glides into the air, sending books into a fictional storm!")
                        print("Looking very elegant and poised, Professor Aaron graces your camera with a moment of his regal grace.")
                        print("> ")
                        camera3_1 = input("> ")

                        if (camera3_1 == "camera"):
                            camera.use()
                            print(camera_art)

                            if (camera.uses == 3):
                                if (camera3_1 is not "camera"):
                                    print("You and Professor Aaron still enjoy yourselves! But you are stuck in the library for the rest of eternity... You find out all of his lore and are invited to his deathday parties!")
                                    return  

                            else:
                                print("Whoops! You dropped your camera and broke it... You spend the rest of your days in the library having fun!)")

                        #insert camera use
                    
                    if response10 == "2":
                        print("Professor Aaron]: YES.  I thought  you would have pieced it together by now.")
                        print("Professor Aaron]: I set this whole thing up, got a Doctorates in  Paranormal Research.")
                        print("Professor Aaron]: Completed SEVERAL roles for Nosferatu University, until I was a senior ranking member.")
                        print("Professor Aaron]: If I sat here recalling all I did to get you to this point... I'd be in ghost jail...")
                        print("You think to yourself... wouldn't ghost jail just be hell?")
                        print("Professor Aaron]: Anyways. you taking it or not brah")
                        print("What do you say to him? Choose 1 or 2.")
                        print("1]: Or what grandpa?! Your so old you remember when 'computer' meant a person who did calculations!")
                        print("2]: Eugh. You are not even worth my time... ")
                        response7 = input("> ")

                        if (response7 == "2"):
                            print("Aaron Pro Phessor]: Well- I- ")
                            print("Aaron Pho Phessor glares at you, wondering how such an insignificant being could be so obliviously insulting to their superior... ")
                            print("Aaron Pho Phessor drags you down into the beyond to work as an eternal sewage cleaner.")
                            print("You spend the rest of eternity cleaning hellish poop.")
                            print_game_over_ascii(game_over)
                            sys.exit()


                        if (response7 == "1"):
                            print("Aaron Pro Phessor]: Well- I- ")
                            print("Aaron Pro Phessor]: Your so young...")
                            print("Aaron Pro Phessor]: - you have your whole life ahead of you...")
                            print("Aaron's eyes glint in the pale moonlight.")
                            print("What do you say to Aaron? Type a number.")
                            print("1]: Aww... Buddy! You can still do so much in your afterlife!")
                            print("2]: Yo momma so fat...")
                            response8 = input("> ")

                            if (response8 == "2"):
                                print("Professor Aaron's face visibly saddens.")
                                print("Professor Aaron]: You think I would let to even think a sentence about MY momma, and let you get away with it?")
                                print("Professor Aaron locks eyes with you. The sheer aura, unfathomable rage from his vicinity blasts you across the study room.")
                                print("DEATH BY AURA")
                                print_game_over_ascii(game_over)
                                sys.exit()

                            if (response8 == "1"):
                                print("Professor Aaron]: Oh yeah?...  Like what! It's nothing but coffins, cobwebs and criminally boring books up in here!")
                                print("You ruffle through your backpack...")
                                print("What do you want to give to Professor Aaron? Type a number.")
                                print("1]: Customised Playstation, with his initials embedded on it, with a PSN subscription.")
                                print("2]: A batch of homemade cinnamon rolls.")
                                print("3]: Your camera.")
                                backpack = input("> ")

                            if (backpack == "1"):
                                print("Professor Aaron gives you a grinning look.")
                                print("No you didn't *He is now uncontrollably happy*.")
                                print("You and Professor  Aaron spend the rest of eternity in perpetual video games fixations.")
                                print("He even spends a day, phase shifting through the walls of Rockstar Games, to retrieve a GTA VI prototype!")
                                print("You form a brotherlike bond and was invited to his deathday party from then onwards!")
                                print("You feel an urge to store the memory...")
                                camera3 = input("> ")

                                if (camera3 == "camera"):
                                    camera.use()
                                    print(camera_art)

                                    if (camera.uses == 3):
                                        if (camera3 is not "camera"):
                                            print("You and Professor Aaron still enjoy yourselves! But you are stuck in the library for the rest of eternity...")
                                            return  

                                        else:
                                            print("Whoops! You dropped your camera and broke it... You spend the rest of your days in the library having fun!)")


                            if (backpack == "2"):
                                print("Professor Aaron gives you a grinning look.")
                                print("No you didn't! *He is now uncontrollably happy*.")
                                print("You and Professor  Aaron spend the rest of eternity baking alternative forms of pastries!")
                                print("You form a brotherlike bond and was invited to his deathday party from then onwards!")
                                print("You feel the urge to capture the moment!")
                                camera3_2 = input("> ")

                                if (camera3_2 == "camera"):
                                    camera.use()
                                    print(camera_art)

                                    if (camera.uses == 3):
                                        #print_castleart()
                                        #initiate turtle document
                                        if (camera3_2 is not "camera"):
                                            print("You and Professor Aaron still enjoy yourselves! But you are stuck in the library for the rest of eternity...")
                                            return  

                                        else:
                                            print("Whoops! You dropped your camera and broke it... You spend the rest of your days in the library having fun!)")


                            if (backpack == "3"):
                                print("Professor Aaron drops the camera!")
                                print("Professor Aaron]: I- I am so sorry.")
                                print("A long silence passes. You are in shock. You signed off to have the camera...")
                                print("Professor Aaron]: So you just don't carry a case for it or anything huh?")
                                print("You shake your head.")
                                print("A painfully long winded silence passes over the two of you.")
                                print("Professor Aaron looking ashamed, waves the door open.")
                                print("You leave the library, wondering how you were going to replace such an expensive paranormal camera.")
                                print("The university campus ground opens up before you, swallowing you whole, taking you as a payment for the broken camera!")
                                print("DEATH BY UNPAID BILLS")
                                print_game_over_ascii(game_over)
                                sys.exit()




#the second act
def meetingRoom():
            print("You adventure on to the Meeting Room.")
            currentRoom = meetingRoom
            print("The meeting room has tables neatly prepared for an eternal conference. ")
            print("In the middle of the table, rests an astonishing figure!")
            print("Haley]: I've been waiting a while for a special someone like you...")
            print("What do you say to Haley? Choose 1 or 2.")
            print("1]: Ha ha! I've ironically been looking for you! So what's a beautiful ghost like you doing in a place like this?")
            print("2]: Ok?....")
            response3 = input("> ")

            if response3 == "1":
                    print("Haley]: A poltergeist keeps me and my little sister all locked up here!")
                    print("Haley]: I though I'd have to wait a million years for a Prince Charming like you to come along")
                    print("Haley]: ♥ **blows you a kiss**")
                    print("You feel flustered and suddenly have the urge to capture the moment.")
                    camera2 = input("> ")

                    if (camera2 == "camera"):
                        camera.use()
                        print(camera_art)

                    if (camera.uses == 1):
                        storytimeRoom()

                    if camera.uses == 2:
                        studyRoom()

                    else:
                        print("Whoops! You dropped your camera! Type camera to see if it still works (which cannot be said for your brain!)")


            if response3 == "2":
                    print("Haley]: I mean- well, What are you doing here handsome?")
                    print("1]: Looking for your disgusting face! No wonder your all alone here...")
                    print("2]: Looking for my newest muse!")
                    print("What do you say to Haley? Choose 1 or 2")
                    response4 = input("> ")

                    if response4 == "1":
                        print("Haley]: Ugh! How dare you waste my time!")
                        print("Haley stares at you with a menacing gaze. She turns you into a rose, and burns you to ash. ")
                        print_game_over_ascii(game_over)
                        sys.exit()

                    if response4 == "2":
                        print("Haley]: I'd be happy to accommodate to such an sweetheart!")
                        print("Haley elegantly glides around, finding the best pose for a photo!")
                        print("Haley]: ♥ **blows you a kiss**")
                        print("You feel flustered and suddenly have the urge to capture the moment.")
                        camera2_1 = input("> ")

                        if (camera2_1 == "camera"):
                            camera.use()
                            print(camera_art)

                            if (camera.uses == 1):
                                storytimeRoom()

                            if camera.uses == 2:
                                studyRoom()
                              
                        else:
                            print("Whoops! You dropped your camera! Type 'camera' to see if it still works (which cannot be said for your brain!)")
                            camera2_1 = input("> ")
                            return  
        

#first act
def storytimeRoom():
                    print("You make your way to the Children's Storytime Room.")
                    print("In the distance, in the far corner of the room awaits a small figure.")
                    print("You see they are reading Grimm's Fairytales. Do you interrupt?")
                    interrupt = input("> ")

                    if (interrupt == "no"):
                        print("Abigail]: Huh- *she gasps* Noone likes being scared!")
                        print("You see tears form in Abigail's eyes.")
                        print("Abigail]: What are you doing here? We don't get a lot of visitors at this nocturnal hour!")
                        print("1]: My Professor asked me to collect some photograph evidence of... well... you.")
                        print("2]: Looking for freaks like you!")
                        print("What do you say to Abigail?")
                        response2 = input("> ")

                        if (response2 == "2"):
                            print("Abigail]: Eh! How dare you!")
                            print("Abigail looks at you with disgust. She can't believe even in her afterlife, humans still cannot respect her space. She turns you into a copy of Harry Potter and the Philosopher's Stone. (As she has been meaning to reread the series.)")
                            print("DEATH BY ROWLING")
                            print_game_over_ascii(game_over)
                            sys.exit()
                        
                            
                        if (response2 == "1"):
                            print("Abigail: Well, I hope I could help! Truth is, I'd love to see what I look like.")
                            print("Abigail:  I've been stuck in this section of the library, because of... well ...")
                            print("Abigail]: Anyways, feel free to take the picture! ")
                            camera1_1 = input("> ")

                            if (camera1_1 == "camera"):
                                camera.use()
                                print(camera_art)

                                if (camera.uses == 1):
                                    meetingRoom()

                                if camera.uses == 2:
                                    studyRoom()


                                if (camera1_1 is not "camera"):
                                    print("Abigail stares at you awkwardly. She wonders if you will have the incentive to type 'camera', at anytime soon.")
                                    return     


                            else:
                                print("Whoops! You dropped your camera! Type camera to see if it still works (which cannot be said for your brain!)")


                    if (interrupt == "yes"):
                        print("Abigail]: huh-")
                        print("Abigail]: wh- who is there? ")
                        print("*You seem to have scared Abigail.*")
                        print("1]: Didn't mean to shake you! I was just wondering if we could chat for a bit?")
                        print("2]: HA! You really scare easily don't you kiddo!?")
                        print("What do you say to Abigail? Choose between 1 or 2.")
                        response = input("> ")

                        if (response == "2"):
                            print("Abigail]: Eh! How dare you!")
                            print("Abigail looks at you with disgust. She can't believe even in her afterlife, humans still cannot respect her space. She turns you into a copy of Harry Potter and the Philosopher's Stone. (As she has been meaning to reread the series.)")
                            print("DEATH BY ROWLING")
                            print_game_over_ascii(game_over)
                            sys.exit()

                        if (response == "1"):
                            print("Abigail]: Ah- It's okay! I'm just a bit jumpy sometimes!")
                            print("Abigail]: Anyways, what are you doing around here? We don't get a lot of visitors when we come out!")
                            print("1]: My professor asked me to collect some photograph evidence of... well... you.")
                            print("2]: Looking for freaks like you!")
                            print("What do you say to Abigail? ")
                            response1 = input("> ")

                            if (response1 == "1"):
                                print("Abigail]: Well, I hope I could help! Truth is, I'd love to see what I look like.")
                                print("Abigail]:  I've been stuck in this section of the library, because of... well ...")
                                print("Abigail]: Anyways, feel free! ")
                                camera1 = input("> ")

                                if (camera1 == "camera"):
                                    camera.use()
                                    print(camera_art)

                                    if (camera.uses == 1):
                                        meetingRoom()

                                    if camera.uses == 2:
                                        studyRoom()

                            else:
                                print("Woops! You dropped your camera! Type camera to see if it still works (which cannot be said for your brain!)")

                            if (response1 == "2"):
                                print("Abigail]: Eh! How dare you!")
                                print("Abigail looks at you with disgust. She can't believe even in her afterlife, humans still cannot respect her space. She turns you into a copy of Harry Potter and the Philosopher's Stone. (As she has been meaning to reread the series.)")
                                print("DEATH BY ROWLING")
                                print_game_over_ascii(game_over)
                                sys.exit()





#the first act
if roomChoice == "no":
        print("You were arrested for trespassing on campus property. You now spend the rest of your life in jail.")
        print_game_over_ascii(game_over)
        sys.exit()

if roomChoice == "yes":
    print("You enter the library!")
    print("As you enter, a waft of dust and rotting books fill your nose.")
    print("Do you take a look at a book?")

    bookChoice = input("> ")
    if bookChoice == "yes":
        print("You grab a book off the shelf, and open to see various information on ghosts.")
        print("Poltergeists are associated with physical disturbances like moving objects, noises and levitation. They are often linked to strong emotions, especially fear.")
        print("As you read, you hear a chair across from you slowly move out of place.")
        print("A notible poltergeist is the spirit of Aaron Pro Phessor - An aristocrat from the 1800s who accidentally called an ancient ghost ugly, plunging him into a umbearable lack of access to mirrors, and his hair gel.")
        print("You find yourself making your way back to the study room, where you await your Professor.")
        print("Professor Aaron greets you with a warm smile as you enter the study room.")
        print("Professor Aaron]: Hello there, my most promising student! ")
        print("Professor Aaron]: I have something for you")
        print("*you receive a paranormal camera*")
        print("Type 'camera' when to use the camera when  the moment is right!")
        print("Professor Aaron]: This camera will assist you on your investigation.")
        print("Professor Aaron]: It will allow you to photograph the invisible occupants of these hallowed halls.")
        print("Onwards, my protege. You must return all 3 pictures to make it out without a scratch!")

        print("Do you go to the go to the Storytime Room or the Meeting Room?")
        roomchoice1 = input("> ").lower()

        if (roomchoice1 == "storytime room"):
            storytimeRoom()

        if (roomchoice1 == "storytime"):
            storytimeRoom()

        if (roomchoice1  == "meeting room"):
            meetingRoom()

        if (roomchoice1 == "meeting"):
            meetingRoom()

    elif(bookChoice == "no"):
        print("You decide to not read the book.")
        print("You find yourself making your way back to the study room, where you anxiously await your professor, feeling somewhat unprepared.")
        print("Professor Aaron greets you with a warm smile as you enter the study room.")
        print("Professor Aaron]: Hello there, student!")
        print("Professor Aaron]: I have something for you")
        print("*you receive a paranormal camera*")
        print("Type 'camera' when to use the camera when  the moment is right!")
        print("Professor Aaron]: This camera will assist you on your investigation.")
        print("Professor Aaron]: It will allow you to photograph the invisible occupants of these hallowed halls.")
        print("Onwards, my protege. You must return all 3 pictures to make it out without a scratch!")
        print("Do you go to the go to the Storytime Room or the Meeting Room?")
        roomchoice2 = input("> ").lower()

        if (roomchoice2 == "storytime room"):
            storytimeRoom()

        if (roomchoice2 == "storytime"):
            storytimeRoom()

        if (roomchoice2  == "meeting room"):
            meetingRoom()

        if (roomchoice2 == "meeting"):
            meetingRoom()


#player can terminate at any input
while True:
    command = input("> ")
    if command == "quit":
        break
