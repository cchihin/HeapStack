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

	return avrg_halloc, avrg_salloc, \
		std_halloc, std_salloc

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
	return avrg_hcompute, avrg_scompute, \
		std_hcompute, std_scompute

if __name__ == "__main__":

	fig, ax = plt.subplots(2,2)
	
	avrg_halloc, avrg_salloc, \
	std_halloc, std_salloc = get_allocation()

	N = [2**i for i in range(10, 21, 2)]

	ax[0,0].errorbar(N, avrg_halloc, yerr=std_halloc, capsize=5.0, label='Heap')
	ax[0,0].errorbar(N, avrg_salloc, yerr=std_salloc, capsize=5.0, label='Stack')
	ax[0,0].grid()
	ax[0,0].set_xscale('log')
	ax[0,0].set_yscale('log')
	ax[0,0].set_xlabel('Size of array (N)')
	ax[0,0].set_ylabel('Clock time (ms)')
	ax[0,0].set_title('Heap v.s. Stack Allocation')
	ax[0,0].legend()

	alloc_speedup = np.array(avrg_halloc) / np.array(avrg_salloc)
	
	ax[1,0].plot(N, alloc_speedup, 'ko-')
	ax[1,0].grid()
	ax[1,0].set_xscale('log')
	ax[1,0].set_xlabel('Size of array (N)')
	ax[1,0].set_ylabel('Speed up (Stack / Heap)')

	avrg_hcompute, avrg_scompute, \
	std_hcompute, std_scompute = get_compute()

	ax[0,1].errorbar(N, avrg_hcompute, yerr=std_hcompute, capsize=5.0, label='Heap')
	ax[0,1].errorbar(N, avrg_scompute, yerr=std_scompute, capsize=5.0, label='Stack')
	ax[0,1].grid()
	ax[0,1].set_xscale('log')
	ax[0,1].set_yscale('log')
	ax[0,1].set_ylabel('Clock time (ms)')
	ax[0,1].set_xlabel('Size of array (N)')
	ax[0,1].set_title('Heap v.s. Stack Compute')

	compute_speedup = np.array(avrg_hcompute) / np.array(avrg_scompute)

	ax[1,1].plot(N, compute_speedup, 'ko-')
	ax[1,1].grid()
	ax[1,1].set_xscale('log')
	ax[1,1].set_xlabel('Size of array (N)')
	ax[1,1].set_ylabel('Speed up (Stack / Heap)')

	fig.suptitle(r'Benchmarking vector addition of $c = a + b \in \mathbb{R}^{N}$' + '\n' + 'between heap and stack allocation and compute', y=0.98)

	fig.set_size_inches(9,8)
	fig.subplots_adjust(wspace=0.4)
	fig.savefig('plots/benchmarkplot.png', bbox_inches='tight')
