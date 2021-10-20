import time
import sys
# Import functions from the local package mptpkg
from tp_pkg import voice_to_text
from tp_pkg import print_say
# Print and announce the rules of the game in a human voice
print_say('''Think of an integer,
bigger or equal to 1 but smaller or equal to 99,
and write it on a piece of paper''')
print_say("You have 5 seconds to write your number down")
# Wait for five seconds for you to write down the number
time.sleep(5)
print_say('''Now let's start. I will guess a number and you can say:
big, that is right, or small''')
low=0
high=99
mid=low+(high-low)//2
while low<high:
    mid = low + (high - low) // 2
    print_say(f"Is it {mid}?")
    re= voice_to_text()
    print_say(f"You said {re}")
    if re == "big":
        high = mid
    elif re == "small":
        low=mid+1
    elif re == "that is right":
        print_say("Yay, lucky me!")
        sys.exit
        break
