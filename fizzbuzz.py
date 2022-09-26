from curses.ascii import isdigit
import sys


#simple fizzbuzz implementation
def part1():
    for counter in range(1,101):
        output = counter
        if counter % 15 == 0:
            output = 'FizzBuzz'
        elif counter % 3 == 0:
            output = 'Fizz'
        elif counter % 5 == 0:
            output = 'Buzz'
        print(output)

def part2(MAX_ITERS, THREE, FIVE, SEVEN, ELEVEN, THIRTEEN, SEVENTEEN):
    for counter in range(1,MAX_ITERS):
        output = []
        if counter % 3 == 0 and THREE:
            output.append('Fizz')
        if counter % 5 == 0 and FIVE:
            output.append('Buzz')
        if counter % 7 == 0 and SEVEN:
            output.append('Bang')
        if counter % 11 == 0 and ELEVEN:
            output = ['Bong']
        if counter % 13 == 0 and THIRTEEN:
            new_output = ['Fezz']
            new_output.extend(output)
            output = new_output
        if counter % 17 == 0 and output != [] and SEVENTEEN:
            output.reverse()
        if output == []:
            output = [str(counter)]
        text_out = ''
        for o in output:
            text_out += o
        print(counter, text_out)

def arg_error():
    print('Usage: ./fizzbuzz.py <max number> <enable/disable rules for 3,5,7,11,13,17>')
    print('e.g. ./fizzbuzz.py 100 3 5 7 runs fizzbuzz up to 100 with 3 5 7 rules enabled and others disabled')
    exit()

def main():
    MAX_ITERS = 256
    THREE = False
    FIVE = False
    SEVEN = False
    ELEVEN = False
    THIRTEEN = False
    SEVENTEEN = False

    if len(sys.argv) > 1:
        if not sys.argv[1].isdigit():
            arg_error()
        else:
            MAX_ITERS = int(sys.argv[1]) + 1
        for arg in sys.argv[2:]:
                if not arg.isdigit():
                    arg_error()
                else:
                    if (arg == '3'):
                        THREE = True
                    elif (arg == '5'):
                        FIVE = True
                    elif (arg == '7'):
                        SEVEN = True
                    elif (arg == '11'):
                        ELEVEN = True
                    elif (arg == '13'):
                        THIRTEEN = True
                    elif (arg == '17'):
                        SEVENTEEN = True
                    else:
                        arg_error()
    else:
        THREE = True
        FIVE = True
        SEVEN = True
        ELEVEN = True
        THIRTEEN = True
        SEVENTEEN = True
    # part1()
    part2(MAX_ITERS, THREE, FIVE, SEVEN, ELEVEN, THIRTEEN, SEVENTEEN)


main()