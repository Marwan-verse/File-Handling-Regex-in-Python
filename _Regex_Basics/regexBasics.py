import re # import the regex module 

# Basic regex operations
pattern = r"cat" #pattern to match the word 'cat'
text = "The cat sat gaeg cat" #text with two 'cat' occurrences
print(re.findall(pattern, text))  # ['cat', 'cat']

pattern = r"\d+" #pattern to match one or more digits
text = "Order 123 placed6622" #text with numbers
print(re.findall(pattern, text))  # ['123', '6622']

pattern = r"[A-Za-z]+"  #pattern to match words with only letters
text = "Hello 123 World" #text with words and numbers
print(re.findall(pattern, text))   # ['Hello', 'World']

pattern = r"[A-Za-z]+" #pattern to match words with only letters
text = "Hello 123 World gg9 ggus 1fa gg'g aagja!ga "
print(re.findall(pattern, text))   # ['Hello', 'World', 'gg', 'ggus', 'fa', 'gg', 'g', 'aagja', 'ga']

pattern = r"\d+\.\d+\.\d+\.\d+" #pattern to match an IP address
text = "Login from 192.168.0.1" #text with an IP address
print(re.findall(pattern, text))   # ['192.168.0.1']

pattern = r"for (?:invalid user )?(\S+) from" #searhing for username after 'for' and before 'from', optionally ignoring 'invalid user'
line = "Failed password for invalid user bob from 10.0.0.5" #line with 'invalid user'
print(re.search(pattern, line).group(1))   # 'bob'