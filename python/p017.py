# 17

wordCounts = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    1000: 'onethousand'
}

def countChars (x: int) -> str:
    try:
        return wordCounts[x]
    except:
        if x < 100:
            if x % 10 == 0:
                return wordCounts[x - x % 10]
            else:
                return wordCounts[x - x % 10] + wordCounts[x % 10]
        else:
            if x % 100 == 0:
                return wordCounts[int(x / 100)] + 'hundred'
            else:
                return wordCounts[int(x / 100)] + 'hundred' + 'and' + countChars(x % 100)

s = ''
for i in range(1000):
    s += countChars(i + 1)

print(len(s))
