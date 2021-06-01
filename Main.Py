import time
text = str(input("What's the task that i need to remind you about?\n"))
local_time = float(input("In how many minutes should i remind you about the task?\n")) * 60
time.sleep(local_time)
print("Yooo, this is your reminder to:",text)
print("For more options press the mentioned keys")
option = int(input(print("Enter 1 to Complete task \n Enter 2 to Snooze the task \n Enter 3 to insert new task\n")))
if option == 1:
    print("Task Marked as complete") 
elif option == 2: 
    new_time = float(input("For how many minutes would you like to snooze the task?\n"))*60
    time.sleep(new_time)
    print("Yooo, this is your reminder to:",text)
elif option == 3:
    text = str(input("What's the task that i need to remind you about?"))
    local_time = float(input("In how many minutes should i remind you about the task?")) * 60
    time.sleep(local_time)
    print("Yooo, this is your reminder to:",text)

