import numpy as np
from scipy.integrate import simpson


def calculate_ein(voltage, current, time):
    """ Calcula a energia de entrada (Ein) integrando V * I ao longo do tempo. """
    power = np.array(voltage) * np.array(current)
    return simpson(power, time)

def calculate_eout(voltage, current, time):
    """ Calcula a energia de saída (Eout) integrando V * I ao longo do tempo. """
    power = np.array(voltage) * np.array(current)
    return simpson(power, time)

def calculate_ebattery(voltage_ocv, capacity_ah, soc_initial, soc_final):
    """ Calcula a energia armazenada na bateria. """
    capacity_coulombs = capacity_ah * 3600  # Convertendo Ah para Coulombs
    return simpson(voltage_ocv, np.linspace(soc_initial, soc_final, len(voltage_ocv))) * capacity_coulombs

def changes(): 
    pass