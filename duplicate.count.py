#!/usr/bin/python

def duplicate_count(text):
    # Your code goes here
    text = text.lower()
    characterCount = {}
    for character in text:
        characterCount[character] = text.count(character)
    duplicateCharacters = [x for x in characterCount.keys() if characterCount[x] > 1]
    return len(duplicateCharacters)

if __name__ == '__main__':
    # test.assert_equals(duplicate_count("abcde"), 0)
    # test.assert_equals(duplicate_count("abcdea"), 1)
    # test.assert_equals(duplicate_count("indivisibility"), 1)
    print duplicate_count("abcde")
    print duplicate_count("abcdea")
    print duplicate_count("indivisibility")