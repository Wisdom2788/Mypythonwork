def rider_one(successful_delivery1):
    parcel = 160
    base_pay = 5000
    daily_wage = 0

    if successful_delivery1 <= 50:
        daily_wage = (successful_delivery1 * parcel) + base_pay
    return daily_wage


def rider_two(successful_delivery2):
    parcel = 200
    base_pay = 5000
    daily_wage_one = 0

    if 50 <= successful_delivery2 <= 59:
        daily_wage_one = (successful_delivery2 * parcel) + base_pay
    return daily_wage_one


def rider_three(successful_delivery3):
    parcel = 250
    base_pay = 5000
    daily_wage_two = 0

    if 60 <= successful_delivery3 <= 69:
        daily_wage_two = (successful_delivery3 * parcel) + base_pay
    return daily_wage_two


def rider_four(successful_delivery4):
    parcel = 500
    base_pay = 5000
    daily_wage_three = 0

    if successful_delivery4 >= 70:
        daily_wage_three = (successful_delivery4 * parcel) + base_pay
    return daily_wage_three


def main():
    print("Welcome to Back To Sender Logistics Services oooooo...\n")

    successful_delivery1 = 45
    successful_delivery2 = 55
    successful_delivery3 = 66
    successful_delivery4 = 90

    total_wage_one = rider_one(successful_delivery1)
    print(f"Rider 1 daily wage: {total_wage_one}")
    print(f"{successful_delivery1}(successful delivery) x 160(Amount Per Parcel) + 5000(BasePay) = {total_wage_one}\n")

    total_wage_two = rider_two(successful_delivery2)
    print(f"Rider 2 daily wage: {total_wage_two}")
    print(f"{successful_delivery2}(successful delivery) x 200(Amount Per Parcel) + 5000(BasePay) = {total_wage_two}\n")

    total_wage_three = rider_three(successful_delivery3)
    print(f"Rider 3 daily wage: {total_wage_three}")
    print(f"{successful_delivery3}(successful delivery) x 250(Amount Per Parcel) + 5000(BasePay) = {total_wage_three}\n")

    total_wage_four = rider_four(successful_delivery4)
    print(f"Rider 4 daily wage: {total_wage_four}")
    print(f"{successful_delivery4}(successful delivery) x 500(Amount Per Parcel) + 5000(BasePay) = {total_wage_four}\n")


if __name__ == "__main__":
    main()
