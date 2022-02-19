import pandas as pd
import numpy as np

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

authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая']
book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
book_info['мягкая'] = book_info['мягкая'].fillna(0)
book_info['твердая'] = book_info['твердая'].fillna(0)
print(book_info)

book_info.to_pickle('book_info.pkl')
book_info2 = pd.read_pickle('book_info.pkl')
print(f'\nbook_info и book_info2 идентичны?\n'
      f'{book_info.equals(book_info2)}')
