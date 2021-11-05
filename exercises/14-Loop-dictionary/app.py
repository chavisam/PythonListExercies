
spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

more_translations = { 'love':'amor','code':'codigo','smart':'inteligente'}

for i in more_translations:
    spanish_translations[i] = more_translations[i]

print("Translation", spanish_translations["dog"])
print("All", spanish_translations)

