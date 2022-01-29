"""
Main script for the password manager.
"""

import userInterface as cli
import os


##############
#    Main    #
##############

if __name__ == "__main__":

    #set cwd to src if it is not already
    if "src" not in os.getcwd():
        os.chdir("src")
    
    print()
    print("--------------- WELCOME TO NERPASS ---------------")
    print()

    cli.menuLoop()