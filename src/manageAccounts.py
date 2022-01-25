"""
Module to manage user accounts.
"""

import bcrypt as bc

from csv import DictReader


###################
#    Constants    #
###################

ACCOUNTS_FILE_PATH = "../data/.accounts" #path to accounts file


#######################
#    Session Class    #
#######################

class Session():
    """
    A class to manage the current login session.
    """

    #####################
    #    Constructor    #
    #####################

    def __init__(self, username: str, pwHash: bytes):
        """
        Creates a new Session object.
        Parameters:
            `username`: The username for the current user.
            `pwHash`: The current user's password hash as bytes.
        """

        #init

        self.username = username
        self.pwHash = pwHash


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
    Returns:
        A Session object.
    """

    salt = bc.gensalt() #generate salt for password
    pwHash = bc.hashpw(bytes(password, encoding="utf-8"), salt) #hash password

    #save account info
    with open(ACCOUNTS_FILE_PATH, 'a') as accountsFile:
        accountsFile.write(username.lower() + "," + str(pwHash)[2:-1] + "," + str(salt)[2:-1] + "\n")

    return Session(username, pwHash)

def login(username: str, password: str):
    """
    Attempts to log the given user in. If the username doesn't exist or the password is incorrect, the attempt is
    rejected.
    Parameters:
        `username`: The account username.
        `password`: The account password in plaintext.
    Returns:
        A Session object if the login is successful. If not, None is returned.
    """

    #check username
    if not doesAccountExist(username):
        return None

    #load account information
    with open(ACCOUNTS_FILE_PATH, 'r') as accountsFile:

        csvReader = DictReader(accountsFile) #csv file reader

        #find matching account
        for row in csvReader:
            if row["username"] == username:

                password = bytes(password, encoding="utf8") #convert password to bytes
                storedPwHash = bytes(row["password"], encoding="utf8") #get stored password hash

                #check hash against existing
                if bc.checkpw(password, storedPwHash):
                    return Session(username, storedPwHash) #return Session object
                else:
                    return None

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
    
    session = login("tlorenz", "password")
    print(session.username)