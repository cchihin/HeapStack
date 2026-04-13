#include <time.h>
#include <iostream>
#include <chrono>

// Initialise
void innit_vec(int* a, int* b, int* c, int N, double* t, int B)
{
    for (int i = 0; i < N; ++i)
    {
        a[i] = 1;
        b[i] = 1;
        c[i] = 0;
    }

    for (int i = 0; i < B; ++i)
    {
        t[i] = 0.0;
    }
}
void vector_add(int* a, int* b, int* c, int N)
{
    for (int i = 0; i < N; ++i)
    {
        c[i] = a[i] + b[i];
    }
} 

int main(int argc, char** argv)
{
    int N = std::stoll(argv[1]);
    int B = std::stoi(argv[2]);

    int a[N];
    int b[N];
    int c[N];
    double t[B];
    double  t_avrg = 0.0;

    // Initialise vectors
    std::cout << "--- Benchmarking vector addition of size " << N << " ---" << std::endl;
    auto start = std::chrono::steady_clock::now();
    innit_vec(a, b, c ,N, t, B);
    auto end = std::chrono::steady_clock::now();
    auto diff = end - start;
    std::cout << "[Initialise] Time taken: " << std::chrono::duration<double, std::milli>(diff).count() << "ms" << std::endl;

    std::cout << "Running benchmark addition over " << B << " loops." << std::endl;
    for (int i = 0; i < B; ++i)
    {
        start = std::chrono::steady_clock::now();
        vector_add(a, b, c ,N);
        end = std::chrono::steady_clock::now();
        diff = end - start;
        t[i] = std::chrono::duration<double, std::milli>(diff).count();
        t_avrg += t[i];
        // std::cout << "[Compute] Time taken: " << t[i] << "ms" << std::endl;
    }
    std::cout << std::endl;
    std::cout << "[Compute] Average Time taken: " << (double)(t_avrg / B) << "ms" << std::endl;
}
