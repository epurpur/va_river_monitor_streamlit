# import matplotlib.pyplot as plt

# plt.style.use('ggplot')

# x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
# energy = [5, 6, 15, 22, 24, 8]

# x_pos = [i for i, _ in enumerate(x)]

# plt.bar(x_pos, energy, color='green')
# plt.xlabel("Energy Source")
# plt.ylabel("Energy Output (GJ)")
# plt.title("Energy output from various fuel sources")

# plt.xticks(x_pos, x)

# plt.show()


import matplotlib.pyplot as plt
import numpy as np

values = [189, 186, 186, 186, 186, 595, 587, 462]
current_value = 345

plt.title('South Fork Rivanna River')
plt.axhline(y=np.mean(values), color='red', linestyle="--", label='Average Water Level')
plt.legend()

plt.ylim(min(values) * .9, max(values) * 1.1)

plt.bar('Current Water Level', current_value)

plt.grid(axis='y', linestyle='-')

plt.subplots_adjust(left=0.1, right=0.6, top=0.9, bottom=0.1)
plt.show()