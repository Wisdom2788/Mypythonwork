pizza_types = ["Sapa size", "Small Money", "Big boys", "Odogwu"]
slices_in_box = [4, 6, 8, 12]
price_of_box = [2500, 2900, 4000, 5200]

print("\nWelcome to SIKIRU AND FAMILY PIZZA INC")
guests = int(input("Enter number of guests: "))

print("\nPizza Type")
print("0 = Sapa size")
print("1 = Small Money")
print("2 = Big boys")
print("3 = Odogwu")

pizza_type_index = int(input("Enter the pizza type: "))

slices_per_box = slices_in_box[pizza_type_index]
price_per_box = price_of_box[pizza_type_index]

boxes_needed = guests // slices_per_box
if guests % slices_per_box != 0:
    boxes_needed += 1

total_slices = boxes_needed * slices_per_box
leftovers = total_slices - guests
total_price = boxes_needed * price_per_box

print("\nResults:")
print(f"Number of pizza boxes to buy = {boxes_needed} boxes")
print(f"Number of leftovers = {leftovers} slices")
print(f"Total price = {total_price} NGN")
