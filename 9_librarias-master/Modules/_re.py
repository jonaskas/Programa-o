"""
re
See: https://docs.python.org/3/howto/regex.html#regex-howto
See: https://docs.python.org/3/library/re.html#module-re
"""

import re

zen = """Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense.Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those"""

# starts with c followed by letters 
result = re.findall(r"\bc[a-z]*", zen)
print(result)

# Add breakline before words with uppercase first letter
result = re.sub(r"((?!Dutch)\b[A-Z]+)", r'\n\1', zen) 
print(result)
