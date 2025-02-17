def caesar_cipher(key, start_text, encrypt):
    
    result_text = []

    alphabets = {
        'en_upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'en_lower': 'abcdefghijklmnopqrstuvwxyz',
        'ru_upper': 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
        'ru_lower': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    }

    key = key if encrypt else -key

    for char in start_text:
        for alphabet_name, alphabet in alphabets.items():
            if char in alphabet:
                index = alphabet.index(char)
                shift = key % len(alphabet)
                new_index = (index + shift) % len(alphabet)
                result_text.append(alphabet[new_index])
                break
        else:
            result_text.append(char)

    result_text = ''.join(result_text)

    with open("caesar_result.txt", "w", encoding="utf-8") as file:
            file.write(result_text)