from pylab import *
from thermocouples_reference import *
import seaborn as sns

figtype = '.pdf'
saveopts = {} #'bbox_inches':'tight'} #, 'transparent':True, 'frameon':True}

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.sans-serif": ["Computer Modern Roman"]})

def doplot(tclist,T,endlabels=True):
    fig = figure()
    ax = axes([0.17,0.14,0.80,0.83])
    #T = linspace(lim[0],lim[1],2001)
    for letter,tc in tclist:
        print(tc)
        emf = tc.emf_mVC(T,out_of_range="nan")
        l = plot(T, emf, label=tc.type)[0]
        if endlabels:
            Tmax = tc.maxT_C; emfmax = tc.emf_mVC(Tmax)
            text(Tmax,emfmax,tc.type, fontsize='x-small',
                 color=l.get_color(),va='center')
    ax.tick_params(labelsize="x-small")
    xlabel("Temperature $T$ (deg C)")
    ylabel("$E(T)$ (mV)")
    xlim(amin(T),amax(T))
    fig.set_size_inches(3,3)
    fig.patch.set_alpha(0)
    grid()

if __name__ == '__main__':
    ##### Low temperature
    lowTcouples = [(k, thermocouples[k]) for k in list('EJKNT')]
    doplot(lowTcouples,linspace(-273.015,40.,2001),endlabels=False)
    ylim(-10.5,2.1)
    xticks([-270,-200,-100,0,22])
    # dual legend
    ul = [gca().lines[i] for i in [3]]
    ll = [gca().lines[i] for i in [2,1,0]]
    l1 = legend(ul, [l.get_label() for l in ul],fontsize="x-small",loc='upper left')
    l2 = legend(ll, [l.get_label() for l in ll],fontsize="x-small",loc='lower right')
    gca().add_artist(l1)
    savefig('low_t_thermocouples'+figtype,**saveopts)
    
    ##### Medium temperature
    medTcouples = [(k, thermocouples[k]) for k in
    list('EJKNT')]
    doplot(medTcouples,linspace(-110.,1790.,2001))
    ylim(-6,82)
    xticks([0,500,1000,1500])
    gca().texts[1].set_ha('center') # type J
    gca().texts[1].set_va('bottom') # type J
    gca().texts[2].set_ha('center') # type K
    gca().texts[2].set_va('bottom') # type K
    gca().texts[4].set_ha('right') # type T
    gca().texts[4].set_va('bottom') # type T
    gca().lines[4].set_zorder(9)   # type T
    savefig('med_t_thermocouples'+figtype,**saveopts)
    
    ##### High temperature
    highTcouples = [(k, thermocouples[k]) for k in
        list('BRS')]
    doplot(highTcouples,linspace(-70.,2850.,2421))
    ylim(-2,49)
    gca().texts[1].set_ha('center') # type D
    gca().texts[1].set_va('bottom') # type D
    gca().texts[0].set_va('top') # type C
    savefig('high_t_thermocouples'+figtype,**saveopts)
