import pandas as pd
data = {
    'post_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'likes': [50, 100, 150, 100, 200, 50, 100, 300, 50, 150]
}
interaction_data = pd.DataFrame(data)
likes_distribution = interaction_data['likes'].value_counts().sort_index()
 print(likes_distribution)
