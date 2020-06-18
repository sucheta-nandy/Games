import random
doors=[0]*3
goatdoor=[0]*2
swap=0
dont_swap=0
x=random.randint(0,2)  #x will comprise of the BMW
doors[x]="BMW"
for i in range(0,3):
    if(i==x):
        continue 
    else:
        doors[i]="Goat"
        goatdoor.append(i)
choice=int(input("Enter your choice"))
door_open=random.choice(goatdoor)
while(door_open==choice):
    door_open=random.choice(goatdoor)
ch = input("do u want to swap? y/ n ")
if(ch=='y'):
    if(doors[choice]=='Goat'):
        print("player wins")
        swap=swap+1
    else:
        print("Player lost")
else:
    if(doors[choice]=='Goat'):
        print("Player lost")
    else:
        print("player wins")
        dont_swap=dont_swap+1
        
print(swap)
print(dont_swap)

        
    
    
    

    
