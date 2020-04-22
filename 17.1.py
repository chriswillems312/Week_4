days = ["N", "E", "S", "W"]


def turn_clockwise(day):
    for i in day:
        if day == "N":
            return "E"
        elif day == "E":
            return "S"
        elif day == "S":
            return "W"
        elif day == "W":
            return "N"


print(turn_clockwise("N") == "E")


