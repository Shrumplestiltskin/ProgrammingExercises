#!/usr/bin/python
#Project Euler #17

ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['onehundred', 'twohundred', 'threehundred', 'fourhundred', 'fivehundred', 'sixhundred', 'sevenhundred', 'eighthundred', 'ninehundred']
hundreds_and = ['onehundredand', 'twohundredand', 'threehundredand', 'fourhundredand', 'fivehundredand', 'sixhundredand', 'sevenhundredand', 'eighthundredand', 'ninehundredand']
thousands = ['onethousand']

letter_count = 0
#cycle through hundreds + tens + ones
for x in range(len(hundreds_and)):
    for y in range(len(tens)):
        for z in range(len(ones)):
            letter_count += len(hundreds_and[x]) + len(tens[y]) + len(ones[z])
#cycle through hundreds + tens
for x in range(len(hundreds_and)):
    for y in range(len(tens)):
        letter_count += len(hundreds_and[x]) + len(tens[y])
#cycle through hundreds + teens
for x in range(len(hundreds_and)):
    for y in range(len(teens)):
        letter_count += len(hundreds_and[x]) + len(teens[y])
#cycle through hundreds + ones
for x in range(len(hundreds_and)):
    for y in range(len(ones)):
        letter_count += len(hundreds_and[x]) + len(ones[y])
#cycle through hundreds
for x in range(len(hundreds)):
    letter_count += len(hundreds[x])
#cycle through tens + ones
for x in range(len(tens)):
    for y in range(len(ones)):
        letter_count += len(tens[x]) + len(ones[y])
#cycle through tens
for x in range(len(tens)):
    letter_count += len(tens[x])
#cycle through teens
for x in range(len(teens)):
    letter_count += len(teens[x])
#cycle through ones
for x in range(len(ones)):
    letter_count += len(ones[x])
#cycle through thousands
for x in range(len(thousands)):
    letter_count += len(thousands[x])
print(letter_count)
