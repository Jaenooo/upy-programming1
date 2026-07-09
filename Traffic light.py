#Traffic light
#red = stop, yellow = warning, green = go
#Any other color = invalid
color = (input("Ingresa un color: ")) .lower()
if color== "red":
    print("stop")
elif color == "green":
    print ("Go")
elif color == "yellow":
    print ("Warning")
else:
    print ("Invalid")