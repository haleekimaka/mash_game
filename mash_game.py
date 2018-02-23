def welcome():
    """Prints the Welcome text"""
    print
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print "Welcome to the MASH fortune teller."
    print "-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print "You will be inputting different values and selecting options.\nThe MASH fortune that will be revealed at the end of the game."
    print
    print "First thing's first... What is your first name?"
    
    #ask for player name
    user_name = raw_input("> ")
    user_name = user_name.title()
    user_name = user_name.strip()
    results_list.append(user_name)
    
    print "-----------------------------------"
    print "Awesome {}, we are going to start, I hope you have some fun with this!".format(user_name)
    return user_name

def user_pick_list_entry(choice):
    """Allows user to pick from choices A or B when prompted, returns choice value."""
    choosing = True
    
    while choosing:
        choice = raw_input("> ")
    
        if choice.isalpha() == True:
            choice = choice.upper()
            
            if (choice == "A") or (choice == "B"):
                choosing = False
                return choice
            else:
                print "That isn't a valid entry, try again."
        
        else:
            print "We didn't recognize that input. Try again."

def print_list(list_choice):  
    """Passes specific list as parameter, and prints that pecific list for users to choose from."""
    order = 0 
    
    for values in list_choice:
        order = order + 1
        print "{}.".format(order), values

def celeb_crushes():
    """Determines which crushes appear on the MASH board"""
    print "-----------------------------------------"
    print "In the world of MASH, entertainment is key."
    print "So we need you to pick 4 celebrity crushes."
    print "-----------------------------------"
    print "Would you like to:\nA. Choose from our list\nB. Enter your own"
    
    selection_1 = ""
    celeb_list_choice = user_pick_list_entry(selection_1)
    
    if celeb_list_choice == "A":
        print "-----------------------------------------"
        print "Cool, which list would you like to see?"
        print "A. Female celebs"
        print "B. Male celebs"
                
        selection_2 = ""
        celeb_gender = user_pick_list_entry(selection_2)
        
        choice_1 = ""
        choice_2 = ""
        choice_3 = ""
        choice_4 = ""
                        
        print "-----------------------------------------"
        print "Select from the following celebrities:"
        print "-----------------------------------------"
                        
        if celeb_gender == "A":
            print_list(female_celebs)
                
            print "-----------------------------------------"
            print "Enter the number of each crush one at a time:"
            user_choices(choice_1, female_celebs, crush_list, "Crush", 1)
            user_choices(choice_2, female_celebs, crush_list, "Crush", 2)
            user_choices(choice_3, female_celebs, crush_list, "Crush", 3)
            user_choices(choice_4, female_celebs, crush_list, "Crush", 4)
            
            results_list.append(crush_list)
            choosing = False
            celeb_choosing = False
                
        elif celeb_gender == "B":
            print_list(male_celebs)
                
            print "-----------------------------------------"
            print "Enter the number of each crush one at a time:"
            user_choices(choice_1, male_celebs, crush_list, "Crush", 1)
            user_choices(choice_2, male_celebs, crush_list, "Crush", 2)
            user_choices(choice_3, male_celebs, crush_list, "Crush", 3)
            user_choices(choice_4, male_celebs, crush_list, "Crush", 4)
            
            results_list.append(crush_list)
            choosing = False
            celeb_choosing = False

    elif celeb_list_choice == "B":
        print "-----------------------------------------"
        print "Sweet enter your celebrity crushes, one at a time:"
        user_entry(crush_1, crush_list, "Crush", 1)
        user_entry(crush_2, crush_list, "Crush", 2)
        user_entry(crush_3, crush_list, "Crush", 3)
        user_entry(crush_4, crush_list, "Crush", 4)
                
        results_list.append(crush_list)
        celeb_choosing = False
        return crush_list
          
    else:
        print "We didn't recognize that input. Try again."

def user_choices(choice_num, given_list, output_list, category, num):
    """Asks for the users choice from a given numbered list, and adds choice to the crush_list"""

    choosing = True
    
    while choosing:
        choice = raw_input("{} Choice #{}> ".format(category, num))
        
        if choice.isdigit() == False:
            print "Oops! That isn't a number, try again."
            
        elif (int(choice) > 0) and (int(choice) <= (len(given_list))):
            choice_num = given_list[int(choice) - 1]
            
            if choice_num in output_list:
                print "You've already selected that option, please choose another."
            
            else:
                output_list.append(choice_num)
                choosing = False
                return choice_num
        
        else:
            print "I didn't understand that selection, try again."

