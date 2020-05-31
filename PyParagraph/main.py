import os
import re

filepath = os.path.join("Resources", "paragraph_3.txt")
wordC= scentenceC= letterC = sentenceLen= wordLen =0
with open(filepath, 'r') as txtfile:
    filereader= txtfile.read()
    #print(filereader)
    filereader.strip()
    scentenceC=filereader.count(".")

    wordList= re.split("[^a-zA-z]+", filereader.strip())
    wordC= len(wordList)- 1
    for word in wordList:
        #print(word)
        wordLen += len(word)
    letterC = round(wordLen/wordC, 1)
    
    sentenceList= re.split("(?<=[.!?]) +", filereader.strip())
    for sentence in sentenceList:
        sentenceLen += sentence.strip().count(" ")+1
    sentenceLen= round(sentenceLen/scentenceC, 1)
    

print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {wordC}")
print(f"Approximate Sentence Count: {scentenceC}")
print(f"Average Letter Count: {letterC}")
print(f"Average Sentence Length: {sentenceLen}")