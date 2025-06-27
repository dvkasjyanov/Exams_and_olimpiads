'''
Дана последовательность N целых положительных чисел. Рассматриваются все пары элементов последовательности, разность которых чётна, и в этих парах, по крайней мере, 
одно из чисел пары делится на 17. Порядок элементов в паре неважен. Среди всех таких пар нужно найти и вывести пару с максимальной суммой элементов. Если одинаковую 
максимальную сумму имеет несколько пар, можно вывести любую из них. Если подходящих пар в последовательности нет, нужно вывести два нуля.
'''

file = open('27991_B.txt')
content = list(map(int, file.readlines()))
content.pop(0)  # Важно убрать первый элемент, так как это число N

a = 0
b = 0

'''
По def, разность двух целых чисел делится на 2, если оба числа имеют одну чётность.
(Э.Б. Винберг, "Курс Алгебры". Введение / Кольца вычетов)
'''

# max выдаёт ошибку для пустого списка. defalut необходим, чтобы не вылетала ошибка. 
M17_even = max([k for k in content if (k % 17 == 0) and (k % 2 == 0)], default=0)
M17_odd = max([k for k in content if (k % 17 == 0) and (k % 2 != 0)], default=0)

if (M17_even + M17_odd != 0):

    M_even = max([k for k in content if k % 2 == 0], default=0)
    M_odd = max([k for k in content if k % 2 != 0], default=0)

    # Работаем с чётными числами
    if M17_even != 0:    
        if M_even == M17_even:
            k17_even = content.count(M17_even)
            if k17_even == 1:
                M_even = max([k for k in content if k % 2 == 0 and k != M17_even], default=0)

        if (M_even != 0) and (M_even + M17_even > a + b):
            a = M_even
            b = M17_even

    # То же самое с нечётными числами
    if M17_odd != 0:    
        if M_odd == M17_odd:
            k17_odd = content.count(M17_odd)
            if k17_odd == 1:
                M_odd = max([k for k in content if k % 2 != 0 and k != M17_odd], default=0)

        if (M_odd != 0) and (M_odd + M17_odd > a + b):
            a = M_odd
            b = M17_odd


print(a, b)