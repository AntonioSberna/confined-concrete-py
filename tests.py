



from conf_concr import conf_concr_EC2
import numpy as np
import matplotlib.pyplot as plt





# Parabole-rectangle stress-strain curve for confined concrete
def par_rect_concr(**kwargs):
    f_c = kwargs.get('f_c')
    eps_c2 = kwargs.get('eps_c2', 0.002)
    eps_cu = kwargs.get('eps_cu', 0.0035)
    epss = kwargs.get('epss', np.linspace(0, eps_cu*1.1, 100))

    # Stress-strain curve EC2 §3.1.7
    fcs = np.where(
        epss <= eps_c2,
        f_c * (1 - (1 - (epss / eps_c2))**2),
        np.where(
            epss <= eps_cu,
            f_c,
            0
        )
    )
    return fcs, epss






### Examples
unconf_conc = {"f_c": 20}
conf_conc = conf_concr_EC2(f_c= unconf_conc["f_c"], 
                            b=300, h=400, c=25, ## be careful with the units that should be consistent and the sign (in this case positive)
                            A_stx=2 * np.pi * 4**2, A_sty= 2 * np.pi * 4**2, # for example 2 legs of Ø8 stirrups
                            s=150, f_yw=450, phi_l = 18)




# Plot
fig = plt.figure(figsize=(6, 5))
ax = fig.gca()

ax.plot(par_rect_concr(**unconf_conc)[1], par_rect_concr(**unconf_conc)[0],
        label='Unconfined concrete', color='midnightblue')
ax.plot(par_rect_concr(**conf_conc)[1], par_rect_concr(**conf_conc)[0],
        label='Confined concrete', color='firebrick')


ax.set_xlabel(r'$\varepsilon_c\; \left[\mathrm{-}\right]$ '), ax.set_ylabel(r'$\sigma_c\; \left[\mathrm{MPa}\right]$ ')
ax.set_xlim(0), ax.set_ylim(0)
ax.set_title("Concrete stress-strain curves - EC2 §3.1.9")
ax.legend()
ax.grid(alpha = 0.3)
plt.show()  



