"""
Urllib
"""

import urllib.request

with urllib.request.urlopen("http://python.org/") as response:
    html = response.read()
    # print(html) # bytes
    print(html.decode("utf-8"))

with urllib.request.urlopen("http://www.google.com/") as everyWords:
    words = []
    for line in everyWords:
        # line_words = line.decode("utf-8").split()
        line_words = line.decode("latin1").split()
        for word in line_words:
            words.append(word)
    print(words)
