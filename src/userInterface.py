"""
Module to handle the command line interface for the program.
"""

import manageAccounts as ma
import logging

from getpass import getpass


######################
#    Module Setup    #
######################

logger = logging.getLogger(__name__) #create logger
logFormatter = logging.Formatter("[(%(name)s) %(asctime)s %(levelname)s] %(message)s", datefmt="%m/%d/%Y %I:%M:%S")
logHandler = logging.StreamHandler() #create handler for console

#init handler
logHandler.setLevel(logging.DEBUG)
logHandler.setFormatter(logFormatter)

logger.addHandler(logHandler) #set handler
logger.setLevel(logging.DEBUG)


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
        session = _handleLogin() #login and get session
        welcomeString = f"Welcome back, {session.USERNAME}!"

    #handle account creation
    elif userChoice == 1:
        session = _handleCreateAccount() #create account and get session
        welcomeString = f"Welcome, {session.USERNAME}!"

    print()
    print("-" * len(welcomeString))
    print(welcomeString)
    print("-" * len(welcomeString))

def _handleCreateAccount() -> ma.Session:
    """
    Handles the account creation option from the main menu.
    Returns:
        A Session object representing the new user's current session.
    """

    #get username
    username = _getInputUntilCondition(
            lambda username: not ma.doesAccountExist(username), #check if this username already exists
            "Enter a username",
            "That username already exists. Please enter another username."
    )

    password = _getAndConfirmPassword() #get password

    session = ma.createAccount(username, password) #create account

    print("Account created successfully.")

    return session

def _handleLogin() -> ma.Session:
    """
    Handles the login option from the main menu.
    Returns:
        A Session object representing the current user's session.
    """

    #validation loop
    while True:

        username = input("Enter your username: ") #get username
        password = getpass("Enter your password: ")

        session = ma.login(username, password) #attempt login

        if session is not None:
            print("Logged in successfully.")
            return session
        else:
            print("That username or password is incorrect. Please try again.")

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