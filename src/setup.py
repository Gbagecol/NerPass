"""
Script to set up directories and install dependencies.
"""

import logging
import os
import subprocess as sp

from pathlib import Path


######################
#    Module Setup    #
######################

logger = logging.getLogger("setup") #create logger
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

        logger.info("Generating data directory")
        print("Creating data directory...")

        os.mkdir(DATA_DIR_PATH) #top level data directory
        os.mkdir(PASSWORD_DIR_PATH) #dir for password files
        os.mkdir(KEY_DIR_PATH) #dir for AES key files

        #create accounts file
        with open(ACCOUNTS_FILE_PATH, 'w') as accountsFile:
            accountsFile.write("username,password,salt\n")

    else:
        logger.info("Data directory already exists")
        print("Data directory already exists")

def _installDependencies():
    """
    Uses pip to install the required python libraries.
    """

    logger.info("Installing dependencies")
    print("Installing external libraries...")

    logger.info("Installing bcrypt")
    sp.run(["pip", "install", "bcrypt"])

    logger.info("Installing fuzzywuzzy")
    sp.run(["pip", "install", "fuzzywuzzy"])

    logger.info("Installing pycryptodome")
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
        logger.debug("Changed cwd to src")
        os.chdir("src")

    _setup()