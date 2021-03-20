# сохраняем файл в список построчно:
def save_file_as_list(file='recipes.txt'):
    with open(file, 'r', encoding='utf-8') as recipes:
        recipes_list = []
        for line in recipes:
            recipes_list.append(line.strip())
        return recipes_list


# превращаем список в словарь:
def convert_list_to_dictionary():
    ingredient_params = ['ingredient_name', 'quantity', 'measure']
    ingredient_dictionary = {}
    cook_book = {}
    dish = []
    counter = []
    ingredient = []
    for item in save_file_as_list():
        if not item.isdigit() and '|' not in item and item != '':
            dish.append(item)
        if item.isdigit():
            counter.append(item)
        if '|' in item:
            count = 0
            ingredient_dictionary = {}
            for parameter in item.split(' | '):
                ingredient_dictionary[ingredient_params[count]] = parameter
                count += 1
            ingredient.append(ingredient_dictionary)
    count = 0
    for dish_num in range(len(dish)):
        ingredients_count = int(counter[dish_num])
        cook_book[dish[dish_num]] = ingredient[count:count + ingredients_count]
        count += ingredients_count

    return cook_book


# составляем шоппинг лист: 
def get_shop_list_by_dishes(dishes, person_count):
    shoppinglist_dict = {}
    ingredient_list = []
    cook_book = convert_list_to_dictionary()
    for dish in dishes:
        if dish in cook_book:
            ingredient_list = cook_book.get(str(dish))
        for ingredient in ingredient_list:
            if ingredient['ingredient_name'] not in shoppinglist_dict.keys():
                shoppinglist_dict[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': 0}
            shoppinglist_dict[ingredient['ingredient_name']]['quantity'] += (
                int(ingredient['quantity'])) * person_count

    return shoppinglist_dict


print(convert_list_to_dictionary())
print()
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
