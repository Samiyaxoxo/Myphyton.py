
def count_vowels(s):
    vowels = "aeiou"
    count = 0

    for char in s:
        if char in vowels:
            count += 1
    return count
input_string = "Hello, how are you?"
vowel_count = count_vowels(input_string)
print(f"Number of vowels: {vowel_count}")
