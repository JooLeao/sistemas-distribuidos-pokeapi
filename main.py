import time
import statistics
import metodos

def measure_performance(func, *args, iterations=10):
    """
    Executa a função 'iterations' vezes, guarda os tempos individuais 
    e retorna a Média, Mediana e o Desvio Padrão.
    """
    tempos_individuais = []
    
    for _ in range(iterations):
        start_time = time.time()
        func(*args)
        end_time = time.time()

        tempos_individuais.append(end_time - start_time)
    
    avg_time = statistics.mean(tempos_individuais)
    med_time = statistics.median(tempos_individuais)
    stdev_time = statistics.stdev(tempos_individuais)
    
    return avg_time, med_time, stdev_time

if __name__ == "__main__":
    QTD_POKEMON = 10 
    WORKERS = 8 
    ITERATIONS = 10 
    
    print(f"--- Iniciando testes para {QTD_POKEMON} requisições com {WORKERS} workers ---")

    print("\n1. A testar Sequencial...")
    avg_seq, med_seq, stdev_seq = measure_performance(metodos.run_sequential, QTD_POKEMON, iterations=ITERATIONS)
    print(f"Média: {avg_seq:.2f}s | Mediana: {med_seq:.2f}s | Desvio P.: {stdev_seq:.2f}s")

    print("\n2. A testar Threading...")
    avg_thread, med_thread, stdev_thread = measure_performance(metodos.run_threading, QTD_POKEMON, WORKERS, iterations=ITERATIONS)
    print(f"Média: {avg_thread:.2f}s | Mediana: {med_thread:.2f}s | Desvio P.: {stdev_thread:.2f}s")

    print("\n3. A testar Multiprocessing...")
    avg_multi, med_multi, stdev_multi = measure_performance(metodos.run_multiprocessing, QTD_POKEMON, WORKERS, iterations=ITERATIONS)
    print(f"Média: {avg_multi:.2f}s | Mediana: {med_multi:.2f}s | Desvio P.: {stdev_multi:.2f}s")

    print("\n4. A testar Concurrent.Futures...")
    avg_fut, med_fut, stdev_fut = measure_performance(metodos.run_concurrent_futures, QTD_POKEMON, WORKERS, iterations=ITERATIONS)
    print(f"Média: {avg_fut:.2f}s | Mediana: {med_fut:.2f}s | Desvio P.: {stdev_fut:.2f}s")