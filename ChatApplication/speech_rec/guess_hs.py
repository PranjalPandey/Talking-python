import time
import sys
# Import functions from the local package mptpkg
from tp_kg import voice_to_text
from tp_pkg import print_say
# Print and announce the rules of the game in a human voice
print_say('''Think of an integer,
bigger or equal to 1 but smaller or equal to 9,
and write it on a piece of paper''')
print_say("You have 5 seconds to write your number down")
# Wait for five seconds for you to write down the number
time.sleep(5)
print_say('''Now let's start. I will guess a number and you can say:
too high, that is right, or too small''')
# The script asks in a human voice whether the number is 5
print_say("Is it 5?")
# The script is trying to get your response and save it as re1
# Your response has to be 'too high', 'that is right', or 'too small'
while True:
    re1 = voice_to_text()
    print_say(f"You said {re1}")
    if re1 in ("too high", "that is right", "too small"):
        break
# If you say "that is right", game over
    if re1 == "that is right":
        print_say("Yay, lucky me!")
        sys.exit