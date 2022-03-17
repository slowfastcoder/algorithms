#hw 2 - An Tran

def split_in_half(testString):
    numChars = len(testString)
    results = numChars
    firsthalf = ""
    secondhalf = ""


    if (numChars%2) == 0:
        #regularswap
        firsthalf = testString[0:(numChars // 2)]
        secondhalf = testString[(numChars // 2):numChars]
        results = str(secondhalf) + str(firsthalf)

    else:
        #start with one extra character longer
        firsthalf = testString[0:((numChars+1) // 2) ]
        secondhalf = testString[((numChars+1) // 2): numChars]
        results = secondhalf + firsthalf
    return results



print(split_in_half("bbbbbcaaaaa"))
print(split_in_half("bbbbbcaaaaax"))


def uniquechars(testString):
    #return true if it contains unique chars
    #return false if it has duplicate characters
    set01 = set()

    for f in testString:
        #print(f)
        set01.add(f)

    #for y in set01:
        #print(y)

    if len(testString) == len(set01):
        return True
    else:
        return False


if (uniquechars("abcc")):
    print("THere are no duplicate chars")
else:
    print("There are duplicate chars")