myDict = {
    "dabba": "box",
    "pankha":"fan",
    "vastu":"item"
}
print("options are ",myDict.keys())
a= input("enter the hindi word\n")
print("the meaning of your word is: ",myDict.get(a))