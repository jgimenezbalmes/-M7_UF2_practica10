import matplotlib.pyplot as plt
import poblacio as pb
import densitatkm as dkm
import densitatm as dm



def exp():
    fig, axs = plt.subplots(2, 2)
    fig.delaxes(ax=axs[1,1])
    axs[0, 0].set_title('Ciutats per població')
    axs[0, 0].pie(pb.df2["Population"], labels=pb.df2['City'], autopct='%1.1f%%')
    axs[0, 1].set_title('Ciutats per densitat en m2')
    axs[0, 1].pie(dm.df6['Density  M2'], labels=dm.df6['City'], autopct='%1.1f%%')
    axs[1, 0].set_title('Ciutats per densitat en km2')
    axs[1, 0].pie(dkm.df4['Density KM2'], labels=dkm.df4['City'], autopct='%1.1f%%')
    plt.show()


