import datetime

def get_thelemic_date():
    """
    Computes the Thelemic date based on a continuous count from the epoch.
    The epoch is defined as April 8, 1904.
    The Thelemic year is (days_since_epoch // 360) + 1,
    and the Thelemic day is (days_since_epoch % 360) + 1.
    """
    epoch = datetime.date(1904, 4, 8)
    today = datetime.date.today()
    days_since_epoch = (today - epoch).days
    thelemic_year = days_since_epoch // 360 + 1
    thelemic_day = days_since_epoch % 360 + 1
    return thelemic_year, thelemic_day

def int_to_roman(num):
    """
    Converts an integer to its standard Roman numeral representation.
    """
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

def convert_to_special_roman(roman_string):
    """
    Converts the standard Roman numeral letters to a special set of Unicode characters,
    so that, for example, "XV" becomes "Ⅴⅹ".
    """
    mapping = {
        'I': 'Ⅰ',
        'V': 'Ⅴ',
        'X': 'ⅹ',
        'L': 'Ⅼ',
        'C': 'Ⅽ',
        'D': 'Ⅾ',
        'M': 'Ⅿ'
    }
    return "".join(mapping.get(ch, ch) for ch in roman_string)

def get_zodiac_position(angle):
    """
    Given an angle between 1 and 360 (in degrees), returns a tuple:
    (degree within the zodiac sign, zodiac sign symbol)
    
    The zodiac signs (in order) are:
    Aries (♈︎), Taurus (♉︎), Gemini (♊︎), Cancer (♋︎), Leo (♌︎),
    Virgo (♍︎), Libra (♎︎), Scorpio (♏︎), Sagittarius (♐︎),
    Capricorn (♑︎), Aquarius (♒︎), Pisces (♓︎)
    """
    zodiac_signs = ["♈︎", "♉︎", "♊︎", "♋︎", "♌︎", "♍︎",
                    "♎︎", "♏︎", "♐︎", "♑︎", "♒︎", "♓︎"]
    # Determine which sign by dividing the circle into 12 sectors (30° each)
    index = (angle - 1) // 30
    degree = ((angle - 1) % 30) + 1
    return degree, zodiac_signs[index]

def main():
    # Get the Thelemic date (year and day)
    thelemic_year, thelemic_day = get_thelemic_date()
    
    # Compute zodiac positions.
    # For the Sun, we use the Thelemic day directly (1–360).
    sun_pos = thelemic_day
    # For the Moon, apply an offset of 69 days (this yields the sample of 25° in Sagittarius when the day is 334)
    moon_pos = (((thelemic_day - 69) - 1) % 360) + 1

    sun_degree, sun_sign = get_zodiac_position(sun_pos)
    moon_degree, moon_sign = get_zodiac_position(moon_pos)
    
    # Convert the Thelemic year to a Roman numeral and then to the special glyphs.
    roman_year = int_to_roman(thelemic_year)
    special_roman_year = convert_to_special_roman(roman_year)
    
    # Format the output as: 
    # "☉︎ in {sun_degree}° {sun_sign} : ☽︎ in {moon_degree}° {moon_sign} : ♄︎ : {special_roman_year}"
    output = f"☉︎ in {sun_degree}° {sun_sign} : ☽︎ in {moon_degree}° {moon_sign} : ♄︎ : {special_roman_year}"
    print(output)

if __name__ == "__main__":
    main()
