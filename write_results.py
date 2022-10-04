import os
import sys
def read_data(read_file,write_file ):
    reverse_line_num = 0
    file = open(write_file,"a")
    file.write(read_file + "\n")
    for line in reversed(list(open(read_file))):
        for word in line.split():
            if word == "PE" or word == "KE" or word == "g_im(w=0," or word == "dens" or word == "MC":
                file.write(line + "\n")
        if reverse_line_num == 50:
            file.write(50*"-"+2*"\n")
            break
        reverse_line_num +=1
    file.close()

if __name__=='__main__':
    read_data(sys.argv[1],sys.argv[2])