def user_entry(entered_choice, any_list, category, num):
    """Allows user to enter their own values for crushes or jobs, checks for legal entry before adding to respective list"""
    choosing = True
   
    while choosing:
        #prompt user for entry of their choices
        entered_choice = raw_input("{} Choice #{}> ".format(category, num))
        entered_choice = entered_choice.title()
        
        if entered_choice.isdigit() == True:
            print "Oops, a number is not a valid entry. Try again."
            
        elif entered_choice in any_list:
            print "Oops can't enter the same choice twice."
            
        else:
            any_list.append(entered_choice)
            choosing = False
            return entered_choice

def user_nums():
    """Get four unique numbers from the user that will appear in the MASH board"""
    
    print "-----------------------------------------"
    print "Numbers are your friend!!! "
    print "Time to pick 4 of them, any numbers will do, but they can't be the same."
    print "-----------------------------------------"
    
    duplicate_alpha(num_1, 1)
    duplicate_alpha(num_2, 2)
    duplicate_alpha(num_3, 3)
    duplicate_alpha(num_4, 4)

    results_list.append(num_list)
    return num_list

def duplicate_alpha(num_entry, num):
    """Checks if what was entered is a number and if it's a duplicate, if it meets the criteria, entry added to num_list"""
    checking = True
    
    while checking:
        num_entry = raw_input("Number #{}> ".format(num))
        if len(num_list) == 0:
            
            alpha = True
            
            while alpha:
                if num_entry.isalpha() == True:
                    print "Oops! That isn't a number, try again."
                    alpha = False
                    
                else:
                    num_list.append(num_entry)
                    alpha = False
                    checking = False
    
        elif num_entry.isdigit() == False:
            print "Oops! That isn't a number, try again."
            
        elif num_entry in num_list:
            print "Oops, that number is already in the list! Choose another one."
        
        else:
            num_list.append(num_entry)
            checking = False
            return num_entry
    
def jobs_module():
    """Determines which jobs appear on the MASH board"""
    
    print "-----------------------------------------"
    print "Work makes the world go round..."
    print "So we need you to pick 4 ideal professions."
    print "-----------------------------------"
    print "Would you like to:\nA. Choose from our list\nB. Enter your own"
    
    job_list_choice = ""
    job_list_choice = user_pick_list_entry(job_list_choice)
    
    if job_list_choice == "A":
        print "-----------------------------------------"
        print "Select from the following jobs:"
        print "-----------------------------------------"
        
        print_list(given_job_list)
            
        print "-----------------------------------------"
        print "Enter the number of each job one at a time:"
        user_choices(job_1, given_job_list, job_list, "Job", 1)
        user_choices(job_2, given_job_list, job_list, "Job", 2)
        user_choices(job_3, given_job_list, job_list, "Job", 3)
        user_choices(job_4, given_job_list, job_list, "Job", 4)

        results_list.append(job_list)
        return job_list

    elif job_list_choice == "B":
        print "-----------------------------------------"
        print "Cool! If you could be anything, what would you be????"
        print "Enter 4 dream jobs, sky's the limit, but they can't be the same."
        print "-----------------------------------------"

        user_entry(job_1, job_list, "Job", 1)
        user_entry(job_2, job_list, "Job", 2)
        user_entry(job_3, job_list, "Job", 3)
        user_entry(job_4, job_list, "Job", 4)
        
        results_list.append(job_list)
        return job_list
        
def iterations_choice(any_list):
    """Determine how many spaces to count before eliminating a value"""
    print "-----------------------------------------"
    print "In order to determine your MASH fortune, "
    print "pick a number between 2 and 16."
    print "-----------------------------------"
    
    choosing = True
    
    while choosing:
        choice = raw_input("Choice> ")
        
        if choice.isalpha() == True:
            print "Oops! That isn't a number, try again."
            
            
        elif (int(choice) >= 2) and (int(choice) <= 16):
            any_list.append(choice)
            choosing = False
            
        else:
            print "Selection out of range, please choose a number between 2 and 16."

    return any_list  

def create_new_list(iterable_list, other_list):
    """for each array at a list index, extend a new list with the indexed values, to have a list to iterate on for elimination logic"""

    for values in iterable_list[0]:
        other_list.append(values)
    
    for values in iterable_list[1]:
        other_list.append(values)
    
    for values in iterable_list[2]:
        other_list.append(values)

    mash = ["mansion", "apartment", "shack", "house"]
    
    for values in mash:
        other_list.append(values)
                      
    return other_list

def create_dictionary(empty_dict, other_list):
    key = 1
    
    for values in other_list:
        
        empty_dict[key] = values
        key += 1
        
    return empty_dict
   
