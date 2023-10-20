import pandas as pd


data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City B', 'City C'],
    'number_of_bedrooms': [3, 4, 3, 5, 2],
    'area_sqft': [1500, 1800, 1600, 2200, 1200],
    'listing_price': [250000, 320000, 280000, 400000, 180000]
}

property_data = pd.DataFrame(data)


average_listing_price = property_data.groupby('location')['listing_price'].mean()
print("Average listing price of properties in each location:")
print(average_listing_price)


properties_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
count_more_than_four_bedrooms = len(properties_more_than_four_bedrooms)
print("\nNumber of properties with more than four bedrooms:", count_more_than_four_bedrooms)


property_with_largest_area = property_data[property_data['area_sqft'] == property_data['area_sqft'].max()]
print("\nProperty with the largest area:")
print(property_with_largest_area)
