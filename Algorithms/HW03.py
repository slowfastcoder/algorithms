'''
An Tran 3/23/22
Algorithm HW 3

Reverse a Statement
Build an algorithm that will print the given statement in reverse.
Example: Initial string = Everything is hard before it is easy
Reversed string = easy is it before hard is Everything

Permutations
Write a solution that will print all permutations of a string.
A permutation is an act of changing the arrangement of characters.
Example: String = ABC, Return {ABC, ACB, BAC, BCA, CBA, CAB}

Count Characters
Create a program that will count vowels and consonants in a string.
Example: String = “hello world”, Return {Vowels: 3, Consonants: 7}
'''

from itertools import permutations

def reverse_statement(statement):
    #testString = statement [::-1]
    newString = ""
    testString = list(statement.split(" "))
    testString.reverse()
    #for n in testString:
    #    print(n)

    #print(" ".join(testString))
    newString= (" ".join(testString))
    print(newString)
    return newString


def permutation_string(teststring):
    teststring = [''.join(p) for p in permutations(teststring)]
    #testPerm = permutations(['A', 'B', 'C'], 3)
    #for i in testPerm:
    #    print(i)

    #teststring = permutations(teststring, 3)
    for b in teststring:
        print(b)

def count_chars(testString):
    vowels = 0
    consonents = 0
    spaces = 0
    for n in testString:
        if n.upper() == 'A' or n.upper() == 'E' or n.upper() == 'I' or n.upper() == 'O' or n.upper() == 'U':
            vowels = vowels + 1
        elif n == ' ':
            #do nothing skip it, it's not a consonent
            spaces = spaces + 1
        else:
            consonents = consonents + 1
    print(f"vowels: {vowels} consonents: {consonents}")



stringP = "Everything is hard before it is easy"
reverse_statement(stringP)
permutation_string("ABC")
count_chars("Hello World")