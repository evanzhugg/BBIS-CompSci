# base 10 to base 2
decimal = int(input('What is your number?'))
numlist = []
while decimal > 0:
    numlist.append(decimal % 2)
    decimal = decimal // 2

print(numlist[::-1])
