# Object oriented  number Genius

class user:
    def __init__(self,name):
        user.name = name
        user.score = 0
        user.points = 0
        user.gamesPlayed = 0
        user.gamesWon = 0

    def makeFile(self):
        with open(user.name+".txt", "w", encoding = "utf-8") as userInfo:
            userInfo.write(user.name.upper())

#main
def main():
    username = input("Enter your name: ")
    User = user(username)
    User.makeFile()
    with open(username+".txt", "r", encoding = "utf-8") as readUI:#readUserInfo
        readInfo = readUI.read()
        print(readInfo)
    return

main()
