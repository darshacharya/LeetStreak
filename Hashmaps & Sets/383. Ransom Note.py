"""383. Ransom Note"""

ransomNote = "bca"
magazine = "bac"
def canConstruct(ransomNote, magazine):
    for char in ransomNote:
        if char not in magazine:
            return False
        else:
            magazine = magazine.replace(char, "", 1)
    return True


print(canConstruct(ransomNote,magazine))