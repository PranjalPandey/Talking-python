from tp_pkg.mysay import print_say
from tp_pkg.myscr import voice_to_text

while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print_say(f'You just said {inp}; goodbye!')
        break
    else:
        print_say(f'You just said {inp}')
        continue