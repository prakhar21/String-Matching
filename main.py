import sys
import argparse
import math
import nltk

_CONSTANT = 101

# Hash Function Logic
def getHash(s):
    H = 0 
    while i < len(s):
        H += ord(s[i])*math.pow(_CONSTANT,i)
    return H

def getMatch(sHashed, s, l):
    hashV = []
    for i in xrange(len(s)-l+1):
	if i != 0:
	    H += ((hashV[i-1] - ord(s[i-1])) / l) + ord(s[i+l])*math.pow(_CONSTANT,l-1)
	else:
	    for j in xrange(len(s[i:i+l])):
	        H += ord(s[i:i+l][j])*math.pow(_CONSTANT,j)
	

        # Stopping Condition
	if H == sHashed:
	    return 'Found'
	else:
            pass
        
        # Required for next level hash comparison
        # Rolling Window hash function Implentation
	hashV.append(H)
    
    return 'Not Found'


def runKarp(s1, s2):
    if len(s1) < len(s2):
	s1Hased = getHash(s1)
        # Slide over s2 with window length of `len(s1)`
        m =  getMatch(s1Hashed, s2, len(s1))

    elif len(s2) < len(s1):
	s2Hashed = getHash(s2)
    else:
	# Random selection
        # Let's choose s1
	s1Hashed = getHash(s1)
    return m

# Calculate the Hamming Distance between 2 Strings
# s1 and s2
# s2 and s2 must have same length
def runHamming(s1, s2):
    distance = 0
    if len(s1) == len(s2):
        for i, j in zip(s1,s2):
	    if i != j:
	        distance += 1
	    else:
		pass    
    else:
	return 'String should be of same length for this algorithms'
    
    return distance

def runLaven(s1, s2):
    pass

def runAffineGap(s1, s2):
    pass


def main(algo, s1, s2):
    
    if algo == 'karp':
        result = runKarp(s1, s2)
	if result == 'Found':
            print '\nSubstring found\n'
	else:
            print '\nSubstring not found\n'
    elif algo == 'hamming':
	result = runHamming(s1, s2)
	if type(result) == int:
	    print '\nSubstitutions needed are: ' + str(result) + '\n'
	else:
	    print result
    elif algo == 'laven':
	runLaven(s1, s2)
    elif algo == 'affinegap':
	runAffineGap(s1, s2)

    sys.exit()

def parseArguments():
    parser = argparse.ArgumentParser(description='String Matching')
    parser.add_argument('-s1', action="store", dest="s1")
    parser.add_argument('-s2', action="store", dest="s2")
    parser.add_argument('-algo', action="store", dest="algo")
    val = parser.parse_args()		        
    return val.algo, val.s1, val.s2


if __name__=='__main__':
    algo, s1, s2 = parseArguments() 
    main(algo, s1, s2)
