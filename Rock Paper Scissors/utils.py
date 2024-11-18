import platform
import os

def find_os():
    return platform.system()

def clear_terminal():
    if find_os().startswith("Windows"):
        return os.system("cls")
    return os.system("clear")

def paper():

    return """
  _____________________
 /                    /
/                    /
|                   |
|                   |
|      paper        |
|                   |
|                   |
|                   |
|___________________|
"""
def rock():

    return """
   _______
  /       \\
 /         \\
 |  ROCK   |
 \\_________/
"""

def scissors():

    return """
       _______
      /       |
     /  O  O  |
    |     ^    |
     \\   '-'  /
      |_______|
      //     \\\\
     ((       ))
      \\\\     //
       \\\\___//
"""