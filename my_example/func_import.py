def LongestWord(sen):
    sen=sen.split()
    sen=max(sen,key=len)
    return sen



# keep this function call here
print(LongestWord('To największe slowo i wyd!!!!!!!e%*#'))
