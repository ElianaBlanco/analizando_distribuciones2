import matplotlib.pyplot as plt

# Datos para cada gráfica de torta
labels = ['No anémicos', 'Anémicos']
sizes_anemicos = [len(df[df['anaemia'] == 0]), len(df[df['anaemia'] == 1])]

sizes_diabeticos = [len(df[df['diabetes'] == 0]), len(df[df['diabetes'] == 1])]

sizes_fumadores = [len(df[df['smoking'] == 0]), len(df[df['smoking'] == 1])]

sizes_muertos = [len(df[df['DEATH_EVENT'] == 0]), len(df[df['DEATH_EVENT'] == 1])]

# Crear subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Gráfica de torta para cantidad de anémicos
axs[0, 0].pie(sizes_anemicos, labels=labels, autopct='%1.1f%%')
axs[0, 0].set_title('Cantidad de anémicos')

# Gráfica de torta para cantidad de diabéticos
axs[0, 1].pie(sizes_diabeticos, labels=labels, autopct='%1.1f%%')
axs[0, 1].set_title('Cantidad de diabéticos')

# Gráfica de torta para cantidad de fumadores
axs[1, 0].pie(sizes_fumadores, labels=labels, autopct='%1.1f%%')
axs[1, 0].set_title('Cantidad de fumadores')

# Gráfica de torta para cantidad de muertos
axs[1, 1].pie(sizes_muertos, labels=labels, autopct='%1.1f%%')
axs[1, 1].set_title('Cantidad de muertos')

plt.tight_layout()
plt.show()
