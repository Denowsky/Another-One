# Задача 20:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

try:
    n = input('Введите слово(анг/рус): ')
    price_for_ru = {1: 'АВЕИНОРСТ',2:'ДКЛМП',3:'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ',10: 'ФЩЪ'}
    price_for_en = {1: 'AEIOULNSTR',2:'DG',3:'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX',10: 'QZ'}
    price_count = 0
    temp = []
    for v in price_for_en.values():
        temp.append(v)
    count_char = ''.join(temp)
    for i in n.upper():
            if i in count_char:
                for j in price_for_en:
                    if i in price_for_en[j]:
                        price_count+=j
            else:
                for j in price_for_ru:
                    if i in price_for_ru[j]:
                        price_count+=j
    print(price_count)

except:
    print('Ввод не совсем корректный. Попробуйте еще раз!')

