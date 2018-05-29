"""
string
"""

import string

in_char = "aeiou"
trans_char = "12345"

text = "Ullamco et duis ad cupidatat cillum ullamco ipsum ut nulla."
print(text.translate(str.maketrans(in_char, trans_char)))

text = "Laborum quis amet eu culpa sunt deserunt proident laboris enim et esse eu. Aliqua proident magna dolor aliqua labore et sint labore sint. Esse enim qui aliqua aute incididunt ex exercitation dolore."

print(text.translate(str.maketrans({key: None for key in string.punctuation})))

print(string.ascii_letters)
print(string.punctuation)

print(string.capwords(text))

#print(dir(string))