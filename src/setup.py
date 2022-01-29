"""
Script to set up directories and install dependencies.
"""

import os
import subprocess as sp

from pathlib import Path


###################
#    Constants    #
###################

DATA_DIR_PATH = "../data" #path to data directory
PASSWORD_DIR_PATH = "../data/.passwords" #path to password file directory
KEY_DIR_PATH = "../data/.keys" #path to keys directory
ACCOUNTS_FILE_PATH = "../data/.accounts" #path to accounts file


#################
#    Methods    #
#################

def _createDataDirectory():
    """
    Builds the data directories.
    """

    dataPath = Path(DATA_DIR_PATH) #Path object for data dir

    #create data directory if it doesn't exist
    if not dataPath.exists():

        print("Creating data directory...")

        os.mkdir(DATA_DIR_PATH) #top level data directory
        os.mkdir(PASSWORD_DIR_PATH) #dir for password files
        os.mkdir(KEY_DIR_PATH) #dir for AES key files

        #create accounts file
        with open(ACCOUNTS_FILE_PATH, 'w') as accountsFile:
            accountsFile.write("username,password,salt\n")

    else:
        print("Data directory already exists")

def _installDependencies():
    """
    Uses pip to install the required python libraries.
    """

    print("Installing external libraries...")

    sp.run(["pip", "install", "bcrypt"])
    sp.run(["pip", "install", "fuzzywuzzy"])
    sp.run(["pip", "install", "pycryptodome"])

def _setup():
    """
    Runs the entire setup process.
    """

    print("Running setup...")

    _createDataDirectory()
    _installDependencies()

    print("Done")


##############
#    Main    #
##############

if __name__ == "__main__":

    #set cwd to src if it is not already
    if "src" not in os.getcwd():
        os.chdir("src")

    _setup()