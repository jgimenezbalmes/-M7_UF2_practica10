import matplotlib.pyplot as plt
import clockspeed as cs
import megapixels as mp
import batterypower as bp

def subplots():
    window = plt.figure()
    #Determinem que la figura tindra quatre seccions
    fig, axs = plt.subplots(2, 2)
    #Borrem el contingut de la posicio inferior dreta (per si un cas sortis alguna informacio)
    fig.delaxes(ax=axs[1,1])
    #Titol del primer grafic
    axs[0, 0].set_title('Clockspeed per mòbil')
    #Posem el primer grafic a la posicio superior esquerra (0,0)
    axs[0, 0].bar(cs.a.id, cs.a.clock_speed, color ='maroon', width=6)
    #Posició superior dreta, fem el mateix que abans pero amb battery power
    axs[0, 1].set_title('Battery power per mòbil')
    axs[0, 1].bar(bp.a.id, bp.a.battery_power, color ='green', width=6)
    #Posicio inferior esquerra, fem el mateix pero amb pixel height
    axs[1, 0].set_title('Pixel height per mòbil')
    axs[1, 0].bar(mp.a.id, mp.a.px_height, width=6)
    #Fem que la figure surti per pantalla
    plt.show()