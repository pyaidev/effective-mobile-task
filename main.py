import json
import os
from typing import List, Dict, Union

BOOKS_FILE = "books.json"

class Book:
    def __init__(self, title: str, author: str, year: int):
        """
        Инициализация новой книги с заголовком, автором и годом.
        Идентификатор генерируется автоматически, и статус устанавливается как "в наличии".

        :param title: Название книги.
        :param author: Автор книги.
        :param year: Год издания.
        """
        self.id = Book.generate_id()
        self.title = title
        self.author = author
        self.year = year
        self.status = "available"

    @staticmethod
    def generate_id() -> int:
        """
        Генерация уникального идентификатора для новой книги.

        :return: Уникальный целочисленный идентификатор.
        """
        if not os.path.exists(BOOKS_FILE):
            return 1
        with open(BOOKS_FILE, "r") as file:
            books = json.load(file)
            if not books:
                return 1
            return max(book["id"] for book in books) + 1

    def to_dict(self) -> Dict[str, Union[int, str]]:
        """
        Преобразование объекта книги в словарь.

        :return: Словарь, представляющий книгу.
        """
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

def load_books() -> List[Dict[str, Union[int, str]]]:
    """
    Загрузка книг из JSON файла.

    :return: Список книг в виде словарей.
    """
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)

def save_books(books: List[Dict[str, Union[int, str]]]):
    """
    Сохранение книг в JSON файл.

    :param books: Список книг в виде словарей.
    """
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)

def add_book():
    """
    Добавление новой книги в библиотеку.
    Запрашивает у пользователя данные о книге и добавляет книгу в библиотеку.
    """
    try:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания: "))
        book = Book(title, author, year)
        books = load_books()
        books.append(book.to_dict())
        save_books(books)
        print(f"Книга '{title}' добавлена с ID {book.id}.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите правильные данные.")

def delete_book():
    """
    Удаление книги из библиотеки.
    Запрашивает у пользователя ID книги и удаляет книгу, если она существует.
    """
    try:
        book_id = int(input("Введите ID книги для удаления: "))
        books = load_books()
        book_to_delete = next((book for book in books if book["id"] == book_id), None)
        if book_to_delete:
            books = [book for book in books if book["id"] != book_id]
            save_books(books)
            print(f"Книга с ID {book_id} удалена.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
    except ValueError:
        print("Некорректный ID. Пожалуйста, введите правильный числовой ID.")

def search_books():
    """
    Поиск книг в библиотеке.
    Запрашивает у пользователя критерий поиска и запрос, отображает соответствующие книги.
    """
    try:
        criteria = input("Поиск по названию, автору или году: ").lower()
        if criteria not in ["title", "author", "year"]:
            raise ValueError("Некорректный критерий поиска")
        query = input(f"Введите {criteria}: ").lower()
        books = load_books()
        results = []
        for book in books:
            if criteria == "year":
                if str(book[criteria]) == query:
                    results.append(book)
            else:
                if query in book[criteria].lower():
                    results.append(book)
        if results:
            for book in results:
                print(book)
        else:
            print("Книги не найдены.")
    except ValueError as e:
        print(f"Ошибка: {e}")

def display_books():
    """
    Отображение всех книг в библиотеке.
    """
    books = load_books()
    if books:
        for book in books:
            print(book)
    else:
        print("В библиотеке нет книг.")

def update_status():
    """
    Обновление статуса книги в библиотеке.
    Запрашивает у пользователя ID книги и новый статус, обновляет статус, если книга существует.
    """
    try:
        book_id = int(input("Введите ID книги для обновления статуса: "))
        new_status = input("Введите новый статус (available/issued): ").lower()
        if new_status not in ["available", "issued"]:
            raise ValueError("Некорректный статус. Пожалуйста, введите 'available' или 'issued'.")
        books = load_books()
        book_to_update = next((book for book in books if book["id"] == book_id), None)
        if book_to_update:
            book_to_update["status"] = new_status
            save_books(books)
            print(f"Статус книги с ID {book_id} обновлен на {new_status}.")
        else:
            print(f"Книга с ID {book_id} не найдена.")
    except ValueError as e:
        print(f"Ошибка: {e}")

def main():
    """
    Основная функция для запуска системы управления библиотекой.
    Предоставляет меню для взаимодействия пользователя с системой.
    """
    while True:
        print("\nСистема управления библиотекой")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Поиск книги")
        print("4. Показать все книги")
        print("5. Обновить статус книги")
        print("6. Выйти")
        choice = input("Введите ваш выбор: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            search_books()
        elif choice == "4":
            display_books()
        elif choice == "5":
            update_status()
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
