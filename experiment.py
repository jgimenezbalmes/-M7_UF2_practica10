import matplotlib.pyplot as plt
import poblacio as pb
import densitatkm as dkm
import densitatm as dm



def exp():
    #Determinem les proporcions de separacio de cada sector del grafic
    explode = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    #Determinem que la figura tindra quatre seccions
    fig, axs = plt.subplots(2, 2)
    #Borrem el contingut de la posicio inferior dreta (per si un cas sortis alguna informacio)
    fig.delaxes(ax=axs[1,1])
    #Titol del primer grafic
    axs[0, 0].set_title('Ciutats per població')
    #Posem el primer grafic a la posicio superior esquerra (0,0), i indiquem que les dades siguin de la columna
    #population, que es classifiqui segons City, i que es faci explode com s'ha indicat a l'array anterior
    axs[0, 0].pie(pb.df2["Population"], labels=pb.df2['City'], autopct='%1.1f%%', explode=explode)
    #Posició superior dreta, fem el mateix que abans pero amb Density M2
    axs[0, 1].set_title('Ciutats per densitat en m2')
    axs[0, 1].pie(dm.df6['Density  M2'], labels=dm.df6['City'], autopct='%1.1f%%', explode=explode)
    #Posicio inferior esquerra, fem el mateix pero amb Density KM2
    axs[1, 0].set_title('Ciutats per densitat en km2')
    axs[1, 0].pie(dkm.df4['Density KM2'], labels=dkm.df4['City'], autopct='%1.1f%%', explode=explode)
    #Fem que la figure surti per pantalla
    plt.show()


