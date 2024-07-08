while True:
    try:
        day = round(float(input("t= ")))

        if 1 <= day <= 31:
            print(f"\nJanuary {day}")
            break
        elif 32 <= day <= 59:
            date = day - 31
            print(f"\nFebruary {date}")
            break
        elif 60 <= day <= 90:
            date = day - 59
            print(f"\nMarch {date}")
            break
        elif 91 <= day <= 120:
            date = day - 90
            print(f"\nApril {date}")
            break
        elif 121 <= day <= 151:
            date = day - 120
            print(f"\nMay {date}")
            break
        elif 152 <= day <= 181:
            date = day - 151
            print(f"\nJune {date}")
            break
        elif 182 <= day <= 212:
            date = day - 181
            print(f"\nJuly {date}")
            break
        elif 213 <= day <= 243:
            date = day - 212
            print(f"\nAugust {date}")
            break
        elif 244 <= day <= 273:
            date = day - 243
            print(f"\nSeptember {date}")
            break
        elif 274 <= day <= 304:
            date = day - 273
            print(f"\nOctober {date}")
            break
        elif 305 <= day <= 334:
            date = day - 304
            print(f"\nNovember {date}")
            break
        elif 335 <= day <= 365:
            date = day - 334
            print(f"\nDecember {date}")
            break
        else:
            print("\nPLEASE INPUT A NUMBER FROM 1 TO 365 ONLYY!!!!!!!!!!!!!!")
    except ValueError:
        print("\nNumber only Please")
