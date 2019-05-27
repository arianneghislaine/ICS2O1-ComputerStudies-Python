#Mr. Kordbacheh
#Arianne and Celina
#May 6th 2019
#Culminating Activity

#################################################################
#############LIST: iventory and pets#############################
#############SET: human interaction confirmation#################
#############DICTIONARY: weaponry shop###########################
#############TUPLES: credits#####################################
#############RANDOM VARIABLE: lottery############################
#################################################################



### IMPORTANT VARIABLES ###
coins = 5
points = 0
import time
import random

####Greetings####
print('Welcome to Treasure-island!\n')
#input the user's name and greet them
userN=input('Enter your username\n')
time.sleep(1)
print('Welcome',userN,'to Treasure-island\n')
time.sleep(2)

##START OF TUPLES FOR THE CREDITS##
tuple=('This', 'game', 'is', 'made', 'by', 'Arianne', 'and', 'Celina', 'for', 'elementary', 'students', '.')
print (tuple)
print ('The length of the tuple is')
print (len(tuple))
print ('\n')
##END OF TUPLES FOR THE CREDITS##



########FUN FACTs##########
print ('Here are some fun facts to feed your brain with knowledge.')
funFacts = ['The word “hundred” comes from the old Norse term, “hundrath”, which actually means 120 and not 100.','In a room of 23 people there’s a 50% chance that two people have the same birthday.','A new word is added to the dictionary every two hours.','A pangram sentence is one that contains every letter in the language.','“Forty” is the only number that is spelt with letters arranged in alphabetical order.']
print (funFacts)
print ('\n')
########FUN FACTs##########

