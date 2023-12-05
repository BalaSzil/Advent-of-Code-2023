data = open(r"C:\Users\Callipolis\Documents\GitHub\Advent of Code 2023\Task 1 data.txt", "r")
data_list = data.readlines()

# data_list = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

list_of_numbers = []
sum_of_numbers = 0

number_words = {"one" : ("1"), "two" : ("2"), "three" : ("3"), "four" : ("4"), "five" : ("5"), "six" : ("6"), "seven" : ("7"), "eight" : ("8"), "nine" : ("9")}


def is_there_written_number_in_item(item):
    written_number_in_item = False
    
    for written_number in number_words:        
        if written_number in item:
            written_number_in_item = True
            break
    
    return written_number_in_item

def is_there_digit_in_item(item):
    digit_in_item = False
    
    for character in item[::]:
        if character.isnumeric():
            digit_in_item = True
            break
    
    return digit_in_item
    

def get_first_digit_position(item):
    for character_moving_forward in item[::]:
        if character_moving_forward.isnumeric():
            digit = character_moving_forward
            first_digit_position = item.find(digit)
            break
    return first_digit_position

def get_last_digit_position(item):
    for character_moving_backward in item[::-1]:
        if character_moving_backward.isnumeric():
            digit = character_moving_backward
            last_digit_position = item.find(digit)
            break
    return last_digit_position

def get_first_written_number_position(item):
    written_number_positions = []
    for written_number in number_words:
        if written_number in item:
            written_number_positions.append(item.find(written_number))
    first_written_number_position = min(written_number_positions)
    return first_written_number_position

def get_last_written_number_position(item):
    written_number_positions = []
    for written_number in number_words:
        if written_number in item:
            written_number_positions.append(item.rfind(written_number))
    last_written_number_position = max(written_number_positions)
    return last_written_number_position

def get_first_digit(item):
    for character_moving_forward in item[::]:
        if character_moving_forward.isnumeric():
            first_digit = character_moving_forward
            break
    return first_digit
    
def get_last_digit(item):
    for character_moving_backward in item[::-1]:
        if character_moving_backward.isnumeric():
            last_digit = character_moving_backward
            break
    return last_digit

def get_first_written_number(item, first_written_number_position):
    for written_number in number_words:
        first_written_number = item.find(written_number, first_written_number_position, first_written_number_position + len(written_number))
        if first_written_number != -1:
            break
    first_written_number = number_words[written_number][0]
    return first_written_number
    
def get_last_written_number(item, last_written_number_position):
    for written_number in number_words:
        last_written_number = item.find(written_number, last_written_number_position)
        if last_written_number != -1:
            break
    last_written_number = number_words[written_number][0]
    return last_written_number

def is_there_written_number_before_first_digit(written_number_position, digit_position):
    if written_number_position < digit_position:
        return True
    else:
        return False
    
def is_there_written_number_after_last_digit(written_number_position, digit_position):
    if written_number_position > digit_position:
        return True
    else:
        return False
    
def get_digits():
    
    for item in data_list:
        
        if is_there_written_number_in_item(item):
            
            if is_there_digit_in_item(item):
        
                first_written_number_position = get_first_written_number_position(item)
                first_digit_position = get_first_digit_position(item)
                
                last_written_number_position = get_last_written_number_position(item)
                last_digit_position = get_last_digit_position(item)
                        
                if is_there_written_number_before_first_digit(first_written_number_position, first_digit_position): 
                    first_digit = get_first_written_number(item, first_written_number_position)
        
                else:
                    first_digit = get_first_digit(item)
                    
                if is_there_written_number_after_last_digit(last_written_number_position, last_digit_position):
                    last_digit = get_last_written_number(item, last_written_number_position)
                    
                else:
                    last_digit = get_last_digit(item)
                
                item_number = int(first_digit + last_digit)
                list_of_numbers.append(item_number)
            
            if not is_there_digit_in_item(item):
                
                first_written_number_position = get_first_written_number_position(item)
                last_written_number_position = get_last_written_number_position(item)
                
                first_digit = get_first_written_number(item, first_written_number_position)
                last_digit = get_last_written_number(item, last_written_number_position)
                
                item_number = int(first_digit + last_digit)
                list_of_numbers.append(item_number)
        
        else:
            
            first_digit_position = get_first_digit_position(item)
            last_digit_position = get_last_digit_position(item)
            first_digit = get_first_digit(item)
            last_digit = get_last_digit(item)
            
            item_number = int(first_digit + last_digit)
            list_of_numbers.append(item_number)
        
    return list_of_numbers
        
       
def add_numbers():
   
    sum_of_numbers = 0
    
    for number in list_of_numbers:
        number = int(number)
        sum_of_numbers = sum_of_numbers + number
    
    print(sum_of_numbers)

# test_item = "sasdeight6eight"
# first_digit_position = get_first_digit_position(test_item)
# print(f"first digit position: {first_digit_position}")
# first_digit = get_first_digit(test_item)
# print(f"first digit: {first_digit}")

# last_digit_position = get_last_digit_position(test_item)
# print(f"last digit position: {last_digit_position}")
# last_digit = get_last_digit(test_item)
# print(f"last digit: {last_digit}")

# first_written_number_position = get_first_written_number_position(test_item)
# print(f"first written number position: {first_written_number_position}")
# first_written_number = get_first_written_number(test_item, first_written_number_position)
# print(f"first written number: {first_written_number}")

# last_written_number_position = get_last_written_number_position(test_item)
# print(f"last written number position: {last_written_number_position}")
# last_written_number = get_last_written_number(test_item, last_written_number_position)
# print(f"last written number: {last_written_number}")

get_digits()
add_numbers()

print(list_of_numbers)

# HA NINCS DIGIT