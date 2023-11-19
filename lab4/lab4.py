
list_of_users = []
current_user = None


def create_user():
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    address = input("Address: ")
    mail = input("Email: ")

    while True:
        for user in list_of_users:
            if mail == user['email']:
                print("Email already exists")
                mail = input("Email: ")
        break

    password = input("Password: ")

    while len(password) < 8:
        print("Password should be longer!")
        password = input("Password: ")

    user = {
        "name": name,
        "surname": surname,
        "age": age,
        "address": address,
        "email": mail,
        "password": password
    }

    list_of_users.append(user)


def show_all_users():
    print("List of Users:")
    for index, user in enumerate(list_of_users, start=1):
        print(f"{index}. {user['name']} {user['surname']} {user['email']}")


def del_user():
    global current_user
    if current_user:
        print(f"Delete current user {current_user['name']} {current_user['surname']}:")
        confirmation = input("Are you sure? (yes/no): ")
        if confirmation.lower() == 'yes':
            list_of_users.remove(current_user)
            current_user = None
            print("User successfully deleted.\n")
        else:
            print("Canceled.\n")
    else:
        print("You need to login.\n")


def auth_user():
    mail = input("Email: ")
    password = input("Password: ")

    for i in list_of_users:
        if mail == i['email'] and password == i['password']:
            global current_user
            current_user = i
            print(f"Welcome, {i['name']} {i['surname']}!\n")
            return
    print("Wrong password or email. Try again.\n")


def logout():
    global current_user
    current_user = None
    print("Successfully logged out!")


def main():
    while True:
        print("1. Create user")
        print("2. Show list of users")
        print("3. Delete user from list")
        if current_user:
            print("4. Logout")
        else:
            print("4. Login")
        print("5. Exit")

        choice = input("Choose one option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            show_all_users()
        elif choice == '3':
            del_user()
        elif choice == '4':
            if current_user:
                logout()
            else:
                auth_user()
        elif choice == '5':
            print("Good Bye!")
            break
        else:
            print("Wrong input. Please choose right option.\n")


if __name__ == "__main__":
    main()
