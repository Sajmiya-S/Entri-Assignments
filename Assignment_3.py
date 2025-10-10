# Write a function has_unique_chars(s) that checks whether a given string contains all unique characters.

def has_unique_chars(s):
    has_unique_char = True
    for i in range(0,len(s)):
        for j in range(1,len(s)):
            if i != j and s[i] == s[j]:
                has_unique_char = False
    return has_unique_char

s = input("\nEnter a string: ")
print(has_unique_chars(s))