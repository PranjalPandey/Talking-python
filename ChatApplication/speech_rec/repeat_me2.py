# Import functions from the local package mptpkg
from tp_pkg import voice_to_text
from tp_pkg import print_say
while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print_say(f'you just said {inp}; goodbye!')
        break
    else:
        print_say(f'you just said {inp}')
        continue