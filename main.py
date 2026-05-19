import time
import metodos

def measure_average_time(func, *args, iterations=10):
    total_time = 0
    for _ in range(iterations):
        start_time = time.time()
        func(*args)
        end_time = time.time()
        total_time += (end_time - start_time)
    
    return total_time / iterations

if __name__ == "__main__":
    QTD_POKEMON = 1000
    WORKERS = 8   
    ITERATIONS = 10 
    
    print(f"--- Iniciando testes para {QTD_POKEMON} requisições com {WORKERS} workers ---")

    print("1. A testar Sequencial...")
    avg_seq = measure_average_time(metodos.run_sequential, QTD_POKEMON, iterations=ITERATIONS)
    print(f"Tempo médio Sequencial: {avg_seq:.2f} segundos\n")

    print("2. A testar Threading...")
    avg_thread = measure_average_time(metodos.run_threading, QTD_POKEMON, WORKERS, iterations=ITERATIONS)
    print(f"Tempo médio Threading: {avg_thread:.2f} segundos\n")

    print("3. A testar Multiprocessing...")
    avg_multi = measure_average_time(metodos.run_multiprocessing, QTD_POKEMON, WORKERS, iterations=ITERATIONS)
    print(f"Tempo médio Multiprocessing: {avg_multi:.2f} segundos\n")

    print("4. A testar Concurrent.Futures...")
    avg_concurrent = measure_average_time(metodos.run_concurrent_futures, QTD_POKEMON, WORKERS, iterations=ITERATIONS)
    print(f"Tempo médio Concurrent.Futures: {avg_concurrent:.2f} segundos\n")