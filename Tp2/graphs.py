import matplotlib.pyplot as plt
#-------------------------------------------------------------------
#							EXAMPLE 1
#-------------------------------------------------------------------
x = [0, 1, 2, 3, 4, 5,6, 7, 8, 9]
y1 = [0.11, 0.11, 0.18, 0.33, 0.05, 0.02, 0.04, 0.08, 0.01, 0.07]
y2 = [0.15, 0.11, 0.25, 0.17, 0.05, 0.04, 0.09, 0.08, 0.0, 0.06]

plt.plot(x,y1, marker='o', linestyle='-.', color='c', label="una simulacion")
# plt.plot(x, y2, label="otra simulacion")
plt.plot(x, y2, marker='o', linestyle='-.', color='r', label='Square')
plt.xlabel("Nodos")
plt.ylabel("Recurrencias")
plt.title("Interesting Graph")
plt.legend()

plt.show()

#-------------------------------------------------------------------
#							EXAMPLE 2
#-------------------------------------------------------------------

# x = [0, 1, 2, 3, 4, 5,6, 7, 8, 9]
# y1 = [0.11, 0.11, 0.18, 0.33, 0.05, 0.02, 0.04, 0.08, 0.01, 0.07]
# y2 = [0.15, 0.11, 0.25, 0.17, 0.05, 0.04, 0.09, 0.08, 0.0, 0.06]
# plt.bar(x, y1, label="another graph", color='b')
# plt.bar(x, y2, label="Another another graph", color='g')
# plt.xlabel('Nodos')
# plt.ylabel('Recurrencias')
# plt.show()