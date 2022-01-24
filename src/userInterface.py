"""
Module to handle the command line interface for the program.
"""

###################
#    Constants    #
###################

MAIN_MENU_OPTIONS = ["Log In", "Create Account"] #cli prompts for main menu


#################
#    Methods    #
#################

def getUserChoice(choices: list, prompt=None) -> int:
    """
    Prompts the user to select from a list of choices.
    Parameters:
        `choices`: A list of string prompts to ask the user to choose from.
        `prompt`: An optional prompt to display to the user. If a prompt is not given, a default prompt is used.
        Defaults to None.
    Returns:
        The index of the choice the user selects.
    """

    #print prompt
    if prompt is not None:
        print(prompt)
    else:
        print("Select an option:")

    #print choices
    for x in range(len(choices)):
        print(" " + str(x+1) + ") " + choices[x])

    #get user choice
    while True:
        
        userChoice = input() #get input

        #check if choice is valid
        try:
            
            userChoice = int(userChoice) #convert to num

            #check range
            if userChoice < 1 or userChoice > len(choices):
                raise Exception

            break

        except:
            print("That is an invalid option, please choose again.")

    return userChoice-1

def menuLoop():
    """
    Starts at the main menu and handles the entire command line interface.
    """

    _handleMainMenu()

def _handleMainMenu():
    """
    Handles the main menu selections.
    """

    userChoice = getUserChoice(MAIN_MENU_OPTIONS) #present main menu

    #handle login
    if userChoice == 0:
        print("TODO: Login")

    #handle account creation
    elif userChoice == 1:
        print("TODO: Create account")


##############
#    Main    #
##############

if __name__ == "__main__":

    choice = getUserChoice(["Login", "Create Account"])
    print("User selected {}".format(choice))