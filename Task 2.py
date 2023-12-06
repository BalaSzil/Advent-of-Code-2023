data = open(r"C:\Users\Callipolis\Documents\GitHub\Advent-of-Code-2023\Task 2 data.txt", "r")
data_list = data.readlines()

# data_list = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#              "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#              "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#              "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#              "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

def get_list_of_game_rounds(data_list):
    list_of_game_rounds = []
    
    for game_round in data_list:
        
        number_of_game_round = game_round.split(":")[0]        
        list_of_game_rounds.append(number_of_game_round)
    
    return list_of_game_rounds
        
def get_list_of_colors_and_draws(data_list):
    list_of_colors_and_draws = []
        
    for game_round in data_list:
        
        colors_and_draws = game_round.split(":")[1]
        list_of_colors_and_draws.append(colors_and_draws)

    return list_of_colors_and_draws

def get_individual_draws(list_of_colors_and_draws):
    list_of_draws = []
    for draw in list_of_colors_and_draws:
        list_of_draws.append(draw.split(";"))

    return list_of_draws

def count_number_per_color():
    reds = []
    blues = []
    greens = []
    
    for draw in list_of_draws:
        reds_in_draw = []
        blues_in_draw = []
        greens_in_draw = []
        
        for item in draw:
            if "red" in item:
                red_position = item.find(" red")
                if item[red_position - 2].isnumeric():
                    red = int(item[red_position - 2] + (item[red_position - 1]))
                    reds_in_draw.append(red)
                else:
                    red = int(item[red_position - 1])
                    reds_in_draw.append(red)
            
            if " blue" in item:
                blue_position = item.find(" blue")
                if item[blue_position - 2].isnumeric():
                    blue = int(item[blue_position - 2] + (item[blue_position - 1]))
                    blues_in_draw.append(blue)
                else:
                    blue = int(item[blue_position - 1])
                    blues_in_draw.append(blue)
        
            if " green" in item:
                green_position = item.find(" green")
                if item[green_position - 2].isnumeric():
                    green = int(item[green_position - 2] + (item[green_position - 1]))
                    greens_in_draw.append(green)
                else:
                    green = int(item[green_position - 1])
                    greens_in_draw.append(green)
                
        reds.append(reds_in_draw)
        blues.append(blues_in_draw)
        greens.append(greens_in_draw)
        
    return (reds, blues, greens)

def get_highest_number_of_color_for_each_game(color):
    highest_numbers = []
    
    for i in color:
        highest_numbers.append(max(i))
    
    return highest_numbers

def get_power_of_color_numbers():
    list_of_powers = []
    
    for i in range(len(highest_reds)):
        power = highest_reds[i] * highest_blues[i] * highest_greens[i]
        list_of_powers.append(power)
        
    return list_of_powers

def sum_up_powers():
    end_sum = 0
    
    for i in power_of_color_numbers:
        end_sum = end_sum + i
        
    return(end_sum)
    
# def check_if_color_number_is_below_limit(color, limit):
#     list_of_booleans = []

# def check_if_color_number_is_below_limit(color, limit):
#     list_of_booleans = []
    
#     for draw in color:
        
#         if max(draw) <= limit:
#             list_of_booleans.append(True)
#         elif max(draw) > limit:
#             list_of_booleans.append(False)
        
    
    # for draw in color:
    #     number_of_color_cubes_in_draw = 0
        
    #     for i in range(len(draw)):
    #         number_of_color_cubes_in_draw = number_of_color_cubes_in_draw + draw[i]
            
    #     if number_of_color_cubes_in_draw <= limit:
    #         list_of_booleans.append(True)
    #     elif number_of_color_cubes_in_draw > limit:
    #         list_of_booleans.append(False)
    
    # return list_of_booleans

# def check_if_game_is_possible():
#     list_of_game_possibilities = []
    
#     for game in range(len(is_red_possible)):
#         if is_red_possible[game] is True and is_blue_possible[game] is True and is_green_possible[game] is True:
#             list_of_game_possibilities.append(True)
#         else:
#             list_of_game_possibilities.append(False)
    
#     return list_of_game_possibilities
        

# def sum_up_IDs_of_possible_games():
#     sum_of_possible_game_IDs = 0
    
#     for game in range(len(list_of_game_possibilities)):
#         if list_of_game_possibilities[game] == True:
#             sum_of_possible_game_IDs = sum_of_possible_game_IDs + game + 1
            
#     return sum_of_possible_game_IDs

list_of_game_rounds = get_list_of_game_rounds(data_list)
# print(list_of_game_rounds)
list_of_colors_and_draws = get_list_of_colors_and_draws(data_list)
# print(list_of_colors_and_draws)
list_of_draws = get_individual_draws(list_of_colors_and_draws)
# print(list_of_draws)
(reds, blues, greens) = count_number_per_color()
# print(reds)
# print(blues)
# print(greens)
# is_red_possible = check_if_color_number_is_below_limit(reds, 12)
# is_blue_possible = check_if_color_number_is_below_limit(blues, 14)
# is_green_possible = check_if_color_number_is_below_limit(greens, 13)
# print(is_red_possible)
# print(is_blue_possible)
# print(is_green_possible)
# list_of_game_possibilities = check_if_game_is_possible()
# sum_of_possible_game_IDs = sum_up_IDs_of_possible_games()
# print(sum_of_possible_game_IDs)

highest_reds = get_highest_number_of_color_for_each_game(reds)
highest_blues = get_highest_number_of_color_for_each_game(blues)
highest_greens = get_highest_number_of_color_for_each_game(greens)
power_of_color_numbers = get_power_of_color_numbers()
sum_of_powers = sum_up_powers()
print(sum_of_powers)