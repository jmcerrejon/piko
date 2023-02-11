# Author: Jose Cerrejon
# Email: contact at ulysess dot gmail dot com
# License: MIT
# Version: 0.1.1

import openai

openai.api_key = "YOUR-API-KEY"

print("""
d8888b. d888888b db   dD  .d88b.  
88  `8D   `88'   88 ,8P' .8P  Y8. 
88oodD'    88    88,8P   88    88 
88~~~      88    88`8b   88    88 
88        .88.   88 `88. `8b  d8' 
88      Y888888P YP   YD  `Y88P'  

Version 0.1.PQR

Hi! I'm PIKO!. The new AI created from the collective mind of trillons of flies.
Type [exit] to exit the program or [imagine] to get a picture something you input.
""")


def open_default_browser(url):
    import webbrowser
    webbrowser.open_new_tab(url)


def draw() -> str:
    print("\nYou want a picture!")
    prompt = input("\nImagine... ")

    if prompt == "exit":
        print("\nBye! I hope I was helpful!")
        exit()

    print("\nLet me draw something about that...\n")
    answer = openai.Image.create(prompt=prompt,
                                 size="1024x1024")
    url = answer['data'][0]['url']
    open_default_browser(url)

    return url


def answer(prompt) -> str:
    print("\nLet me think about that...")

    answer = openai.Completion.create(engine="text-davinci-003",
                                      prompt=prompt,
                                      max_tokens=2048)
    return answer.choices[0].text


while True:
    prompt = input("\nBuzZ: ")

    if prompt == "exit":
        print("\nBye! I hope I was helpful!")
        break

    response = answer(prompt) if prompt != "imagine" else draw()
    print(response)
