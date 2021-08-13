import numpy as np
import os
import subprocess as sp
import time
import corridor_testbench_gen

readfile = open("Corridor_file.txt", "r")

def patternnum_read():
    global size_num 

    string_dir            = 'image/'
    extensions            = ['.jpg']
    patternnum_read_list  = [f for f in os.listdir(string_dir) if os.path.splitext(f)[1] in extensions]
    size_num              = len(patternnum_read_list)

def array_read():
    global element_new2list
    global test_list

    element          = readfile.readline()
    element_new      = element[1:-2]
    element_new2list = element_new.split()
    #print(element)
    #print(element_new)

def main_loop():
    global testcase
    testcase = 0
    while True:
        array_read()
        print(element_new2list)
        #time.sleep(5)

        if not element_new2list:
            print("test finish, totally test case: ", testcase)
            break
        else:
            testcase += 1
            test_list = element_new2list

        writefile = open("corridor_file_write.txt", "w")

        output_path_12_num_string = [str(int) for int in test_list]
        final_output_path         = " ".join(output_path_12_num_string)
        writefile.write(final_output_path)
        
        writefile.close()


        print("test_list: ", test_list)
        print("test case: ", testcase)
        #time.sleep(90)
        
        extProc = sp.Popen(['python','Corridor_test_5_20.py']) # runs myPyScript.py 

        status = sp.Popen.poll(extProc)

        time.sleep(45)

        sp.Popen.terminate(extProc)
        time.sleep(5)
    

            

if __name__ == '__main__':
    patternnum_read()
    corridor_testbench_gen.array_gen(size_num)
    main_loop()
    
    #array_read()
    
    readfile.close()
    
