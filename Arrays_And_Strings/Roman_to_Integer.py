"""Roman to Integer Approach : (1)"""
"""TC:O(n) """
"""SC:O(1) """
s = "III"

def roman_to_int(s):
    # dictiory of roman value to int
    roman = { "I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000 }

    j = len(s)-1 # to access from last index

    result = 0
    rom = ["I","V","X","L","C","D","M"] #to check with index values

    result+=roman[s[j]] #adding last value directly
    #iterate all the values from last till j is grater than 0
    while j>0:
        if rom.index(s[j])>rom.index(s[j-1]):
            result -= roman[s[j-1]]
        else:
            result+= roman[s[j-1]]
        j-=1
    return result

print(roman_to_int(s))

"""Roman to Integer Approach : (2)"""
"""TC:O(n) """
"""SC:O(1) """
def roman_to_int_(s):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    result = 0
    prev_value = 0  # Track the value of the previous numeral

    for char in reversed(s):
        current_value = roman[char]
        if current_value < prev_value:
            result -= current_value  # Subtract if the current value is less than the previous
        else:
            result += current_value  # Otherwise, add the current value
        prev_value = current_value  # Update the previous value for the next iteration

    return result

print(roman_to_int_(s))