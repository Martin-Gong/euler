# 19

sundays = 0
day = 2
for yr in range(1901, 2001):
    print(yr)
    for mon in range(1, 13):
        print(f'\t{mon}:{day}')
        if day == 0:
            sundays += 1
        if mon == 2:
            if yr % 4 == 0 and (yr % 100 != 0 or yr % 400 == 0):
                day = (day + 29) % 7
            else:
                day = (day + 28) % 7
        elif mon in (4, 6, 9, 11):
            day = (day + 30) % 7
        else:
            day = (day + 31) % 7

print(sundays)
