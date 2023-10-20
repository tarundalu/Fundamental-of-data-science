import pandas as pd
data = {
    'customer_id': [1, 1, 2, 3, 3],
    'order_date': ['2023-10-01', '2023-10-02', '2023-10-01', '2023-10-03', '2023-10-04'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'order_quantity': [2, 3, 1, 4, 2]
}
order_date = pd.DataFrame(data)
customer_orders = order_date.groupby('customer_id').size()
print("Total number of orders made by each customer:")
print(customer_orders)
average_order_quantity = order_date.groupby('product_name')['order_quantity'].mean()
print("\nAverage order quantity for each product:")
print(average_order_quantity)
earliest_order_date = order_date['order_date'].min()
latest_order_date = order_date['order_date'].max()
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
