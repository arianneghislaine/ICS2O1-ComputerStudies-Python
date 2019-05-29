#Memory tiles

#import
import random
import time
score = 0

#prints the instructions
print ('This is the memory tile game.\n The goal is to match two pairs from the tile of the same letter.\n The asterisks represent the place of the tile.\n The rows are the x-coordinates, while the columns are the y-coordinates.\n Type (x,y) coordinates of the tiles to match them with another pair.\n')
time.sleep(2)

#Variables with their pairs
answer = list('AABBCCDDEEFFGGHH')
#Shuffles and randomizes the variables
random.shuffle(answer)
answer = [answer[:4],
         answer[4:8],
         answer[8:12],
         answer[12::]]

#four rows of asterisks
board = [list('*'*4)for i in range(4)]

#function to choose
#Allows the player to choose
def choose():
    a,b = map (int, input('? '))
    show_board((a,b))
    x,y = map (int, input('? '))
    
    #Shows the board with the pattern
    show_board ((a,b),(x,y))
    time.sleep(2)#2-second delay
    
    #Waits for two seconds to figure out, if it is a match or not
    if answer[a][b] == answer[x][y]:
        #correct pattern - result
        tscore = score + 1
        print('Great Job! It is a match!')
        print('You have', tscore ,'point/s')
        board[a][b] = answer[a][b]
        board[x][y] = answer[x][y]
        
    else:
        #incorrect pattern - result
        print('Sorry, not a match.')
        
    #figures out if there are any asterisks in any row
    if any('*' in row for row in board):
        #keeps going, even if there are no matches
        return True

#Function to choose the necessary tiles
def show_board(*tiles):
    for row in range(len(answer[0])):
        for column in range(len(answer[0])):
            if (row, column) in tiles:
                print(answer[row][column].lower(), end='', flush=True)
            else:
                print(board[row][column], end='', flush=True)
        print()
            
#Starts by showing the board
show_board()

#defines t
#uses monotonic method of counting the time
t = time.monotonic()

while choose():
    pass

#prints the time
print('Completed!\n Time:', time.monotonic()-t)

