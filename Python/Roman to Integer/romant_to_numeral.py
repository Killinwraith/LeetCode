input = input("Enter roman numeral to convert: ")

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        if "IV" in s:
            x = s.index("IV")
            total += 4
            s = s[:x] + s[x+2:]

        if "IX" in s:
            x = s.index("IX")
            total += 9
            s = s[:x] + s[x+2:]

        if "XL" in s:
            x = s.index("XL")
            total += 40
            s = s[:x] + s[x+2:]

        if "XC" in s:
            x = s.index("XC")
            total += 90
            s = s[:x] + s[x+2:]

        if "CD" in s: 
            x = s.index("CD")
            total += 400
            s = s[:x] + s[x+2:]

        if "CM" in s:
            x = s.index("CM")
            total += 900
            s = s[:x] + s[x+2:]

        for letter in s:
            if letter == "I":
                total += 1
            elif letter == "V":
                total += 5
            elif letter == "X":
                total += 10
            elif letter == "L":
                total += 50
            elif letter == "C":
                total += 100
            elif letter == "D":
                total += 500
            elif letter == "M":
                total += 1000

        return(total)
                
print(romanToInt(input))
