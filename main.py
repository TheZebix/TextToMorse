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

What do you want to translate today?""")

    def text_to_morse(self, input):
        output = ""

        for char in input:
            output += self.morse_code_dict[char] + " "

        print(output)

END = False
text_to_morse_converter = TextToMorse()

while END == False:
    user_input = input('>')

    text_to_morse_converter.text_to_morse(user_input)

    print("Do you want to translate the next text?(yes/no)")
    if((input('>')).lower() == "no"):
        print("Exiting TextToMorse") 
        END = True

