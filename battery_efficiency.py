def calculate_efficiency(eout, ein):
    """ Calcula a eficiência geral da bateria. """
    return eout / ein if ein != 0 else 0

def calculate_ncha_n_dis(ein, eout, ebattery):
    """ Calcula as eficiências de carga (n_cha) e descarga (n_dis). """
    n_cha = ebattery / ein if ein != 0 else 0
    n_dis = eout / ebattery if ebattery != 0 else 0
    return n_cha, n_dis
