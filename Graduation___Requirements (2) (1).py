#Comments
#Arianne Rull
#ICS201
#April 11, 2019
#Graduation Requirements

#Write a program to ask students if they are ready to graduate. The program must ask question and help the students to take the next step required for graduation. 


#The following are the guide line:
 
#a)	Enter comments for name and program information as it’s been instructed 
#b)	Comment to explain the code and algorithm 
#c)	Prompt the user for their full name (first and last name).
#d)	Prompt the user with greeting followed with their full name. 
#e)	Ask the user to enter number of credit requires for graduation
#f)	Elective courses
#g)	Compulsory courses
#h)	Specific subject required for graduation
#i)	Language test requirement
#j)	40 hours community service

#Note: The program must loop for 3 times to accommodate other users.
#You should congratulate those who are ready to graduate, and your program should be user friendly. 
#Total mark 20

count = 0
while count <3:

    print ('Graduation Requirements')

#c)	Prompt the user for their full name (first and last name).
    print ('Full Name')
    firstNameS=input ('Please enter your first name')
    lastNameS=input ('Please enter your last name')

#d)	Prompt the user with greeting followed with their full name.
    print ('Greetings')
    print ('Bonjour', firstNameS, lastNameS, '!' )
    print ('This program is used to see if you are eligible to graduate.')

#
#print('HIIII')
#age = input ('How old are you?')
#age = int (age)
#if (age>16 and age<85) :
    #print ('You can apply for driving license.')
    #print ('Have you passed the test? If yes, press 1 ')
    #passTest=input()
    #passTest=int(passTest)
    #if passTest==1:
        #print ('You can go for driving lessons')

#e)	Ask the user to enter number of credit requires for graduation
    print ('How many required credits are there to be eligible for graduation?')
    numOfCredits=input()
    numOfCredits=int(numOfCredits)
    if numOfCredits==30:
        print ('That is the correct number of required credits.')
        print ('A student needs at least 30 credits to claim the OSSD.')
        
#f)	Elective courses

    #12 Elective Credits
    print('How many elective credits have you obtained?')
    electiveCreditsx=input()
    electiveCreditsx=int(electiveCreditsx)
    if electiveCreditsx==12:
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif electiveCreditsx>12:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement to graduate.')
        
#g)	Compulsory courses

            #4 credits in English (1 credit per grade)
            #1 credit in French as a second language
            #3 credits in mathematics (at least 1 credit in grade 11 or 12)
            #2 credits in science
            #1 credit in Canadian history
            #1 credit in Canadian geography
            #1 credit in the arts
            #1 credit in health and physical education
            #0.5 credits in civics
            #0.5 credits in career studies

    #4 credits in English (1 credit per grade)
    print ('How many English credits have you received?')
    englishCredits=input()
    englishCredits=int(englishCredits)
    if englishCredits==4:
        print ('You can proceed to the second question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif englishCredits>4:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #3 credits in Mathematics
    print ('How many Mathematics credits have you received?')
    mathematicsCredits=input()
    mathematicsCredits=int(mathematicsCredits)
    if mathematicsCredits==3:
        print ('You can proceed to the third question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif mathematicsCredits>3:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #2 credits in Science
    print ('How many Science credits have you received?')
    scienceCredits=input()
    scienceCredits=int(scienceCredits)
    if scienceCredits==3:
        print ('You can proceed to the fourth question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif scienceCredits>3:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #1 credit in French
    print ('How many French credits have you received?')
    frenchCredit=input()
    frenchCredit=int(frenchCredit)
    if frenchCredit==1:
        print ('You can proceed to the fifth question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif frenchCredit>1:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #1 credit in Canadian History
    print ('How many Canadian History credits have you received?')
    canadianHistoryCredit=input()
    canadianHistoryCredit=int(canadianHistoryCredit)
    if canadianHistoryCredit==1:
        print ('You can proceed to the sixth question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif canadianHistoryCredit>1:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #1 credit in Canadian Geography
    print ('How many Canadian Geography credits have you received?')
    canadianGeographyCredit=input()
    canadianGeographyCredit=int(canadianGeographyCredit)
    if canadianHistoryCredit==1:
        print ('You can proceed to the seventh question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif canadianGeographyCredit>1:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #1 credit in Art
    print ('How many Art credits have you received?')
    artCredit=input()
    artCredit=int(artCredit)
    if artCredit==1:
        print ('You can proceed to the eighth question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif artCredit>1:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #1 credit in Physical Education
    print ('How many P.E. credits have you received?')
    peCredit=input()
    peCredit=int(peCredit)
    if peCredit==1:
        print ('You can proceed to the ninth question.')
        print ('You are eligible to graduate. You can proceed to the next question.')
    elif peCredit>1:
        print ('You are eligible to graduate. You can proceed to the next question.')
    else:
        print ('You are missing a requirement.')

    #1 credit in Civics and Careers
    civcarCredit=input('Have you received your Civics and Careers?')
    if civcarCredit=='yes':
        print ('You can proceed to the tenth question.')
    else:
        print ('You are missing a requirement to graduate.')

    #Group1
    group1Credit=input('Have you received a credit in Group 1?')
    if group1Credit=='yes':
        print ('You can proceed to the next question.')
    else:
        print ('You are missing a requirement to graduate.')
        
    #Group2
    group2Credit=input('Have you received a credit in Group 2?')
    if group2Credit=='yes':
        print ('You can proceed to the next question.')
    else:
        print ('You are missing a requirement to graduate.')
        
    #Group3
    group3Credit=input('Have you received a credit in Group 3?')
    if group3Credit=='yes':
        print ('You can proceed to the next question.')
    else:
        print ('You are missing a requirement to graduate.')
        
#h)	Specific subject required for graduation
        
#i)	Language test requirement
    osslt=input('Did you pass the OSSLT?')
    if osslt=='yes':
        print ('You can proceed to the next question.')
    else:
        print ('You are missing a requirement to graduate.')
        
        
#j)	40 hours community service
    communityservicehours=input('Did you accumulate 40 community service hours or more?')
    if communityservicehours=='yes':
        print ('You can proceed to the next question.')
    else:
        print ('You are missing a requirement to graduate.')

#Closing Statements
    count==count+1
    print ('You are the applicant number ',count)
    print ('Congratulations', firstNameS, lastNameS, ',if you have met all the graduation requirements.')
    print ('THE END OF THE PROGRAM.')

#LOOPS
    count = count + 1


