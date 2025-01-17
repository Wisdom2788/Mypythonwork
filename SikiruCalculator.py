def calculate_compound_interest(start_amount, monthly_add, total_years, annual_rate, frequency):
    rate = annual_rate / 100
    total_amount = start_amount
    months = total_years * 12

    for _ in range(months):
        total_amount += monthly_add
        total_amount += total_amount * (rate / frequency)

    
    return round(total_amount, 2)


def main():
    print("Welcome to Oga SIKIRUUU Compound Calculator!, NOTHING WE NO DEY COMPOUND FOR HERE")

    
    initial_investment = float(input("Enter the initial investment amount: "))
    monthly_contribution = float(input("Enter the monthly contribution: "))
    years = int(input("Enter the number of years: "))
    interest_rate = float(input("Enter the annual interest rate (in %): "))
    rate_variance = float(input("Enter the interest rate variance (in %): "))
    compound_frequency = int(input("Enter the number of times interest is compounded per year: "))

    
    average_result = calculate_compound_interest(initial_investment, monthly_contribution, years, interest_rate, compound_frequency)
    best_case_result = calculate_compound_interest(initial_investment, monthly_contribution, years, interest_rate + rate_variance, compound_frequency)
    worst_case_result = calculate_compound_interest(initial_investment, monthly_contribution, years, interest_rate - rate_variance, compound_frequency)

    
    total_investment_without_interest = initial_investment + monthly_contribution * years * 12

    print("\nResults:")
    print(f"Total Investment Without Interest: ${total_investment_without_interest:.2f}")
    print(f"Average Scenario: ${average_result:.2f}")
    print(f"Best Case Scenario: ${best_case_result:.2f}")
    print(f"Worst Case Scenario: ${worst_case_result:.2f}")



if __name__ == "__main__":
    main()
