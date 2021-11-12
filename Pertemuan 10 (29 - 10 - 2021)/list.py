myList = ["Aku", "Suka", "Kamu"]

# kalimat = " ".join(myList)
myList2 = myList.copy()
myList.pop()


print(id(myList))
print(id(myList2))