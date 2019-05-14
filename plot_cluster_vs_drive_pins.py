"""
Make a plot of cluster size vs drive 
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


plt.rc('font', size=12)


if __name__ == "__main__":


    #------------------------------------------------------------------------
    #get data for initial frame, 
    #------------------------------------------------------------------------
    
    plot_file = "cluster_stats.txt"
    p_data = di.get_data(plot_file,3,sep=" ")

    index = 1
    rows=3
    columns=2
    cluster = np.zeros([8], float)
    stddev = np.zeros([8], float)
    
    gs=gridspec.GridSpec(rows,columns)
    fig = plt.figure(figsize=(8*columns,4*rows))
    
    driveIndex = 3
    
    density = np.array([0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    cluster[0] = p_data[index, driveIndex]
    cluster[1] = p_data[index, 15 + driveIndex]
    cluster[2] = p_data[index, 30 + driveIndex]
    cluster[3] = p_data[index, 45 + driveIndex]
    cluster[4] = p_data[index, 60 + driveIndex]
    cluster[5] = p_data[index, 75 + driveIndex]
    cluster[6] = p_data[index, 90 + driveIndex]
    cluster[7] = p_data[index, 105 + driveIndex]
    stddev[0] = p_data[2, driveIndex]
    stddev[1] = p_data[2, 15 + driveIndex]
    stddev[2] = p_data[2, 30 + driveIndex]
    stddev[3] = p_data[2, 45 + driveIndex]
    stddev[4] = p_data[2, 60 + driveIndex]
    stddev[5] = p_data[2, 75 + driveIndex]
    stddev[6] = p_data[2, 90 + driveIndex]
    stddev[7] = p_data[2, 105 + driveIndex]
    
    ax1 = fig.add_subplot(gs[0,0])  #scatter plot of particles
    #ax1.set_xlabel("Pin Number Density")
    ax1.set_ylabel("Average Cluster Fraction")   
    ax1.set_title("$F_D/F_P$ = 0.1")
    ax1.plot(density, cluster, c = "b", label = "$F_D$ = 1")
    ax1.plot(density, cluster+stddev, c = "b")
    ax1.plot(density, cluster-stddev, c = "b")
    plt.fill_between(density, cluster+stddev, cluster-stddev, facecolor = 'b',
                     alpha = 0.4)
    plt.ylim(0,0.65)

    driveIndex = 10
    
    density = np.array([0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    cluster[0] = p_data[index, driveIndex]
    cluster[1] = p_data[index, 15 + driveIndex]
    cluster[2] = p_data[index, 30 + driveIndex]
    cluster[3] = p_data[index, 45 + driveIndex]
    cluster[4] = p_data[index, 60 + driveIndex]
    cluster[5] = p_data[index, 75 + driveIndex]
    cluster[6] = p_data[index, 90 + driveIndex]
    cluster[7] = p_data[index, 105 + driveIndex]
    stddev[0] = p_data[2, driveIndex]
    stddev[1] = p_data[2, 15 + driveIndex]
    stddev[2] = p_data[2, 30 + driveIndex]
    stddev[3] = p_data[2, 45 + driveIndex]
    stddev[4] = p_data[2, 60 + driveIndex]
    stddev[5] = p_data[2, 75 + driveIndex]
    stddev[6] = p_data[2, 90 + driveIndex]
    stddev[7] = p_data[2, 105 + driveIndex]
    
    ax1 = fig.add_subplot(gs[1,0])
    #ax1.set_xlabel("Pin Number Density")
    ax1.set_ylabel("Average Cluster Fraction")   
    ax1.set_title("$F_D/F_P$ = 0.5")
    ax1.plot(density, cluster, c = "r", label = "$F_D$ = 5")
    ax1.plot(density, cluster+stddev, c = "r")
    ax1.plot(density, cluster-stddev, c = "r")
    plt.fill_between(density, cluster+stddev, cluster-stddev, facecolor = 'r',
                     alpha = 0.4)
    plt.ylim(0,0.65)
    
    driveIndex = 1
    
    density = np.array([0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    cluster[0] = p_data[index, driveIndex]
    cluster[1] = p_data[index, 15 + driveIndex]
    cluster[2] = p_data[index, 30 + driveIndex]
    cluster[3] = p_data[index, 45 + driveIndex]
    cluster[4] = p_data[index, 60 + driveIndex]
    cluster[5] = p_data[index, 75 + driveIndex]
    cluster[6] = p_data[index, 90 + driveIndex]
    cluster[7] = p_data[index, 105 + driveIndex]
    stddev[0] = p_data[2, driveIndex]
    stddev[1] = p_data[2, 15 + driveIndex]
    stddev[2] = p_data[2, 30 + driveIndex]
    stddev[3] = p_data[2, 45 + driveIndex]
    stddev[4] = p_data[2, 60 + driveIndex]
    stddev[5] = p_data[2, 75 + driveIndex]
    stddev[6] = p_data[2, 90 + driveIndex]
    stddev[7] = p_data[2, 105 + driveIndex]
    
    ax1 = fig.add_subplot(gs[2,0])
    ax1.set_xlabel("Pin Number Density")
    ax1.set_ylabel("Average Cluster Fraction")   
    ax1.set_title("$F_D/F_P$ = 1.0")
    ax1.plot(density, cluster, c = "y", label = "$F_D$ = 10")
    ax1.plot(density, cluster+stddev, c = "y")
    ax1.plot(density, cluster-stddev, c = "y")
    plt.fill_between(density, cluster+stddev, cluster-stddev, facecolor = 'y',
                     alpha = 0.4)   
    plt.ylim(0,0.65)
      
    driveIndex = 2
    
    density = np.array([0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    cluster[0] = p_data[index, driveIndex]
    cluster[1] = p_data[index, 15 + driveIndex]
    cluster[2] = p_data[index, 30 + driveIndex]
    cluster[3] = p_data[index, 45 + driveIndex]
    cluster[4] = p_data[index, 60 + driveIndex]
    cluster[5] = p_data[index, 75 + driveIndex]
    cluster[6] = p_data[index, 90 + driveIndex]
    cluster[7] = p_data[index, 105 + driveIndex]
    stddev[0] = p_data[2, driveIndex]
    stddev[1] = p_data[2, 15 + driveIndex]
    stddev[2] = p_data[2, 30 + driveIndex]
    stddev[3] = p_data[2, 45 + driveIndex]
    stddev[4] = p_data[2, 60 + driveIndex]
    stddev[5] = p_data[2, 75 + driveIndex]
    stddev[6] = p_data[2, 90 + driveIndex]
    stddev[7] = p_data[2, 105 + driveIndex]
    
    ax1 = fig.add_subplot(gs[0,1])
    #ax1.set_xlabel("Pin Number Density")
    #ax1.set_ylabel("Average Cluster Fraction")   
    ax1.set_title("$F_D/F_P$ = 1.5")
    ax1.plot(density, cluster, c = "g", label = "$F_D$ = 15")
    ax1.plot(density, cluster+stddev, c = "g")
    ax1.plot(density, cluster-stddev, c = "g")
    plt.fill_between(density, cluster+stddev, cluster-stddev, facecolor = 'g',
                     alpha = 0.4)
    plt.ylim(0,0.65)
    
    driveIndex = 4
    
    density = np.array([0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    cluster[0] = p_data[index, driveIndex]
    cluster[1] = p_data[index, 15 + driveIndex]
    cluster[2] = p_data[index, 30 + driveIndex]
    cluster[3] = p_data[index, 45 + driveIndex]
    cluster[4] = p_data[index, 60 + driveIndex]
    cluster[5] = p_data[index, 75 + driveIndex]
    cluster[6] = p_data[index, 90 + driveIndex]
    cluster[7] = p_data[index, 105 + driveIndex]
    stddev[0] = p_data[2, driveIndex]
    stddev[1] = p_data[2, 15 + driveIndex]
    stddev[2] = p_data[2, 30 + driveIndex]
    stddev[3] = p_data[2, 45 + driveIndex]
    stddev[4] = p_data[2, 60 + driveIndex]
    stddev[5] = p_data[2, 75 + driveIndex]
    stddev[6] = p_data[2, 90 + driveIndex]
    stddev[7] = p_data[2, 105 + driveIndex]
    
    ax1 = fig.add_subplot(gs[1,1])
    #ax1.set_xlabel("Pin Number Density")
    #ax1.set_ylabel("Average Cluster Fraction")   
    ax1.set_title("$F_D/F_P$ = 2.0")
    ax1.plot(density, cluster, c = "purple", label = "$F_D$ = 20")
    ax1.plot(density, cluster+stddev, c = "purple")
    ax1.plot(density, cluster-stddev, c = "purple")
    plt.fill_between(density, cluster+stddev, cluster-stddev, facecolor = 'purple',
                     alpha = 0.4) 
    plt.ylim(0,0.65)
    
    driveIndex = 7
    
    density = np.array([0.02, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
    cluster[0] = p_data[index, driveIndex]
    cluster[1] = p_data[index, 15 + driveIndex]
    cluster[2] = p_data[index, 30 + driveIndex]
    cluster[3] = p_data[index, 45 + driveIndex]
    cluster[4] = p_data[index, 60 + driveIndex]
    cluster[5] = p_data[index, 75 + driveIndex]
    cluster[6] = p_data[index, 90 + driveIndex]
    cluster[7] = p_data[index, 105 + driveIndex]
    stddev[0] = p_data[2, driveIndex]
    stddev[1] = p_data[2, 15 + driveIndex]
    stddev[2] = p_data[2, 30 + driveIndex]
    stddev[3] = p_data[2, 45 + driveIndex]
    stddev[4] = p_data[2, 60 + driveIndex]
    stddev[5] = p_data[2, 75 + driveIndex]
    stddev[6] = p_data[2, 90 + driveIndex]
    stddev[7] = p_data[2, 105 + driveIndex]
    
    ax1 = fig.add_subplot(gs[2,1])
    ax1.set_xlabel("Pin Number Density")
    #ax1.set_ylabel("Average Cluster Fraction")   
    ax1.set_title("$F_D/F_P$ = 3.0")
    ax1.plot(density, cluster, c = "orange", label = "$F_D$ = 30")
    ax1.plot(density, cluster+stddev, c = "orange")
    ax1.plot(density, cluster-stddev, c = "orange")
    plt.fill_between(density, cluster+stddev, cluster-stddev, facecolor = 'orange',
                     alpha = 0.4) 
    plt.ylim(0,0.65)
    
    plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
    
    #ax1.legend(loc = "best", fontsize = 12)

    #------------------------------------------------------------------------
    # (turned off) add an annotation
    # note: "force" was for a different system, here time is relevant
    #------------------------------------------------------------------------
    if 0:
        force_template = r'$F_D/F_p = %1.2f$'
        #force_template = r'time = %d'        
        force_text = ax1.text(0.5, 1.05, '', ha='center',
                              transform=ax1.transAxes,fontsize=22)

    out_name="clump_vs_drive_plot.png"
    fig.savefig(out_name)
        
    sys.exit()
