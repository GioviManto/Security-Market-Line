import numpy as np
import matplotlib.pyplot as plt

# Define the risk-free rate
Rf = 0.08

# Generate beta values from 0 to 2, excluding the risk-free rate
beta = np.linspace(0, 2, 100)[1:]  # Exclude the first point (beta = 0)

# Define the expected return on the market portfolio
E_Rm = 0.11

# Calculate the expected return for each beta using the SML equation
E_Ri = Rf + beta * (E_Rm - Rf)

# Plot the SML
plt.figure(figsize=(8, 6))
plt.plot(beta, E_Ri, color='blue', label='Security Market Line (SML)')
plt.scatter(1, E_Rm, color='red', label='Market Portfolio (M)')
plt.text(0.5, E_Rm, 'Market Portfolio (M)', color='red',fontsize=7, verticalalignment='bottom')
plt.scatter(0, Rf, color='green')  # Add a point for the risk-free rate at (0, Rf)
plt.text(-0.15, Rf, 'Risk-Free Rate (Rf)', color='green', rotation=90, fontsize=7, verticalalignment='bottom')
plt.axhline(y=E_Rm, color='gray', linestyle='--', linewidth=0.5)
plt.text(-0.08, E_Rm, 'E[Rm]', color='red', fontsize=7, verticalalignment='bottom')
plt.xlabel('Beta (βi)')
plt.ylabel('Expected Return (E[Ri])')
plt.title('Security Market Line (SML)')
plt.grid(True)
plt.legend()

# Label undervalued and overvalued stocks
plt.text(0.1, 0.13, 'Undervalued Stocks', color='black', verticalalignment='bottom')
plt.text(1.2, 0.08, 'Overvalued Stocks', color='black', verticalalignment='top')

# Generate some random data points for undervalued and overvalued stocks
np.random.seed(0)
undervalued_beta = np.random.uniform(0, 1.2, 5)
undervalued_E_Ri = np.random.uniform(0.10, 0.12, 5)

overvalued_beta = np.random.uniform(0.8, 2, 5)
overvalued_E_Ri = np.random.uniform(0.075, 0.09, 5)

plt.scatter(undervalued_beta, undervalued_E_Ri, color='orange', label='Undervalued Stocks')
plt.scatter(overvalued_beta, overvalued_E_Ri, color='purple', label='Overvalued Stocks')

plt.scatter(1.5, 0.13, color='orange', label='Undervalued Stocks')
plt.scatter(0.5, 0.082, color='purple', label='Overvalued Stocks')

plt.xticks([0, 1])
plt.yticks([])

plt.show()
