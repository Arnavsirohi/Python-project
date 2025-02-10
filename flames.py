#INTRODUCTION TO FLAMES AND WELCOME THE USER AND TAKE THEIR OUTPUT....

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

#DEFINING THE NAME OF THE FLAMES OF THE USER BY SEPREATE VARIABLE......

def flame_name():
     global name1
     global name2
     name1=input("enter first name of flames:.....")
     name2=input("enter second name of flames......")
   

#COMMON LETTER FOR FLAMES

def common_letter():
    global common_char1
    set1=set(name1)
    set2=set(name2)
    common_char=set1.intersection(set2)
    if common_char:
        common_char1=''.join(common_char)
        print("WE FOUND THE COMMON CHARACTER......",common_char1)
    else:
        print("NO COMMON FOUND IN THE LETTER")


#COUNT THE LETTER IN THE COMMON CHARACTER........



def count():
    global remaining_count
    remaining_count = len(name1) + len(name2)  # Calculate total remaining characters
    print(f"Total remaining characters: {remaining_count}")


#NOW THE CIRCULAR ROTATION ON FLAMES:..........
def logic():
    flames=['F','L','A','M','E','S']
    index=0
    while len(flames)>1:
        index=(index+remaining_count-1)%len(flames)
        flames.pop(index)
    return flames[0]

#NOW TELLING THE RELATIONSHIP STATUS:........

def realtion():
    realtion1=logic()
    if(realtion1=='F'):
        print("THE RELATIONSHIP STATUS IS FRIEND.......")
    if(realtion1=='L'):
        print("THE RELATIONSHIP STATUS IS lover.......")
    if(realtion1=='A'):
        print("THE RELATIONSHIP STATUS IS AFFECTION.......")
    if(realtion1=='M'):
        print("THE RELATIONSHIP STATUS IS MARRIAGE.......")
    if(realtion1=='E'):
        print("THE RELATIONSHIP STATUS IS ENEMY.......")
    if(realtion1=='S'):
        print("THE RELATIONSHIP STATUS IS SISTER.......")
    




#FUNCTION CALLING
welcome()
if input("would u like to display the name(Y/N)").upper()=='Y':
    flame_name()
    common_letter()
    count()
    realtion()
else:
    print("it will not proceed.. exiting........")




