#!/usr/bin/python3
'''Contains function text_indentation()
text_indentation function prints a new line in text after these charactrers
[., ?, :]
'''


def text_indentation(text):
    '''Prints a text with 2 new lines after each of these characters: ., ? and :
    args:
        text (string): The text to be parsed and printed
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    seps = ['.', '?', ':']
    for i in range(len(text)):
        if text[i] not in seps:
            if text[i] == " ":
                if text[i - 1] in seps:
                    continue
            print("{}".format(text[i]), end="")
        else:
            print("{}".format(text[i]))
            print()
