#############################################################################
#                                  FreeBSD                                  #
#############################################################################

import os
import subprocess
import sys
import getpass

def addUser():
    username = input("Enter username")
    password = getpass.getpass()

    try:
        subprocess.run(['pw', 'user', 'add', username, '-p', password])
        print(f"Successfully user {username} created.")
    except:
        print(f"Failed to add user {username}")
        sys.exit(1)

def removeUser():
    username = input("Enter username")

    try:
        output = subprocess.run(['rmuser', '-y', username])
        if output.returncode == 0:
            print(f"user {username} successfully deleted with given credentials")
    except:
        print(f"Failed to delete user {username}")
        sys.exit(1)
