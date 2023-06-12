def count_vowels(word):
    vowels = "aeiouyаеиоуыяюэ"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    words = poem.split()
    syllables = [count_vowels(word) for word in words]
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Enter your poem: ")
print(check_rhythm(poem))