# raw_input = open(r"C:\Users\Callipolis\Documents\GitHub\Advent-of-Code-2023\Task 3 data.txt", "r")
# raw_input = raw_input.read()

# input_chunks = ["467..114..",
#               "...*......",
#               "..35..633.",
#               "......#...",
#               "617*......",
#               ".....+.58.",
#               "..592.....",
#               "......755.",
#               "...$.*....",
#               ".664.598.."]

input_chunks = ["12.......*..",
              "+.........34",
              ".......-12..",
              "..78........",
              "..*....60...",
              "78..........",
              ".......23...",
              "....90*12...",
              "............",
              "2.2......12.",
              ".*.........*",
              "1.1.......56"]

# input_chunks = ["12.......*..",
#               "+.........34",
#               ".......-12..",
#               "..78........",
#               "..*....60...",
#               "78.........9",
#               ".5.....23..$",
#               "8...90*12...",
#               "............",
#               "2.2......12.",
#               ".*.........*",
#               "1.1..503+.56"]


def split_into_chunks(raw_input, chunk_length):
    input_chunks = []
    raw_input = raw_input.replace('\n', '')
    
    for i in range(0, len(raw_input), chunk_length):
        input_chunks.append(raw_input[i:i + chunk_length])

    return input_chunks



def get_special_characters(input_chunks):
    special_characters = []

    for characters in input_chunks:
        for character in characters:
            if is_it_unique_special_character(character, special_characters):
                special_characters.append(character)

    return special_characters

def is_it_unique_special_character(character, special_characters):
    return not character.isnumeric() and not character.isalpha() and character != "." and character not in special_characters



def get_digit_positions (input_chunks):
    digit_positions = []
    
    for characters in input_chunks:
        positions_in_chunk = []
        character_position = 0
        
        for character in characters:
            if character.isnumeric():
                positions_in_chunk.append(character_position)
            
            character_position += 1
            
        digit_positions.append(positions_in_chunk)
        
    return digit_positions



def get_all_numbers(input_chunks, digit_positions):
    all_numbers = []
    
    for i, positions_in_input_chunk in enumerate(digit_positions):
        number_string = ""
        previous_position = ""
        is_it_first_position = previous_position == ""
        
        for position in positions_in_input_chunk:
            position_of_last_digit, is_previous_position_a_digit, next_character = set_variables_for_get_all_numbers(position, positions_in_input_chunk, previous_position, i)
            is_this_the_last_digit = position == position_of_last_digit
            is_next_character_a_digit = next_character.isnumeric()
            
            
            if is_it_first_position or is_previous_position_a_digit:
                number_string = add_character_to_string(number_string, input_chunks, i, position)
                
                if is_this_the_last_digit:
                    all_numbers, number_string = add_number_to_all_numbers_and_reset_string(all_numbers, number_string)
                    
                elif not is_next_character_a_digit:
                    all_numbers, number_string = add_number_to_all_numbers_and_reset_string(all_numbers, number_string)
                    
                previous_position = position
                
    return all_numbers

def add_character_to_string(number_string, input_chunks, chunk, position):
    number_string += input_chunks[chunk][position]
    
    return number_string
    
def set_variables_for_get_all_numbers(position, positions_in_input_chunk, previous_position, i):
    position_of_last_digit = positions_in_input_chunk[len(positions_in_input_chunk) - 1]
    position_of_next_digit = position + 1
    last_position = len(input_chunks[i]) - 1
    
    if previous_position != "":
        if str(previous_position).isnumeric() == True:
            is_previous_position_a_digit = True
        else:
            is_previous_position_a_digit = False
    else:
        is_previous_position_a_digit = False
        
    if position_of_next_digit <= last_position:
        next_character = input_chunks[i][position_of_next_digit]
    else:
        next_character = ""
        
    return (position_of_last_digit, is_previous_position_a_digit, next_character)

def add_number_to_all_numbers_and_reset_string(all_numbers, number_string):
    all_numbers.append(number_string)
    number_string = ""
    
    return (all_numbers, number_string)



def get_numbers_adjacent_to_symbols():
    numbers_adjacent_to_symbols = []
    numbers_already_checked = []
    
    for number in all_numbers:
        previous_occurances = numbers_already_checked.count(number)
        
        for chunk_position, examined_input_chunk in enumerate(input_chunks):
            
            if number in examined_input_chunk:
                    
                is_this_new_occurance = previous_occurances == 0
                
                if not is_this_new_occurance:
                    previous_occurances -= 1
                    continue
                    
                elif is_this_new_occurance:
                    numbers_already_checked.append(number)
                    
                    if check_if_it_is_entire_number(examined_input_chunk, number):
                        times_number_occurs_in_examined_input_chunk = examined_input_chunk.count(number)
                        
                        if times_number_occurs_in_examined_input_chunk == 1:
                        
                            number_position = examined_input_chunk.find(number)
                            
                            if check_if_special_character_before_examined_number(number, number_position, examined_input_chunk):
                                numbers_adjacent_to_symbols.append(number)
                                break
                            elif check_if_special_character_after_examined_number(number, number_position, examined_input_chunk):
                                numbers_adjacent_to_symbols.append(number)
                                break
                            elif check_if_special_character_above_examined_number(number, number_position, chunk_position):
                                numbers_adjacent_to_symbols.append(number)
                                break
                            elif check_if_special_character_below_examined_number(number, number_position, chunk_position):
                                numbers_adjacent_to_symbols.append(number)
                                break
                            break
    
                        else:
                            break
                        
                    # elif times_number_occurs_in_examined_input_chunk > 1:


    return numbers_adjacent_to_symbols