###START OF TEST IF HUMAN##USED SETS##
print ('A question will pop up.\n Answering it correctly, proves that you are a human. \n Only humans are allowed to play this game.\n')
this_is_a_set= {'A','B','C'}
print (this_is_a_set)
question = input ('What is missing?')
if question=='D':
    print ('That is the correct answer')
    this_is_a_set.add ('D')
    print ('This is now the new set.')
    print (this_is_a_set)
    print ('You are indeed a human who is intellectual enough to answer the question.')
    


    ###############################################

    ##LIST FOR INVENTORY##
    inventory = ['scissors','pen','paper']
    print(inventory)
    time.sleep(2)
    print('These are the items that are currently inside your inventory.')
    time.sleep(2)

    instruct=input('Press 1 to see the instructions.\n')
    time.sleep(2)
    if instruct=='1':
        print('Here are the instructions')
        print('Type your answer after the question. ')
        print('Type <<hint>> to get a clue. ')
        print('Every time you get the wrong answer, you will lose a heart')
        print('Type <<end game>> to exit the program.\n ')

    #####PETS########LIST######## 
        print ('These are the options for the pet. It will help you in journey at Treasure Land.\n')
        #types of pets
        companionList = ['dog','cat','bird','fox','penguin','panda','dinosaur','snake','unicorn']
        #call the list
        print (companionList)
        time.sleep(2)
        print('You may pick a pet of your choice from the list\n')
        #let the player choose a pet
        companionType = input('What kind of pet would you want to have? Choose above the list.\n')
        time.sleep(2)
        if 'dog''cat''bird''fox''penguin''panda''dinosaur''snake''unicorn':
            print ('You have chosen a',companionType,'.\n')
            #name the companion
            companionName = input('What do you want to name the pet?\n')
            print ('You have named your',companionType,'as',companionName)
            print ('That is such a cool name!\n')
        else:
            print ('Were you not following instructions?\n')
            print ('Ok, you will enjoy the journey without the disturbance of a companion.\n')

    #####DICTIONARY for buying weapons#####

    print('Welcome to Weaponry Shop! Here are the options available.\n')
    print('You have 5 coins to start with.\nType the name of the weapon you desire to choose.\nThe price of the weapons are next to each weapon choice.\n')
    weaponry = {"sword":3,"gun":5,"spear":2}
    print (weaponry)                                                                          

        ####buyAweapon
    buyAweapon = input ('Choose your weapon here.')
    if buyAweapon=='sword':
        print('Sword costs 3 coins.')
        coins = coins - 3
        print('You have',coins,'coins left.')
        inventory.append('sword')
        print ('The following items are in your inventory:')
        print (inventory)


    ###################################################
        print('Ok, cool.')
        print('Continue playing the game.')
        print('What level are you?')
        print('Level 1 is for Grade 1 and 2')
        print('Level 2 is for Grade 3 and 4')
        print('Level 3 is for Grade 5')
        lvl=input('Type the level number here. ')



        ###THIS IS LEVEL 1###
        #Question1
        if lvl=='1':
            print('You have chosen level 1\n')
            q1=input('Susie needs 13 balloons.\n She already has 4 balloons.\n How many more balloons does she need?\n')
            if q1=='9':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q1=='hint':
                print('13-4\n')
                q1=input('Susie needs 13 balloons. She already has 4 balloons. How many more balloons does she need?\n')
                if q1=='9':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q1=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')
                    

            #Question2
            q2=input('Order these numbers from lowest to highest: 12,25,18, 23,14\n')
            if q2=='12,14,18,23,25':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q2=='hint':
                print('ascending\n')
                q2=input('Order these numbers from lowest to highest: 12,25,18,23,14\n')
                if q2=='12,14,18,23,25':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q2=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')


            #Question3
            q3=input('My book has 28 pages. I have read 23 pages. How many pages are left to read?\n')
            if q3=='5':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q3=='hint':
                print('28-23\n')
                q3=input('My book has 28 pages. I have read 23 pages. How many pages are left to read?\n')
                if q3=='5':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q3=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question4
            q4=input('I ___ good at climbing trees\n.')
            if q4=='am':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q4=='hint':
                print('It is a helping verb.\n')
                q4=input('I ___ good at climbing trees\n.')
                if q4=='am':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q4=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question5
            q5=input('I have to ___ my homework.\n')
            if q5=='do':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q5=='hint':
                print('It starts with the letter D.\n')
                q5=input('I have to ___ my homework.\n')
                if q5=='do':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q5=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question6
            q6=input('They ___ at the zoo.\n ')
            if q6=='are':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q6=='hint':
                print('It has 3 letters and starts with an a\n')
                q6=input('They ___ at the zoo.\n')
                if q6=='are':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q6=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question7
            q7=input('Sonny and Baek  ___  eating ice cream.\n ')
            if q7=='are':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q7=='hint':
                print('It has 3 letters and starts with an a\n')
                q7=input('Sonny and Baek  ___  eating ice cream.\n')
                if q7=='are':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q7=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question8
            q8=input('Jono   : ____________ is your name? Johny : My name is Johny.\n ')
            if q8=='What':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q8=='hint':
                print('It has 4 letters and starts with a w\n')
                q8=input('Jono   : ____________ is your name? Johny : My name is Johny.\n ')
                if q8=='What':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q8=='skip':
                print ('DODGED\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question9
            q9=input('Mr. Zaka    : _________________ are you late?  Sayyaf      : I am late because I woke up late.')
            if q9=='Why':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q9=='hint':
                print('It has 3 letters and starts with a w')
                q9=input('Mr. Zaka    : _________________ are you late?  Sayyaf      : I am late because I woke up late.')
                if q9=='Why':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q9=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question10
            q10=input('I like playing soccer.There are ___________ syllables in the sentence above.')
            if q10=='6':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q10=='hint':
                print('What is 3 times 2')
                q10=input('I like playing soccer.There are ___________ syllables in the sentence above.')
                if q10=='6':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q10=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question11
            q11=input('He is sick.The past tense of the sentence above is ________________.')
            if q11=='He was sick.':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q11=='hint':
                print('Change “is” to past tense.')
                q11=input('He is sick.The past tense of the sentence above is ________________.')
                if q11=='He was sick.':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q11=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question12
            q12=input('My teeth are ___ sharp as a knife.')
            if q12=='as':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q12=='hint':
                print('Two letters')
                q12=input('My teeth are ___ sharp as a knife.')
                if q12=='as':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q12=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question13
            q13=input('What comes just before 413.')
            if q13=='414':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q13=='hint':
                print('Two 4s and one 1 ')
                q13=input('What comes just before 413.')
                if q13=='414':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q13=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question14
            q14=input('In 289, the place value of 8 is____________.')
            if q14=='Tens':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q14=='hint':
                print('It is after ones')
                q14=input('In 289, the place value of 8 is____________.')
                if q14=='Tens':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q14=='skip':
                print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question15
            q15=input('Three hundred and one can be written as ______.')
            if q15=='301':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            elif q15=='hint':
                
                print('Three digits')
                q15=input('Three hundred and one can be written as ______.')
                if q15=='301':
                    print('That is the correct answer')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                else:
                    print ('Too bad, that is the incorrect answer.')
                    print ('You have',points,'points.')

                    #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                    
            elif q15=='skip':
                print('Dodged\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            else:
                print('Too bad, that is the incorrect answer.')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


        ###THIS IS LEVEL 2###
        elif lvl=='2':
            print('You have chosen level 2\n')

            #lvl2Question1
            q21=input('What is the plural form of a knife \nA.\nKnifes \nB.\nKnives \nC.\nNifes \nD.\nNives\n(Enter A,B,C or D in caps)\n')
            if q21=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q21=='hint':
                print('Bee\n')
                q21=input('What is the plural form of a knife \nA.\nKnifes \nB.\nKnives \nC.\nNifes \nD.\nNives\n(Enter A,B,C or D in caps)\n')
                if q21=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q21=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question2
            q22=input('What is the past tense of  place? \nA.\nPlaced \nB.\nPlased \nC.\nPlasis \nD.\nPlacing\n(Enter A,B,C or D in caps)\n')
            if q22=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q22=='hint':
                print('Ends with ed\n')
                q22=input('What is the past tense of  place? \nA.\nPlaced \nB.\nPlased \nC.\nPlasis \nD.\nPlacing\n(Enter A,B,C or D in caps)\n')
                if q22=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q22=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question3
            q23=input('What is the verb in the following sentence.\n <<I set the glass on the table.>> \nA.\nGlass \nB.\nSet \nC.\nOn \nD.\nTable\n(Enter A,B,C or D in caps)\n')
            if q23=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q23=='hint':
                print('It starts with S\n')
                q23=input('What is the verb in the following sentence.\n <<I set the glass on the table.>> \nA.\nGlass \nB.\nSet \nC.\nOn \nD.\nTable\n(Enter A,B,C or D in caps)\n')
                if q23=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q23=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question4
            q24=input('What is the helping verb? Sidney has helped stray cats before. \nA.\nHas \nB.\nCats \nC.\nHelped \nD.\nBefore\n(Enter A,B,C or D in caps)\n')
            if q24=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q24=='hint':
                print('It starts with H\n')
                q24=input('What is the helping verb? Sidney has helped stray cats before. \nA.\nHas \nB.\nCats \nC.\nHelped \nD.\nBefore\n(Enter A,B,C or D in caps)\n')
                if q24=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q24=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question5
            q25=input('I was amazed ______ his brilliance. \nA.\nWith \nB.\nAt \nC.\nBy \nD.\nTo\n(Enter A,B,C or D in caps)\n')
            if q25=='C':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q25=='hint':
                print('It has two letters\n')
                q25=input('I was amazed ______ his brilliance. \nA.\nWith \nB.\nAt \nC.\nBy \nD.\nTo\n(Enter A,B,C or D in caps)\n')
                if q25=='C':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q25=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question6
            q26=input('He is afflicted ________ a serious illness. \nA.\nWith \nB.\nTo \nC.\nBy \nD.\nof\n(Enter A,B,C or D)\n')
            if q26=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q26=='hint':
                print('It has 4 letters\n')
                q26=input('He is afflicted ________ a serious illness. \nA.\nWith \nB.\nTo \nC.\nBy \nD.\nof\n(Enter A,B,C or D)\n')
                if q26=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q26=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question7
            q27=input('She does not agree _________ me \nA.\nUpon \nB.\nTo \nC.\nWith\nD.\nNone of these\n(Enter A,B,C or D)\n')
            if q27=='C':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q27=='hint':
                print('It has 4 letters\n')
                q27=input('She does not agree _________ me \nA.\nUpon \nB.\nTo \nC.\nWith\nD.\nNone of these\n(Enter A,B,C or D)\n')
                if q27=='C':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q27=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question8
            q28=input('You must apologize ________. him for your rude behaviour. \nA.\nTo \nB.\nBy \nC.\nWith\nD.\nFor\n(Enter A,B,C or D)\n')
            if q28=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q28=='hint':
                print('It has 2 letters\n')
                q28=input('You must apologize ________. him for your rude behaviour. \nA.\nTo \nB.\nBy \nC.\nWith\nD.\nFor\n(Enter A,B,C or D)\n')
                if q28=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q28=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question9
            q29=input('The roman numeral for 18 is ______.\n')
            if q29=='XVIII':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q29=='hint':
                print('Three Is\n')
                q29=input('The roman numeral for 18 is ______.\n')
                if q29=='XVIII':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q29=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question10
            q210=input('The smallest 4-digit number formed by using the digits 0, 3, 5, 6 is _____.\n')
            if q210=='0356':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q210=='hint':
                print('Reverse the order of 6530\n')
                q210=input('The smallest 4-digit number formed by using the digits 0, 3, 5, 6 is _____.\n')
                if q210=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q210=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question11
            q211=input('The predecessor of the smallest 5-digit number is ____.\n')
            if q211=='9999':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q211=='hint':
                print('After 9998\n')
                q211=input('The predecessor of the smallest 5-digit number is ____.\n')
                if q211=='9999':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q211=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question12
            q212=input('The smallest single digit composite number is ____.\n')
            if q212=='4':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q212=='hint':
                print('2 times 2\n')
                q212=input('The smallest single digit composite number is ____.\n')
                if q212=='4':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q212=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question13
            q213=input('Ram had 342 coins in his collection. How would you write 342?\n')
            if q213=='Three hundred forty two':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q213=='hint':
                print('How do you say 342?\n')
                q213=input('Ram had 342 coins in his collection. How would you write 342?\n')
                if q213=='Three hundred forty two':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q213=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question14
            q214=input('Which number comes next in the series? 4231, 4331, 4431, ?\n')
            if q214=='4531':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q214=='hint':
                print('+100\n')
                q214=input('Which number comes next in the series? 4231, 4331, 4431, ?\n')
                if q214=='4531':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q214=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question15
            q215=input('Rita had $150. She wanted to buy a doll that costs $230. How much more money does she need to buy the doll?\n')
            if q215=='$80':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


            elif q215=='hint':
                print('230-150\n')
                q215=input('Rita had $150. She wanted to buy a doll that costs $230. How much more money does she need to buy the doll?\n')
                if q215=='$80':
                    print('That is the correct answer\n')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
                else:
                    print('Too bad, that is the incorrect answer.\n')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            elif q215=='skip':
                print('Dodged!\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            else:
                print('Too bad, that is the incorrect answer.\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


        ###THIS IS LEVEL 3###
        else:
            print('You have chosen level 3\n')

            #lvl3Question1
            q31=input('A large box contains 18 small boxes and each small box contains 25 chocolate bars.\n How many chocolate bars are in the large box?\n')
            if q31=='450':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q31=='hint':
                print('Multiplication\n')
                q31=input('A large box contains 18 small boxes and each small box contains 25 chocolate bars.\n How many chocolate bars are in the large box?\n')
                if q31=='450':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q31=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question2
            q32=input('Today I was late for school.\n But since it had happened for the first time, the teacher did not punish me.\n Which word can replace <<did not punish>> in the sentence given above?\n A. Excused \nB. Explained \n C. Examined \n D. Expected \n')
            if q32=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q32=='hint':
                print('Ends with an <<e>>\n')
                q32=input('Today I was late for school.\n But since it had happened for the first time, the teacher did not punish me.\n Which word can replace <<did not punish>> in the sentence given above?\n A. Excused \nB. Explained \n C. Examined \n D. Expected \n')
                if q32=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q32=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

             #lvl3Question3
            q33=input('It takes John 25 minutes to walk to the car park and 45 minutes to drive to work. \n At what time should he get out of the house in order to get to work at 9:00 a.m.?\n')
            if q33=='7:50am':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q33=='hint':
                print('Subtraction\n')
                q33=input('It takes John 25 minutes to walk to the car park and 45 minutes to drive to work. \n At what time should he get out of the house in order to get to work at 9:00 a.m.?\n')
                if q33=='7:50am':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q33=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question4
            q34=input('Shahrukh Khan is a <<famous>> actor today.But when he came to Mumbai several years ago, he was almost _____________.\nWhich word is OPPOSITE in meaning to "famous" and can be used to complete the sentence given above?\nA. Poor\nB. Unknown\nC. Familiar\nD. Worthless\n')
            if q34=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q34=='hint':
                print('Starts with ‘U’\n')
                q34=input('Shahrukh Khan is a <<famous>> actor today.But when he came to Mumbai several years ago, he was almost _____________.\nWhich word is OPPOSITE in meaning to "famous" and can be used to complete the sentence given above?\nA. Poor\nB. Unknown\nC. Familiar\nD. Worthless\n')
                if q34=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q34=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question5
            q35=input('Kim can walk 4 kilometers in one hour.\nHow long does it take Kim to walk 18 kilometers?\n')
            if q35=='4 hours and 30 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q33=='hint':
                print('4 x 4 = 16 km\n')
                q35=input('Kim can walk 4 kilometers in one hour.\nHow long does it take Kim to walk 18 kilometers?\n')
                if q35=='4 hours and 30 minutes':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q35=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question6
            q6=input('The car in front of our scooter stopped "abruptly".\nSince we were not prepared for that, we banged hard into it!the word "abruptly" as used in the sentence above, means__________\nDiscuss\nA. Slowly, without hurry\nB. Suddenly, without warning\nC. Loudly, with a hard bang\nD. Quietly, in an unusual manner\n ')
            if q6=='b':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q6=='hint':
                print('D is not the answer')
                q6=input('The car in front of our scooter stopped "abruptly".\nSince we were not prepared for that, we banged hard into it!the word "abruptly" as used in the sentence above, means__________\nDiscuss\nA. Slowly, without hurry\nB. Suddenly, without warning\nC. Loudly, with a hard bang\nD. Quietly, in an unusual manner\n \n')
                if q6=='b':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q6=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question7
            q7=input('Linda bought 3 notebooks at $1.20 each; a box of pencils at $1.50 and a box of pens at $1.70.\n How much did Linda spend?\n')
            if q7=='$6.80':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q7=='hint':
                print('Addition\n')
                q7=input('Linda bought 3 notebooks at $1.20 each; a box of pencils at $1.50 and a box of pens at $1.70.\n How much did Linda spend?\n')
                if q7=='$6.80':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q7=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question8
            q8=input('Which option punctuates the sentence given below CORRECTLY?\nNisha said to me do you want me to drop you home.\nA. Nisha said to me,"do you want me to drop you home."\nB. Nisha said to me,"Do you want me to drop you home?"\nC. Nisha said to me"do you want me to drop you home?"\nD. Nisha said to me"Do you want me to drop you home."\n ')
            if q8=='b':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q8=='hint':
                print('D is not the answer\n')
                q8=input('Which option punctuates the sentence given below CORRECTLY?\nNisha said to me do you want me to drop you home.\nA. Nisha said to me,"do you want me to drop you home."\nB. Nisha said to me,"Do you want me to drop you home?"\nC. Nisha said to me"do you want me to drop you home?"\nD. Nisha said to me"Do you want me to drop you home."\n ')
                if q8=='b':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q8=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question9
            q9=input('Tom and Bob have a total of 49 toys.\nIf Bob has 5 more toys than Tom, how many toys does each one have?\n')
            if q9=='22,27':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q9=='hint':
                print('Tom’s is an even number. Bob’s is an odd number.')
                q9=input('Tom and Bob have a total of 49 toys.\nIf Bob has 5 more toys than Tom, how many toys does each one have?\n')
                if q9=='22,27':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q9=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question10
            q10=input('Identify the sentence with a SPELLING MISTAKE\nA. It is neccessary to drink enough water daily.\nB. Having a balanced diet is extremely important.\nC. Spinach is plentiful in Minerals like Iron and Calcium.\nD. Tomatoes and Lemons are good sources of Vitamin C\n')
            if q10=='a':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q10=='hint':
                print('D is not the answer\n')
                q10=input('Identify the sentence with a SPELLING MISTAKE\nA. It is neccessary to drink enough water daily.\nB. Having a balanced diet is extremely important.\nC. Spinach is plentiful in Minerals like Iron and Calcium.\nD. Tomatoes and Lemons are good sources of Vitamin C\n')
                if q10=='a':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q10=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question11
            q11=input('John can eat a quarter of a pizza in one minute.\nHow long does it take John to eat one pizza and a half?\n')
            if q11=='6 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q11=='hint':
                print('Multiplication\n')
                q11=input('John can eat a quarter of a pizza in one minute. How long does it take John to eat one pizza and a half?')
                if q11=='6 minutes':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q11=='skip':
                print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question12
            q12=input('Identify the option with CORRECT spelling to complete the sentence given below.\n The_________________took his sheep and goats to graze on the mountains.\nA. Shepard\nB. Shepherd\nC. Shepperd\nD. Sheepherd\n')
            if q12=='b':
                print('That is the correct answer')
            elif q12=='hint':
                print('D is not the answer')
                q12=input('Identify the option with CORRECT spelling to complete the sentence given below.\n The_________________took his sheep and goats to graze on the mountains.\nA. Shepard\nB. Shepherd\nC. Shepperd\nD. Sheepherd\n')
                if q12=='b':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q12=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question13
            q13=input('John read the quarter of the time that Tom read.\nTom read only two-fifth of the time that Sasha read.\nSasha read twice as long as Mike.\nIf Mike read 5 hours, how long did John read?\n')
            if q13=='1 hour':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q13=='hint':
                print('John reads ⅕ of what Mike reads.')
                q13=input('John read the quarter of the time that Tom read.\nTom read only two-fifth of the time that Sasha read.\nSasha read twice as long as Mike.\nIf Mike read 5 hours, how long did John read?\n')
                if q13=='1 hour':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q13=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question14
            q14=input('Which sentence has a GRAMMAR mistake?\nA. My mother told me to put the book back in it is place.\nB. Tennis has lost its charm for me since Steffi Graf retired.\nC. My neighbours dog tries to catch its own tail all day long.\nD. It is sunday tomorrow so I will watch my favourite cartoons.\n')
            if q14=='a':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q14=='hint':
                print('D is not the answer')
                q14=input('Which sentence has a GRAMMAR mistake?\nA. My mother told me to put the book back in it is place.\nB. Tennis has lost its charm for me since Steffi Graf retired.\nC. My neighbours dog tries to catch its own tail all day long.\nD. It is sunday tomorrow so I will watch my favourite cartoons.\n')
                if q14=='a':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q14=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question15
            q15=input('How many minutes are in one week?')
            if q15=='10,080 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            elif q15=='hint':
                print('Multiplication')
                q15=input('How many minutes are in one week?')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')
                if q15=='10,080 minutes':
                    print('That is the correct answer')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                else:
                    print('Too bad, that is the incorrect answer.')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                                #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                    
            elif q15=='skip':
                print('Dodged!\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                            #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            else:
                print('Too bad, that is the incorrect answer.')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                            #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
    ###################################################


    if buyAweapon=='gun':
        print('Gun costs 5 coins.')
        coins = coins - 5
        print('You have',coins,'coins left.')
        inventory.append('gun')
        print ('The following items are in your inventory:')
        print (inventory)

    ####

    ###################################################
        print('Ok, cool.')
        print('Continue playing the game.')
        print('What level are you?')
        print('Level 1 is for Grade 1 and 2')
        print('Level 2 is for Grade 3 and 4')
        print('Level 3 is for Grade 5')
        lvl=input('Type the level number here. ')



        ###THIS IS LEVEL 1###
        #Question1
        if lvl=='1':
            print('You have chosen level 1\n')
            q1=input('Susie needs 13 balloons.\n She already has 4 balloons.\n How many more balloons does she need?\n')
            if q1=='9':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q1=='hint':
                print('13-4\n')
                q1=input('Susie needs 13 balloons. She already has 4 balloons. How many more balloons does she need?\n')
                if q1=='9':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q1=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')
                    

            #Question2
            q2=input('Order these numbers from lowest to highest: 12,25,18, 23,14\n')
            if q2=='12,14,18,23,25':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q2=='hint':
                print('ascending\n')
                q2=input('Order these numbers from lowest to highest: 12,25,18,23,14\n')
                if q2=='12,14,18,23,25':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q2=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')


            #Question3
            q3=input('My book has 28 pages. I have read 23 pages. How many pages are left to read?\n')
            if q3=='5':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q3=='hint':
                print('28-23\n')
                q3=input('My book has 28 pages. I have read 23 pages. How many pages are left to read?\n')
                if q3=='5':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q3=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question4
            q4=input('I ___ good at climbing trees\n.')
            if q4=='am':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q4=='hint':
                print('It is a helping verb.\n')
                q4=input('I ___ good at climbing trees\n.')
                if q4=='am':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q4=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question5
            q5=input('I have to ___ my homework.\n')
            if q5=='do':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q5=='hint':
                print('It starts with the letter D.\n')
                q5=input('I have to ___ my homework.\n')
                if q5=='do':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q5=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question6
            q6=input('They ___ at the zoo.\n ')
            if q6=='are':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q6=='hint':
                print('It has 3 letters and starts with an a\n')
                q6=input('They ___ at the zoo.\n')
                if q6=='are':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q6=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question7
            q7=input('Sonny and Baek  ___  eating ice cream.\n ')
            if q7=='are':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q7=='hint':
                print('It has 3 letters and starts with an a\n')
                q7=input('Sonny and Baek  ___  eating ice cream.\n')
                if q7=='are':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q7=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question8
            q8=input('Jono   : ____________ is your name? Johny : My name is Johny.\n ')
            if q8=='What':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q8=='hint':
                print('It has 4 letters and starts with a w\n')
                q8=input('Jono   : ____________ is your name? Johny : My name is Johny.\n ')
                if q8=='What':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q8=='skip':
                print ('DODGED\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question9
            q9=input('Mr. Zaka    : _________________ are you late?  Sayyaf      : I am late because I woke up late.')
            if q9=='Why':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q9=='hint':
                print('It has 3 letters and starts with a w')
                q9=input('Mr. Zaka    : _________________ are you late?  Sayyaf      : I am late because I woke up late.')
                if q9=='Why':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q9=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question10
            q10=input('I like playing soccer.There are ___________ syllables in the sentence above.')
            if q10=='6':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q10=='hint':
                print('What is 3 times 2')
                q10=input('I like playing soccer.There are ___________ syllables in the sentence above.')
                if q10=='6':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q10=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question11
            q11=input('He is sick.The past tense of the sentence above is ________________.')
            if q11=='He was sick.':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q11=='hint':
                print('Change “is” to past tense.')
                q11=input('He is sick.The past tense of the sentence above is ________________.')
                if q11=='He was sick.':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q11=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question12
            q12=input('My teeth are ___ sharp as a knife.')
            if q12=='as':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q12=='hint':
                print('Two letters')
                q12=input('My teeth are ___ sharp as a knife.')
                if q12=='as':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q12=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question13
            q13=input('What comes just before 413.')
            if q13=='414':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q13=='hint':
                print('Two 4s and one 1 ')
                q13=input('What comes just before 413.')
                if q13=='414':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q13=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question14
            q14=input('In 289, the place value of 8 is____________.')
            if q14=='Tens':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q14=='hint':
                print('It is after ones')
                q14=input('In 289, the place value of 8 is____________.')
                if q14=='Tens':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q14=='skip':
                print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question15
            q15=input('Three hundred and one can be written as ______.')
            if q15=='301':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            elif q15=='hint':
                
                print('Three digits')
                q15=input('Three hundred and one can be written as ______.')
                if q15=='301':
                    print('That is the correct answer')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                else:
                    print ('Too bad, that is the incorrect answer.')
                    print ('You have',points,'points.')

                    #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                    
            elif q15=='skip':
                print('Dodged\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            else:
                print('Too bad, that is the incorrect answer.')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


        ###THIS IS LEVEL 2###
        elif lvl=='2':
            print('You have chosen level 2\n')

            #lvl2Question1
            q21=input('What is the plural form of a knife \nA.\nKnifes \nB.\nKnives \nC.\nNifes \nD.\nNives\n(Enter A,B,C or D in caps)\n')
            if q21=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q21=='hint':
                print('Bee\n')
                q21=input('What is the plural form of a knife \nA.\nKnifes \nB.\nKnives \nC.\nNifes \nD.\nNives\n(Enter A,B,C or D in caps)\n')
                if q21=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q21=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question2
            q22=input('What is the past tense of  place? \nA.\nPlaced \nB.\nPlased \nC.\nPlasis \nD.\nPlacing\n(Enter A,B,C or D in caps)\n')
            if q22=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q22=='hint':
                print('Ends with ed\n')
                q22=input('What is the past tense of  place? \nA.\nPlaced \nB.\nPlased \nC.\nPlasis \nD.\nPlacing\n(Enter A,B,C or D in caps)\n')
                if q22=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q22=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question3
            q23=input('What is the verb in the following sentence.\n <<I set the glass on the table.>> \nA.\nGlass \nB.\nSet \nC.\nOn \nD.\nTable\n(Enter A,B,C or D in caps)\n')
            if q23=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q23=='hint':
                print('It starts with S\n')
                q23=input('What is the verb in the following sentence.\n <<I set the glass on the table.>> \nA.\nGlass \nB.\nSet \nC.\nOn \nD.\nTable\n(Enter A,B,C or D in caps)\n')
                if q23=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q23=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question4
            q24=input('What is the helping verb? Sidney has helped stray cats before. \nA.\nHas \nB.\nCats \nC.\nHelped \nD.\nBefore\n(Enter A,B,C or D in caps)\n')
            if q24=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q24=='hint':
                print('It starts with H\n')
                q24=input('What is the helping verb? Sidney has helped stray cats before. \nA.\nHas \nB.\nCats \nC.\nHelped \nD.\nBefore\n(Enter A,B,C or D in caps)\n')
                if q24=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q24=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question5
            q25=input('I was amazed ______ his brilliance. \nA.\nWith \nB.\nAt \nC.\nBy \nD.\nTo\n(Enter A,B,C or D in caps)\n')
            if q25=='C':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q25=='hint':
                print('It has two letters\n')
                q25=input('I was amazed ______ his brilliance. \nA.\nWith \nB.\nAt \nC.\nBy \nD.\nTo\n(Enter A,B,C or D in caps)\n')
                if q25=='C':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q25=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question6
            q26=input('He is afflicted ________ a serious illness. \nA.\nWith \nB.\nTo \nC.\nBy \nD.\nof\n(Enter A,B,C or D)\n')
            if q26=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q26=='hint':
                print('It has 4 letters\n')
                q26=input('He is afflicted ________ a serious illness. \nA.\nWith \nB.\nTo \nC.\nBy \nD.\nof\n(Enter A,B,C or D)\n')
                if q26=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q26=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question7
            q27=input('She does not agree _________ me \nA.\nUpon \nB.\nTo \nC.\nWith\nD.\nNone of these\n(Enter A,B,C or D)\n')
            if q27=='C':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q27=='hint':
                print('It has 4 letters\n')
                q27=input('She does not agree _________ me \nA.\nUpon \nB.\nTo \nC.\nWith\nD.\nNone of these\n(Enter A,B,C or D)\n')
                if q27=='C':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q27=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question8
            q28=input('You must apologize ________. him for your rude behaviour. \nA.\nTo \nB.\nBy \nC.\nWith\nD.\nFor\n(Enter A,B,C or D)\n')
            if q28=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q28=='hint':
                print('It has 2 letters\n')
                q28=input('You must apologize ________. him for your rude behaviour. \nA.\nTo \nB.\nBy \nC.\nWith\nD.\nFor\n(Enter A,B,C or D)\n')
                if q28=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q28=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question9
            q29=input('The roman numeral for 18 is ______.\n')
            if q29=='XVIII':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q29=='hint':
                print('Three Is\n')
                q29=input('The roman numeral for 18 is ______.\n')
                if q29=='XVIII':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q29=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question10
            q210=input('The smallest 4-digit number formed by using the digits 0, 3, 5, 6 is _____.\n')
            if q210=='0356':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q210=='hint':
                print('Reverse the order of 6530\n')
                q210=input('The smallest 4-digit number formed by using the digits 0, 3, 5, 6 is _____.\n')
                if q210=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q210=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question11
            q211=input('The predecessor of the smallest 5-digit number is ____.\n')
            if q211=='9999':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q211=='hint':
                print('After 9998\n')
                q211=input('The predecessor of the smallest 5-digit number is ____.\n')
                if q211=='9999':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q211=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question12
            q212=input('The smallest single digit composite number is ____.\n')
            if q212=='4':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q212=='hint':
                print('2 times 2\n')
                q212=input('The smallest single digit composite number is ____.\n')
                if q212=='4':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q212=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question13
            q213=input('Ram had 342 coins in his collection. How would you write 342?\n')
            if q213=='Three hundred forty two':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q213=='hint':
                print('How do you say 342?\n')
                q213=input('Ram had 342 coins in his collection. How would you write 342?\n')
                if q213=='Three hundred forty two':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q213=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question14
            q214=input('Which number comes next in the series? 4231, 4331, 4431, ?\n')
            if q214=='4531':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q214=='hint':
                print('+100\n')
                q214=input('Which number comes next in the series? 4231, 4331, 4431, ?\n')
                if q214=='4531':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q214=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question15
            q215=input('Rita had $150. She wanted to buy a doll that costs $230. How much more money does she need to buy the doll?\n')
            if q215=='$80':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


            elif q215=='hint':
                print('230-150\n')
                q215=input('Rita had $150. She wanted to buy a doll that costs $230. How much more money does she need to buy the doll?\n')
                if q215=='$80':
                    print('That is the correct answer\n')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
                else:
                    print('Too bad, that is the incorrect answer.\n')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            elif q215=='skip':
                print('Dodged!\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            else:
                print('Too bad, that is the incorrect answer.\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


        ###THIS IS LEVEL 3###
        else:
            print('You have chosen level 3\n')

            #lvl3Question1
            q31=input('A large box contains 18 small boxes and each small box contains 25 chocolate bars.\n How many chocolate bars are in the large box?\n')
            if q31=='450':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q31=='hint':
                print('Multiplication\n')
                q31=input('A large box contains 18 small boxes and each small box contains 25 chocolate bars.\n How many chocolate bars are in the large box?\n')
                if q31=='450':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q31=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question2
            q32=input('Today I was late for school.\n But since it had happened for the first time, the teacher did not punish me.\n Which word can replace <<did not punish>> in the sentence given above?\n A. Excused \nB. Explained \n C. Examined \n D. Expected \n')
            if q32=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q32=='hint':
                print('Ends with an <<e>>\n')
                q32=input('Today I was late for school.\n But since it had happened for the first time, the teacher did not punish me.\n Which word can replace <<did not punish>> in the sentence given above?\n A. Excused \nB. Explained \n C. Examined \n D. Expected \n')
                if q32=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q32=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

             #lvl3Question3
            q33=input('It takes John 25 minutes to walk to the car park and 45 minutes to drive to work. \n At what time should he get out of the house in order to get to work at 9:00 a.m.?\n')
            if q33=='7:50am':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q33=='hint':
                print('Subtraction\n')
                q33=input('It takes John 25 minutes to walk to the car park and 45 minutes to drive to work. \n At what time should he get out of the house in order to get to work at 9:00 a.m.?\n')
                if q33=='7:50am':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q33=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question4
            q34=input('Shahrukh Khan is a <<famous>> actor today.But when he came to Mumbai several years ago, he was almost _____________.\nWhich word is OPPOSITE in meaning to "famous" and can be used to complete the sentence given above?\nA. Poor\nB. Unknown\nC. Familiar\nD. Worthless\n')
            if q34=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q34=='hint':
                print('Starts with ‘U’\n')
                q34=input('Shahrukh Khan is a <<famous>> actor today.But when he came to Mumbai several years ago, he was almost _____________.\nWhich word is OPPOSITE in meaning to "famous" and can be used to complete the sentence given above?\nA. Poor\nB. Unknown\nC. Familiar\nD. Worthless\n')
                if q34=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q34=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question5
            q35=input('Kim can walk 4 kilometers in one hour.\nHow long does it take Kim to walk 18 kilometers?\n')
            if q35=='4 hours and 30 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q33=='hint':
                print('4 x 4 = 16 km\n')
                q35=input('Kim can walk 4 kilometers in one hour.\nHow long does it take Kim to walk 18 kilometers?\n')
                if q35=='4 hours and 30 minutes':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q35=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question6
            q6=input('The car in front of our scooter stopped "abruptly".\nSince we were not prepared for that, we banged hard into it!the word "abruptly" as used in the sentence above, means__________\nDiscuss\nA. Slowly, without hurry\nB. Suddenly, without warning\nC. Loudly, with a hard bang\nD. Quietly, in an unusual manner\n ')
            if q6=='b':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q6=='hint':
                print('D is not the answer')
                q6=input('The car in front of our scooter stopped "abruptly".\nSince we were not prepared for that, we banged hard into it!the word "abruptly" as used in the sentence above, means__________\nDiscuss\nA. Slowly, without hurry\nB. Suddenly, without warning\nC. Loudly, with a hard bang\nD. Quietly, in an unusual manner\n \n')
                if q6=='b':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q6=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question7
            q7=input('Linda bought 3 notebooks at $1.20 each; a box of pencils at $1.50 and a box of pens at $1.70.\n How much did Linda spend?\n')
            if q7=='$6.80':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q7=='hint':
                print('Addition\n')
                q7=input('Linda bought 3 notebooks at $1.20 each; a box of pencils at $1.50 and a box of pens at $1.70.\n How much did Linda spend?\n')
                if q7=='$6.80':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q7=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question8
            q8=input('Which option punctuates the sentence given below CORRECTLY?\nNisha said to me do you want me to drop you home.\nA. Nisha said to me,"do you want me to drop you home."\nB. Nisha said to me,"Do you want me to drop you home?"\nC. Nisha said to me"do you want me to drop you home?"\nD. Nisha said to me"Do you want me to drop you home."\n ')
            if q8=='b':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q8=='hint':
                print('D is not the answer\n')
                q8=input('Which option punctuates the sentence given below CORRECTLY?\nNisha said to me do you want me to drop you home.\nA. Nisha said to me,"do you want me to drop you home."\nB. Nisha said to me,"Do you want me to drop you home?"\nC. Nisha said to me"do you want me to drop you home?"\nD. Nisha said to me"Do you want me to drop you home."\n ')
                if q8=='b':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q8=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question9
            q9=input('Tom and Bob have a total of 49 toys.\nIf Bob has 5 more toys than Tom, how many toys does each one have?\n')
            if q9=='22,27':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q9=='hint':
                print('Tom’s is an even number. Bob’s is an odd number.')
                q9=input('Tom and Bob have a total of 49 toys.\nIf Bob has 5 more toys than Tom, how many toys does each one have?\n')
                if q9=='22,27':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q9=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question10
            q10=input('Identify the sentence with a SPELLING MISTAKE\nA. It is neccessary to drink enough water daily.\nB. Having a balanced diet is extremely important.\nC. Spinach is plentiful in Minerals like Iron and Calcium.\nD. Tomatoes and Lemons are good sources of Vitamin C\n')
            if q10=='a':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q10=='hint':
                print('D is not the answer\n')
                q10=input('Identify the sentence with a SPELLING MISTAKE\nA. It is neccessary to drink enough water daily.\nB. Having a balanced diet is extremely important.\nC. Spinach is plentiful in Minerals like Iron and Calcium.\nD. Tomatoes and Lemons are good sources of Vitamin C\n')
                if q10=='a':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q10=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question11
            q11=input('John can eat a quarter of a pizza in one minute.\nHow long does it take John to eat one pizza and a half?\n')
            if q11=='6 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q11=='hint':
                print('Multiplication\n')
                q11=input('John can eat a quarter of a pizza in one minute. How long does it take John to eat one pizza and a half?')
                if q11=='6 minutes':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q11=='skip':
                print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question12
            q12=input('Identify the option with CORRECT spelling to complete the sentence given below.\n The_________________took his sheep and goats to graze on the mountains.\nA. Shepard\nB. Shepherd\nC. Shepperd\nD. Sheepherd\n')
            if q12=='b':
                print('That is the correct answer')
            elif q12=='hint':
                print('D is not the answer')
                q12=input('Identify the option with CORRECT spelling to complete the sentence given below.\n The_________________took his sheep and goats to graze on the mountains.\nA. Shepard\nB. Shepherd\nC. Shepperd\nD. Sheepherd\n')
                if q12=='b':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q12=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question13
            q13=input('John read the quarter of the time that Tom read.\nTom read only two-fifth of the time that Sasha read.\nSasha read twice as long as Mike.\nIf Mike read 5 hours, how long did John read?\n')
            if q13=='1 hour':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q13=='hint':
                print('John reads ⅕ of what Mike reads.')
                q13=input('John read the quarter of the time that Tom read.\nTom read only two-fifth of the time that Sasha read.\nSasha read twice as long as Mike.\nIf Mike read 5 hours, how long did John read?\n')
                if q13=='1 hour':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q13=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question14
            q14=input('Which sentence has a GRAMMAR mistake?\nA. My mother told me to put the book back in it is place.\nB. Tennis has lost its charm for me since Steffi Graf retired.\nC. My neighbours dog tries to catch its own tail all day long.\nD. It is sunday tomorrow so I will watch my favourite cartoons.\n')
            if q14=='a':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q14=='hint':
                print('D is not the answer')
                q14=input('Which sentence has a GRAMMAR mistake?\nA. My mother told me to put the book back in it is place.\nB. Tennis has lost its charm for me since Steffi Graf retired.\nC. My neighbours dog tries to catch its own tail all day long.\nD. It is sunday tomorrow so I will watch my favourite cartoons.\n')
                if q14=='a':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q14=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question15
            q15=input('How many minutes are in one week?')
            if q15=='10,080 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            elif q15=='hint':
                print('Multiplication')
                q15=input('How many minutes are in one week?')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')
                if q15=='10,080 minutes':
                    print('That is the correct answer')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                else:
                    print('Too bad, that is the incorrect answer.')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                                #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                    
            elif q15=='skip':
                print('Dodged!\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                            #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            else:
                print('Too bad, that is the incorrect answer.')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                            #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
    ###################################################
    ####


    if buyAweapon=='spear':
        print('Spear costs 2 coins.')
        coins = coins - 2
        print('You have',coins,'coins left.')
        inventory.append('spear')
        print ('The following items are in your inventory:')
        print (inventory)
        
    ####

    ###################################################
        print('Ok, cool.')
        print('Continue playing the game.')
        print('What level are you?')
        print('Level 1 is for Grade 1 and 2')
        print('Level 2 is for Grade 3 and 4')
        print('Level 3 is for Grade 5')
        lvl=input('Type the level number here. ')



        ###THIS IS LEVEL 1###
        #Question1
        if lvl=='1':
            print('You have chosen level 1\n')
            q1=input('Susie needs 13 balloons.\n She already has 4 balloons.\n How many more balloons does she need?\n')
            if q1=='9':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q1=='hint':
                print('13-4\n')
                q1=input('Susie needs 13 balloons. She already has 4 balloons. How many more balloons does she need?\n')
                if q1=='9':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q1=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')
                    

            #Question2
            q2=input('Order these numbers from lowest to highest: 12,25,18, 23,14\n')
            if q2=='12,14,18,23,25':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q2=='hint':
                print('ascending\n')
                q2=input('Order these numbers from lowest to highest: 12,25,18,23,14\n')
                if q2=='12,14,18,23,25':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q2=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')


            #Question3
            q3=input('My book has 28 pages. I have read 23 pages. How many pages are left to read?\n')
            if q3=='5':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q3=='hint':
                print('28-23\n')
                q3=input('My book has 28 pages. I have read 23 pages. How many pages are left to read?\n')
                if q3=='5':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q3=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question4
            q4=input('I ___ good at climbing trees\n.')
            if q4=='am':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q4=='hint':
                print('It is a helping verb.\n')
                q4=input('I ___ good at climbing trees\n.')
                if q4=='am':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q4=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question5
            q5=input('I have to ___ my homework.\n')
            if q5=='do':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q5=='hint':
                print('It starts with the letter D.\n')
                q5=input('I have to ___ my homework.\n')
                if q5=='do':            
                    print('That is the correct answer\n')                
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q5=='skip':
                print('Dodged')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question6
            q6=input('They ___ at the zoo.\n ')
            if q6=='are':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q6=='hint':
                print('It has 3 letters and starts with an a\n')
                q6=input('They ___ at the zoo.\n')
                if q6=='are':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q6=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question7
            q7=input('Sonny and Baek  ___  eating ice cream.\n ')
            if q7=='are':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q7=='hint':
                print('It has 3 letters and starts with an a\n')
                q7=input('Sonny and Baek  ___  eating ice cream.\n')
                if q7=='are':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q7=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question8
            q8=input('Jono   : ____________ is your name? Johny : My name is Johny.\n ')
            if q8=='What':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer\n')
            elif q8=='hint':
                print('It has 4 letters and starts with a w\n')
                q8=input('Jono   : ____________ is your name? Johny : My name is Johny.\n ')
                if q8=='What':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q8=='skip':
                print ('DODGED\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question9
            q9=input('Mr. Zaka    : _________________ are you late?  Sayyaf      : I am late because I woke up late.')
            if q9=='Why':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q9=='hint':
                print('It has 3 letters and starts with a w')
                q9=input('Mr. Zaka    : _________________ are you late?  Sayyaf      : I am late because I woke up late.')
                if q9=='Why':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q9=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question10
            q10=input('I like playing soccer.There are ___________ syllables in the sentence above.')
            if q10=='6':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q10=='hint':
                print('What is 3 times 2')
                q10=input('I like playing soccer.There are ___________ syllables in the sentence above.')
                if q10=='6':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q10=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question11
            q11=input('He is sick.The past tense of the sentence above is ________________.')
            if q11=='He was sick.':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q11=='hint':
                print('Change “is” to past tense.')
                q11=input('He is sick.The past tense of the sentence above is ________________.')
                if q11=='He was sick.':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q11=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question12
            q12=input('My teeth are ___ sharp as a knife.')
            if q12=='as':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q12=='hint':
                print('Two letters')
                q12=input('My teeth are ___ sharp as a knife.')
                if q12=='as':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q12=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question13
            q13=input('What comes just before 413.')
            if q13=='414':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q13=='hint':
                print('Two 4s and one 1 ')
                q13=input('What comes just before 413.')
                if q13=='414':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q13=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question14
            q14=input('In 289, the place value of 8 is____________.')
            if q14=='Tens':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
            elif q14=='hint':
                print('It is after ones')
                q14=input('In 289, the place value of 8 is____________.')
                if q14=='Tens':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q14=='skip':
                print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question15
            q15=input('Three hundred and one can be written as ______.')
            if q15=='301':
                points = points + 1
                print ('This is your score so far',points,'. Keep it going!')
                print('That is the correct answer')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            elif q15=='hint':
                
                print('Three digits')
                q15=input('Three hundred and one can be written as ______.')
                if q15=='301':
                    print('That is the correct answer')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                else:
                    print ('Too bad, that is the incorrect answer.')
                    print ('You have',points,'points.')

                    #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                    
            elif q15=='skip':
                print('Dodged\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            else:
                print('Too bad, that is the incorrect answer.')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


        ###THIS IS LEVEL 2###
        elif lvl=='2':
            print('You have chosen level 2\n')

            #lvl2Question1
            q21=input('What is the plural form of a knife \nA.\nKnifes \nB.\nKnives \nC.\nNifes \nD.\nNives\n(Enter A,B,C or D in caps)\n')
            if q21=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q21=='hint':
                print('Bee\n')
                q21=input('What is the plural form of a knife \nA.\nKnifes \nB.\nKnives \nC.\nNifes \nD.\nNives\n(Enter A,B,C or D in caps)\n')
                if q21=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q21=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question2
            q22=input('What is the past tense of  place? \nA.\nPlaced \nB.\nPlased \nC.\nPlasis \nD.\nPlacing\n(Enter A,B,C or D in caps)\n')
            if q22=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q22=='hint':
                print('Ends with ed\n')
                q22=input('What is the past tense of  place? \nA.\nPlaced \nB.\nPlased \nC.\nPlasis \nD.\nPlacing\n(Enter A,B,C or D in caps)\n')
                if q22=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q22=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question3
            q23=input('What is the verb in the following sentence.\n <<I set the glass on the table.>> \nA.\nGlass \nB.\nSet \nC.\nOn \nD.\nTable\n(Enter A,B,C or D in caps)\n')
            if q23=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q23=='hint':
                print('It starts with S\n')
                q23=input('What is the verb in the following sentence.\n <<I set the glass on the table.>> \nA.\nGlass \nB.\nSet \nC.\nOn \nD.\nTable\n(Enter A,B,C or D in caps)\n')
                if q23=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q23=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question4
            q24=input('What is the helping verb? Sidney has helped stray cats before. \nA.\nHas \nB.\nCats \nC.\nHelped \nD.\nBefore\n(Enter A,B,C or D in caps)\n')
            if q24=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q24=='hint':
                print('It starts with H\n')
                q24=input('What is the helping verb? Sidney has helped stray cats before. \nA.\nHas \nB.\nCats \nC.\nHelped \nD.\nBefore\n(Enter A,B,C or D in caps)\n')
                if q24=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q24=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question5
            q25=input('I was amazed ______ his brilliance. \nA.\nWith \nB.\nAt \nC.\nBy \nD.\nTo\n(Enter A,B,C or D in caps)\n')
            if q25=='C':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q25=='hint':
                print('It has two letters\n')
                q25=input('I was amazed ______ his brilliance. \nA.\nWith \nB.\nAt \nC.\nBy \nD.\nTo\n(Enter A,B,C or D in caps)\n')
                if q25=='C':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q25=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question6
            q26=input('He is afflicted ________ a serious illness. \nA.\nWith \nB.\nTo \nC.\nBy \nD.\nof\n(Enter A,B,C or D)\n')
            if q26=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q26=='hint':
                print('It has 4 letters\n')
                q26=input('He is afflicted ________ a serious illness. \nA.\nWith \nB.\nTo \nC.\nBy \nD.\nof\n(Enter A,B,C or D)\n')
                if q26=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q26=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question7
            q27=input('She does not agree _________ me \nA.\nUpon \nB.\nTo \nC.\nWith\nD.\nNone of these\n(Enter A,B,C or D)\n')
            if q27=='C':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q27=='hint':
                print('It has 4 letters\n')
                q27=input('She does not agree _________ me \nA.\nUpon \nB.\nTo \nC.\nWith\nD.\nNone of these\n(Enter A,B,C or D)\n')
                if q27=='C':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q27=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question8
            q28=input('You must apologize ________. him for your rude behaviour. \nA.\nTo \nB.\nBy \nC.\nWith\nD.\nFor\n(Enter A,B,C or D)\n')
            if q28=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q28=='hint':
                print('It has 2 letters\n')
                q28=input('You must apologize ________. him for your rude behaviour. \nA.\nTo \nB.\nBy \nC.\nWith\nD.\nFor\n(Enter A,B,C or D)\n')
                if q28=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q28=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question9
            q29=input('The roman numeral for 18 is ______.\n')
            if q29=='XVIII':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q29=='hint':
                print('Three Is\n')
                q29=input('The roman numeral for 18 is ______.\n')
                if q29=='XVIII':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q29=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question10
            q210=input('The smallest 4-digit number formed by using the digits 0, 3, 5, 6 is _____.\n')
            if q210=='0356':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q210=='hint':
                print('Reverse the order of 6530\n')
                q210=input('The smallest 4-digit number formed by using the digits 0, 3, 5, 6 is _____.\n')
                if q210=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q210=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question11
            q211=input('The predecessor of the smallest 5-digit number is ____.\n')
            if q211=='9999':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q211=='hint':
                print('After 9998\n')
                q211=input('The predecessor of the smallest 5-digit number is ____.\n')
                if q211=='9999':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q211=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question12
            q212=input('The smallest single digit composite number is ____.\n')
            if q212=='4':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q212=='hint':
                print('2 times 2\n')
                q212=input('The smallest single digit composite number is ____.\n')
                if q212=='4':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q212=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question13
            q213=input('Ram had 342 coins in his collection. How would you write 342?\n')
            if q213=='Three hundred forty two':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q213=='hint':
                print('How do you say 342?\n')
                q213=input('Ram had 342 coins in his collection. How would you write 342?\n')
                if q213=='Three hundred forty two':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q213=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question14
            q214=input('Which number comes next in the series? 4231, 4331, 4431, ?\n')
            if q214=='4531':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q214=='hint':
                print('+100\n')
                q214=input('Which number comes next in the series? 4231, 4331, 4431, ?\n')
                if q214=='4531':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q214=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl2Question15
            q215=input('Rita had $150. She wanted to buy a doll that costs $230. How much more money does she need to buy the doll?\n')
            if q215=='$80':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


            elif q215=='hint':
                print('230-150\n')
                q215=input('Rita had $150. She wanted to buy a doll that costs $230. How much more money does she need to buy the doll?\n')
                if q215=='$80':
                    print('That is the correct answer\n')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
                else:
                    print('Too bad, that is the incorrect answer.\n')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            elif q215=='skip':
                print('Dodged!\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            else:
                print('Too bad, that is the incorrect answer.\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')


        ###THIS IS LEVEL 3###
        else:
            print('You have chosen level 3\n')

            #lvl3Question1
            q31=input('A large box contains 18 small boxes and each small box contains 25 chocolate bars.\n How many chocolate bars are in the large box?\n')
            if q31=='450':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q31=='hint':
                print('Multiplication\n')
                q31=input('A large box contains 18 small boxes and each small box contains 25 chocolate bars.\n How many chocolate bars are in the large box?\n')
                if q31=='450':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q31=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question2
            q32=input('Today I was late for school.\n But since it had happened for the first time, the teacher did not punish me.\n Which word can replace <<did not punish>> in the sentence given above?\n A. Excused \nB. Explained \n C. Examined \n D. Expected \n')
            if q32=='A':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q32=='hint':
                print('Ends with an <<e>>\n')
                q32=input('Today I was late for school.\n But since it had happened for the first time, the teacher did not punish me.\n Which word can replace <<did not punish>> in the sentence given above?\n A. Excused \nB. Explained \n C. Examined \n D. Expected \n')
                if q32=='A':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q32=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

             #lvl3Question3
            q33=input('It takes John 25 minutes to walk to the car park and 45 minutes to drive to work. \n At what time should he get out of the house in order to get to work at 9:00 a.m.?\n')
            if q33=='7:50am':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q33=='hint':
                print('Subtraction\n')
                q33=input('It takes John 25 minutes to walk to the car park and 45 minutes to drive to work. \n At what time should he get out of the house in order to get to work at 9:00 a.m.?\n')
                if q33=='7:50am':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q33=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question4
            q34=input('Shahrukh Khan is a <<famous>> actor today.But when he came to Mumbai several years ago, he was almost _____________.\nWhich word is OPPOSITE in meaning to "famous" and can be used to complete the sentence given above?\nA. Poor\nB. Unknown\nC. Familiar\nD. Worthless\n')
            if q34=='B':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q34=='hint':
                print('Starts with ‘U’\n')
                q34=input('Shahrukh Khan is a <<famous>> actor today.But when he came to Mumbai several years ago, he was almost _____________.\nWhich word is OPPOSITE in meaning to "famous" and can be used to complete the sentence given above?\nA. Poor\nB. Unknown\nC. Familiar\nD. Worthless\n')
                if q34=='B':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q34=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question5
            q35=input('Kim can walk 4 kilometers in one hour.\nHow long does it take Kim to walk 18 kilometers?\n')
            if q35=='4 hours and 30 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q33=='hint':
                print('4 x 4 = 16 km\n')
                q35=input('Kim can walk 4 kilometers in one hour.\nHow long does it take Kim to walk 18 kilometers?\n')
                if q35=='4 hours and 30 minutes':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q35=='skip':
                 print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question6
            q6=input('The car in front of our scooter stopped "abruptly".\nSince we were not prepared for that, we banged hard into it!the word "abruptly" as used in the sentence above, means__________\nDiscuss\nA. Slowly, without hurry\nB. Suddenly, without warning\nC. Loudly, with a hard bang\nD. Quietly, in an unusual manner\n ')
            if q6=='b':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q6=='hint':
                print('D is not the answer')
                q6=input('The car in front of our scooter stopped "abruptly".\nSince we were not prepared for that, we banged hard into it!the word "abruptly" as used in the sentence above, means__________\nDiscuss\nA. Slowly, without hurry\nB. Suddenly, without warning\nC. Loudly, with a hard bang\nD. Quietly, in an unusual manner\n \n')
                if q6=='b':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q6=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #lvl3Question7
            q7=input('Linda bought 3 notebooks at $1.20 each; a box of pencils at $1.50 and a box of pens at $1.70.\n How much did Linda spend?\n')
            if q7=='$6.80':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q7=='hint':
                print('Addition\n')
                q7=input('Linda bought 3 notebooks at $1.20 each; a box of pencils at $1.50 and a box of pens at $1.70.\n How much did Linda spend?\n')
                if q7=='$6.80':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.\n')
            elif q7=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.\n')

            #Question8
            q8=input('Which option punctuates the sentence given below CORRECTLY?\nNisha said to me do you want me to drop you home.\nA. Nisha said to me,"do you want me to drop you home."\nB. Nisha said to me,"Do you want me to drop you home?"\nC. Nisha said to me"do you want me to drop you home?"\nD. Nisha said to me"Do you want me to drop you home."\n ')
            if q8=='b':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q8=='hint':
                print('D is not the answer\n')
                q8=input('Which option punctuates the sentence given below CORRECTLY?\nNisha said to me do you want me to drop you home.\nA. Nisha said to me,"do you want me to drop you home."\nB. Nisha said to me,"Do you want me to drop you home?"\nC. Nisha said to me"do you want me to drop you home?"\nD. Nisha said to me"Do you want me to drop you home."\n ')
                if q8=='b':
                    print('That is the correct answer\n')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q8=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question9
            q9=input('Tom and Bob have a total of 49 toys.\nIf Bob has 5 more toys than Tom, how many toys does each one have?\n')
            if q9=='22,27':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q9=='hint':
                print('Tom’s is an even number. Bob’s is an odd number.')
                q9=input('Tom and Bob have a total of 49 toys.\nIf Bob has 5 more toys than Tom, how many toys does each one have?\n')
                if q9=='22,27':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q9=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question10
            q10=input('Identify the sentence with a SPELLING MISTAKE\nA. It is neccessary to drink enough water daily.\nB. Having a balanced diet is extremely important.\nC. Spinach is plentiful in Minerals like Iron and Calcium.\nD. Tomatoes and Lemons are good sources of Vitamin C\n')
            if q10=='a':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q10=='hint':
                print('D is not the answer\n')
                q10=input('Identify the sentence with a SPELLING MISTAKE\nA. It is neccessary to drink enough water daily.\nB. Having a balanced diet is extremely important.\nC. Spinach is plentiful in Minerals like Iron and Calcium.\nD. Tomatoes and Lemons are good sources of Vitamin C\n')
                if q10=='a':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q10=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question11
            q11=input('John can eat a quarter of a pizza in one minute.\nHow long does it take John to eat one pizza and a half?\n')
            if q11=='6 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q11=='hint':
                print('Multiplication\n')
                q11=input('John can eat a quarter of a pizza in one minute. How long does it take John to eat one pizza and a half?')
                if q11=='6 minutes':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q11=='skip':
                print('Dodged\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question12
            q12=input('Identify the option with CORRECT spelling to complete the sentence given below.\n The_________________took his sheep and goats to graze on the mountains.\nA. Shepard\nB. Shepherd\nC. Shepperd\nD. Sheepherd\n')
            if q12=='b':
                print('That is the correct answer')
            elif q12=='hint':
                print('D is not the answer')
                q12=input('Identify the option with CORRECT spelling to complete the sentence given below.\n The_________________took his sheep and goats to graze on the mountains.\nA. Shepard\nB. Shepherd\nC. Shepperd\nD. Sheepherd\n')
                if q12=='b':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q12=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #lvl3Question13
            q13=input('John read the quarter of the time that Tom read.\nTom read only two-fifth of the time that Sasha read.\nSasha read twice as long as Mike.\nIf Mike read 5 hours, how long did John read?\n')
            if q13=='1 hour':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q13=='hint':
                print('John reads ⅕ of what Mike reads.')
                q13=input('John read the quarter of the time that Tom read.\nTom read only two-fifth of the time that Sasha read.\nSasha read twice as long as Mike.\nIf Mike read 5 hours, how long did John read?\n')
                if q13=='1 hour':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q13=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

            #Question14
            q14=input('Which sentence has a GRAMMAR mistake?\nA. My mother told me to put the book back in it is place.\nB. Tennis has lost its charm for me since Steffi Graf retired.\nC. My neighbours dog tries to catch its own tail all day long.\nD. It is sunday tomorrow so I will watch my favourite cartoons.\n')
            if q14=='a':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
            elif q14=='hint':
                print('D is not the answer')
                q14=input('Which sentence has a GRAMMAR mistake?\nA. My mother told me to put the book back in it is place.\nB. Tennis has lost its charm for me since Steffi Graf retired.\nC. My neighbours dog tries to catch its own tail all day long.\nD. It is sunday tomorrow so I will watch my favourite cartoons.\n')
                if q14=='a':
                    print('That is the correct answer')
                else:
                    print('Too bad, that is the incorrect answer.')
            elif q14=='skip':
                print('Dodged!\n')
            else:
                print('Too bad, that is the incorrect answer.')

             #Question15
            q15=input('How many minutes are in one week?')
            if q15=='10,080 minutes':
                points = points + 1
                print('That is the correct answer\n')
                print ('This is your score so far',points,'. Keep it going!')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                #ending1
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                
            elif q15=='hint':
                print('Multiplication')
                q15=input('How many minutes are in one week?')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')
                if q15=='10,080 minutes':
                    print('That is the correct answer')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                    #ending2
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')

                else:
                    print('Too bad, that is the incorrect answer.')
                    print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                                #ending3
                    print('Congradulations for finishing the game!\n')
                    time.sleep(2)
                    print('As a reward for finishing the game we shall generate a fortune for you!\n')
                    time.sleep(2)
                    print('I wonder what your fortune will be...o(≧∇≦o)\n')
                    time.sleep(4)
                    fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                    "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                    print (random.choice(fortune))
                    time.sleep(4)
                    print('\n')
                    print('Interesting.......hmmmm（￣ﾍ￣）\n')
                    time.sleep(2)
                    print('It is up to you to follow it or not (＾▽＾)\n')
                    time.sleep(2)
                    print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                    
            elif q15=='skip':
                print('Dodged!\n')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                            #ending4
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
            else:
                print('Too bad, that is the incorrect answer.')
                print ('You have',points,'points! Congratulations, you have finished answering 15 questions.')

                            #ending5
                print('Congradulations for finishing the game!\n')
                time.sleep(2)
                print('As a reward for finishing the game we shall generate a fortune for you!\n')
                time.sleep(2)
                print('I wonder what your fortune will be...o(≧∇≦o)\n')
                time.sleep(4)
                fortune=["A beautiful, smart, and loving person will be coming into your life.", "A dubious friend may be an enemy in camouflage.", "A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A pleasant surprise is waiting for you.","A soft voice may be awfully persuasive.","Be careful or you could fall for some tricks today.","Change is happening in your life, so go with the flow!","Don’t just think, act!","Education is the ability to meet life’s situations.","Every wise man started out by asking many questions.","Failure is the chance to do better next time.","Feeding a cow with roses does not get extra appreciation.","Go take a rest; you deserve it.","If you look in the right places, you can find some good offerings.","In order to take, one must first give.",
                "It’s time to get moving. Your spirits will lift accordingly.","One of the first things you should look for in a problem is its positive side."]
                print (random.choice(fortune))
                time.sleep(4)
                print('\n')
                print('Interesting.......hmmmm（￣ﾍ￣）\n')
                time.sleep(2)
                print('It is up to you to follow it or not (＾▽＾)\n')
                time.sleep(2)
                print('OK that is all for today! BYEEEEEE (〃･ω･)ﾉ~☆･ﾟ+｡*ﾟ･.+')
                
    ###################################################
    ####

else:
    print ('Sorry, you cannot play the game.')
###END OF TEST IF HUMAN##USED SETS##
    


###############################################
