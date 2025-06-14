# Build the "AutoFocus" command line app
# It should support (0) display the list w/ each list item's status (new/dotted/completed),
# (1) adding items to one's list, 
# (2) prioritizing the list,
# (3) deleting the entire list at once, and
# (4) marking the current "most want to do" item as done
#SDM this is my attempt at creating an auto focus app. I'll start the program by creating the
#  menu. Each menu option will a number the user can type to access that option. Depending on
#  the number typed the program called upon a specific function. For the add a new item function
#  the function will ask for an input and save it as the variable 'answer'. Then it will check that
#  the answer is not empty text. If it is, it gets rejected and you get sent back to the main menu.
#  If the input is valid it gets saved as a list that includes the answer and its marker. We will attempt
#  to use nested lists to solve the algorithm.
# For the delete function we will use the same method as when we created our todo list in class. It asks
#  for the user to input the specific number of the list item they would like to remove. It checks if the
#  answer is valid b checking if its a number and if the number is within the list items. If the user types all
# the entire list gets deleted.
# Now comes the function that I never got to work properly. This function was suppose to look for the first
#  blank/new task in the list and mark it as prioritized(o). It then would go to the next item in the list with a
#  blank and ask if you would like to prioritize that item over the last one. if you said yes then those items were
#  marked with a "o" until it went over the entire list. After that process was completed it would use the nested lists
#  to and the marks to look for the priotized tasks and put them in a new list. At the same time it would create a
#  second list where all the blank tasks would be placed. Then theyy would be combined in order to move all the
#  prioritized tasks to the end of the new list. I tried to creat a bubbling to to the end effect through this
#  function. I used a copy of the original list to do so because otherwise it would now work as intended.
# The highest priority done function was surpeisingly the easiest.I found online that if you add tripple negative 1s
#  the behaviour of the "for" loop gets reversed. It starts by looking for the last item of the list and looks at its
#  marker if its a "o" then it gets assigned an "x" to be marked as complete. In case it goes over the list and doest find
# any priotized tasks it will print the message "No prioritized tasks were found"
# The display function is also pretty straight forward it uses a for loop to make sure it prints every item on the list.
# It then prints formated string with the index # + 1 to not display 0, the task from[i][0] and its marker[i][1].
# I didn't create a function for the last option quit. What I did is I created a boolean for listing and while loop for the
#  program to run as long as listing was true. If the user pressed 6 it will make listing False thus stopping the 
# program.
#  Overall this program was very challenging as well as very "fun". In the way that most of the things I tried dind't
#  work but when I got something to work as I invisioned, it was very gratifying. I spent at least 10 hours working on this and
#  I was able to use many of the techniques we learned in class as well as new ones I found online. The reason I tried using
#  nested lists was because that was the latest zybooks topic I had worked on and I had the material fresh in my head and it
#  seemed like the best option at the time. I Wish I was able to work on this project during different circumstances as I leave with a sour
# taste in my mouth because I was never able to get it to work 100% the way I wanted to. 
awesome_list = []

print("Welcome to my Auto-Focus App")

def add_new_item():
    """This function allows to add items to the list. In addition it creates
      an empty space in a nested list that is connected to the task. This will be our marker"""
    answer = input("Please type the activity to be added to the list.\n> ")
    if answer != "":
        awesome_list.append([answer, ' '])
    else:
        print("Please enter a valid item")
    
def delete_list():

    """This function allows the user to delete specific items from the list and allows"""
    print("Would you like to remove a single item from the list or would you like to delete the entire list?\n" \
     "Type a number to remove that specific item.\nType 'all' to delete the whole list or type 'c'.")
    answer = input("> ")
    # if answer == 'c': #add while loop to add option to back up
        
    if answer.isnumeric():  # attempt to remove an item from the list
        index = int(answer) - 1
        if len(awesome_list) == 0:
            print("You can't remove anything from an empty list")
        else:
            if index >= 0 and index < len(awesome_list):
                awesome_list.pop(index)
            else:
                print("There isn't an item with that number")
    elif answer == "all":
        awesome_list.clear()
        print("All items have been deleted.")
    else:
        print("Please input a valid answer.")
def prioritize_list():
    """This funcction automatically assigns priority to the first typed task and ignores the ones marked
        with x since they are alreadyy completed then sends the task that has been prioritized to the end of the list."""

    for i in range(len(awesome_list)):
        if awesome_list[0][1] == ' ':
            awesome_list[0][1] = 'o'
            index = i
            break
       
    else:
        print("There are no new items to prioritize.")
    for j in range(index + 1, len(awesome_list)):
        if awesome_list[j][1] == ' ':
            decision = input(f"Would you like to '{awesome_list[j][0]}' more than '{awesome_list[index][0]}'? (y/n)\nPlease type 'y' or 'n'\n> ")
            while decision != 'y' and decision != 'n':
                print("please input a valid selection")
            if decision == 'y':
                awesome_list[j][1] = 'o'
                index = j
    blank_list = []
    priority_list = []
    for task in awesome_list:
        if task[1] == 'o':
            priority_list.append(task)
        else:
            blank_list.append(task)

    awesome_list[:] = blank_list + priority_list
               

def highest_priorty_done():
    """This function starts looking from the end of the list for the first 'o' mark
    on the second nested list [i][1] of the highest priority task and  changes the mark to 'x' aka marks it as done."""
    looking = True
    while looking:
        for i in range(len(awesome_list)-1, -1, -1):
            if awesome_list[i][1] == 'o':
                awesome_list[i][1] = 'x'
                looking = False
            else:
                print("No prioritized tasks were found")
                looking = False


def display_list():
    """This function displays the the number of the task which hold no meaning apart from helping when deleting,
    before displaying it check if the list if empty. It then proceeds to show each task i with its respective mark nested[i][1] and the task itself[i][0]"""
    if len(awesome_list) == 0:
        print("Your list is empty.")
        return
    else:
        for i in range(len(awesome_list)):
            print(f"{i + 1}). [{awesome_list[i][1]}] {awesome_list[i][0]}")

listing = True

while listing:  # we need to loop for an indefinite number of times

    print("1. Add new item to list")
    print("2. Delete list")
    print("3. Prioritize list")
    print("4. Mark ready item as done")
    print("5. View List")
    print("6. Quit AutoFocus")

    answer = input("> ")  # get the user input and save it

    # options
    if answer == "1":
        add_new_item()
    elif answer == "2":
        delete_list()
    elif answer == "3":
        prioritize_list()
    elif answer == "4":
        highest_priorty_done()
    elif answer == "5":
        display_list()
    elif answer == "6":
        print("Good bye and good luck on your tasks!")
        listing = False
    else:
        print("Please input a valid selection.\n")
