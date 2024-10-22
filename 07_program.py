data = {
  "roll_no": 1, 
  "name": "abc", 
  "class": "Btech2b"
}

print("Dictionary is:",data)
print("Name is:",data["name"])
data["age"] = 18
print("Updated dictionary is:",data)

del data["age"]
print("Updated dictionary is:",data)
print("length is:",len(data))
