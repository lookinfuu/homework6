def number(l):
    while True:
        x = input(f"Введите {'первое' if l == 1 else 'второе'} число:")
        try:
            x = int(x)
        except ValueError:
            print(f"{x} - дробное число." if x.find('.') != -1 and x.count('.') == 1 else f"{x} - не число." if x else "Вы ничего не ввели.")
            continue
        except OverflowError:
            print("Число слишком большое.")
            continue
        else:
            return x

def symbols(text):
    d = {}
    for i in text:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return(d)

print("***  Программа по подсчету цифр в диапазоне чисел  ***")
a = number(1)
b = number(2)
if a > b:
    a, b = b, a
num_list = []
for i in range(a,b + 1):
    i = str(i)
    i = list(i)
    for u in range(0,len(i)):
        num_list.append(i[u])
d = symbols(num_list)
print(f"Частота использования цифр в диапазоне чисел от {a} до {b}:")
for i in d:
    print(f'{i}:{d[i]}')