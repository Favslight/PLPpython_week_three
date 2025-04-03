def calculate_discount(price, discount_percent):
    """calculate the discount price on an item

    Args:
        price (selling pricw): The main price
        discount_price (_percentage_): the discount price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
price = float(input("Enter the selling price"))
discount_percent = float(input("Enter the discount percent"))

final_price = calculate_discount(price, discount_percent)
print(f"The final price after applying discount is: {final_price:.2f}")