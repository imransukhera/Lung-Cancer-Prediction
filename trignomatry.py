# %%

import numpy as np
import matplotlib.pyplot as plt

sin_val1 = np.sin(180)
print(sin_val1)

sin_val2 = np.sin(90)
print(sin_val2)


cos_val1 = np.cos(180)
print(cos_val1)


tan_val1 = np.tan(180)
print(tan_val1)

# pilot by the visualization

x_sin = np.arange(0, 3*np.pi , 0.1)
print(x_sin)


# fint the y-axis value by using the sin value
y_sin = np.sin(x_sin)
print(y_sin)


# using the value of x-axis and t-axis to pilot the graph
plt.figure()
plt.plot(x_sin,y_sin)
plt.title("Sine Wave")
plt.show()

# using the x-axis value to fint out the y-axis value
y_cos = np.cos(x_sin)
plt.figure()
plt.plot(x_sin, y_cos)
plt.title("Cosine Wave")
plt.show()

# using the x-axis value to fint out the y-axis value
y_tan = np.tan(x_sin)
plt.figure()
plt.plot(x_sin, y_tan)
plt.title("Tan Wave")
plt.legend()
plt.show()



# %%
