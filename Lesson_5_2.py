while True:
    new_text = input('Новая запись: ')
    with open('L_5_12.txt', 'a+') as new_file:
        if new_text == '':
            """Если поле ввода пустое, то указатель перемещается вначало"""
            new_file.seek(0)
            """выводится все содержимое файла"""
            print(new_file.read())

            new_file.seek(0)
            file_lines = new_file.readlines()
            """выводится колличество строк"""
            print(f'В данном файле {len(file_lines)} строк.')

            new_file.seek(0)
            """колличество символов в каждой строке"""
            for i in range(len(file_lines)):
                print(f'Колличество символов в {i + 1} строке - {len(file_lines[i])}')
            break
        else:
            """В противном случае в файл делается новая запись"""
            new_file.writelines(new_text + '\n')
