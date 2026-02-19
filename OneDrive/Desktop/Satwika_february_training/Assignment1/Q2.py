# Question 2: Online Shopping Discount System


customer_name = input("Enter customer name: ")
product_price = float(input("Enter product price: "))
premium_member = input("Is the customer a premium member? (True/False): ")
coupon_code = input("Enter coupon code: ")

premium_member = premium_member == "True"

discount = 0


if product_price > 5000 and premium_member:
    discount = product_price * 0.20
elif coupon_code == "SAVE10" or premium_member:
    discount = product_price * 0.10

final_price = product_price - discount


print("\nOriginal Price:", product_price)
print("Discount Applied:", discount)
print("Final Price:", final_price)

if premium_member:
    print("Premium benefits applied")
