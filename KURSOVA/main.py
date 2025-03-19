import tkinter as tk
from book_recommendation_app import run_gui  # імпортуємо функцію, яка запускає інтерфейс
from database_connection import create_tables, add_book_to_db, get_recommendations_from_db

def initialize_database():
    """Ініціалізація бази даних, створення таблиць, якщо їх немає."""
    try:
        create_tables()  # створюємо таблиці, якщо їх ще не існує
    except Exception as e:
        print(f"Помилка при ініціалізації бази даних: {e}")

def main():
    # Ініціалізація бази даних
    initialize_database()

    # Запуск візуальної частини додатка
    run_gui()

if __name__ == "__main__":
    main()
