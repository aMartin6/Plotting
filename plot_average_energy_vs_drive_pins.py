"""
Make a plot of Vx vs Drive
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as colors
#from matplotlib import cm
import matplotlib.ticker as ticker
import sys
#functions written by D.M. to get and plot specific data files
import data_importerDM as di


plt.rc('font', size=10)


if __name__ == "__main__":


    #------------------------------------------------------------------------
    #get data for initial frame, 
    #------------------------------------------------------------------------
    
    plot_file = "AverageEnergies.txt"
    p_data = di.get_data(plot_file,3,sep=",")
    for i in range(len(p_data[0,:])):
        p_data[0][i] = p_data[0][i]/10
        p_data[1][i] = p_data[1][i]/(2610*50)
        p_data[2][i] = p_data[2][i]/(2610*50)
    #Use index 1 for scaled velocity and index 3 for plain velocity
    index = 1
    rows = 1
    columns = 1

    gs=gridspec.GridSpec(rows,columns)
    fig = plt.figure(figsize=(8*columns,4*rows))

    ax1 = fig.add_subplot(gs[:])  #scatter plot of particles

    ax1.set_xlabel("Drive Force/Pin Force")
    ax1.set_ylabel("Average Energy Per Particle")   
    #ax1.set_title("Average Particle Energy vs Drive Force")
    #ax1.set_ylim(-1,30)

    drive1 = p_data[0, 0:15]
    pd02 = p_data[index, 0:15]
    pd1 = p_data[index, 15:30]
    pd2 = p_data[index, 30:45]
    pd3 = p_data[index, 45:60]
    pd4 = p_data[index, 60:75]
    pd5 = p_data[index, 75:90]
    pd6 = p_data[index, 90:105]
    pd7 = p_data[index, 105:120]
    stddev02 = p_data[2, 0:15]
    stddev1 = p_data[2, 15:30]
    stddev2 = p_data[2, 30:45]
    stddev3 = p_data[2, 45:60]
    stddev4 = p_data[2, 60:75]
    stddev5 = p_data[2, 75:90]
    stddev6 = p_data[2, 90:105]
    stddev7 = p_data[2, 105:120]

    drive, pd02 = zip(*sorted(zip(drive1, pd02)))
    drive, pd1 = zip(*sorted(zip(drive1, pd1)))
    drive, pd2 = zip(*sorted(zip(drive1, pd2)))
    drive, pd3 = zip(*sorted(zip(drive1, pd3)))
    drive, pd4 = zip(*sorted(zip(drive1, pd4)))
    drive, pd5 = zip(*sorted(zip(drive1, pd5)))
    drive, pd6 = zip(*sorted(zip(drive1, pd6)))
    drive, pd7 = zip(*sorted(zip(drive1, pd7)))

    drive, stddev02 = zip(*sorted(zip(drive1, stddev02)))
    drive, stddev1 = zip(*sorted(zip(drive1, stddev1)))
    drive, stddev2 = zip(*sorted(zip(drive1, stddev2)))
    drive, stddev3 = zip(*sorted(zip(drive1, stddev3)))
    drive, stddev4 = zip(*sorted(zip(drive1, stddev4)))
    drive, stddev5 = zip(*sorted(zip(drive1, stddev5)))
    drive, stddev6 = zip(*sorted(zip(drive1, stddev6)))
    drive, stddev7 = zip(*sorted(zip(drive1, stddev7)))

    ax1.errorbar(drive, pd02, yerr = stddev02,label =
                 "$n_p$ = 0.02")                 
                 #"$\phi_p$ = 0.0628")
                 #"$\phi_p$ = 0.0157")
    ax1.errorbar(drive, pd1, yerr = stddev1,label =
                "$n_p$ = 0.1")
                 #"$\phi_p$ = 0.314")
                 #"$\phi_p$ = 0.0785")    
    ax1.errorbar(drive, pd2, yerr = stddev2, label =
                 "$n_p$ = 0.2")                 
                 #"$\phi_p$ = 0.628")
                 #"$\phi_p$ = 0.157")    
    ax1.errorbar(drive, pd3, yerr = stddev3, label =
                 "$n_p$ = 0.3")                 
                 #"$\phi_p$ = 0.942")
                 #"$\phi_p$ = 0.237")    
    ax1.errorbar(drive, pd4, yerr = stddev4, label =
                 "$n_p$ = 0.4")                 
                 #"$\phi_p$ = 1.257")
                 #"$\phi_p$ = 0.314")    
    ax1.errorbar(drive, pd5, yerr = stddev5, label =
                 "$n_p$ = 0.5")                 
                 #"$\phi_p$ = 1.571")
                 #"$\phi_p$ = 0.393")    
    ax1.errorbar(drive, pd6, yerr = stddev6, label =
                 "$n_p$ = 0.6")                 
                 #"$\phi_p$ = 1.885")
                 #"$\phi_p$ = 0.472")    
    ax1.errorbar(drive, pd7, yerr = stddev7, label =
                 "$n_p$ = 0.7")                 
                 #"$\phi_p$ = 2.199")
                 #"$\phi_p$ = 0.550")    

    ax1.legend(loc = "lower right", fontsize = 10)

    #------------------------------------------------------------------------
    # (turned off) add an annotation
    # note: "force" was for a different system, here time is relevant
    #------------------------------------------------------------------------
    if 0:
        force_template = r'$F_D/F_p = %1.2f$'
        #force_template = r'time = %d'        
        force_text = ax1.text(0.5, 1.05, '', ha='center',
                              transform=ax1.transAxes,fontsize=22)

    out_name="energy_vs_drive_plot.png"
    fig.savefig(out_name)
        
    sys.exit()
