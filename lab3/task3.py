# TODO  Напишите функцию count_letters


# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

def count_letters(text: str):
    chars = [sym.lower() for sym in list(text) if sym.isalpha()]
    #we need keep origin order
    #unique_letters = set(chars)
    unique_letters = dict.fromkeys(chars)
    letter_dict = {}
    for letter in unique_letters:
        occ_times = chars.count(letter)
        letter_dict[letter] = occ_times

    return letter_dict, len(chars)

def calculate_frequency(letter_dict, total_letter_count):
    for key, value in letter_dict.items():
        letter_dict[key] = value/total_letter_count


letter_dict, total_letter_count = count_letters(main_str)
calculate_frequency(letter_dict, total_letter_count)
for key, value in letter_dict.items():
    print(f'{key}: {round(value,2):.2f}')
