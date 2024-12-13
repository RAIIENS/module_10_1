# Импортируем необходимые модули threading для работы с потоками и time для измерения времени.
import threading
from time import sleep, time
# Создаём функцию для записи слов в файл
# Определяем функцию write_words которая принимает количество слов и имя файла,
# в который будет производиться запись. В ней происходит запись слова с номером в файл
# с паузой 0.1 секунды между записями.
def write_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)  # Пауза 0.1 секунды
    print(f"Завершилась запись в файл {file_name}")
# фиксируем текущее время
start_time = time()
# Сначала записываем слова в четыре файла последовательно и измеряем общее время выполнения.
# Запускаем функции с аргументами из задачи
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
# фиксируем текущее время
end_time = time()
print(f"Работа функций {end_time - start_time:.6f} секунд")
# фиксируем текущее время перед запуском потоков
start_time_threads = time()
# Создаём и запускаем потоки с аргументами из задачи
threads = []
threads.append(threading.Thread(target=write_words, args=(10, 'example5.txt')))
threads.append(threading.Thread(target=write_words, args=(30, 'example6.txt')))
threads.append(threading.Thread(target=write_words, args=(200, 'example7.txt')))
threads.append(threading.Thread(target=write_words, args=(100, 'example8.txt')))

for thread in threads:
    thread.start()

# Ждём завершение потоков
for thread in threads:
    thread.join()

# Фиксируем текущее время после завершения потоков
end_time_threads = time()
print(f"Работа потоков {end_time_threads - start_time_threads:.6f} секунд")
