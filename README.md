# FizzBuzz implementation for Corndel Bootcamp 2022
Usage: `python fizzbuzz.py` for fizzbuzz with default options (default being all rules enabled)

For customised setup, use `python fizzbuzz.py <max_iters> <rules>` e.g. `python fizzbuzz.py 255 3 7 11` would run fizzbuzz up to 255 with the rules for 3, 7, and 11 enabled, but others disabled

## Possible rules
- If a number is a multiple of 3, print 'Fizz' instead of the number
- If a number is a multiple of 5, print 'Buzz' instead of the number. For numbers that have multiples of three, append 'Buzz', (e.g. 3*5 = 15: "FizzBuzz)
- If a number is a multiple of 7, print "Bang" instead of the number. For numbers which are multiples of seven and three / five, append Bang to what you'd have printed anyway. (E.g. 3 * 7 = 21: "FizzBang").
- If a number is a multiple of 11, print "Bong" instead of the number. Do not print anything else in these cases. (E.g. 3 * 11 = 33: "Bong")
- If a number is a multiple of 13, print "Fezz" instead of the number. For multiples of most other numbers, the Fezz goes immediately in front of the first thing beginning with B, or at the end if there are none. (E.g. 5 * 13 = 65: "FezzBuzz", 3 * 5 * 13 = 195: "FizzFezzBuzz"). Note that Fezz should be printed even if Bong is also present (E.g. 11 * 13 = 143: "FezzBong")

If a number is a multiple of 17, reverse the order in which any fizzes, buzzes, bangs etc. are printed. (E.g. 3 * 5 * 17 = 255: "BuzzFizz")