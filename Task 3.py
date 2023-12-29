data = open(r"C:\Users\Callipolis\Documents\GitHub\Advent-of-Code-2023\Task 3 data.txt", "r")
data = data.read()
# print(data)

# data_list = ["467..114..",
#               "...*......",
#               "..35..633.",
#               "......#...",
#               "617*......",
#               ".....+.58.",
#               "..592.....",
#               "......755.",
#               "...$.*....",
#               ".664.598.."]


def split_into_chunks(data, chunk_length):
    data_list = []
    data = data.replace('\n', '')
    
    for i in range(0, len(data), chunk_length):
        data_list.append(data[i:i + chunk_length])

    return data_list

def find_special_characters(data_list):
    list_of_special_characters = []

    for item in data_list:
        for i in item:
            if not i.isnumeric() and not i.isalpha() and i != "." and i not in list_of_special_characters:
                list_of_special_characters.append(i)

    return list_of_special_characters

def get_digit_positions (data_list):
    list_of_digit_positions = []
    
    for item in data_list:
        positions = []
        character_position = 0
        
        for character in item:
            if character.isnumeric():
                positions.append(character_position)
            
            character_position += 1
            
        list_of_digit_positions.append(positions)
        
    # print(list_of_positions)
    return list_of_digit_positions 

def get_all_numbers(list_of_digit_positions):
    list_of_numbers = []
    
    for i, positions_in_item in enumerate(list_of_digit_positions):
        number_string = ""
        previous_position = ""
        for position in positions_in_item:
            if previous_position == "" or previous_position + 1 == position:
                number_string += data_list[i][position]
                previous_position = position
                if position == positions_in_item[len(positions_in_item) - 1]:
                    list_of_numbers.append(number_string)
                    
            else:
                if number_string != "":
                    list_of_numbers.append(number_string)
                number_string = data_list[i][position]
                previous_position = ""
                
    # print(list_of_numbers)
    return list_of_numbers
            

# def find_number_in_list(list_of_numbers):
#     list_of_number_positions = []
#     list_of_previous_numbers = []
    
#     for number in list_of_numbers:
        
#         if number not in list_of_previous_numbers:
#             list_of_previous_numbers.append(number)
#             for item in data_list:
#                 number_starting_position = item.find(number)
#                 if number_starting_position != -1 and number_starting_position + len(number) == "." or number_starting_position != -1 and number_starting_position + len(number) in list_of_special_characters or number_starting_position != -1 and number_starting_position + len(number) <= len(item) or number_starting_position != -1 and len(number) == 1:
#                     list_of_number_positions.append(number_starting_position)
#                     break
                
#         elif number in list_of_previous_numbers:
#             number_of_previous_occurances = list_of_previous_numbers.count(number)
            
#             for item in data_list:
#                 if number_of_previous_occurances > 0:
#                     is_it_found = item.find(number)
#                     if is_it_found != -1:
#                         number_of_previous_occurances -= 1
                        
#                 elif number_of_previous_occurances == 0:
#                     number_starting_position = item.find(number)
#                     if number_starting_position != -1 and number_starting_position + len(number) == "." or number_starting_position != -1 and number_starting_position + len(number) in list_of_special_characters or number_starting_position != -1 and number_starting_position + len(number) <= len(item) or number_starting_position != -1 and len(number) == 1:
#                         number_of_previous_occurances -= 1
#                         list_of_previous_numbers.append(number)
#                         list_of_number_positions.append(number_starting_position)
#                         break
    
#     return (list_of_number_positions, list_of_previous_numbers)

def check_for_duplication_of_numbers(list_of_numbers):
    check_list = []
    for number in list_of_numbers:
        print(number)
        if number in check_list:
            print(f"There is duplication for {number}!")
        else:
            check_list.append(number)
            
def check_if_it_is_entire_number(item, number):
        number_position = item.find(number)
        if number_position != 0 and item[number_position - 1].isnumeric():
            return False
        elif number_position + len(number) == len(item) and not item[number_position - 1].isnumeric():
            return True
        elif number_position == 0 and not item[number_position + len(number)].isnumeric():
            return True
        elif item[number_position + len(number)].isnumeric() or item[number_position - 1].isnumeric():
            return False
        else:
            return True

