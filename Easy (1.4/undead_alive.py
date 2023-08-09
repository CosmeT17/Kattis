# Undead or Alive: https://open.kattis.com/problems/undeadoralive
# Cosme M. Tejeda

def isAlive():
    string = input()

    if string.find(":)") != -1:
        if string.find(":(") != -1:
            print("double agent")
        else:
            print("alive")
        return

    if string.find(":(") != -1:
        print("undead")
    else:
        print("machine")

isAlive()
