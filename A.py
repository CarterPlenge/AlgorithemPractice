# Fibonacci Numbering System
# fundamentally binary but not binary as we know it
# each place value is valued fibonaccily. (def a real word) ie: 1, 1, 2, 3, 5, 8 ect
# Given a number find how many repretitions of that number exist.
# ie: 1101 = (3+2+0+1) = 6  and  10010 = (5+0+0+1+0) = 6

# input
# each number on its own line
# all values fit in 16 bit int
# exit case 0

# thoughts
# 

def defibb(num:str):
    num = num[::-1]
    val1 = 1
    val2 = 0
    total = 0
    for digit in num:
        val3 = val2 + val1
        if digit == "1":
            total += val3
        val1 = val2
        val2 = val3
    return total

# brute force cuz im tired and my head hurts
def brute_force(num:str, value:int):
    length = len(num)
    trueCases = 0 
    testCase = ["0"]*length
    for x in range(length):
        testCase[x] = "1"
        print(value, "=", defibb("".join(testCase)))
        if value == defibb("".join(testCase)):
            trueCases += 1
    return trueCases
# yeah i fucked up the implementation but done for now i need to eat

get_number = "11010"

# get_number = input()

# while get_number != 0:
    
#     get_number = input()

decimalValue = defibb(get_number)
trueCaseCount = brute_force(get_number, decimalValue)

print(f"Case num: {decimalValue} {trueCaseCount}")