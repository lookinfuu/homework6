print("***  Программа по удалению элемета в списке, если такой встречался ранее  ***")
text_list = list(input("Введите Ваш список значений:"))
for i in text_list:
    a = text_list.count(i)
    if a > 1:
        i1 = text_list.index(i)
        while a != 1:
            i2 = text_list.index(i,i1 + 1,len(text_list))
            text_list.pop(i2)
            i1 = i2 - 1
            a -= 1
print(f"Ваш список без повторов в элементах:{text_list}")