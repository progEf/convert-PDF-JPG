from pdf2image import convert_from_path
import os

print('Обнаружение вложенных PDF файлов ...')
print()
for file in os.listdir():  # цикл поиска файлов
    if file.endswith(".PDF") or file.endswith(".pdf"):  # определение файлов пдф
        print('Конвертирование', file, 'в jpg')
        print()
        name = os.path.join(file)  # вывод имен найденых пдфов
        index = name.index('.')  # отсекаем все после точки
        name = name[:index]  # получаем имя без расширения
        put = os.path.abspath(file)  # получаем путь
        # print('Путь: ', put)
        print()
        pages = convert_from_path(put, 200, poppler_path=r'poppler-23.11.0\Library\bin')
        if not os.path.isdir(name):
            os.mkdir(name)
        for i, page in enumerate(pages):
            page.save(name + f'/{name} {i + 1}.jpg', 'JPEG')