def checking_future_days_of_the_week():
    print("Days of the week")
    
days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(days_of_the_week)):
    print(f"{i}: {days_of_the_week[i]}")

today = int(input("Enter today's day: "))
if today < 0 or today > 6:
    print("Oga/maddam, there are 7 days a week ooo...\nplease input a valid day")
else:
    today = int(input("Enter today's day: "))

days_that_passed = int(input("Enter the number of days that has passed before today: "))
if days_that_passed < 0 or days_that_passed > 7:
    print("Mummmyyy ooo my body dey Shake")
else:
    days_that_passed = int(input("Enter the number of days that has passed before today: "))
    

future_day = (today + days_that_passed) % 7

print(f"Today is {days_of_the_week[today]} and the future day is {days_of_the_week[future_day]}")
