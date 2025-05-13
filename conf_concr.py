


def conf_concr_EC2(**kwargs):
    """
    Confined concrete parameters according to EC2 (1992.1.1 2004) §3.1.9
    Parameters
    ----------
    f_ck : float
        Characteristic compressive strength of concrete. (be careful with the units and the sign)
    b : float
        Width of the cross-section.
    h : float
        Height of the cross-section.
    c : float
        Cover to the reinforcement.
    A_stx : float
        Area of rebars legs in width direction.
    A_sty : float
        Area of rebars legs in height direction.
    s : float
        Spacing of the rebars.
    f_yw : float
        Yield strength of the stirrups. (be careful with the units and the sign)
    phi_l : float, optional
        Diameter of the longitudinal rebars. The default is 0.
    eps_c2 : float, optional    
        Concrete strain at beginning of the plastic range. The default is 0.002. (be careful with the units and the sign)
    eps_cu2 : float, optional
        Ultimate strain of concrete. The default is 0.0035. (be careful with the units and the sign)
    Returns
    -------
    dict
        Dictionary containing the concrete properties. (per esempio da usare per un concrete01)
    """

    # Parameters
    f_c = kwargs.get('f_c')
    b = kwargs.get('b')
    h = kwargs.get('h')
    c = kwargs.get('c')
    A_stx = kwargs.get('A_stx')
    A_sty = kwargs.get('A_sty', A_stx)
    s = kwargs.get('s')
    f_yw = kwargs.get('f_yw')
    phi_l = kwargs.get('phi_l', 0)
    eps_c2 = kwargs.get('eps_c2',0.002)
    eps_cu2 = kwargs.get('eps_cu2',0.0035)



    # Net distance between the stirrups (Hp no internal stirrups)
    b_x = b - 2*c - phi_l
    b_y = h - 2*c - phi_l

    # Confinement efficiency coefficients
    alpha_n = 1 - (b_x**2/(6*b_x*b_y) + b_y**2/(6*b_x*b_y))
    alpha_s = (1 - s/(2*b_x))*(1 - s/(2*b_y)) # the diameter of the stirrups is not considered in the calculation of the spacing (Hp that it's negligible)

    alpha = alpha_n * alpha_s

    # Lateral confining pressure
    sigma_lx = (A_stx * f_yw) / (b_x * s)
    sigma_ly = (A_sty * f_yw) / (b_y * s)
    sigma_l = (sigma_lx * sigma_ly)**0.5
    
    # Effective confining pressure    
    sigma_2 = alpha * sigma_l

    # Strength of confined concrete
    if sigma_2 <= 0.05 * f_c:
        f_cc = f_c * (1 + 5 * sigma_2 / f_c)
    else:
        f_cc = f_c * (1.125 + 2.5 * sigma_2 / f_c)

    # "Yielding" strain of confined concrete
    eps_cc2 = eps_c2 * (f_cc / f_c)**2
    # Ultimate strain of confined concrete
    eps_ccu = eps_cu2 + 0.2 * sigma_2 / f_c


    # Return the results as a dictionary
    return {'f_c': f_cc, 'eps_c2': eps_cc2, 'eps_cu': eps_ccu}
