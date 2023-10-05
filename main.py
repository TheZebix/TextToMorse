class TextToMorse:
    
    def __init__(self):
        self.morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}
        print(r"""
 ______________________________________
|  _____         _  _____              |
| |_   _|____  _| ||_   _|__     ___   |
|   | |/ _ \ \/ / __|| |/ _ \   /  .\  |
|   | |  __/>  <| |_ | | (_) | /  =__| |
|   |_|\___/_/\_\\__||_|\___/ /    ||  |
|______________________________________|
""")

        print("""Welcome to TextToMorse! 
*The application supports English letters, characters and numbers.
type -help for help""")

    def help(self):
        print("""--------------------------------------------------------------
What Is Morse Code?
Morse code is a method used in telecommunication to encode text characters as standardized sequences of two different signal durations, called dots and dashes, or dits and dahs. Morse code is named after Samuel Morse, one of the inventors of the telegraph.
--------------------------------------------------------------""")

    def text_to_morse(self):
        print("You choose 1")
        print("Type your text:")
        user_input = input('>')
        output = ""

        for char in user_input:
            output += self.morse_code_dict[char.lower()] + " "

        print(output)

    def morse_to_text(self):
        print("You choose 2")
        print("Type your code:")
        user_input = input('>').split(" ")
        output = ""

        for morse_code in user_input:
            for letter, morse in self.morse_code_dict.items():
                if morse == morse_code:
                    output += letter

        print(output)

END = False
text_to_morse_converter = TextToMorse()

while END == False:
    print('''--------------------------------------------------------------
What do you want to do today?
Pick one number(1-2):

1. Translate text to morse code
2. Translate morse code to text
''')
    user_input = input('>')

    if(user_input == '-help'):
        text_to_morse_converter.help()
    if(user_input == '1'):
        text_to_morse_converter.text_to_morse()
    elif(user_input == '2'):
        text_to_morse_converter.morse_to_text()

    print("Do you want to do the next operation?(yes/no)")
    if((input('>')).lower() == "no"):
        print("Exiting TextToMorse") 
        END = True

