import wikipedia
from tp_pkg import voice_to_text, print_say

# Ask what you want to know
print_say("What do you want to know?")
try:
    # Capture your voice input
    my_query = voice_to_text()
    print_say (f"you said {my_query}")
    # Obtain answer from Wikipedia
    ans = wikipedia.summary(my_query)
    # Say the answer in a human voice
    print_say(ans[0:500])
except Exception as e:
    print(e)