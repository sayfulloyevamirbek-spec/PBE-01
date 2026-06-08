from buy_section import add_product
from sell_section import sell_product
from database import default_database_info, sell_product_database_info, add_product_database_info


def survey():
    print("Bizni do'konimizga xush kelibsiz!".center(108))
    print("Siz nima qilmoqchisiz?".center(108))
    print("1. Mahsulot sotib olish".center(108))
    print("2. Mahsulot sotish".center(108))
    print("3. Ko'rish".center(108))
    print("4. Chiqish".center(108))
    while True:
        choice = input("Tanlovingizni kiriting (1-4): ")
        if choice == '1':
            add_product
        elif choice == '2':
            sell_product
        elif choice == '3':
            print("Talang".center(108))
            print("1. Qo'shilgan mahsulotlar".center(108))
            print("2. Sotilgan mahsulotlar".center(108))
            print("3. Barcha mahsulotlar".center(108))
            print("4. Ortga".center(108))
            while True:
                choice = input("Tanlovingizni kiriting (1-4): ")
                if choice == '1':
                    ("Qo'shilgan mahsulotlar", add_product_database_info())
                elif choice == '2':
                    ("Sotilgan mahsulotlar", sell_product_database_info())
                elif choice == '3':
                    login = 'Admin'
                    password = 'Admin123'
                    user_login = input("Login: ")
                    user_password = input("Parol: ")
                    if user_login == login and user_password == password:
                       ("Barcha mahsulotlar", default_database_info())
                    else:
                        print("Bu bo'limga kirishga ruxsat yo'q")
                        break
                elif choice == '4':
                    break
                else:
                    print("Noto'g'ri tanlov. Iltimos, 1-4 orasida tanlov qiling.")
        elif choice == '4':
            print("Do'konimizdan foydalanganingiz uchun rahmat!")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, 1-4 orasida tanlov qiling.")


if __name__ == "__main__":
    survey()
