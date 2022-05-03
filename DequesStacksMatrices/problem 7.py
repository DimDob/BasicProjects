from collections import deque

vowels = deque([x for x in input().split()])
consonants = [x for x in input().split()]

success = False
word_found = ""
current_rose = 'rose'
current_tulip = 'tulip'
current_lotus = 'lotus'
current_daffodil = 'daffodil'
while True:


    if not vowels or not consonants:
        break
    if success:
        break
    vowel = vowels.popleft()
    consonant = consonants.pop()



    if vowel or consonant in current_rose:
        if vowel in current_rose:
            current_rose = current_rose.replace(vowel, '')
        if consonant in current_rose:
            current_rose = current_rose.replace(consonant, '')
    if vowel or consonant in current_tulip:
        if vowel in current_tulip:
            current_tulip = current_tulip.replace(vowel, '')
        if consonant in current_tulip:
            current_tulip = current_tulip.replace(consonant, '')
    if vowel or consonant in current_lotus:
        if vowel in current_lotus:
            current_lotus = current_lotus.replace(vowel, '')
        if consonant in current_lotus:
            current_lotus = current_lotus.replace(consonant, '')
    if vowel or consonant in current_daffodil:
        if vowel in current_daffodil:
            current_daffodil = current_daffodil.replace(vowel, '')
        if consonant in current_daffodil:
            current_daffodil = current_daffodil.replace(consonant, '')

    if current_rose == '':
        word_found = 'rose'
        success = True
    elif current_tulip == '':
        word_found = 'tulip'
        success = True
    elif current_lotus == '':
        word_found = 'lotus'
        success = True
    elif current_daffodil == '':
        word_found = 'daffodil'
        success = True

if success:
    print(f"Word found: {word_found}")
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")
else:
    print(f'Cannot find any word!')
    if vowels:
        print(f"Vowels left: {' '.join(vowels)}")
    if consonants:
        print(f"Consonants left: {' '.join(consonants)}")