# biblioteca do python para gráficos
import matplotlib.pyplot as plt
font = {
        'weight' : 'bold',
        'size'   : 16}
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{amsmath}')
plt.rc('font', **font)

import math
import numpy as np
'''

	gráficos no papel milimetrado

'''
def grafico_papel_milimetrado(x_i, y_i):

	fig1, ax1 = plt.subplots(1,1, figsize=(7,5))
	ax1.plot(x_i, y_i, 'ko', label=r'dados')

	x_max = x_i.max()
	y_max = y_i.max()

	pow_10_x = math.floor(math.log(x_max, 10))
	pow_10_y = math.floor(math.log(y_max, 10))

	xtick_max = math.ceil(x_max / 10**pow_10_x)
	ytick_max = math.ceil(y_max / 10**pow_10_y)

	xticks = np.linspace(0, xtick_max,xtick_max+1) * 10**pow_10_x
	yticks = np.linspace(0, ytick_max,ytick_max+1) * 10**pow_10_y

	ax1.set_xticks(xticks)
	ax1.set_yticks(yticks)

	ax1.set_xlim(0, xticks.max())
	ax1.set_ylim(0, yticks.max())


	xticks_minor = np.linspace(0, xtick_max,10*xtick_max+1) * 10**pow_10_x
	yticks_minor = np.linspace(0, ytick_max,10*ytick_max+1) * 10**pow_10_y	

	ax1.set_xticks(xticks_minor, minor=True)
	ax1.set_yticks(yticks_minor, minor=True)


	ax1.grid(which='major', color='gray', linestyle='-', alpha=1, lw=0.45)
	ax1.grid(which='minor', color='r', linestyle='-', alpha=0.5, lw=0.25)

	return fig1, ax1
