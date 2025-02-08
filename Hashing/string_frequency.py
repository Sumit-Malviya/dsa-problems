"""
my_string = aabzqhrttt

count frequency of element 
given in lst = ["a", "z", "q", "i", "j"]

constraint: my_string[i] is between a to z
"""

my_string = "aabzqhrttt"
lst = ["a", "z", "q", "i", "j"]
d = {}
for ch in my_string:
    d[ch] = d.get(ch, 0) + 1

for ch in lst:
    print(d.get(ch, 0))
