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

part1()