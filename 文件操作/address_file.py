import os


class AddressManagement:#类
    def __init__(self, filename='address_book.txt'):
        self.filename = filename
        self.address_book = self.load_address_book()#调用下面的load_address_book方法，逐行输入name，address，phone

    def load_address_book(self):
        if os.path.exists(self.filename):  # 判断文件是否存在
            with open(self.filename, 'r', encoding='utf-8') as file:
                entries = file.readlines()#逐行读取文件，每一行保存为一个字符串
                return [entry.strip() for entry in entries if entry.strip()]#列表推导式，for循环逐行读取列表，if判断是否非空，strip（）用于去除首尾空字符
        else:
            return []

    def save_address_book(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for entry in self.address_book:
                file.write(entry + '\n')

    def add_contact(self, name, address, phone):
        self.address_book.append(f"{name}: {address}, {phone}")
        self.save_address_book()

    def delete_contact(self, name):
        self.address_book = [entry for entry in self.address_book if name not in entry]
        self.save_address_book()

    def update_contact(self, old_name, new_name=None, new_address=None, new_phone=None):
        for i, entry in enumerate(self.address_book):
            if old_name in entry:
                updated_entry = entry.replace(old_name, new_name) if new_name else entry
                updated_entry = updated_entry.replace(old_name + ':', new_name + ':') if new_name else updated_entry
                updated_entry = updated_entry.replace(old_address, new_address) if new_address else updated_entry
                updated_entry = updated_entry.replace(old_phone, new_phone) if new_phone else updated_entry
                self.address_book[i] = updated_entry
                self.save_address_book()
                return
        print("Contact not found.")

    def display_contacts(self):
        for entry in self.address_book:
            print(entry)

        # 主程序


def main():
    address_manager = AddressManagement()

    while True:
        print("\nAddress Book Management")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Display Contacts")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            address_manager.add_contact(name, address, phone)
            print("Contact added successfully.")

        elif choice == '2':
            name = input("Enter name to delete: ")
            address_manager.delete_contact(name)
            print("Contact deleted successfully.")

        elif choice == '3':
            old_name = input("Enter old name: ")
            new_name = input("Enter new name (leave blank if no change): ")
            new_address = input("Enter new address (leave blank if no change): ")
            new_phone = input("Enter new phone number (leave blank if no change): ")
            address_manager.update_contact(old_name, new_name, new_address, new_phone)
            print("Contact updated successfully.")

        elif choice == '4':
            address_manager.display_contacts()

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()