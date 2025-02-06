import time
q= ["What is the capital of Italy?","Which country has highest GDP?","Who is the captain of Indian cricket team in 2024?","Who is the PM of India?"]
a= ["Rome","USA","Rohit","Modi"]
op1= ["Milan","Pisa", "Torino", "Rome"]
op2 =["USA", "Germany", "China", "India"]
op3 =["Rohit","Dhoni","Kohli","Bumrah"]
op4 =["Modi","Rahul","Kejriwal","Amit"]
i=0
while i < 1:
    count=0
    #print(len(q))
    print("Welcome to KBC program! Please read questions carefully and answer") 
    print("Now, Let's start!")
    time.sleep(2)  
    print("Your first Question is:\n" ,q[0])
    opa1=input(f"your options are :\n a.{op1[0]}   b.{op1[1]} \n c.{op1[2]}  d.{op1[3]} \n")
    if(a[0]==opa1):
        print(".....Congrats! you won 100$.....\n")
    else:
        print("Sorry! your Answer is wrong and you won nothing")
        break
    time.sleep(2)
    print("Your Second Question is:\n" ,q[1])

    opa2=input(f" your options are :\n a.{op2[0]}   b.{op2[1]} \n c.{op2[2]}  d.{op2[3]} \n")
    if(a[1]==opa2):
        print("............... Congrats! you won 200$ ..............\n")
        time.sleep(2)
    else:
        print("Sorry! your Answer is wrong and you'll receive 100$")
        time.sleep(2)
        break

    time.sleep(2)
    print("Your Third Question is:\n" ,q[2])
    opa3=input(f"your options are :\n a.{op3[0]}   b.{op3[1]} \n c.{op3[2]}  d.{op3[3]} \n")

    if(a[2]==opa3):
        print("........Congrats! you won 500$............\n")
    else:
        print("Sorry! your Answer is wrong and you'll receive 200$")
        time.sleep(2)
        break

    time.sleep(2)
    print("Your Last Question is for 1000$:\n" ,q[3])
    opa4=input(f"Your options are :\n a.{op4[0]}   b.{op4[1]} \n c.{op4[2]}  d.{op4[3]} \n")

    if(a[3]==opa4):
        print(".........Congrats on your win! you won 1000$............")
        print("Enjoy 1000$ :) Claps,Claps...")
        time.sleep(3)
        print("Game ends here!")
        
    else:
        print("Sorry! your question is wrong and  and you'll receive 500$")
        print("You played well!")
        time.sleep(2)
        break
    i=i+1