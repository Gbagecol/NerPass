"""
Module to handle the command line interface for the program.
"""

import manageAccounts as ma

from getpass import getpass


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
        _handleCreateAccount()

def _handleCreateAccount():
    """
    Handles the account creation option from the main menu.
    """

    #get username
    username = _getInputUntilCondition(
            lambda username: not ma.doesAccountExist(username), #check if this username already exists
            "Enter a username",
            "That username already exists. Please enter another username."
    )

    password = _getAndConfirmPassword() #get password

    ma.createAccount(username, password) #create account

    print("Account created successfully.")

def _getAndConfirmPassword() -> str:
    """
    Prompts the user to enter a password, then to confirm it.
    Returns:
        The plaintext password entered by the user.
    """

    #validation loop
    while True:

        password1 = getpass("Enter a password (Please make this STRONG): ")
        password2 = getpass("Enter your password again: ")

        if password1 == password2:
            return password1
        else:
            print("Those passwords do not match. Please enter them again.")

def _getInputUntilCondition(condition, prompt: str, badInputResponse: str, useGetpass=False) -> str:
    """
    Requests the user for some input until the input satisfies the given condition.
    Parameters:
        `condition`: A function of the form `func(str) -> bool`. The function should take a string (the
        user's input) and return true if the input is considered valid, or false if it isn't.
        `prompt`: A string to prompt the user with. A colon is appended.
        `badInputResponse`: A string to display when the user's input is not valid.
        `useGetpass`: Whether the input() function should be replaced with the getpass() function. Defaults to false.
    Returns:
        The user's input after being validated by the condition.
    """

    #validation loop
    while True:

        if not useGetpass:
            userInput = input("{}: ".format(prompt))
        else:
            userInput = getpass("{}: ".format(prompt))

        if condition(userInput):
            return userInput
        else:
            print(badInputResponse)


##############
#    Main    #
##############

if __name__ == "__main__":

    password = _getAndConfirmPassword()
    print(password)