from itertools import permutations
import Dictionary as d
import os

def valid_input_letters(inp):

    if (len(inp) < 1):

        return False

    for i in inp:

        if ((not (i.isalpha())) and (not (i == ','))):

            return False

    if (inp[-1] == ','):

        return False
    
    for i in inp.split(","):

        if (len(i) != 1):

            return False
    
    return True

def get_letters():

    print("Enter given letters separated by commas.")
    print("Examples: [A,b,C,e] or [Z,y,G,o,G].")
    l = input()
    print()

    while(not valid_input_letters(l)):

        print("Input Error! Try Again.")
        print("Enter given letters separated by commas.")
        print("Examples: [A,b,C,e] or [Z,y,G,o,G].")
        l = input()
        print()

    letters = [l.lower() for l in l.split(",")]
    return letters

def valid_input_numbers(inp):

    if (len(inp) < 1):

        return False

    for i in inp:

        if ((not (i.isdigit())) and (not (i == ','))):

            return False

    if (inp[-1] == ','):

        return False
    
    return True

def get_numbers():

    print("Enter possible sizes separated by commas (min 3).")
    print("Examples: [3,4,5] or [8,4,5,2].")
    nums = input()
    print()

    while(not valid_input_numbers(nums)):

        print("Input Error! Try Again.")
        print("Enter possible sizes separated by commas (min 3).")
        print("Examples: [3,4,5] or [8,4,5,2].")
        nums = input()
        print()

    numbers = [int(n) for n in nums.split(",")]
    numbers.sort(reverse=True)

    return numbers

print("Word Game Solver v0.1")

inp = ""

while(inp != "Q" and inp != "q"):

    letters = get_letters()
    numbers = get_numbers()

    for n in list(numbers):
        
        print("Words with " , n , "letters:")
        
        perm = permutations(letters, n)
        perm = set(["".join(p) for p in perm if (d.check("".join(p)))])
        perm = list(perm)
        perm.sort()
        for p in perm:
            
            print(p)

        print()

    inp = input("Type Q to exit or any other key to give new answers -> ")
    os.system('cls')