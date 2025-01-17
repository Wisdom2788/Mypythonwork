import math

class Kata:

    staticmethod
    def task_one(number):
        return number % 2 == 0

    staticmethod
    def task_two(number):
        return number / number == 1

    staticmethod
    def task_three(first_number, second_number):
        return abs(first_number - second_number)

    staticmethod
    def task_four(first_integer, second_integer):
        if second_integer == 0:
            return 0
        else:
            return first_integer / second_integer

    staticmethod
    def task_five(numbers):
        counter = 0
        for counting in range(1, numbers + 1):
            if numbers % counting == 0:
                counter += 1
        return counter

    staticmethod
    def task_six(number):
        get_the_square = int(math.sqrt(number))
        return get_the_square * get_the_square == number

    staticmethod
    def task_eight(number):
        if number == 0 or number == 1:
            return 1
        else:
            total = 1
            for j in range(2, number + 1):
                total *= j
            return total

    staticmethod
    def task_nine(number):
        return number * number


if __name__ == "__main__":
    print(Kata.task_one(5))
    print(Kata.task_one(10))

    print(Kata.task_two(11))

    print(Kata.task_three(3, 7))
    print(Kata.task_three(7, 3))

    print(Kata.task_four(15, 3))
    print(Kata.task_four(15, 0))

    print(Kata.task_five(10))
    print(Kata.task_six(25))
    print(Kata.task_eight(5))
    print(Kata.task_nine(5))
