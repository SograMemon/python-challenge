import os
import re

fileList = ["paragraph_1.txt", "paragraph_2.txt", "paragraph_3.txt"]

for file in fileList:
    filepath = os.path.join("Resources", file)
    outputPath = os.path.join("Analysis", "output_"+file)
    wordC= scentenceC= letterC = sentenceLen= wordLen =0
    with open(filepath, 'r') as txtfile:
        filereader= txtfile.read()
        #print(filereader)
        filereader.strip()
        scentenceC=filereader.count(".")

        wordList= re.split("[^a-zA-z]+", filereader.strip())
        wordC= len(wordList) - 1
        for word in wordList:
            #print(word)
            wordLen += len(word)
        letterC = round(wordLen/wordC, 1)

        sentenceList= re.split("(?<=[.!?]) +", filereader.strip())
        for sentence in sentenceList:
            sentenceLen += sentence.strip().count(" ")+1
        sentenceLen= round(sentenceLen/scentenceC, 1)
    
    writerTxtFile = open(outputPath, 'w')
    writerTxtFile.write(f"\n Paragraph Analysis for {file} \n ---------------------------------------- \n Approximate Word Count: {wordC} \n Approximate Sentence Count: {scentenceC} \n Average Letter Count: {letterC} \n Average Sentence Length: {sentenceLen}") 
    writerTxtFile.close()

    with open(outputPath, 'r') as filereader:
        reader= filereader.read()
        print(reader)
