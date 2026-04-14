import os
import numpy as np
import matplotlib.pyplot as plt

def get_allocation():
	# Plotting allocation speed
	avrg_halloc = []
	avrg_salloc = []
	std_halloc = []
	std_salloc = []
	for n in range(10, 21, 2):
		if (2**n) < 10000:
			B = 500000
		else:
			B = 1000
		
		# Reading heap and stack allocation logs
		halloc = np.genfromtxt(f'logs/heap_allocate_N{2**n}_{B}.log')
		salloc = np.genfromtxt(f'logs/stack_allocate_N{2**n}_{B}.log')
		
		
		# Computing average and std of heap allocation 
		avrg_halloc.append(halloc.mean())
		std_halloc.append(halloc.std())

		# Computing average and std of stack allocation 
		avrg_salloc.append(salloc.mean())
		std_salloc.append(salloc.std())
	return avrg_halloc, avrg_salloc

def get_compute():
	# Plotting allocation speed
	avrg_hcompute = []
	avrg_scompute = []
	std_hcompute = []
	std_scompute = []
	for n in range(10, 21, 2):
		if (2**n) < 10000:
			B = 500000
		else:
			B = 1000
		
		# Reading heap and stack computeation logs
		hcompute = np.genfromtxt(f'logs/heap_compute_N{2**n}_{B}.log')
		scompute = np.genfromtxt(f'logs/stack_compute_N{2**n}_{B}.log')
		
		
		# Computing average and std of heap computeation 
		avrg_hcompute.append(hcompute.mean())
		std_hcompute.append(hcompute.std())

		# Computing average and std of stack computeation 
		avrg_scompute.append(scompute.mean())
		std_scompute.append(scompute.std())
	return avrg_hcompute, avrg_scompute

if __name__ == "__main__":

	fig, ax = plt.subplots(1,2)
	
	avrg_halloc, avrg_salloc = get_allocation()

	N = [2**i for i in range(10, 21, 2)]

	ax[0].semilogx(N, avrg_halloc, '-o', label='Heap')
	ax[0].semilogx(N, avrg_salloc, '-o', label='Stack')
	ax[0].grid()
	ax[0].set_xlabel('Size of array (N)')
	ax[0].set_ylabel('Clock time (ms)')
	ax[0].set_title('Heap v.s. Stack Allocation')
	ax[0].legend()

	avrg_hcompute, avrg_scompute = get_compute()

	ax[1].semilogx(N, avrg_hcompute, '-o')
	ax[1].semilogx(N, avrg_scompute, '-o')
	ax[1].grid()
	ax[1].set_ylabel('Clock time (ms)')
	ax[1].set_title('Heap v.s. Stack Compute')

	fig.suptitle(r'Benchmarking vector addition of $c = a + b \in \mathbb{R}^{N}$' + '\n' + 'between heap and stack allocation and compute', y=1.05)

	fig.set_size_inches(9,5)
	fig.subplots_adjust(wspace=0.4)
	fig.savefig('benchmarkplot.pdf', bbox_inches='tight')
