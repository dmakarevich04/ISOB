def vigenere_cipher(key, start_text, encrypt):

    result_text = []

    alphabets = {
        'en_upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'en_lower': 'abcdefghijklmnopqrstuvwxyz',
        'ru_upper': 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
        'ru_lower': 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    }

    key_index = 0

    for char in start_text:
        for alphabet_name, alphabet in alphabets.items():
            if char in alphabet:
                index = alphabet.index(char)

                key_char = key[key_index % len(key)]
                if key_char in alphabet:
                    shift = alphabet.index(key_char)
                else: 
                    shift = 0
            
                shift = shift if encrypt else -shift

                new_index = (index+shift) % len(alphabet)
                result_text.append(alphabet[new_index])

                key_index += 1
                break
        else: 
            result_text.append(char)

    result_text = ''.join(result_text)

    with open("vigenere_result.txt", "w", encoding="utf-8") as file:
            file.write(result_text)

    