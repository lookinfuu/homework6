import random
import string

def key(text):
    key = input("Введите ключ (Enter - ключ будет создан автоматически):")
    if not key:
        key = "".join(random.choice(string.digits + string.ascii_letters) for i in range(random.randint(1, len(text))))
        print(f"Ключ был создан автоматически:{key}")
    key = bytearray(key, "utf-8")
    return key

def read_file(road_to_file):
    with open(road_to_file, "rb") as f:
        f = f.read()
        return f

def write_file(road_to_file, xor_code):
    with open(road_to_file, "wb") as f:
        f.write(xor_code)

def XOR(text, key):
    xor_code = bytearray()
    for i in range(len(text)):
        xor_code.append(text[i] ^ key[i % len(key)])
    return xor_code

print("****  XOR-шифрование  ****\nДля выхода введите:\"выход\"")
road_to_file = ""
while road_to_file.lower() != "выход":
    road_to_file = input("Укажите путь к файлу:\n")
    if road_to_file.lower() != "выход":
        text = input("Введите текст (Enter - взять данные из файлы):")
        if not text:
            try:
                text = read_file(road_to_file)
            except PermissionError:
                print("Недостаточно прав для работы с файлом.")
                continue
            except FileNotFoundError:
                print("Неверный путь к файлу или такого файла не существует.")
                continue
        else:
            text = bytearray(text, "utf-8")
        try:
            write_file(road_to_file, XOR(text, key(text)))
        except PermissionError:
                print("Недостаточно прав для работы с файлом.")
                continue
        except FileNotFoundError:
                print("Неверный путь к файлу или такого файла не существует.")
        else:
            print("Успешно. Результат записан в файл.")