#Comparison Operators >,<,>=,<=,==,!=
#ICS2O1 - Mr. Kordbacheh
#April 10, 2019
#Arianne Ghislaine Rull

count = 0
while count <3:

    age = input ('How old are you?')
    age = int (age)
    if (age>16 and age<85) :
        print ('You can apply for driving license.')
        print ('Have you passed the test? If yes, press 1 ')
        passTest=input()
        passTest=int(passTest)
        if passTest==1:
            print ('You can go for driving lessons')
    elif age<16:
        print ('You have not reached the age limit.')
        print ('You are not old enough, come back after ',16-count,'year/s')
        print ('This is the end of the program.')
    elif age>85:
        print ('You cannot drive anymore, since you passed the age limit.')
        medicalTest=input ('If you like to drive you have to take the medical test. If you have taken it already, type YES')
        if medicalTest=='YES':
            print('You can drive for an extra year.')
    else:
        print ('You cannot apply to get your driving license.')
        print ('You cannot drive anymore')
        print ('This is the end of the program.')
    count==count+1
    print ('You are the applicant number ',count)
    print ('THE END OF THE PROGRAM.')
   
