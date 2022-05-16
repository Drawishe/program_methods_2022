import sys
import task3,task2, task1
import os


def remove_cash(param):
    """
    **Удаляет сгенерированные файлы графов**
    """
    for f in os.listdir('.'):
        if not f.endswith(f'{param}'):
            continue
        os.remove(os.path.join('.', f))


if __name__ == "__main__":
    print("             .';coxO00KKKK0000Oxdl:,.             \n          .;lxO0KKKKKKKKKK000000KKK0Od:'          \n        'lxOO00000KKKKKKKK0000000KKKKKK0x:.       \n      ,okkkOOOOO000KKKKKKK000000KKKKKKKKXXOc.     \n    .cxxxkkkkkOO000KKKKKKK000000KKKKKKXXXXXXO;    \n   ,oxxxxxxkkkOOOO0KK0OOkkkO00KKKKKKKXXXXXNNNXo.  \n  ;oddddxxxxxkkkkkoc;'.......,cdOKKXXXXNNNNNNNNx. \n ,oddddddddxxxxd;.              .:kXNNNNNNNNNNNNd.\n.loooodddddddd:.                  .cKNNNNNNNNNNNXc\n;oooooooooodo,                      ;0NNNWWWWWWWWO\ncooooooooooo;                        cXWMMMMMMMMMN\nloollollllol.                        '0MMMMMMMMMMM\nlllllllllloc.                        .OMMMMMMMMMMW\nclllllllllll'                         cXMMMMMMMMM0\nclllllllllll'                         cXMMMMMMMMM0\n'clccccccccc:,.                          .;:c:,.  \n.;cccccc:::::;,.                                  \n .;c::::::;;;;,,'..                               \n  .,::::;;;;,,,''''.......   ........             \n    ';;;;;,,,,'''.....................            \n     .',,,,,,''''.......................          \n       ..','''''.........................         \n          ..'''.......................            \n             ......................               \n                 ..............                   ")
    print('Программное решение по дисциплине "Технологии и методы программирования"')
    print('Выполнили студенты уч.гр. 181-331 Фурман Кирилл, Еремин Иван, Корниенко Екатерина')
    print('2022')
    print('\n\n 1 — Построение по автомату Мили эквивалентный ему автомат Мура')
    print(' 2 — Построение автоматов для объединения и пересечения двух языков')
    print(' 3 — Построение автомата для дополнения языка')
    print('\"delete\" — Удаление созданных изображений графов')
    print(' 0 — Выход из программы')

    number = input('Выберите необходимую вам задачу: ')
    while number:
        if number == '1' or number =='kornienko':
            task1.main()
            print('task1 - Успешно\n')
        if number == '2' or number == 'eremin':
            task2.main()
            print('task2 - Выполнен успешно\n')
        elif number == '3' or number == 'furman':
            task3.main()
            print('task3 - Выполнен успешно\n')
        elif number == '0' or number == 'exit' or number == 'x':
            print('Благодарим за использование программы, хорошего Вам дня!')
            sys.exit()
        elif number == 'delete' or number == 'd':
            remove_cash('png')
        else:
            print('Введено неверное значение!\nПожалуйста, введите корректный номер для выполнения программы, или 0 - чтобы выйти из программы')
        number = input('Выберите необходимую вам задачу: ')