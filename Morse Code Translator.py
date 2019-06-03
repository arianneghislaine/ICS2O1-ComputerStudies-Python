#Morse Code Translator

#Greeting
print('This is a Morse Code Translator.')
#Gets the input
choice = input('Press 1 to convert word text to morse code.\n Press 2 to convert morse code to word text.\n')

if choice=="1":#if the input is 1
    #define to_morse_code
    def to_morse_code(text):
        #translation of word characters
        code = {'a':'.-', 'b':'-...', 
                'c':'-.-.', 'd':'-..', 'e':'.', 
                'f':'..-.','g':'--.', 'h':'....', 
                'i':'..', 'j':'.---', 'k':'-.-', 
                'l':'.-..', 'm':'--', 'n':'-.', 
                'o':'---', 'p':'.--.', 'q':'--.-', 
                'r':'.-.', 's':'...', 't':'-', 
                'u':'..-', 'v':'...-', 'w':'.--', 
                'x':'-..-', 'y':'-.--', 'z':'--..', 
                '1':'.----', '2':'..---', '3':'...--', 
                '4':'....-', '5':'.....', '6':'-....', 
                '7':'--...', '8':'---..', '9':'----.', 
                '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                '?':'..--..', '/':'-..-.', '-':'-....-', 
                '(':'-.--.', ')':'-.--.-', ' ':' '}
        morse_code =""
        
        #translates each character into morse_code
        for x in text:
            morse_code += code[x.lower()]
        #return command does not print the value
        return morse_code
    
    #Program asks for the user's input to be converted
    text = input("Enter NORMAL TEXT to convert to MORSE CODE: ")
    #Prints the output()
    print(to_morse_code(text))
    print('Thank you for using the program!')

if choice=="2":#if the input is 2
    #define to_normal_text
    def to_normal_text(text):
        #translation of word characters
        alphabet = {'.-':'a', '-...':'b', 
                '-.-.':'c', '-..':'d', '.':'e',
                '..-.':'f', '--.':'g', '....':'h',
                '..':'i', '.---':'j', '-.-':'k',
                '.-..':'l', '--':'m', '-.':'n',
                '---':'o', '.--.':'p', '--.-':'q',
                '.-.':'r', '...':'s', '-':'t',
                '..-':'u', '...-':'v', '.--':'w',
                '-..-':'x', '-.--':'y', '--..':'z',
                '.----':'1', '..---':'2', '...--':'3',
                '....-':'4', '.....':'5', '-....':'6',
                '--...':'7', '---..':'8', '----.':'9',
                '-----':'0', '--..--':', ', '.-.-.-':'.',
                '..--..':'?', '-..-.':'/', '-....-':'-',
                '-.--.':'(', '-.--.-':')', ' ':' '}
        to_normal_text=""
        
        #translates each character into morse_code
        for x in text:
            to_normal_text += alphabet[x.lower()]
                    
        return to_normal_text
    
    #Program asks for the user's input to be converted
    text = input("Enter MORSE CODE to convert to NORMAL TEXT: ")
    #Prints the output()
    print(to_normal_text(text))   
    print('Thank you for using the program!')

