
#!/usr/bin/python -tt
import sys
def word_counts(filename):
    f = open(filename, 'rU')
    online_file = f.read()
    online_file.lower()
    word_counts = {}
    for char in online_file:
        if(char in word_counts):
            word_counts[char]+=1
        else:
            word_counts[char] =1
    return word_counts



