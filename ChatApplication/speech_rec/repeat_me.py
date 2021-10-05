from tp_pkg.myscr import voice_to_text

import platform
if platform.system() == "Windows":
    import pyttsx3
    engine = pyttsx3.init()
else:
    import os
while True:
    print('Python is listening...')
    inp = voice_to_text()
    if inp == "stop listening":
        print(f' You just said {inp}; Goodbye!')
        if platform.system() == "Windows":
            engine.say(f'You just said {inp}; Goodbye!')
            engine.runAndWait()
        else:
            os.system(f'gtts-cli --nocheck "You just said {inp}; goodbye!" | mpg123 -q -')
        break
    else:
        print(f'You just said {inp}')
        if platform.system() == "Windows":
            engine.say(f'You just said {inp}')
            engine.runAndWait()
        else:
            os.system(f'gtts-cli --nocheck "You just said {inp}" | mpg123 -q -')
        continue