def show_board(start_list):
    """Print the MASH board for the first time"""
    print "-----------------------------------------"
    print "This is your starting MASH board."
    print "-----------------------------------------"
  
    mash_board = ["",
               "-*-*-*-*-*-*-*-*-*-*-*|    {}    |    {}    |    {}    |    {}    |-*-*-*-*-*-*-*-*-*-*-*".format(mansion,apt,shack,house), 
               "--------------------------------------------------------------------------------------------",
               "{}  |                                       | {}                    ".format(start_list[1][0].ljust(20,), start_list[3][3]),
               "{}  |              STARTING                 | {}                    ".format(start_list[1][1].ljust(20,), start_list[3][2]),
               "{}  |               BOARD                   | {}                    ".format(start_list[1][2].ljust(20,), start_list[3][1]),
               "{}  |                                       | {}                    ".format(start_list[1][3].ljust(20,), start_list[3][0]),
               "-------------------------------------------------------------------------------------------------",
               "-*-*-*-*-*-*-*-*-*-*-*|  {}  |  {}  |  {}  |  {}  |-*-*-*-*-*-*-*-*-*-*-*".format(start_list[2][0], start_list[2][1], start_list[2][2], start_list[2][3]),
               "",]
    
    for rows in mash_board:
        print rows

    print "-----------------------------------------"
    continue_entry = raw_input("Press 'ENTER' key to continue.")
    print "-----------------------------------------"        

    return start_list

def argument_2_check(dict_key, any_dict):
    """Checks to see if there the key value is an eliminated value, returns a True or False"""
    if "-" in any_dict[dict_key]:
        return True
    else:
        return False
    
def argument_3_check(dict_key, secondary_list):
    """Checks the secondary list to make sure the category actually has values to eliminate (returns a False boolean)"""
    break_command = []
    position = dict_key
       
    check_1 = bool(sum(secondary_list[0:4]) == 1)
    check_2 = bool(sum(secondary_list[4:8]) == 1)
    check_3 = bool(sum(secondary_list[8:12]) == 1)
    check_4 = bool(sum(secondary_list[12:]) == 1)
    
    check_list = [check_1,check_2,check_3,check_4]
    
    if check_list == [True,True,True,True]:
        break_command.append("Break")
        # print "Set break command." #TESTLINE
    
    elif (position > 0) and (position < 5):
        return check_1
        
    elif (position >= 5) and (position < 9):
        return check_2
        
    elif (position >= 9) and (position < 13):
        return check_3
        
    elif (position >= 13) and (position <= 16):
        return check_4
        
    else:
        print "fail check_logic"
        break_command.append("Break")

def show_results(final_list):
    """Based on the iterations selected/indicated, the results_list passed through the elimination logic and those results will be shown on the MASH board"""
    print "-----------------------------------------"
    print "This is your final MASH board, but what does it mean????"
    print "-----------------------------------------"   

    results_board = ["",
           "-*-*-*-*-*-*-*-*-*-*-*|    {}    |    {}    |    {}    |    {}    |-*-*-*-*-*-*-*-*-*-*-*".format(final_list[12], final_list[13], final_list[14], final_list[15]), 
           "--------------------------------------------------------------------------------------------",
           "{}  |                                       | {}                    ".format(final_list[0].ljust(20,), final_list[8]),
           "{}  |              RESULTS                  | {}                    ".format(final_list[1].ljust(20,), final_list[9]),
           "{}  |               BOARD                   | {}                    ".format(final_list[2].ljust(20,), final_list[10]),
           "{}  |                                       | {}                    ".format(final_list[3].ljust(20,), final_list[11]),
           "-------------------------------------------------------------------------------------------------",
           "-*-*-*-*-*-*-*-*-*-*-*|  {}  |  {}  |  {}  |  {}  |-*-*-*-*-*-*-*-*-*-*-*".format(final_list[4], final_list[5], final_list[6], final_list[7]),
           "",]


    for rows in results_board:
        print rows
    
    continue_entry = raw_input("Press 'ENTER' key to continue.")

    return final_list

def elimination_logic(any_dict, parallel_list, iterations_num, command):
    """Runs the elimination_logic, checking arguments to ensure legal eliminations, returns results_dict """
    elimination_count = 0

    while sum(parallel_list) > 4: 
    
        for key in any_dict:
            
            argument_2 = argument_2_check(key, any_dict) 
            argument_3 = argument_3_check(key, parallel_list)
    
            if "Break" in command:
                break
            
            elif (argument_2 == True) or (argument_3 == True):
                continue
            
            elif (argument_2 == False) and (argument_3 == False):
                
                if elimination_count + 1 < iterations_num:
                    elimination_count += 1
                    continue
                
                elif (key > 0) and (key < 5):
                    any_dict[key] = "--------------------"
                    parallel_list[key - 1] = 0
                    elimination_count = 0
                
                elif (key >= 5) and (key < 9):
                    any_dict[key] = "------"
                    parallel_list[key - 1] = 0
                    elimination_count = 0
                    
                elif (key >= 9) and (key < 13):
                    any_dict[key] = "--------------------"
                    parallel_list[key - 1] = 0
                    elimination_count = 0
                
                elif (key >= 13) and (key <= 16):
                    any_dict[key] = "--"
                    parallel_list[key - 1] = 0
                    elimination_count = 0
                    
                else:
                    command.append("Break")
        
            else:
                command.append("Break")

