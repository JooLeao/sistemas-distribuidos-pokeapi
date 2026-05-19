import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor

from downloader import download_pokemon_image

def run_sequential(n_requests):
    for i in range(1, n_requests + 1):
        download_pokemon_image(i)

def worker_thread(poke_ids):
    for pid in poke_ids:
        download_pokemon_image(pid)

def run_threading(n_requests, num_threads):
    threads = []
    ids = list(range(1, n_requests + 1))
    chunk_size = max(1, len(ids) // num_threads)
    
    for i in range(num_threads):
        start = i * chunk_size
        end = None if i == num_threads - 1 else (i + 1) * chunk_size
        chunk = ids[start:end]
        
        t = threading.Thread(target=worker_thread, args=(chunk,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()

def run_multiprocessing(n_requests, num_processes):
    ids = list(range(1, n_requests + 1))
    with multiprocessing.Pool(processes=num_processes) as p:
        p.map(download_pokemon_image, ids)

def run_concurrent_futures(n_requests, num_workers):
    ids = list(range(1, n_requests + 1))
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        list(executor.map(download_pokemon_image, ids))