import matplotlib.pyplot as plt
from utils.GenerateScreenPoints import generate_spiral_corn

ps1, ps2 = generate_spiral_corn()
plt.figure()
plt.scatter(ps1[0], ps1[1])
plt.savefig("ps1.png")
plt.figure()
plt.scatter(ps2[0], ps2[1])
plt.savefig("ps2.png")
