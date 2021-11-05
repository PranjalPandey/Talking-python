import pathlib
import random

from tp_pkg import print_say

# Define the joke() function


def joke():
    # Read the content from the file jokes.txt
    joke_file=pathlib.Path.cwd() / 'files' / 'jokes.txt'
    with open(joke_file,'r') as f:
        content = f.read()   
    # Split the content at double line breaks
    jokelist = content.split('\n\n')
    # Randomly selects a joke from the list
    joke = random.choice(jokelist)
    print_say(joke)
