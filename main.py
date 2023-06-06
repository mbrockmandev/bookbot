print("Hello world!")

with open("frankenstein.txt") as f:
    file_contents = f.read()

print(file_contents)
words = file_contents.split()
print(f"{len(words)} words")
