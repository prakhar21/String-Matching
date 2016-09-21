import sys
import argparse



def runKarp(s1, s2):
    pass


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
        runKarp(s1, s2)
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