def create_fortune_list(any_dict, iterations, name):
    """Takes results_dict and extracts values by key, then appends back the popped iterations and player_name""" 
    fortune_list = []
    
    for key in any_dict:
        fortune_list.append(any_dict[key])
        
    fortune_list.append(iterations)
    fortune_list.append(player_name)
    
    return fortune_list   

def mash_fortune(any_list, final_list):
    """Print user their fortune from the remaining values on the MASH board"""
    print "-----------------------------------------"
    print "This is your MASH fortune:"
    print "-----------------------------------------"
    
    for values in any_list:
        if type(values) == int:
            final_list.append(values)
            
        elif "-" in values:
            pass
        else:
            final_list.append(values)

    if int(final_list[4]) % 2 == 0:
        final_list[0] = final_list[0].strip()
                    
        print "Well, well... {}, you are certainly lucky in love!".format(final_list[5])
        print "You married your celebrity crush, {}.".format(final_list[0]) 
        print "Together you live in a fabulous {} in the Hollywood Hills.".format(final_list[3])
        print "After working {} different jobs, you finally landed your dream job as a {}.".format(final_list[1],final_list[2])
        print "This will certainly help you feed your {} children.".format(final_list[4])
        print "Life is GOOD."
        print "-----------------------------------------"
    
        return final_list
        
    else:
        final_list[0] = final_list[0].strip()
        
        print "Dreams do come true {}!".format(final_list[5])
        print "After getting engaged to {}, you both moved into a {} in Malibu.".format(final_list[0], final_list[3]) 
        print "This will be marriage #{} for you, but you know it will be your last.".format(final_list[4])
        print "You currently are a {} in downtown LA, and your new commmute will only take {} hours.".format(final_list[2], final_list[1])
        print "Life is GOOD."
        print "-----------------------------------------"
        
        return final_list

def game_over():
    """Thank user for playing indicates end of game"""
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print
    print "GAME OVER -- Thanks for playing!"
    print
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

# GLOBAL VARIABLES
results_list = []
fortune_list = []
num_list = []
crush_list = []
job_list = []
break_command = []
final_list = []
female_celebs = ["Giselle Bundchen", "Lady Gaga", "Tyra Banks", "Beyonce", "Scarlett Johansson", "Liv Tyler", "Charlize Theron","Meryl Streep","Serena Williams","Mandy Moore","Gabrielle Union","Lucy Liu","Priyanka Chopra","Nicole Kidman","Zoe Saldana"]
male_celebs = ["Tyrese","Chris Hemsworth", "Hugh Jackman", "Denzel Washington", "George Clooney", "Robert Downey Jr.", "Brad Pitt","Zac Efron", "Jamie Foxx","Orlando Bloom","Chris Evans","Adam Levine","LeBron James","Scott Eastwood","Enrique Iglesias"]
given_job_list = ["Janitor","Accountant", "Software Engineer", "Interior Designer", "Stay at Home Parent", "CEO", "Admin", "Pro Sports Player", "Fitness Instructor", "Market Research Analyst","Optometrist","Surgeon","Mechanic","TV Show Host","Model"]
num_1 = ""
num_2 = ""
num_3 = ""
num_4 = ""
crush_1 = ""
crush_2 = ""
crush_3 = ""
crush_4 = ""
job_1 = ""
job_2 = ""
job_3 = ""
job_4 = ""
mansion = "M"
apt = "A"
shack = "S"
house = "H"

#set up empty dictionary with appropriate # of keys (entered as integers) are set to empty values to get a way to work elimination logic
results_dict = {1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:"", 13:"", 14:"", 15:"", 16: ""}

#set up parallel/secondary list to use in arguments used in the elimination logic sequence
secondary_list = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

# ------- BEGIN PROGRAM EXECUTION -------
player_name = welcome()

celeb_crushes()

user_nums()

jobs_module()

show_board(results_list)

results_list = iterations_choice(results_list)

#removes iterations values from results list and assigns to own variable, for use in elimination logic
iterations = int(results_list.pop())

#removes player name
player_name = results_list.pop(0) 

new_list = []
new_list = create_new_list(results_list, new_list)

results_dict = create_dictionary(results_dict, new_list)

elimination_logic(results_dict, secondary_list, iterations, break_command)

fortune_list = create_fortune_list(results_dict, iterations, player_name)

show_results(fortune_list)

mash_fortune(fortune_list, final_list)

game_over()




