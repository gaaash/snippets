adad = int(input('enter num: '))
reminder = 0
output = ""
while adad > 1:
    reminder= adad%16
    if reminder < 10:
        output += str(reminder)
    elif reminder == 10:
        output += "A"
    elif reminder == 11:
        output += "B"
    elif reminder == 12:
        output += "C"
    elif reminder == 13:
            output += "D"
    elif reminder == 14:
            output += "E"
    elif reminder == 15:
            output += "F"
    adad = adad//16

print("0x"+output[::-1])
