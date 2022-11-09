import json


def open_phonebook():
    with open("phonebook.json", "r+") as phonebook_file:
        try:
            phonebook = phonebook_file.read()
            phonebook = json.loads(phonebook)
        except json.JSONDecodeError:
            phonebook = {}
    return phonebook


phonebook = open_phonebook()


def add_new_entry(phonebook: dict):
    phone_number = "+380-" + correct_input(valid_phone_number, "Enter your phone number: +380-",
                                           "Enter your phone number in next format: +380-XX-XXX-XX-XX. Country code by default +380 (Ukraine)")

    first_name = correct_input(valid_first_or_last_name, "Enter your name: ",
                               "Name should be less than 50 characters and contains only letters").lower().title()

    last_name = correct_input(valid_first_or_last_name, "Enter your last name: ",
                              "Last name should be less than 50 characters and contains only letters").lower().title()

    full_name = first_name + " " + last_name

    state = correct_input(valid_city_or_state, "Enter your state: ").strip()
    city = correct_input(valid_city_or_state, "Enter your city: ").strip()

    phonebook[phone_number] = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "address": {
            "state": state,
            "city": city
        },
    }

    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def search_by(key: str, searching_for: str):
    search_result = []

    if key == "phone_number":
        if phonebook.get(searching_for):
            search_result.append(phonebook.get(searching_for))

    for phone_number in phonebook.keys():
        if key in ["state", "city"]:
            if phonebook[phone_number]["address"][key] == searching_for:
                search_result.append(phone_number)

        if phonebook[phone_number][key] == searching_for:
            search_result.append(phone_number)
    if len(search_result) > 0:
        return search_result
    else:
        return "Your search gave no result."


def delete_phone_number(phone_number: str, phonebook: dict):
    try:
        del phonebook[phone_number]
        print(f"Contact with phone number {phone_number} was deleted.")
    except KeyError:
        print("Phone number does not exist!")

    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def update_contact_info(phone_number: str, key: str, phonebook: str):
    try:
        phonebook[phone_number]
    except KeyError:
        print("Phone number does not exist!")

    if key == "phone_number":
        pass

    if key in ["state", "city"]:
        new_value = correct_input(
            valid_city_or_state, f"Enter your {key}: ").strip()
        phonebook[phone_number]["address"][key] = new_value

    if key in ["first_name", "last_name"]:
        new_value = correct_input(valid_first_or_last_name, f"Enter your {key.replace('_', ' ')}: ",
                                  "Name should be less than 50 characters and contains only letters").lower().title()
        phonebook[phone_number][key] = new_value

        contact = phonebook[phone_number]
        contact["full_name"] = contact["first_name"] + \
            " " + contact["last_name"]

    if key == "full_name":
        new_first_name = correct_input(valid_first_or_last_name, f"Enter your first name: ",
                                       "Name should be less than 50 characters and contains only letters").lower().title()

        new_last_name = correct_input(valid_first_or_last_name, f"Enter your last name: ",
                                      "Name should be less than 50 characters and contains only letters").lower().title()

        contact = phonebook[phone_number]
        contact["first_name"] = new_first_name
        contact["last_name"] = new_last_name
        contact["full_name"] = contact["first_name"] + \
            " " + contact["last_name"]

    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def valid_phone_number(phone_number: str):

    phone_number = phone_number.split('-')  # ['96', '123', '40', '50']
    if len(phone_number) != 4:
        print("Not valid format!")
        return False

    format_of_elements = [2, 3, 2, 2]
    for index, digits in enumerate(phone_number):

        if not format_of_elements[index] == len(digits):
            print("Not valid format!")
            return False

        if not digits.isnumeric():
            print("Only digits can be in phone number!")
            return False

    return True


def valid_first_or_last_name(name: str):
    if len(name) > 50:
        print("Too many characters!")
        return False

    if not name.isalpha():
        print("Name must contains only alphabet letters!")
        return False

    return True


def valid_city_or_state(place_name: str):
    set_of_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- "

    if "  " in place_name:
        print("Too many spaces!")
        return False

    if len(place_name) > 50:
        print("Too many characters!")
        return False

    if (place_name[0] == "-") or (place_name[-1] == "-"):
        print("- can not be in the first place")
        return False

    for letter in place_name:
        if letter not in set_of_characters:
            print("Should only contain alphabet or -")
            return False

    return True


def correct_input(valid_func, prompt: str, hint=False):
    valid = False

    if hint:
        print(hint)

    while not valid:
        value = input(prompt)
        valid = valid_func(value)

    return value


def print_menu():
    print("\n1. Add new entry")
    print("2. Search by first name")
    print("3. Search by last name")
    print("4. Search by full name")
    print("5. Search by telephone number")
    print("6. Search by city")
    print("7. Search by state")
    print("8. Delete a record for a given telephone number")
    print("9. Update a record for a given telephone number")
    print("0. Type 0 to exit the program")


def menu_search_by_name(phonebook: dict):
    name = input("Enter name: ")
    print(search_by("first_name", name))


def menu_search_by_last_name(phonebook):
    last_name = input("Enter last name: ")
    print(search_by("last_name", last_name))


def menu_search_by_full_name(phonebook):
    full_name = input("Enter full name: ")
    print(search_by("full_name", full_name))


def menu_search_by_phone_number(phonebook):
    phone_number = input("Enter phone number in format +380-XX-XXX-XX-XX: ")
    print(search_by("phone_number", phone_number))


def menu_search_by_city(phonebook):
    city = input("Enter city: ")
    print(search_by("city", city))


def menu_search_by_state(phonebook):
    state = input("Enter state: ")
    print(search_by("state", state))


def menu_delete_phone_number(phonebook):
    phone_number = input("Enter phone number you would like to delete: ")
    delete_phone_number(phone_number, phonebook)


def menu_update_contact_info(phonebook):
    number = input(
        "Please enter number of a contact you would like to update: ")
    key = input(
        "Please enter an option you would like to update (first_name, last_name full_name, city, state): ")
    update_contact_info(number, key, phonebook)


menu_func = {
    1: add_new_entry,
    2: menu_search_by_name,
    3: menu_search_by_last_name,
    4: menu_search_by_last_name,
    5: menu_search_by_phone_number,
    6: menu_search_by_city,
    7: menu_search_by_state,
    8: menu_delete_phone_number,
    9: menu_update_contact_info
}


# def menu():
#     print_menu()
#     while True:
#         try:
#             menu_choice = int(
#                 input("\nEnter number from 0 to 9 to choose func: "))
#             if menu_choice != 0:
#                 if not menu_choice in menu_func.keys():
#                     print(
#                         "There is no such menu choice, please choose the correct number: ")
#                     print_menu()
#                     break
#                 else:
#                     menu_func[menu_choice](phonebook)
#                     f"\n{menu()}"
#         except ValueError:
#             print("Please use integers from 0 to 9")
#             menu()


# menu()