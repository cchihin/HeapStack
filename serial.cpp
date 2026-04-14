#include <time.h>
#include <iostream>
#include <chrono>
#include <fstream>
#include <iomanip>

// Initialise
void innit_vec(int* a, int* b, int* c, int N, double* t_init, double* t_comp, int B)
{
    for (int i = 0; i < N; ++i)
    {
        a[i] = 1;
        b[i] = 1;
        c[i] = 0;
    }

    for (int i = 0; i < B; ++i)
    {
        t_init[i] = 0.0;
        t_comp[i] = 0.0;
    }
}
void vector_add(int* a, int* b, int* c, int N)
{
    for (int i = 0; i < N; ++i)
    {
        c[i] = a[i] + b[i];
    }
} 

void benchmark_allocate_heap(double* t, int N, int B)
{

	double avrg_t = 0.0;

	for (int i = 0; i < B; ++i)
	{
		auto start = std::chrono::steady_clock::now();

		int *a = new int[N];
		int *b = new int[N];
		int *c = new int[N];

		for (int j = 0; j < N; ++j) a[j] = 1, b[j] = 2, c[j] = 0;

		delete[] a;
		delete[] b;
		delete[] c;

		auto end = std::chrono::steady_clock::now();
		auto diff = end - start;

		t[i] = std::chrono::duration<double, std::milli>(diff).count();
        avrg_t += t[i];
	}

	std::cout << "Average time taken for heap allocation: " << (double)(avrg_t / B) << "ms" << std::endl;
}

void benchmark_allocate_stack(double* t, int N, int B)
{
	double avrg_t = 0.0;

	for (int i = 0; i < B; ++i)
	{
		auto start = std::chrono::steady_clock::now();
		int a[N];
		int b[N];
		int c[N];

		for (int j = 0; j < N; ++j) a[j] = 1, b[j] = 2, c[j] = 0;

		auto end = std::chrono::steady_clock::now();
		auto diff = end - start;

		t[i] = std::chrono::duration<double, std::milli>(diff).count();
        avrg_t += t[i];
	}

	std::cout << "Average time taken for stack allocation: " << (double)(avrg_t / B) << "ms" << std::endl;
}

void benchmark_compute_stack(double* t, int N, int B)
{
	double avrg_t = 0.0;

	int a[N];
	int b[N];
	int c[N];

	for (int j = 0; j < N; ++j) a[j] = 1, b[j] = 2, c[j] = 0;

	for (int i = 0; i < B; ++i)
	{
		auto start = std::chrono::steady_clock::now();
		vector_add(a, b, c, N);
		auto end = std::chrono::steady_clock::now();
		auto diff = end - start;

		t[i] = std::chrono::duration<double, std::milli>(diff).count();
        avrg_t += t[i];
	}

	std::cout << "Average time taken for stack compute: " << (double)(avrg_t / B) << "ms" << std::endl;
}

void benchmark_compute_heap(double* t, int N, int B)
{
	double avrg_t = 0.0;

	int* a = new int[N];
	int* b = new int[N];
	int* c = new int[N];

	for (int j = 0; j < N; ++j) a[j] = 1, b[j] = 2, c[j] = 0;

	for (int i = 0; i < B; ++i)
	{
		auto start = std::chrono::steady_clock::now();
		vector_add(a, b, c, N);
		auto end = std::chrono::steady_clock::now();
		auto diff = end - start;

		t[i] = std::chrono::duration<double, std::milli>(diff).count();
        avrg_t += t[i];
	}

	delete[] a;
	delete[] b;
	delete[] c;

	std::cout << "Average time taken for heap compute: " << (double)(avrg_t / B) << "ms" << std::endl;
}

void save_time(double* time, int B, const std::string& name)
{
	
	std::string fname = "logs/" + name + "_" + std::to_string(B) + ".log";
	std::ofstream outFile(fname);
	
	if (outFile.is_open())
	{
		for (int i = 0; i < B; ++i)
		{
			outFile << time[i] << std::endl;
		}
		outFile.close();
	}
	else
	{
		std::cerr << "Unable to open file" << std::endl;
	}
}
	
int main(int argc, char** argv)
{
    int N = std::stoll(argv[1]);
    int B = std::stoi(argv[2]);
	
    std::cout << "--- Benchmarking vector addition of size " << N << ", over " << B << " loops ---" << std::endl;

	double* init_heap	= new double[B];	
	double* init_stack	= new double[B];

	benchmark_allocate_heap(init_heap, N, B);
	benchmark_allocate_stack(init_stack, N, B);
	
	std::string allocate_heap_name = "heap_allocate_N" + std::to_string(N);
	save_time(init_heap, B, allocate_heap_name);

	std::string allocate_stack_name = "stack_allocate_N" + std::to_string(N);
	save_time(init_stack, B, allocate_stack_name);

	benchmark_compute_heap(init_heap, N, B);
	benchmark_compute_stack(init_stack, N, B);
	
	std::string compute_heap_name = "heap_compute_N" + std::to_string(N);
	save_time(init_heap, B, compute_heap_name);

	std::string compute_stack_name = "stack_compute_N" + std::to_string(N);
	save_time(init_stack, B, compute_stack_name);

	delete[] init_heap;
	delete[] init_stack;

}
