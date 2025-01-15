def get_sum_of_integers_itself(number)

if 0 <= number <= 1000:
    
    digit_sum = sum(int(digit) for digit in str(number))
    print(f"The sum of the digits {number} is {digit_sum}.")



    


