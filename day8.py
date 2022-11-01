name = input("Hi, what's your name?")
print("Hi " + name + ", Welcome to your daily affirmation generator!")
weekday = input("What day of the week is it?")
if weekday == "Monday" or weekday == "monday":
    print("The beginning of the week can be stressful, but you got this! Think of it as a fresh start!")
elif weekday == "Tuesday" or weekday == "tuesday":
    print("The Monday blues should be gone now! Go be productive!")
elif weekday == "Wednesday" or weekday == "wednesday":
    print("You know what time it is,", name, "!!! HUMPDAY!!!")
elif weekday == "Thursday" or weekday == "thursday":
    print("Friday Eve! You're almost there!")
elif weekday == "Friday" or weekday == "friday":
    timeOfDay = input("Is it before 1PM or after?")
    if timeOfDay == "before":
        print("Keep pushing! Alomst there!")
    else:
        print("You're practically done!")
else:
    print("It's the weekend,", name, "! Relax and reset!")
