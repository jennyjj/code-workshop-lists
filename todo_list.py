"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""
    item = raw_input("What would you like to add? ")
    my_list.append(item)

def view_list(my_list):
    """Print each item in the list."""

    for item in my_list:
        print item


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = "Would you like to: A. Add a new item, B. View list, C. Quit the program "
 
    while True:
        user_input = raw_input(user_options)
        if user_input == "A":
            add_to_list(my_list)
        elif user_input == "B":
            view_list(my_list)
        elif user_input == "C":
        # Collect input and include your if/elif/else statements here.
            break
        else:
            #inappropriate response
            print "That is not an appropriate answer."
            print "Please provide another response."

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

