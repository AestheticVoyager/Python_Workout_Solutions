# DomirScire

def how_many_different_numbers(numbers):
    unique_numbers = set(numbers)
    return len(unique_numbers)

if __name__ == "__main__":
    print(how_many_different_numbers([1,2,3,1,2,3,4,1]))
