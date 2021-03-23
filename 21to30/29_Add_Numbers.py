# DomirScire

def sum_numbers(numbers):
    return sum(int(number)
               for number in numbers.split()
               if number.isdigit())

if __name__ == "__main__":
    print(sum_numbers('1 2 3 a b c 4'))
