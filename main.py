from battery_energy import calculate_ein, calculate_eout, calculate_ebattery
from battery_efficiency import calculate_efficiency, calculate_ncha_n_dis
import numpy as np


# Exemplo de dados (valores fictícios)

time = np.linspace(0, 3600, 100)          # Tempo [s]
# Tensão e corrente durante o carregamento
vcha = np.random.uniform(3.5, 4.2, len(time))  # Tensão variando entre 3.5V e 4.2V44
icha = np.random.uniform(0.5, 1.5, len(time))  # Corrente variando entre 0.5A e 1.5A

# Tensão e corrente durante o descarregamento
vdis = np.random.uniform(2.8, 3.5, len(time))  # Tensão variando entre 2.8V e 3.5V
idis = np.random.uniform(0.5, 1.5, len(time))  # Corrente variando entre 0.5A e 1.5A

voltage_ocv = [2.3, 2.35, 2.4]  # Tensão de circuito aberto
capacity_ah = 20
soc_initial = 0.2
soc_final = 0.8

# Cálculo da energia
ein = calculate_ein(vcha, icha, time)
eout = calculate_eout(vdis, idis, time)
ebattery = calculate_ebattery(voltage_ocv, capacity_ah, soc_initial, soc_final)

# Cálculo das eficiências
efficiency = calculate_efficiency(eout, ein)
n_cha, n_dis = calculate_ncha_n_dis(ein, eout, ebattery)

# Exibir resultados
print(f"Ein: {ein:.2f} J")
print(f"Eout: {eout:.2f} J")
print(f"E_battery: {ebattery:.2f} J")
print(f"Eficiência geral: {efficiency:.2%}")
print(f"n_cha: {n_cha:.2%}, n_dis: {n_dis:.2%}")
