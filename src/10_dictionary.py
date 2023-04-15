myDict = {
    "mother": "who loves you the most",
    "sister": "who always support you",
    "anotherdict": {'family' : 'love'}
}
'''print(myDict['mother'])
print(myDict['sister'])
print(myDict['anotherdict']['family'])'''
'''print(myDict.keys())
print(myDict.values ())
print(myDict.items())'''
updateDict = {
    "friends": "closest one",
    "me": "happy",
    "mother" : "love"
}
myDict.update(updateDict)
print(myDict)
print(myDict.get("mother2")) #return none as mother2 is not present in the dictionary
#print(myDict["mother"]) #throws an error as mother is not present in the dictionary
