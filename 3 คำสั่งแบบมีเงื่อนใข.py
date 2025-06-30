light = input("Enter a traffic light: ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Ready to stop")
elif light == "green":
    print("Go")
else:
    print("That is not a traffic light color")