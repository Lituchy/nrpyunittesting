# Acts as a keyboard, being able to type like a human.

from pynput.keyboard import Key, Controller
keyboard = Controller()

# write takes in a string [parseString] to be pressed on a keyboard. Alphanumeric characters act as normal.
# A '+' represents pressing [tab] on the keyboard.
# Example: write('+Hello+') will press [tab], type the word 'Hello', then press [tab] again.
# Useful for automatically filtering the HTML coverage report.
def write(parseString):

    for char in parseString:
        if char == '+':
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
        else:
            keyboard.press(char)
            keyboard.release(char)
