
class loads():
    def get_list_country():
        list1 = list()
        with open("4.Hangman/countries.txt", 'r') as f:
            for line in f:
                list1.append(line.rstrip('\n'))
            return list1
    
    def get_list_food_beverages():
        list2 = list()
        with open("4.Hangman/food.txt", 'r') as g:
            for line in g:
                list2.append(line.rstrip('\n'))
            return list2