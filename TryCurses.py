import re
import os

directory = '.'
files = os.listdir(directory)

condition_list = []
final_state_list = []
rule_list = []

initial_condition = ""
finite_state = ""


def print_files_on_dir():
    n = 0   
    print ('')
    print ('')
    print ('===List of files===')
    print ('')
    print ('')
    while n < len(files):
        name_of_file = files[n]
        result_string = "[" + str(n) + "]" + " - " + name_of_file
        print (result_string)
        n += 1
    print ('')
    print ('')
    print ('===================')
    print ('')
    print ('Select FILE with tests. Enter the number:')

    
def find_conditions(file_path, type_condition):
    f = open(file_path, 'r', encoding='utf-8')

    for line in f:
        if type_condition == "initial":
            pattern_for_state = re.findall(r'^\w+',line)
        else:
            pattern_for_state = re.findall(r'\w+$',line)
            
        n = 0
        equal_file = False
        
        if type_condition == "initial":
            while n < len(condition_list):
                if condition_list[n] == pattern_for_state:
                    equal_file = True
                n += 1
            if equal_file == False:
                condition_list.append(pattern_for_state)
            else:
                equal_file = False
        else:
            while n < len(final_state_list):
                if final_state_list[n] == pattern_for_state:
                    equal_file = True
                n += 1
            if equal_file == False:
                final_state_list.append(pattern_for_state)
            else:
                equal_file = False
                
    f.close()
    n = 0
    print ('')
    print ('')
    if type_condition == "initial":
        print ('===List of conditions===')
        print ('')
        print ('')
        while n < len(condition_list):
            condition = condition_list[n]
            result_string = "[" + str(n) + "]" + " - " + str(condition)
            print (result_string)
            n += 1
    else:
        print ('===List of states===')
        print ('')
        print ('')
        while n < len(final_state_list):
            condition = final_state_list[n]
            result_string = "[" + str(n) + "]" + " - " + str(condition)
            print (result_string)
            n += 1
    
    print ('')
    print ('')
    print ('========================')
    print ('')
    if type_condition == "initial":
        print ('Select INITIAL CONDITION from file. Enter the number:')
    else:
        print ('Select FINITE STATE from file. Enter the number:')
    

def format_list_to_str(element):
    formated_string = str(element).replace("['", "")
    formated_string1 = formated_string.replace("']", "")
    return formated_string1
    
    
#def copy_rules(initial,finite):
#    f = open(file_number, 'r', encoding='utf-8')
    
#    for line in f:
#        pattern_for_input_rules = re.findall(r''initial'',line)


print_files_on_dir() #files in dir
file_number = int(input())

find_conditions(str(files[file_number]),"initial")
initial_condition = int(input())

find_conditions(str(files[file_number]),"finite")
finite_state = int(input())


print (format_list_to_str(condition_list[initial_condition]))
print (format_list_to_str(final_state_list[finite_state]))

#copy_rules(initial_condition,finite_state)
