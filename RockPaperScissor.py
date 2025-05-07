'''
Rock=1
paper=2
Scissor=3
'''
import random
computer=random.choice([1,2,3])
your_choice= input("Enter you Choice")
yourDict={"r": 1, "p": 2, "s": 3}
yourRevDict={1:"Rock", 2:"Paper", 3:"Scissor"}
you=yourDict[your_choice]

print(f"Computer choose: {yourRevDict[computer]}/n You choose: {yourRevDict[you]}")

# if(computer==you):
#     print("It's a Draw")
# else:
#     if(computer==1 and you==2):            #2-1=1
#         print("Yayy!! You WINN!!")
#     elif(computer==1 and you==3):          #3-1=2
#         print("Opps!! You LOOSEE!!")
#     elif(computer==2 and you==3):          #3-2=1
#         print("Yayy!! You WINN!!")        
#     elif(computer==2 and you==1):          #1-2=-1
#         print("Opps!! You LOOSEE!!")
#     elif(computer==3 and you==1):          #1-3=-2
#         print("Yayy!! You WINN!!")
#     elif(computer==3 and you ==2):         #2-3=-1
#         print("Opps!! You LOOSEE!!")
#     else:
#         print("Something went wrong!!!")



#now something diff we are noticing patter so one patter if we did you minus the computer that is maybe eg.2-1=1 so whenever we are winning we are getting either 1 or -2 and when losing we are getting -1 or 2 so instrad of writing upper ka whole if else we can write it as:

if(computer==you):
    print("It's a Draw")
else:
    if((you-computer)==1 or (you-computer)==-2):
        print("You Win")
    else:
        print("You Lose")