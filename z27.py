# Пользователь вводит текст (строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.

# Input: Пользователь вводит текст
# Output: 3



text = "She sells sea shells on the sea shore The shells that she sells are sea shells" +\
"Im sure So if she sells sea shells on the sea shore Im sure that the sells are sea shore shells"

print(text.upper())

list = set(text)
print(list)
print(len(list))
