#!/usr/bin/env python

import string
from morse_code import MORSE_CODE

def decodeBits(bits):
    # strip leading, trailing zeroes from input "stream"
    bits = bits.strip('0')
    # infer time unit from input "stream"
    timeUnit = getTimeUnit(bits)
    # translate bit "stream" to Morse code and return
    return translateBits(bits, timeUnit)

def getTimeUnit(bits):
    # collect high signal timing data from the bit "stream"
    highDurations = [len(token) for token in bits.split('0') if len(token) > 0]
    lowDurations = [len(token) for token in bits.split('1') if len(token) > 0]

    durations = highDurations + lowDurations

    # collect duration frequencies
    durationFrequencies = {}
    for duration in durations:
        try:
            durationFrequencies[duration] += 1
        except KeyError:
            durationFrequencies[duration] = 1

    # as a first pass, get the two most frequent durations and keep the smaller
    return min([x[0] for x in sorted([(key, durationFrequencies[key]) for key in durationFrequencies.keys()], key = lambda a: a[1], reverse = True)[:2]])

def translateBits(bits, timeUnit):
    bits = bits.replace('1' * 3 * timeUnit, '-')
    bits = bits.replace('1' * 1 * timeUnit, '.')
    bits = bits.replace('0' * 7 * timeUnit, '   ')
    bits = bits.replace('0' * 3 * timeUnit, ' ')
    bits = bits.replace('0' * 1 * timeUnit, '')
    
    return bits

def decodeMorse(morseCode):
    # tokenize encoded string on word boundaries and have individual words decoded
    components = [decodeMorseWord(codeWord) for codeWord in morseCode.strip().split('   ')]
    # return decoded words as space-separated string
    return ' '.join(components)

def decodeMorseWord(morseCodeWord):
    # tokenize encoded word and translate resulting encoded characters
    # return the decoded characters as a single string
    return ''.join([MORSE_CODE[codeCharacter] for codeCharacter in morseCodeWord.split(' ')])
    
def testAndPrint(got, expected):
    result = 'FAIL'
    if got == expected:
        result = 'PASS'
    print "[%s]: got %s, expected %s" % (result, got, expected)

if __name__ == "__main__":
    sample = '00000000000110011001100110000001100000011111100110011111100111111000000000000001100111111001111110011111100000011001100111111000000111111001100110000001100000000000000000000000'
    testAndPrint(decodeMorse(decodeBits(sample)), 'HEY JUDE')
    testAndPrint(decodeMorse(decodeBits('...---...')), 'SOS')















