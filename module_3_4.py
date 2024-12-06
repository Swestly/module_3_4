def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
            continue
        elif i.lower() in root_word.lower():
            same_words.append(i)
            continue
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')



print('=' * 80)

print(result1)

print('=' * 80 )


print(result2)

print('=' * 80 )


print('\n' * 2  + '\n' * 2)
