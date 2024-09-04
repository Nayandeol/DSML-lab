import numpy as np
import matplotlib.pyplot as plt
x=np.array(["Java","python","Php","Javascript","c#","Cpp"])
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.title("Popularity of programming languages")
plt.xlabel("Programming languages")
plt.ylabel("popularity")
plt.bar(x,y,color="g")
plt.grid()
plt.show()
