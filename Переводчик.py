import translate

translator = translate.Translator(from_lang="ru", to_lang="en")
text = input("Введите текст: ")
print("Вот перевод: ", translator.translate(text))
input()