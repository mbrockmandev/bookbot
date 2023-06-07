def count_letters(string: str):
    my_dict = {}
    for c in string:
        c_lowered = c.lower()
        if c_lowered.isalpha():
            if c_lowered in my_dict:
                my_dict[c_lowered] += 1
            else:
                my_dict[c_lowered] = 1
    output = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
    for k, v in output:
        print(f"the '{k}' character was found {v} times")


with open("frankenstein.txt") as f:
    file_contents = f.read()

print(file_contents)
words = file_contents.split()
print(f"{len(words)} words")

count_letters(file_contents)
