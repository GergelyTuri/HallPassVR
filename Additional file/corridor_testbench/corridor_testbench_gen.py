import numpy as np
from numpy.core.records import array

def array_gen(file_num):
    corridor_write = open("Corridor_file.txt", "w")
    #randiarray = np.random.randint(0,file_num,file_num)
    #print(randiarray)
    for i in range(50):
        randiarray = np.random.randint(0,file_num,12)
        corridor_write.write(str(randiarray))
        corridor_write.write('\n')

    corridor_write.close()

'''if __name__ == '__main__':
    array_gen(7)
    print("call from corridor_testbench_gen_")'''
    
