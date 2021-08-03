import random
randomNumber = random.randint(1, 100)
# print(randomNumber)

userEnter = 0
while(userEnter != randomNumber):
    user = int(input("Enter the number to guess"))
    if user < randomNumber:
        print("your are near to the answer, Enter little greater value")
        userEnter += 1
    elif user > randomNumber:
        print("your are near to the answer, Enter little smaller value")
        userEnter += 1
    if user == randomNumber:
        print(f"Congratulation! you got the correct value in  {userEnter} try")
        print()
        break
    print()

with open("p1.txt", "r") as f:
    highscore = int(f.read())

if (userEnter < highscore):
    print("congratulation 👍 you have broken the score ")
    with open("p1.txt", "w") as f:
        f.write(str(userEnter))
