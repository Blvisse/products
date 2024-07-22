# a simple application that when called just returns the sum of two numbers

def quick_addition(first: int, second: int, third: int) -> int:
    print("This this is the result of {} + {} + {}".format(first, second, third))
    return first + second + third


if __name__ == '__main__':
    quick_addition(1, 2, 3)