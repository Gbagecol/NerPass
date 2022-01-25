"""
Module to manage user accounts.
"""

import bcrypt as bc

from csv import DictReader


###################
#    Constants    #
###################

ACCOUNTS_FILE_PATH = "../data/.accounts" #path to accounts file


#################
#    Methods    #
#################

def createAccount(username: str, password: str):
    """
    Creates a new account using the given username and password. Generally it should be the caller's responsibility to
    ensure that an account with the same username doesn't already exist first. This can be done with the
    doesAccountExist() function.
    Parameters:
        `username`: The new account's username.
        `password`: A plaintext password for the new account.
    """

    salt = bc.gensalt() #generate salt for password
    pwHash = bc.hashpw(bytes(password, encoding="utf-8"), salt) #hash password

    #save account info
    with open(ACCOUNTS_FILE_PATH, 'a') as accountsFile:
        accountsFile.write(username.lower() + "," + str(pwHash)[2:-1] + "," + str(salt)[2:-1] + "\n")

def doesAccountExist(username: str) -> bool:
    """
    Checks if an account exists for the given username.
    Parameters:
        `username`: The username to check for.
    Returns:
        True if an account exists, false otherwise.
    """

    return username in _loadAccounts()

def _loadAccounts() -> list:
    """
    Loads the usernames for all existing accounts.
    Returns:
        A list of all existing usernames.
    """

    users = [] #username list

    #load account info
    with open(ACCOUNTS_FILE_PATH, 'r') as accountsFile:

        csvReader = DictReader(accountsFile) #csv file reader

        #get usernames
        for row in csvReader:
            users.append(row["username"])

    return users


##############
#    Main    #
##############

if __name__ == "__main__":
    
    createAccount("test", "test")