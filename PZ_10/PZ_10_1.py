# Вариант 4
# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский. Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах можно приобрести книги Маяковского
magistr = {"Лермонтов", "Достоевский", "Пушкин", "Тютчев"}
Domknigi = {"Толстой", "Грибоедов", "Чехов", "Пушкин"}
BukMarket = {"Пушкин", "Достоевский", "Маяковский"}
Galereya = {"Чехов", "Тютчев", "Пушкин"}
book = "Маяковский"
while True:
    if book in magistr:
        print("Книга находится в магазине Magistr")
    if book in Domknigi:
        print("Книга находится в магазине Domknigi")
    if book in BukMarket:
        print("Книга находится в магазине Bukmarket")
    if book in Galereya:
        print("Книга находится в магазине Galereya")
    break
