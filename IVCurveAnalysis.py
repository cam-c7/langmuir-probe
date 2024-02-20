# IV Curve analysis

import math
q = 1.60217663*(10^-19)
k = 1.380649*(10^-23)
qoverk = 11604.5180926
Imin = float(input("Enter smallest value of I in μA: "))
Isat = -Imin
probeAreaCoeff = float(input("Enter coefficient of surface area of probe (both sides) (m^2): "))
probeAreaExp = int(input("Enter coefficient of surface area of probe (both sides) (m^2): "))
M = float(input("Enter ion mass coefficient (kg): "))
Mexp = int(input("Enter ion mass exponent (kg): "))

slopeER = float(input("Enter slope of electron retardation region (ln curve): "))
intER = float(input("Enter y-intercept of electron retardation region (ln curve): "))
slopeES = float(input("Enter slope of electron saturation region (ln curve): "))
intES = float(input("Enter y-intercept of electron saturation region (ln curve): "))

Te = 1/slopeER
phiP = (intES-intER)/(slopeER-slopeES)
TeK = Te * (qoverk)
# ne = (Isat / (q * probeArea * math.exp(-1/2)) * math.sqrt(M/(k * TeK)))/(10^6)
print("Te =", Te, "eV", "=", TeK, "K")
print("Φp =", phiP, "V")
print("To calculate ne, plug this into google (answer in cm^-3): ")
print("(", Isat, "*10^(-6))/(", "1.60217663*(10^-19)*", probeAreaCoeff, "*10^(", probeAreaExp, ")", "*e^(-1/2)) * sqrt(", M, "*10^(", Mexp, ")/(", "1.380649*(10^-23)*", TeK, "))/(10^6)" , sep='')




