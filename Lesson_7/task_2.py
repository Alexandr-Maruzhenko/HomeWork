class Category:
    categories = ["Кино", "Музыка", "Книги", "Игры"]

    @staticmethod
    def my_print():
        my_string = ""
        for _ in Category.categories:
            my_string += _ + " "
        return my_string

    @staticmethod
    def add(category):
        try:
            Category.categories.index(category)
        except ValueError:
            print("Такой категории нет. Добавляю...")
            Category.categories.append(category)
            return Category.categories.index(category)
        else:
            raise ValueError("Такая категория уже есть")

    @staticmethod
    def get(index):
        try:
            return Category.categories[index]
        except IndexError:
            message = "Такого индекса нет"
            return message

    @staticmethod
    def delete(index) -> None:
        try:
            Category.categories.pop(index)
        except IndexError:
            print("Индекса нет")

    @staticmethod
    def update(index, category) -> None:
        cat = Category.categories
        if not cat.count(category):
            try:
                cat[index] = category
            except IndexError:
                print("Индекс не существует. Добавляю в конец списка ...")
                cat.append(category)
        else:
            raise ValueError("Категория не уникальна")


string = Category.my_print()
print(string)

print(Category.get(3))

Category.delete(3)
string = Category.my_print()
print(string)

Category.add("Игры2")
string = Category.my_print()
print(string)

Category.update(0, "Игры3")
string = Category.my_print()
print(string)

Category.update(4, "Шахматы")
string = Category.my_print()
print(string)

Category.update(4, "Шашки")
string = Category.my_print()
print(string)

Category.update(5, "Городки")
string = Category.my_print()
print(string)
