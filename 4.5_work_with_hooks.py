def read_file(road_to_file):
    with open(road_to_file, "rb") as f:
        f = f.read()
        f = f.decode("utf-8")
        return f

print("***  Программа по проверке правильности расставленных скобок  ***")
while True:
    text_list = list(input("Введите Ваш текст на проверку (Enter - взять данные из файла):"))
    if not text_list:
        road_to_file = input("Укажите путь к файлу:")
        if not road_to_file:
            print("Нет данных")
            continue
        try:
            text_list = list(read_file(road_to_file))
        except PermissionError:
            print("Недостаточно прав для работы с файлом.")
            continue
        except FileNotFoundError:
            print("Неверный путь к файлу или такого файла не существует.")
            continue
        if not text_list:
            print("Данных нет.\nПопробуйте снова.")
            continue
    hook_list = list()
    flag = True
    for i in text_list:
        if i == "(":
            hook_list.append(i)
        if i == ")":
            if hook_list and hook_list[-1] == "(":
                hook_list.pop()
            else:
                print("Не удалось найти пару для скобки типа: \")\"")
                flag = False
                break
        if i == "[":
            hook_list.append(i)
        if i == "]":
            if hook_list and hook_list[-1] == "[":
                hook_list.pop()
            else:
                print("Не удалось найти пару для скобки типа: \"]\"")
                flag = False
                break
        if i == "{":
            hook_list.append(i)
        if i == "}":
            if hook_list and hook_list[-1] == "{":
                hook_list.pop()
            else:
                print("Не удалось найти пару для скобки типа: \"}\"")
                flag = False
                break
        if i == "<":
            hook_list.append(i)
        if i == ">":
            if hook_list and hook_list[-1] == "<":
                hook_list.pop()
            else:
                print("Не удалось найти пару для скобки типа: \">\"")
                flag = False
                break
    if len(hook_list) != 0:
        print("В тексте есть незакрытые скобки.")
        flag = False
    print(f"Все {'хорошо' if flag == True else 'плохо'}.")