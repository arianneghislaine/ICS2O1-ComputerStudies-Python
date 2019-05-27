#HST Calculator

import time

print ('CANADIAN HST CALCULATOR')
time.sleep(1)
print ('HST is the Harmonized Sales Tax that is charged on specific items to support the federal and provincial government.\n')
time.sleep(1)

#OPTIONS for PROVINCES
provinces=input("What province are you located in?\n Press the numbers\n 1: New Brunswick\n 2: Newfoundland and Labrador \n 3: Nova Scotia\n 4: Ontario\n 5:Prince Edward Island\n ")
if provinces=='1':
    print("You have chosen that you are located in New Brunswick")
    
    #the command offers the options #Get the input from the user
    options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
    if options=='1':
        #1: price excluding HST
        print("You have chosen to calculate the price excluding HST ")
        print("FORMULA:\n p_w_hst - HST = price excluding HST ")
        #Get input from the user
        p_w_hst=input("Enter the price with the HST ")
        #Convert the string input to float
        p_w_hst=float(p_w_hst)
        #Get input from the user
        hst=input("Enter the HST ")
        #Convert the string input to float
        hst=float(hst)
        #Shows the input from the user
        print('Price with HST is:',p_w_hst,', HST is:',hst)
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        price_excluding_hst=(p_w_hst - hst)
        #Print the output
        print('The price excluding HST is', price_excluding_hst)
        
    if options=='2':
        #2: HST only
        print("You have chosen to calculate HST only")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
        #Get input from the user
        p_no_hst = input("Enter the price without HST ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst=(p_no_hst * 0.15)
        #Print the output
        print('The HST is', hst)
        
    if options=='3':
        #3: Federal part
        print("You have chosen to calculate the federal part")
        print("FORMULA:\n HST * federal part (5%/0.05)")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the federal part is 5% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        federal=(hst * 0.05)
        #Print the output
        print('The federal part is', federal)
        
    if options=='4':
        #4: Provincial part
        print("You have chosen to calculate the provincial part")
        print("FORMULA:\n HST * provincial part")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the provincial part is 10% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        provincial=(hst * 0.1)
        #Print the output
        print('The provincial part is', provincial)
        
    if options=='5':
        #5: Price with HST
        print("You have chosen to calculate the price including HST")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
        #Get input from the user
        p_no_hst = input ("Enter the price without HST  ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print("The price without HST is", p_no_hst,", the HST is 15%")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst = (p_no_hst * 0.15)
        p_w_hst = (hst + p_no_hst)
        #Print the output
        print('The price with HST is', p_w_hst)

if provinces=='2':
    print("You have chosen that you are located in Newfoundland and Labrador")
    
    #the command offers the options #Get the input from the user
    options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
    if options=='1':
        #1: price excluding HST
        print("You have chosen to calculate the price excluding HST ")
        print("FORMULA:\n p_w_hst - HST = price excluding HST ")
        #Get input from the user
        p_w_hst=input("Enter the price with the HST ")
        #Convert the string input to float
        p_w_hst=float(p_w_hst)
        #Get input from the user
        hst=input("Enter the HST ")
        #Convert the string input to float
        hst=float(hst)
        #Shows the input from the user
        print('Price with HST is:',p_w_hst,', HST is:',hst)
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        price_excluding_hst=(p_w_hst - hst)
        #Print the output
        print('The price excluding HST is', price_excluding_hst)
        
    if options=='2':
        #2: HST only
        print("You have chosen to calculate HST only")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
        #Get input from the user
        p_no_hst = input("Enter the price without HST ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst=(p_no_hst * 0.15)
        #Print the output
        print('The HST is', hst)
        
    if options=='3':
        #3: Federal part
        print("You have chosen to calculate the federal part")
        print("FORMULA:\n HST * federal part (5%/0.05)")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the federal part is 5% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        federal=(hst * 0.05)
        #Print the output
        print('The federal part is', federal)
        
    if options=='4':
        #4: Provincial part
        print("You have chosen to calculate the provincial part")
        print("FORMULA:\n HST * provincial part")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the provincial part is 10% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        provincial=(hst * 0.1)
        #Print the output
        print('The provincial part is', provincial)
        
    if options=='5':
        #5: Price with HST
        print("You have chosen to calculate the price including HST")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
        #Get input from the user
        p_no_hst = input ("Enter the price without HST  ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print("The price without HST is", p_no_hst,", the HST is 15%")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst = (p_no_hst * 0.15)
        p_w_hst = (hst + p_no_hst)
        #Print the output
        print('The price with HST is', p_w_hst)
        
if provinces=='3':
    print("You have chosen that you are located in Nova Scotia")

    #the command offers the options #Get the input from the user
    options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
    if options=='1':
        #1: price excluding HST
        print("You have chosen to calculate the price excluding HST ")
        print("FORMULA:\n p_w_hst - HST = price excluding HST ")
        #Get input from the user
        p_w_hst=input("Enter the price with the HST ")
        #Convert the string input to float
        p_w_hst=float(p_w_hst)
        #Get input from the user
        hst=input("Enter the HST ")
        #Convert the string input to float
        hst=float(hst)
        #Shows the input from the user
        print('Price with HST is:',p_w_hst,', HST is:',hst)
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        price_excluding_hst=(p_w_hst - hst)
        #Print the output
        print('The price excluding HST is', price_excluding_hst)
        
    if options=='2':
        #2: HST only
        print("You have chosen to calculate HST only")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
        #Get input from the user
        p_no_hst = input("Enter the price without HST ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst=(p_no_hst * 0.15)
        #Print the output
        print('The HST is', hst)
        
    if options=='3':
        #3: Federal part
        print("You have chosen to calculate the federal part")
        print("FORMULA:\n HST * federal part (5%/0.05)")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the federal part is 5% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        federal=(hst * 0.05)
        #Print the output
        print('The federal part is', federal)
        
    if options=='4':
        #4: Provincial part
        print("You have chosen to calculate the provincial part")
        print("FORMULA:\n HST * provincial part")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the provincial part is 10% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        provincial=(hst * 0.1)
        #Print the output
        print('The provincial part is', provincial)
        
    if options=='5':
        #5: Price with HST
        print("You have chosen to calculate the price including HST")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
        #Get input from the user
        p_no_hst = input ("Enter the price without HST  ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print("The price without HST is", p_no_hst,", the HST is 15%")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst = (p_no_hst * 0.15)
        p_w_hst = (hst + p_no_hst)
        #Print the output
        print('The price with HST is', p_w_hst)
        
if provinces=='4':
    print("You have chosen that you are located in Ontario")

    #the command offers the options #Get the input from the user
    options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
    if options=='1':
        #1: price excluding HST
        print("You have chosen to calculate the price excluding HST ")
        print("FORMULA:\n p_w_hst - HST = price excluding HST ")
        #Get input from the user
        p_w_hst=input("Enter the price with the HST ")
        #Convert the string input to float
        p_w_hst=float(p_w_hst)
        #Get input from the user
        hst=input("Enter the HST ")
        #Convert the string input to float
        hst=float(hst)
        #Shows the input from the user
        print('Price with HST is:',p_w_hst,', HST is:',hst)
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        price_excluding_hst=(p_w_hst - hst)
        #Print the output
        print('The price excluding HST is', price_excluding_hst)
        
    if options=='2':
        #2: HST only
        print("You have chosen to calculate HST only")
        print("FORMULA:\n p_no_hst * 13% or 0.13 = HST")
        #Get input from the user
        p_no_hst = input("Enter the price without HST ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst=(p_no_hst * 0.13)
        #Print the output
        print('The HST is', hst)
        
    if options=='3':
        #3: Federal part
        print("You have chosen to calculate the federal part")
        print("FORMULA:\n HST * federal part (5%/0.05)")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the federal part is 5% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        federal=(hst * 0.05)
        #Print the output
        print('The federal part is', federal)
        
    if options=='4':
        #4: Provincial part
        print("You have chosen to calculate the provincial part")
        print("FORMULA:\n HST * provincial part")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the provincial part is 8% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        provincial=(hst * 0.08)
        #Print the output
        print('The provincial part is', provincial)
        
    if options=='5':
        #5: Price with HST
        print("You have chosen to calculate the price including HST")
        print("FORMULA:\n p_no_hst * 13% or 0.13 = HST\n HST + p_no_hst = price with HST")
        #Get input from the user
        p_no_hst = input ("Enter the price without HST  ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print("The price without HST is", p_no_hst,", the HST is 15%")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst = (p_no_hst * 0.13)
        p_w_hst = (hst + p_no_hst)
        #Print the output
        print('The price with HST is', p_w_hst)
        
if provinces=='5':
    print("You have chosen that you are located in Prince Edward Island")
    #the command offers the options #Get the input from the user
    options=input("What would you like to calculate?\n Press the numbers\n 1: price excluding HST\n 2: HST only\n 3: Federal part\n 4: Provincial part\n 5: price including HST\n")
    if options=='1':
        #1: price excluding HST
        print("You have chosen to calculate the price excluding HST ")
        print("FORMULA:\n p_w_hst - HST = price excluding HST ")
        #Get input from the user
        p_w_hst=input("Enter the price with the HST ")
        #Convert the string input to float
        p_w_hst=float(p_w_hst)
        #Get input from the user
        hst=input("Enter the HST ")
        #Convert the string input to float
        hst=float(hst)
        #Shows the input from the user
        print('Price with HST is:',p_w_hst,', HST is:',hst)
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        price_excluding_hst=(p_w_hst - hst)
        #Print the output
        print('The price excluding HST is', price_excluding_hst)
        
    if options=='2':
        #2: HST only
        print("You have chosen to calculate HST only")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST")
        #Get input from the user
        p_no_hst = input("Enter the price without HST ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print('The price without HST is', p_no_hst,', the percentage of HST is 15%')
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst=(p_no_hst * 0.15)
        #Print the output
        print('The HST is', hst)
        
    if options=='3':
        #3: Federal part
        print("You have chosen to calculate the federal part")
        print("FORMULA:\n HST * federal part (5%/0.05)")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the federal part is 5% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        federal=(hst * 0.05)
        #Print the output
        print('The federal part is', federal)
        
    if options=='4':
        #4: Provincial part
        print("You have chosen to calculate the provincial part")
        print("FORMULA:\n HST * provincial part")
        #Get input from the user
        hst = input ("Enter the HST ")
        #Convert the string input to float
        hst = float (hst)
        #Shows the input from the user
        print("The HST is",hst,", the provincial part is 10% of HST")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        provincial=(hst * 0.1)
        #Print the output
        print('The provincial part is', provincial)
        
    if options=='5':
        #5: Price with HST
        print("You have chosen to calculate the price including HST")
        print("FORMULA:\n p_no_hst * 15% or 0.15 = HST\n HST + p_no_hst = price with HST")
        #Get input from the user
        p_no_hst = input ("Enter the price without HST  ")
        #Convert the string input to float
        p_no_hst = float (p_no_hst)
        #Shows the input from the user
        print("The price without HST is", p_no_hst,", the HST is 15%")
        print("Loading.....")
        #Buffer time
        time.sleep(5)
        #Use the algorithm to calculate
        hst = (p_no_hst * 0.15)
        p_w_hst = (hst + p_no_hst)
        #Print the output
        print('The price with HST is', p_w_hst)
