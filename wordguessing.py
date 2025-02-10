#CREATING THE WORD GUESSING GAME........

def welcome():
    name=input("enter ur name:.......")
    print("we hope u are ready.....")
    yes='Y'
    no='N'
    print("PRESS Y FOR YES AND N FOR NO......")
    answer=input("enter your response......")#ANSWER FOR YES OR NO
    if(answer=='N'):
        print("exiting............")
    elif(answer=='Y'):
        print("WE ARE STARTING THE GAME IN FEW CLICKS.......")
    else:
        print("PLEASE RESTART AND SELECT THE CORRECT KEYS")

#FUNCTION CALLING:.........
