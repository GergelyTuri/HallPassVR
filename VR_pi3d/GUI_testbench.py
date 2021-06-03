# --- GUI Interface testbench ---
#Hongtao Cai Columbia University 

# --- corrsponding command ---
# 1 - onClick_Add
# 2 - onClick_Delete
# 3 - onClick_Delete_All
# 4 - onClick_Generate 
# 5 - onClick_Exit
# 6 - onClick_upload
# 7 - onClick_Delete_hi
# 8 - onClick_Del_hi_all
# 9 - onClick_Start
#10 - change combination

# --- Corrsponding messagebox ---
global messagebox1 
global messagebox2
global messagebox3

messagebox1 = "Add: Error, Out of Limit"
messagebox2 = "Generate: Error, Empty Pattern"
messagebox3 = "Generate: Waring, Need 4 pattern"



import numpy as np
import subprocess as sp
import time


# --- testing ---
global pattern_list_array
global pattern_list_num
global testa_array
global curr_state
global new_state
global output_path_12_num
global comb_select_array
global comb_select


pattern_list_num = 8
#testa_array = [10,1,1,1,2,1,1,4]
pattern_list_array = []

count = 0
curr_state = 0
new_state = 0

output_path_12_num = [0 for i in range(12)]
comb_select_array = ["Combination 1",
                     "Combination 2", 
                     "Combination 3"]

comb_select = "Combination 1"


def command_array_gen():
    print("NEED TO EDIT")
    global count

    count += 1

    operation_num = np.random.randint(1,15) #simulate round of curser selection 
    print(operation_num)
    command_array = np.random.randint(1,11,operation_num)

    return command_array



def fc_add():
    array_length = len(pattern_list_array)
    print("Add array_length: ", array_length)

    if array_length < 4:
        #simulate pattern curser selected
        pattern_add_num = np.random.randint(0, pattern_list_num)
        print("fc_add pattern_add_num: ", pattern_add_num)

        writefile2.write(str(pattern_add_num))
        writefile2.write('\n')

        pattern_list_array.append(pattern_add_num)
    else: 
        print(messagebox1)  

    print("fc_add: ", pattern_list_array)



def fc_delete():
    array_length = len(pattern_list_array)
    print("fc_delete  array_length: ", array_length)

    if array_length == 0:
        pass

    else:
        pattern_delete_count = np.random.randint(0,array_length)
        writefile2.write(str(pattern_delete_count))

        pattern_delete_num = pattern_list_array[pattern_delete_count]
        print("fc_delete pattern_delete_num: ", pattern_delete_num)
        pattern_list_array.remove(pattern_delete_num)

    print("fc_delete: ", pattern_list_array)


def fc_delete_all():
    pattern_list_array.clear()
    print("fc_delete_all: ", pattern_list_array)


def fc_comb_select():
    global comb_select_array
    global comb_select
    array_length = len(comb_select_array)
    #print("fc_comb_select  array_length: ", array_length)

    comb_select_count = np.random.randint(0,array_length)
    writefile2.write(str(comb_select_count))
    writefile2.write('\n')

    print("fc_comb_select  comb_select_count: ", comb_select_count)

    comb_select = comb_select_array[comb_select_count]
    print("fc_comb_select  comb_select: ",comb_select)


def fc_gen():
    global comb_select

    array_length = len(pattern_list_array)
    print("fc_gen  array_length: ", array_length)

    if array_length == 0:
        print(messagebox2)
    
    elif array_length < 4:
        print(messagebox3)

    else:
        if comb_select == "Combination 1":
            output_path_12_num[0:4] = pattern_list_array
        
        if comb_select == "Combination 2":
            output_path_12_num[4:8] = pattern_list_array

        if comb_select == "Combination 3":
            output_path_12_num[8:12] = pattern_list_array

    

    print("fc_gen  pattern_list_array: ", output_path_12_num)


def state_machine():

    global curr_state
    print("NEED TO EDIT")
    print("testa_array: ", testa_array)
    
    for element in testa_array:
        if element == 1:
            print("onClick_Add")
            fc_add()

        if element == 2:
            print("onClick_Delete")
            fc_delete()

        if element == 3:
            print("onClick_Delete_All")
            fc_delete_all()

        if element == 4:
            print("onClick_Generate")
            fc_gen()
        if element == 5:
            print("onClick_Exit")
        if element == 6: 
            print("onClick_upload")
        if element == 7:
            print("onClick_Delete_hi")
        if element == 8:
            print("onClick_Del_hi_all")
        if element == 9:
            print("onClick_Start")  
        if element == 10:
            print("COmbination selection")
            fc_comb_select()             


if __name__ == '__main__':
    testa_array = command_array_gen()

    writefile = open("testbench_testa_array.txt", "w")
    writefile.write(str(testa_array))
    writefile.close()

    writefile2 = open("random.txt", "w")

    state_machine()

    writefile2.close()

    extProc = sp.Popen(['python','GUI_testbench_test.py']) # runs myPyScript.py 

    status = sp.Popen.poll(extProc)

    time.sleep(1)

    sp.Popen.terminate(extProc)