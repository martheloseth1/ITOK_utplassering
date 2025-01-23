import numpy as np
from scipy.stats import gamma
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

feil1 = False

# input-verdier (10-prosentil og MRL)
prosentil = float(input("1. 10th percentile residual life: "))
mrl = float(input("2. Mean residual life (MRL): "))


if prosentil > 0 and mrl > 0 and mrl > prosentil:

    # målfunksjon for å beregne beta
    def goal_function(beta, prosentil, mrl):
        alfa = mrl / beta   # formparameter
        kalkulert_prosentil = gamma.ppf(0.1, a=alfa, scale=beta)
        return kalkulert_prosentil - prosentil


    # startverdi for beta
    initialverdi_beta = 1.0

    # løser for beta
    beta = fsolve(goal_function, initialverdi_beta, args=(prosentil, mrl))[0]


    # beregner alfa basert på beta
    alfa = mrl / beta


    # varians og standardavvik
    varians = alfa * (beta**2)
    sd = varians**(1/2)


    # sjekker om alfa er større enn 100, i så fall endres feil1
    if alfa > 100:
        feil1 = True


    # variabelen skal brukes til å lagre den kumulative verdien fra forrige iterasjon
    kum1 = 0

    for i in range (1, 101):
        




else:
    print("Wrong value! Check if (mean > 10th percentile), (mean > 0) og (10th percentile > 0)")

if feil1 == True:
    print("alpha > 100 !!!!")


print(f"Parameterverdier:")
print(f"Alfa (form): {alfa}")
print(f"Beta (skala): {beta}")
print(f"Varians: {varians}")
print(f"Standardavvik: {sd}")





