from translate import Translator


word = input('Text = ')
translator = Translator(from_lang="ru", to_lang="en")
translation = translator.translate(word)
print(translation)