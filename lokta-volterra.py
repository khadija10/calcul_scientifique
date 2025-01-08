import matplotlib.pyplot as plt
import numpy

import pandas as pd

data  = pd.read_csv('populations_lapins_renards.csv')

time = [0]
lapin = [1]
renard = [2]

real_time = data['date']
real_lapin = data['lapin']
real_renard = data['renard']

alpha= 2/3 
beta = 4/3 
delta = 1 
gama = 1 

step = 0.001

for _ in range(1, len(real_time)):
    new_value_time = time[-1] + step
    new_value_lapin = (lapin[-1] * (alpha - beta * renard[-1])) * step + lapin[-1]
    new_value_renard = (renard[-1] * (delta * lapin[-1] - gama)) * step + renard[-1]

    time.append(new_value_time)
    lapin.append(new_value_lapin)
    renard.append(new_value_renard)

lapin = numpy.array(lapin)
lapin *= 1000

renard = numpy.array(renard)
renard *= 1000

# Fonction pour calculer l'erreur quadratique moyenne (MSE)
def mse(real_lapin, real_renard, pred_lapin, pred_renard):
    mse_lapin = numpy.mean((real_lapin - pred_lapin) ** 2)
    mse_renard = numpy.mean((real_renard - pred_renard) ** 2)
    return mse_lapin + mse_renard


error = mse(real_lapin, real_renard, lapin, renard)

print(error)

plt.figure(figsize=(15, 16))
# plt.plot(time, lapin, "b-", label="Lapins prédits")
# plt.plot(time, renard, "r-", label="Renard prédits")

plt.plot(real_time, real_lapin, "b--", label="Lapins réels")
plt.plot(real_time, real_renard, "r--", label="Renards réels")

plt.xlabel('temps (Mois)')
plt.ylabel('Population')
plt.title("Dynamique des populations Proie-Prédateur")
plt.legend()
plt.show()

