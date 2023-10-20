def calculate_discounted_price(original_price, discount_percentage):
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price


# write the apply_discount() function to apply the discount and return a string stating the discounted price:

def apply_discount(original_price, discount_percentage):
    discounted_price = calculate_discounted_price(original_price, discount_percentage)
    return "The discounted price is $" + str(discounted_price)


# write the shopping_cart() function that calls the apply_discount() function and prints the message with the discounted price:

def shopping_cart(original_price, discount_percentage):
    message = apply_discount(original_price, discount_percentage)
    print(message)