from os import read
import numpy as np 

global readarray2list

def data_read():
    global readarray2list

    readfile = open("testbench_testa_array.txt", "r")
    read_array = readfile.readline()[1:-1]
    #print(read_array)

    readarray2list = read_array.split()
    #print(readarray2list)
    readfile.close()


def fc_add():
    pattern_add_num = readfile2.readline()
    print(pattern_add_num)

    writefile.write(str(pattern_add_num))
    #writefile.write('\n')

def fc_delete():
    pattern_delete_count = readfile2.readline()
    print(pattern_delete_count)

    writefile.write(str(pattern_delete_count))
    #writefile.write('\n')

def fc_comb_select():
    comb_select_count = readfile2.readline()
    print(comb_select_count)

    writefile.write(str(comb_select_count))
    #writefile.write('\n')



def state_machine():

    global curr_state
    print("NEED TO EDIT")
    print("testa_array: ", readarray2list)
    
    for element in readarray2list:
        element = int(element)
        
        if element == 1:
            print("onClick_Add")
            fc_add()

        if element == 2:
            print("onClick_Delete")
            fc_delete()

        if element == 3:
            print("onClick_Delete_All")
            #fc_delete_all()

        if element == 4:
            print("onClick_Generate")
            #fc_gen()
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
            print("Combination selection")
            fc_comb_select() 


if __name__ == '__main__':
    readfile2 = open("random.txt", "r")
    writefile = open("random_test.txt", "w")
    data_read()
    state_machine()

    readfile2.close()
    writefile.close()