def get_list_of_final_numbers():
    list_of_final_numbers = []
    list_of_previous_numbers = []
    # ISMÉTLŐDŐ SZÁMOKAT KELL MEGOLDANI
    
    for number in list_of_numbers:
        number_of_previous_occurances = list_of_previous_numbers.count(number)
        
        for item_position, item in enumerate(data_list):
            # number_position = list_of_number_positions[i]
            if number in item:
                
                if number not in list_of_previous_numbers:
                    list_of_previous_numbers.append(number)
                    
                    if check_if_it_is_entire_number(item, number):
                        number_position = item.find(number)
                        if check_if_special_character_before_examined_number(number, number_position, item):
                            list_of_final_numbers.append(number)
                            break
                        elif check_if_special_character_after_examined_number(number, number_position, item):
                            list_of_final_numbers.append(number)
                            break
                        elif check_if_special_character_above_examined_number(number, number_position, item_position):
                            list_of_final_numbers.append(number)
                            break
                        elif check_if_special_character_below_examined_number(number, number_position, item_position):
                            list_of_final_numbers.append(number)
                            break
                        break
                
                    else:
                        continue
                    
                
                elif number in list_of_previous_numbers:
                    
                    if number_of_previous_occurances > 0:
                        number_of_previous_occurances -= 1
                        continue
                        
                    elif number_of_previous_occurances == 0:
                        list_of_previous_numbers.append(number)
                        number_position = item.find(number)
                        if check_if_special_character_before_examined_number(number, number_position, item):
                            list_of_final_numbers.append(number)
                            break
                        elif check_if_special_character_after_examined_number(number, number_position, item):
                            list_of_final_numbers.append(number)
                            break
                        elif check_if_special_character_above_examined_number(number, number_position, item_position):
                            list_of_final_numbers.append(number)
                            break
                        elif check_if_special_character_below_examined_number(number, number_position, item_position):
                            list_of_final_numbers.append(number)
                            break
                        break

    return list_of_final_numbers
    
def check_if_special_character_before_examined_number(number, number_position, item):
    if number_position != 0:
        return item[number_position - 1] in list_of_special_characters
    else:
        return False

def check_if_special_character_after_examined_number(number, number_position, item):
    if number_position + len(number) < len(item):
        return item[number_position + len(number)] in list_of_special_characters
    else:
        return False

def check_if_special_character_above_examined_number(number, number_position, item_position):
    if item_position != 0:
        item_to_be_examined = data_list[item_position - 1]
    else:
        return False
        
    if number_position != 0 and number_position != len(item_to_be_examined) - len(number):
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + (len(number) + 1)
        characters_examined = item_to_be_examined[exam_starting_point:exam_end_point:]
        for special_character in list_of_special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue
    
    elif number_position == 0:
        exam_starting_point = int(number_position)
        exam_end_point = len(number) + 1
        characters_examined = item_to_be_examined[exam_starting_point:exam_end_point:]
        for special_character in list_of_special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue
    
    elif number_position == len(item_to_be_examined) - len(number):
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + len(number)
        characters_examined = item_to_be_examined[exam_starting_point:exam_end_point:]
        for special_character in list_of_special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue

def check_if_special_character_below_examined_number(number, number_position, item_position):
    if item_position != len(data_list) - 1:
        item_to_be_examined = data_list[item_position + 1]
    else:
        return False
        
    if number_position != 0 and number_position != len(item_to_be_examined) - len(number):
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + (len(number) + 1)
        characters_examined = item_to_be_examined[exam_starting_point:exam_end_point:]
        for special_character in list_of_special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue
        
    elif number_position == 0:
        exam_starting_point = int(number_position)
        exam_end_point = len(number) + 1
        characters_examined = item_to_be_examined[exam_starting_point:exam_end_point:]
        for special_character in list_of_special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue
    
    elif number_position == len(item_to_be_examined) - len(number):
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + len(number)
        characters_examined = item_to_be_examined[exam_starting_point:exam_end_point:]
        for special_character in list_of_special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue        

# def delete_inappropriate_number(list_of_numbers, inappropriate_number):
#     list_of_numbers.remove(inappropriate_number)

def get_sum_of_numbers(list_of_numbers):
    sum_of_numbers = 0
    
    for number in list_of_numbers:
        number = int(number)
        sum_of_numbers = sum_of_numbers + number
    
    print(sum_of_numbers)

data_list = split_into_chunks(data, 10)
# print(data_list)
list_of_special_characters = find_special_characters(data_list)
# print(list_of_special_characters)
list_of_digit_positions = get_digit_positions(data_list)
# print(list_of_digit_positions)
list_of_numbers = get_all_numbers(list_of_digit_positions)
# check_for_duplication_of_numbers(list_of_numbers)
# print(list_of_numbers)
# (list_of_number_positions, list_of_previous_numbers) = find_number_in_list(list_of_numbers)
# print(list_of_number_positions)
list_of_final_numbers = get_list_of_final_numbers()
check_for_duplication_of_numbers(list_of_final_numbers)
# print(list_of_final_numbers)
get_sum_of_numbers(list_of_final_numbers)