def check_if_it_is_entire_number(examined_input_chunk, number):
        number_position = examined_input_chunk.find(number)
        is_it_first_position = number_position == 0
        is_it_last_position = number_position + len(number) == len(examined_input_chunk)
        
        if not is_it_first_position:
            character_before_number_position = examined_input_chunk[number_position - 1]
        if not is_it_last_position:
            character_after_number_position = examined_input_chunk[number_position + len(number)]
        
        if is_it_first_position and character_after_number_position.isnumeric():
            return False
        elif is_it_first_position and not character_after_number_position.isnumeric():
            return True
        elif not is_it_first_position and character_before_number_position.isnumeric():
            return False
        elif is_it_last_position and not character_before_number_position.isnumeric():
            return True
        elif is_it_last_position and character_before_number_position.isnumeric():
            return False
        elif character_before_number_position.isnumeric() or character_after_number_position.isnumeric():
            return False
        else:
            return True
        
def check_if_special_character_before_examined_number(number, number_position, examined_input_chunk):
    is_it_first_position = number_position == 0
    
    if is_it_first_position:
        return False
    if not is_it_first_position:
        previous_character = examined_input_chunk[number_position - 1]
        return previous_character in special_characters
    
def check_if_special_character_after_examined_number(number, number_position, examined_input_chunk):
    is_it_last_position = number_position + len(number) == len(examined_input_chunk)
    
    if is_it_last_position:
        return False
    if not is_it_last_position:
        next_character = examined_input_chunk[number_position + len(number)]
        return next_character in special_characters
    
def check_if_special_character_above_examined_number(number, number_position, chunk_position):
    is_it_first_chunk = chunk_position == 0
    
    
    if is_it_first_chunk:
        return False
    elif not is_it_first_chunk:
        chunk_to_be_examined = input_chunks[chunk_position - 1]
        
    is_it_first_position = number_position == 0
    is_it_last_position = number_position == len(chunk_to_be_examined) - len(number)
        
    if not is_it_first_position and not is_it_last_position:
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + (len(number) + 1)
        characters_examined = chunk_to_be_examined[exam_starting_point:exam_end_point:]
        
        check = check_if_there_is_special_character(characters_examined)
    
    elif is_it_first_position:
        exam_starting_point = int(number_position)
        exam_end_point = len(number) + 1
        characters_examined = chunk_to_be_examined[exam_starting_point:exam_end_point:]
        
        check = check_if_there_is_special_character(characters_examined)
    
    elif is_it_last_position:
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + len(number)
        characters_examined = chunk_to_be_examined[exam_starting_point:exam_end_point:]
        
        check = check_if_there_is_special_character(characters_examined)
        
    return check

def check_if_special_character_below_examined_number(number, number_position, chunk_position):
    is_it_last_chunk = chunk_position == len(input_chunks) - 1
    
    if is_it_last_chunk:
        return False
    elif not is_it_last_chunk:
        chunk_to_be_examined = input_chunks[chunk_position + 1]
        
    is_it_first_position = number_position == 0
    is_it_last_position = number_position == len(chunk_to_be_examined) - len(number)
        
    if not is_it_first_position and not is_it_last_position:
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + (len(number) + 1)
        characters_examined = chunk_to_be_examined[exam_starting_point:exam_end_point:]
        
        check = check_if_there_is_special_character(characters_examined)
        
    elif is_it_first_position:
        exam_starting_point = int(number_position)
        exam_end_point = len(number) + 1
        characters_examined = chunk_to_be_examined[exam_starting_point:exam_end_point:]
        
        check = check_if_there_is_special_character(characters_examined)
    
    elif is_it_last_position:
        exam_starting_point = int(number_position) - 1
        exam_end_point = (int(number_position)) + len(number)
        characters_examined = chunk_to_be_examined[exam_starting_point:exam_end_point:]
        
        check = check_if_there_is_special_character(characters_examined)
    
    return check

def check_if_there_is_special_character(characters_examined):
        for special_character in special_characters:
            if special_character in characters_examined:
                return True
                break
            else:
                continue
        
        return False




def get_sum_of_numbers(numbers):
    sum_of_numbers = 0
    
    for number in numbers:
        number = int(number)
        sum_of_numbers = sum_of_numbers + number
    
    print(sum_of_numbers)




# input_chunks = split_into_chunks(raw_input, 10)
special_characters = get_special_characters(input_chunks)
digit_positions = get_digit_positions(input_chunks)
all_numbers = get_all_numbers(input_chunks, digit_positions)
numbers_adjacent_to_symbols = get_numbers_adjacent_to_symbols()
get_sum_of_numbers(numbers_adjacent_to_symbols)