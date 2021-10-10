import string

if __name__ == '__main__':
    print("Exercise 1:")
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 0: "Sunday"}
    #day = int(input("Input day: "))
    #days[day] = days[day % 7]
    for i in range(8, 32):
        days[i] = days[i % 7]
    print(days)

    print("\nExercise 2:")
    cats = {"Телосложение": {"Крепкий": "Шартрез", "Изящный": "Сиамский"}, 
           "Шёрстный покров": {"Длинношёрстный": "Бирманский", "Короткошёрстный": "Русская голубая", "Вьющейся шерсть": "Корниш-рекс", "Жёсткошёрстные": "Американская жёсткошёрстная", "бесшёрстные": "сфинкс"},
           "Окрас": {"Одноцветный": "Гавана", "Двухцветный": "Рэгдолл", "Пёстрый": "Мейн-кун", "С крапом": "Американская короткошерстная"}}
    classification = int(input("Введите вариант классификации кота (1 - По телосложению, 2 - По типу шёрстного покрова, 3 - По типу окраса): "))
    if classification == 1:
        classification = "Телосложение"
    elif classification == 2:
        classification = "Шёрстный покров"
    elif classification == 3:
        classification = "Окрас"
    else:
        print("Проверьте введёное значение!")
    type = input("Введите тип введёной классификации: ")
    print(cats[classification].get(type, "Проверьте введенные значения!"))

    print("\nExercise 3:")
    text = "Hello, world! Hello, Ivan! Ivan love Python and say: \"Hello Python\""
    res = {}
    for item in string.punctuation:
        text = text.replace(item, "")
    text = text.split()
    for item in text:
        if not res.get(item):
            res[item] = text.count(item)
    print(res)
    
    print("\nExtra Exercise 1:")
    value = {"valutes": {1: "dollars", 2: "cents"}, 
             "d": {1000000: "million", 1000: "thousand", 100: "hundred"},
             "c": {10: "ten", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"},
             "b": {11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"},
             "a": {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}}
    print("How much money do you have?")
    money = float(input())
    res = ""
    if money == 1000000:
        res += value["a"][1] + " " + value["d"][money] + " "
    elif money >= 10000 and money < 1000000:
        #тысячная часть
        if money // 10 ** 5:
            res += value["a"][money // 10 ** 5] + " " + value["d"][100] + " " # число + hundred
        if 10 < money // 10 ** 3 % 10 ** 2 < 20:
            res += value["b"][money // 10 ** 3 % 10 ** 2] + " " + value["d"][1000] + " " #число вида х11-х19 + thousand
        elif value.get("c", money // 10 ** 3 % 10 ** 2) and money // 10 ** 3 % 10 ** 2 - money // 10 ** 3 % 10 == 0:
            res += value["c"][money // 10 ** 3 % 10 ** 2] + " " + value["d"][1000] + " " #число вида x10, x20, ..., x90 + thousand
        elif money // 10 ** 4 % 10:
            res += value["c"][money // 10 ** 3 % 10 ** 2 - money // 10 ** 3 % 10] + " " + value["a"][money // 10 ** 3 % 10] + " " + value["d"][1000] + " " #любое число вида ххх + thousand
        else:
            res += value["a"][money // 10 ** 3 % 10] + " " + value["d"][1000] + " " #число вида x01-x09 + thousand
        #сотая часть
        if money // 10 ** 2 % 10:
            res += value["a"][money // 10 ** 2 % 10] + " " + value["d"][100] + " " # число + hundred
        if 10 < money // 1 % 10 ** 2 < 20:
            res += value["b"][money // 1 % 10 ** 2] + " " #число вида х11-х19
        elif value.get("c", money // 1 % 10 ** 2) and money // 1 % 10 ** 2 - money // 1 % 10 == 0:
            res += value["c"][money // 1 % 10 ** 2] + " " #число вида x10, x20, ..., x90
        elif money // 10 % 10:
            res += value["c"][money // 1 % 10 ** 2 - money // 1 % 10] + " " + value["a"][money // 1 % 10] + " " #любое число вида ххх
        else:
            res += value["a"][money // 1 % 10] + " " #число вида x01-x09
    elif money >= 1000:
        res += value["a"][money // 10 ** 3 % 10] + " " + value["d"][1000] + " "
        if money // 10 ** 2 % 10:
            res += value["a"][money // 10 ** 2 % 10] + " " + value["d"][100] + " " # число + hundred
        if 10 < money // 1 % 10 ** 2 < 20:
            res += value["b"][money // 1 % 10 ** 2] + " " #число вида х11-х19
        elif value.get("c", money // 1 % 10 ** 2) and money // 1 % 10 ** 2 - money // 1 % 10 == 0:
            res += value["c"][money // 1 % 10 ** 2] + " " #число вида x10, x20, ..., x90
        elif money // 10 % 10:
            res += value["c"][money // 1 % 10 ** 2 - money // 1 % 10] + " " + value["a"][money // 1 % 10] + " " #любое число вида ххх
        else:
            res += value["a"][money // 1 % 10] + " " #число вида x01-x09
    elif money >= 10:
        if money // 10 ** 2 % 10:
            res += value["a"][money // 10 ** 2 % 10] + " " + value["d"][100] + " " # число + hundred
        if 10 < money // 1 % 10 ** 2 < 20:
            res += value["b"][money // 1 % 10 ** 2] + " " #число вида х11-х19
        elif value.get("c", money // 1 % 10 ** 2) and money // 1 % 10 ** 2 - money // 1 % 10 == 0:
            res += value["c"][money // 1 % 10 ** 2] + " " #число вида x10, x20, ..., x90
        elif money // 10 % 10:
            res += value["c"][money // 1 % 10 ** 2 - money // 1 % 10] + " " + value["a"][money // 1 % 10] + " " #любое число вида ххх
        else:
            res += value["a"][money // 1 % 10] + " " #число вида x01-x09
    elif money // 1 % 10:
        res += value["a"][money // 1 % 10] + " "
    else:
        res += "null "
    
    res += value["valutes"][1] + " "
    if money % 1:
        if value.get("c", (money / 10 ** -2 + 1) % 10 ** 2) and (money / 10 ** -2 + 1) % 10 ** 2 - (money / 10 ** -2 + 1) % 10 == 0:
            res += value["c"][(money / 10 ** -2 + 1) % 10 ** 2] + " " #число вида 10, 20, ..., 90
        elif 10 < (money / 10 ** -2 + 1) % 10 ** 2 < 20:
            res += value["b"][(money / 10 ** -2 + 1) % 10 ** 2] + " " #число вида 11-19
        elif (money / 10 ** -1) % 10:
            res += value["c"][(money / 10 ** -2 + 1) % 10 ** 2 - (money / 10 ** -2 + 1) % 10] + " " + value["a"][(money / 10 ** -2 + 1) % 10] + " " #любое число вида хх
        else:
            res += value["a"][(money / 10 ** -2 + 1) % 10] + " "#число вида 01-09
        res += value["valutes"][2]
    print("You have:", res)

    print("\nExtra Exrcise 2: ")
    roman_numerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    number = input("Input roman numerals: ")
    prev = number[-1]
    res = roman_numerals[prev]
    for item in number[-2::-1]:
        if roman_numerals[item] >= roman_numerals[prev]:
            res += roman_numerals[item]
        else:
            res -= roman_numerals[item]
        prev = item
    print("Number:", res)
    

