# DomirScire

def join_numbers(numbers):
    return ','.join(str(number) for number in numbers)

if __name__ == "__main__":
    print(join_numbers(range(15)))
