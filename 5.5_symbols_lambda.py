def read_file(road_to_file):
    with open(road_to_file, "rb") as f:
        f = f.read()
        f = f.decode("utf-8")
        return f

words_dict = (lambda x: {i: x.count(i) for i in x})

print("*********   Программа подсчета частоты вхождений символов в текст   *********")
while True:
    text = input("Введите текст (Enter - взять данные из файла):")
    if not text:
        text = input("Укажите путь к файлу:")
        if not text:
            print("Данных нет.\nПопробуйте снова.")
            continue
        try:
            text = read_file(text)
        except PermissionError:
            print("Недостаточно прав для работы с файлом.")
            continue
        except FileNotFoundError:
            print("Неверный путь к файлу или такого файла не существует.")
            continue
        if not text:
            print("Данных нет.\nПопробуйте снова.")
            continue
    text_l = list(text)
    print('Частота вхождения символов текст:')
    symbols_freq = words_dict(text_l)
    for i in symbols_freq:
        print(f"{i}:{symbols_freq[i]}")