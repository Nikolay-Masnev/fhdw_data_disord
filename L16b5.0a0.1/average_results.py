import os
import sys
from math import sqrt

def average_data(read_file, write_file):
    x = []
    y = []
    y_err = []
    counter = 0
    KE = 0
    KE_ERR = 0
    PE = 0
    PE_ERR = 0
    g_im = 0
    g_im_ERR = 0
    g_im_data = []
    dens = 0
    dens_ERR = 0
    rf = open(read_file,"r")
    replicas = 0;
    counter_dens = 0
    dens_plot_x = []
    dens_plot_y = []
    dens_plot_err = []
    for line in rf:
        for word in line.split():
            if word == "KE":
                KE+= float(line.split()[2])
                KE_ERR += abs(float(line.split()[4]))
                replicas +=1
            elif word == "dens":
                dens += float(line.split()[2])
                dens_ERR += abs(float(line.split()[4]))
                dens_plot_y.append(float(line.split()[2]))
                dens_plot_x.append(counter_dens)
                dens_plot_err.append(float(line.split()[4]))
                counter_dens +=1
            elif word == "PE":
                PE+= float(line.split()[2])
                PE_ERR +=abs(float(line.split()[4]))
            elif word == "g_im(w=0,":
                g_im += float(line.split()[3])
                g_im_data.append(float(line.split()[3]))
                g_im_ERR += abs(float(line.split()[5]))
                x.append(counter)
                y.append(float(line.split()[3]))
                y_err.append(float(line.split()[5]))
                counter +=1
    dens = dens/replicas
    dens_ERR = dens_ERR/replicas
    KE = KE/replicas
    PE = PE/replicas
    g_im = g_im/replicas
    sigma_g = 0
    for i in g_im_data:
        sigma_g += (g_im - i)**2
    sigma_g = sqrt( sigma_g / (replicas*(replicas-1)))
    KE_ERR = KE_ERR/replicas
    PE_ERR = PE_ERR/replicas
    g_im_ERR =  sqrt(sigma_g / replicas**2)
    rf.close()
    wf = open(write_file, "a")
    wf.write("AVERAGE VALUES : " + "\n")
    wf.write("PE = %s +/- %s \n" % (str(PE), str(PE_ERR)))
    wf.write("KE = %s +/- %s \n" % (str(KE), str(KE_ERR)))
    wf.write("g_im = %s +/- %s \n" % (str(g_im), str(g_im_ERR)))
    wf.write("Dens = %s +/- %s" % (str(dens), str(dens_ERR))) 
    wf.close()

if __name__=='__main__':
    average_data(sys.argv[1], sys.argv[2])
