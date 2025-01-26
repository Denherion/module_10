# Задача "Потоковая запись в файлы"

import threading as thr
from time import sleep, time
from datetime import timedelta

def write_words(word_count, file_name):
    with open(file_name,  'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}'\n'")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")
started1 = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended1 = time()

def convert_seconds(seconds):
    return str(timedelta(seconds=seconds))
print("Работа функций", convert_seconds(ended1 - started1))

started2 = time()
thread1 = thr.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = thr.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = thr.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = thr.Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
ended2 = time()

def convert_seconds(seconds):
    return str(timedelta(seconds=seconds))
print("Работа потоков", convert_seconds(ended2 - started2))