import datetime


class Ingredients:
    
    start = None


    def __init__(self, ingredients_path):
        self.ingredients_path = ingredients_path
        

    def __enter__(self):
        self.start = datetime.datetime.now()
        print('Время начала работы кода:', self.start)
        return open(self.ingredients_path, 'r', encoding='utf8')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.ingredients_path.close()
        end_time = datetime.datetime.now()
        print('Время окончания работы кода:', end_time)
        print('Продолжительность работы кода:', end_time - self.start)




def create_dictionaty(raw_data):
    recipes_dict = {}
    for data in raw_data.split('\n\n'):
        dish_name = data.split('\n')
        recipes_dict[dish_name[0]] = []
        for items in dish_name[2:]:
            ingridients_list = items.split(' | ')
            recipes_dict[dish_name[0]].append({'ingredient_name' : ingridients_list[0] , 'quantity' : ingridients_list[1] , 'measure' : ingridients_list[2]})
    return recipes_dict



def get_shop_list_by_dishes(dishes, person_count):
    temp_dish_list = []
    temp_dict = {}
    temp_dict = create_dictionaty(data)
    for dishes_names in create_dictionaty(data).keys():
        temp_dish_list.append(dishes_names)
    result_list = list(set(temp_dish_list) & set(dishes))
    for dish_name in result_list:
        for i in temp_dict[dish_name]:
            result_dict = {}
            result_dict[i['ingredient_name']] = {'quantity' : int(i['quantity']) * int(person_count) , 'measure' : i['measure']}

if __name__ == '__main__':
    with Ingredients('recipes.txt') as raw_data:
        data = raw_data.read()
        create_dictionaty(data)
        get_shop_list_by_dishes(['Утка по-пекински', 'Омлет' , 'Запеченный картофель'] , 3)

