print("All Alphabet will show as a Triangle\n")
# Enter a integer number: 5
# A
# B B
# C C C
# D D D D
# E E E E E
def alphapat(n):

    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
        num = num + 1
        print("\r")


alphapat(int(input("Enter a integer number: ")))


# Enter a integer number: 5
# A
# B C
# D E F
# G H I J
# K L M N O

def contalpha(n):

    num = 65
    for i in range(0, n):
        for j in range(0, i + 1):
            ch = chr(num)
            print(ch, end=" ")
            num = num + 1
        print("\r")


contalpha(int(input("Enter a integer number: ")))


