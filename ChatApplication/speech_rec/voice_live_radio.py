# Put web driver in the same folder as this script
# Import the web driver function from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Import functions from the local package
from tp_pkg import voice_to_text, print_say


def live_radio():
    global button
    chrome_options = Options()
    chrome_options.add_argument("—headless")
    browser = webdriver.Chrome\
    (executable_path = './chromedriver',chrome_options = chrome_options)
    browser.get("https://onlineradiobox.com/us/")
    button = browser.find_element_by_xpath('//*[@id="b_top_play"]')
    button.click()
while True:
    print_say("how may I help you?")
    inp = voice_to_text().lower()
    print_say(f'you just said {inp}')
    if inp == "stop listening":
        print_say('Goodbye!')
        break
    elif "radio" in inp:
        print_say('OK, play live radio online for you!')
        live_radio()
        while True:
            background = voice_to_text().lower()
            if "stop playing" in background:
                button.click()
                break
            else:
                continue