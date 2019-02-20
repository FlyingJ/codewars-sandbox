#!/usr/bin/env python

# solution for https://www.codewars.com/kata/decode-the-morse-code-for-real/train/python

import copy
import random
import re
import string

from morse_code import MORSE_CODE

def decodeBitsAdvanced(bits):
    morseCode = ''
    # strip leading, trailing 0s from bit-stream
    bits = bits.strip('0')
    # build bit-string to morse element mapping
    # using k-means clustering of high-, low-signal timings
    bitMapping = getBitMapping(bits)
    # and map bit-string elements to morse elements
    # >>> re.findall('0+|1+', superFreep.strip('0'))
    # ['11', '0', '11', '0', '1', '00', '111', '00000', '11', '000000', '111111', '0', '1', '00', '11111', '00', '111111', '00000000000', '111', '0', '11111111', '0', '11111', '0', '11111', '000000', '1', '0', '11', '000', '111111', '00000', '11111', '00', '111', '0', '11', '00000', '1']
    for bitString in re.findall('0+|1+', bits):
        morseCode += bitMapping[translateBitString(bitString)]
    return morseCode

def getBitMapping(bits):
    # TODO: handle short messages (do not necessarily recieve every morse element)
    #       - empty message
    #       - single element
    #       - single character
    # RECALL:
    #       - 1:3 as '.':'-'
    #       - 1:3:7 as '':' ':'   '
    bitMapping = {}

    highs = sorted([len(token) for token in re.findall('1+', bits)])
    highClusters = kMeans1D(highs, 2)
    for element in highClusters[0]:
        bitMapping[(1, element)] = '.'
    for element in highClusters[1]:
        bitMapping[(1, element)] = '-'

    lows = sorted([len(token) for token in re.findall('0+', bits)])
    lowClusters = kMeans1D(lows, 3)
    for element in lowClusters[0]:
        bitMapping[(0, element)] = ''
    for element in lowClusters[1]:
        bitMapping[(0, element)] = ' '
    for element in lowClusters[2]:
        bitMapping[(0, element)] = '   '

    return bitMapping

def kMeans1D(data, k, maxIterations = 1000):
    # being reproducible for now
    random.seed(1)
    
    # initial centroids
    centroids = [random.randint(min(data), max(data)) for i in xrange(k)]
    centroids.sort()
    
    # repeat assignment of elements and update of cluster means until
    # i) groupings no longer vary or
    # ii) maximum iterations reached
    iteration = 1
    previousGroups = [[] for i in xrange(k)]
    while iteration < maxIterations:
        # assignment of elements to centroid clusters
        groups = [[] for i in xrange(k)]
        for datum in data:
            distances = [abs(centroid - datum) for centroid in centroids]
            groups[distances.index(min(distances))].append(datum)
        
        # break out if groupings have not changed
        if groups == previousGroups:
            return groups
        
        # otherwise
        # update centroids using new groupings
        centroids = [mean(group) for group in groups]
        # deep copy groupings to previousGroupings for delta check in next iteration
        previousGroups = copy.deepcopy(groups)
        # and increment iteration counter
        iteration += 1

def mean(data):
    sum = 0
    for datum in data:
        sum += datum
    return sum/len(data)

def translateBitString(bits):
    return (int(bits[0]), len(bits))

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

if __name__ == '__main__':
    bits = '0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000'

    print "Testing mean()..."
    testAndPrint(mean([0, 1, 2]), 1)
    testAndPrint(mean([0, -1, 1, -2, 2]), 0)

    print "Testing kMeans1D..."
    testAndPrint(kMeans1D([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 5, 5, 5, 5, 6, 6, 8, 11], 3), [[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3], [5, 5, 5, 5, 6, 6, 8], [11]])

    print "Testing getBitMapping..."
    testAndPrint(getBitMapping(bits.strip('0')), {(1, 2): '.', (0, 1): '', (1, 3): '.', (0, 6): ' ', (0, 11): '   ', (0, 2): '', (1, 5): '-', (1, 8): '-', (1, 6): '-', (0, 5): ' ', (0, 3): '', (1, 1): '.'})
    
    print "Testing translateBitString..."
    testAndPrint(translateBitString('11111'), (1, 5))

    print "Testing decodeBitsAdvanced..."
    testAndPrint(decodeBitsAdvanced(bits), '.... . -.--   .--- ..- -.. .')

    print "Testing decodeMorseWord..."
    testAndPrint(decodeMorseWord('.... . -.--'), 'HEY')

    print "Testing decodeMorse..."
    testAndPrint(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
    print "Testing composition of decodeMorse and decodeBitsAdvanced..."
    testAndPrint(decodeMorse(decodeBitsAdvanced(bits)), 'HEY JUDE')

