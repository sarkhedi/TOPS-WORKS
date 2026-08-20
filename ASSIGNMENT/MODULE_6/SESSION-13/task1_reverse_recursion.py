def reverse_string(s):

    if s == "":
        return ""

  
    return reverse_string(s[1:]) + s[0]

text = "hello"

result = reverse_string(text)

print("Original String:", text)
print("Reversed String:", result)