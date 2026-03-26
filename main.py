from database import SessionLocal
from models import User, Category

def add_test_data():
    # 1. Створюємо сесію
    db = SessionLocal()
    
    try:
        print("Починаємо запис даних...")

        # 2. Створюємо об'єкти (користувача та категорію)
        # У тебе в моделях ці поля обов'язкові
        new_user = User(username="Wiktor_Student", total_xp=50)
        new_cat = Category(name="Python ORM", color_hex="#3776AB")

        # 3. Додаємо їх у сесію
        db.add(new_user)
        db.add(new_cat)

        # 4. ФІНАЛЬНИЙ КРОК: Зберігаємо в базу (COMMIT)
        db.commit()
        print("Дані успішно збережені в MySQL!")

    except Exception as e:
        print(f"Помилка: {e}")
        db.rollback() # Відкочуємо зміни, якщо щось пішло не так
    finally:
        db.close() # Закриваємо сесію

if __name__ == "__main__":
    add_test_data()