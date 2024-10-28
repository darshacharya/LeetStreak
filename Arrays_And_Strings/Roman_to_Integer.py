"""Roman to Integer"""
roman = { "I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000 }
# print(roman["I"]+roman["M"])
s = "MCMXCIV"
j = len(s)-1
# print(j)
result = 0
rom = ["I","V","X","L","C","D","M"]
if s[j] in rom:
    result+=roman["I"]