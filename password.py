actualPassword=2387
attemptsCount=3
for i in range(3):
    currentPassword=int(input())
    if currentPassword==actualPassword:
        print("Successfully logged in")
        break
    else:
        if attemptsCount==1:
            print("Your account blocked ,try after 24 hrs")
        else:    
            print("Incorrect Password,your left with",attemptsCount-1,"attempts")
    attemptsCount-=1
