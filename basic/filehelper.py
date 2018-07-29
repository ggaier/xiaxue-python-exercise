
#!/usr/bin/python -tt
import sys
def word_counts(filename):
    f = open(filename, 'rU')
    #不要一次性读完一整个文件, 一次读一行
    online_file = f.read()
    online_file.lower()
    word_counts = {}
    for char in online_file:
        if(char in word_counts):
            word_counts[char]+=1
        else:
            word_counts[char] =1
    f.close()
    return word_counts



