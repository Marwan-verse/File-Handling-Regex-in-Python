import re # import the regex module 

# Basic regex operations
re.findall(pattern, text)
pattern = r"cat"
text = "The cat sat"
re.findall(pattern, text)   # ['cat']