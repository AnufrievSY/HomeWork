import pandas as pd

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']})

books = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                      'book_title': ['Отцы и дети', 'Рудин', 'Дворянское гнездо',
                                     'Толстый и тонкий', 'Дама с собачкой',
                                     'Гроза', 'Таланты и поклонники'],
                      'price': [450, 300, 350, 500, 450, 370, 290]})

authors_price = pd.merge(authors, books, on='author_id', how='inner')

authors_stat = authors_price.groupby('author_name').agg({'price': ['min',
                                                                   'max',
                                                                   'mean']})
authors_stat = authors_stat.rename(columns={'min': 'min_price',
                                            'max': 'max_price',
                                            'mean': 'mean_price'})

print(authors_stat)
