import tkinter as tk
from tkinter import filedialog, ttk
from caesar_cipher import caesar_cipher
from viginere_cipher import vigenere_cipher

file_path = None
crypt_method = None
key_entry = None  

def read_file(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read() 
    except FileNotFoundError:
        return f"Файл '{file_path}' не найден."
    except Exception as e:
        return f"Ошибка при чтении файла: {e}"



def choose_method(file_len):

    global error_label, file_path
    
    if not file_path:
        error_label.config(text="Ошибка! Сначала выберите файл.")
        return False

    if not crypt_method:
        error_label.config(text="Ошибка! Сначала выберите метод шифрования.")
        return False

    if key_entry:
        key = key_entry.get()
        if crypt_method == "Шифр Цезаря":
            if not key.lstrip('-').isdigit(): 
                error_label.config(text="Ошибка! Неверный ключ.")
                return False
            else: 
                error_label.config(text="")
                return True

        if crypt_method == "Шифр Виженера":
            if not key.isalpha() or len(key) >= file_len:
                error_label.config(text="Ошибка! Неверный ключ.")
                return False
            else:
                error_label.config(text="")
                return True

    error_label.config(text="Ошибка! Введите ключ.")
    return False



def on_file_button_click():

    global file_path
    file_path = filedialog.askopenfilename(
        title="Выберите текстовый файл",
        filetypes=(("Текстовые файлы", "*.txt"), ("Все файлы", "*.*"))
    )
    if file_path:
        file_label.config(text=f"Выбранный файл: {file_path.rsplit('/')[-1]}")


def on_method_select(event):

    global crypt_method, key_entry
    crypt_method = method_combobox.get()

    if crypt_method:
        key_label.config(text=f"Введите ключ для {crypt_method}:")
        key_label.pack(pady=5)
        if not key_entry:  
            key_entry = tk.Entry(key_frame, font=("Arial", 10)) 
            key_entry.pack(pady=5)
    else:
        key_label.pack_forget()
        if key_entry:
            key_entry.pack_forget()



def on_encrypt_button_click():

    global crypt_method

    text = read_file(file_path)

    if choose_method(len(text)):
        key = key_entry.get()
        if crypt_method == "Шифр Цезаря":
            caesar_cipher(int(key), text, True)
            result_label.config(text="Текст успешно зашифрован!")
        if crypt_method == "Шифр Виженера":
            vigenere_cipher(key, text, True)
            result_label.config(text="Текст успешно зашифрован!")



def on_decrypt_button_click():

    global crypt_method

    text = read_file(file_path)

    if choose_method(len(text)): 
        key = key_entry.get()
        if crypt_method == "Шифр Цезаря":
            caesar_cipher(int(key), text, False)
            result_label.config(text="Текст успешно расшифрован!")
        if crypt_method == "Шифр Виженера":
            vigenere_cipher(key, text, False)
            result_label.config(text="Текст успешно расшифрован!")



def create_ui(root):

    global file_label, method_combobox, key_label, key_frame, error_label, result_label

    main_label = tk.Label(root, text="Выберите текстовый файл и метод шифрования:", font=("Arial", 16))
    main_label.pack(pady=20)

    file_button = tk.Button(root, text="Выбрать файл", command=on_file_button_click)
    file_button.pack(pady=10)

    file_label = tk.Label(root, text="", font=("Arial", 10))
    file_label.pack(pady=10)

    method_label = tk.Label(root, text="Выберите метод шифрования:", font=("Arial", 10))
    method_label.pack(pady=5)

    method_combobox = ttk.Combobox(root, values=["Шифр Цезаря", "Шифр Виженера"], state="readonly")
    method_combobox.set("Метод шифрования")
    method_combobox.pack(pady=5)
    method_combobox.bind("<<ComboboxSelected>>", on_method_select)

    key_frame = tk.Frame(root)
    key_frame.pack(pady=10)

    key_label = tk.Label(key_frame, text="", font=("Arial", 10))

    button_frame = tk.Frame(root)
    button_frame.pack(pady=50)

    encrypt_button = tk.Button(button_frame, text="Зашифровать", command=on_encrypt_button_click)
    encrypt_button.pack(side=tk.LEFT, padx=5)

    decrypt_button = tk.Button(button_frame, text="Расшифровать", command=on_decrypt_button_click)
    decrypt_button.pack(side=tk.LEFT, padx=5)

    error_label = tk.Label(root, text="", font=("Arial", 10), fg="red")
    error_label.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
    result_label.pack(pady=10)

def main():
    global root
    root = tk.Tk()
    root.title("Шифровальщик файлов")
    root.geometry("600x600")
    create_ui(root)
    root.mainloop()

if __name__ == "__main__":
    main()