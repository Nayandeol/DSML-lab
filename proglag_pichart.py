import numpy as np
import matplotlib.pyplot as plt
mylabel=["Java","python","Php","Javascript","c#","Cpp"]
y=np.array([22.2,17.6,8.8,8,7.7,6.7])
plt.title("Popularity of programming languages")
plt.pie(y,labels=mylabel)
plt.show()
