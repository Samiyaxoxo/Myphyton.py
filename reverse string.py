def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  
    return reversed_str
string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
print("samiya,23")
