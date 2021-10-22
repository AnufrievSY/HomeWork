while True:
    new_text = input('Новая запись: ')
    with open('L_5_12.txt', 'a+') as new_file:
        if new_text == '':
            """Если поле ввода пустое, то указатель перемещается вначало, читается и выводится
            все содержимое файла"""
            new_file.seek(0)
            print(new_file.read())
            break
        else:
            """В противном случае в файл делается новая запись"""
            new_file.writelines(new_text + '\n')
