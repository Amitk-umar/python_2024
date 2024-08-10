name = "amit-kumar"
print(len(name)) # '10'

print(name.endswith("onar"))  # 'false'
print(name.startswith("Ami")) # 'true'
print(name.capitalize())
text = "Hello, World!"
print(text.lower())  # Output: "hello, world!"
text = "Hello, World!"
print(text.upper())  # Output: "HELLO, WORLD!"
text = "  Hello, World!  "
print(text.strip())  # Output: "Hello, World!"
text = "Hello, World!"
print(text.replace("World", "Python"))  # Output: "Hello, Python!"
text = "Hello, World!"
words = text.split(",")
print(words)  # Output: ["Hello", "World!"]
words = ["Hello", "World"]
print(", ".join(words))  # Output: "Hello, World"
text = "Hello, World!"
print(text.find("World"))  # Output: 7
text = "Hello, {}!"
print(text.format("World"))  # Output: "Hello, World!"