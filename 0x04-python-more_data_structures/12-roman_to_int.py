#!/usr/bin/python3

def roman_to_int(roman_number):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    for i in range(len(roman_number)):
        if i > 0 and roman[roman_number[i]] > roman[roman_number[i - 1]]:
            num += roman[roman_number[i]] - 2 * roman[roman_number[i - 1]]
        else:
            num += roman[roman_number[i]]
    return num
