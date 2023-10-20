item_prices = [10.0, 5.0, 3.0, 2.0]  
item_quantities = [2, 3, 4, 1]  
discount_rate = 10.0 
tax_rate = 8.0  
total_cost_before_discount = sum([item_price * item_quantity for item_price, item_quantity in zip(item_prices, item_quantities)])
discount = (discount_rate / 100) * total_cost_before_discount
total_cost_after_discount = total_cost_before_discount - discount
tax = (tax_rate / 100) * total_cost_after_discount
final_total_cost = total_cost_after_discount + tax
print("Total cost before discount:", total_cost_before_discount)
print("Total cost after discount:", total_cost_after_discount)
print("Total cost after tax:", final_total_cost)
