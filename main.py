from database import SessionLocal
from models import User, Category

def add_test_data():
    # 1. Створюємо сесію
    db = SessionLocal()
    
    try:
        print("Починаємо запис даних...")

        # 2. Створюємо об'єкти (користувача та категорію)
        new_user = User(username="Wiktor_Student", total_xp=50)
        new_cat = Category(name="Python ORM", color_hex="#3776AB")

        # 3. Додаємо їх у сесію
        db.add(new_user)
        db.add(new_cat)

        # 4. Зберігаємо в базу (COMMIT)
        db.commit()
        print("Дані успішно збережені в MySQL!")

    except Exception as e:
        print(f"Помилка: {e}")
        db.rollback() 
    finally:
        db.close() # Закриваємо сесію

if __name__ == "__main__":
    add_test_data()