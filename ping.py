import socket
import time

def tcping(host, port):
    try:
        start_time = time.time()
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Waktu maksimal untuk menunggu respons dalam detik
        sock.connect((host, port))
        end_time = time.time()
        elapsed_time = end_time - start_time
        sock.close()
        return elapsed_time
    except socket.error:
        return None

# Baca daftar alamat IP dan port dari file sumber.txt
hosts = []
with open('hasil2.txt', 'r') as file:
    for line in file:
        ip, port = line.strip().split(':')
        hosts.append({'ip': ip, 'port': int(port)})

    
# Melakukan ping untuk setiap alamat IP dan format hasilnya
results = []
for host in hosts:
    ping_time = tcping(host['ip'], host['port'])
    if ping_time is not None:
        result = f"{host['ip']} - {ping_time * 1000:.2f} ms"
    else:
        result = f"{host['ip']} - Host is unreachable"
    results.append(result)

# Menyimpan hasil ping ke file hasil-ping.txt
with open('hasil-ping.txt', 'w') as file:
    for result in results:
        file.write(result + '\n')

print('Hasil ping telah disimpan ke hasil-ping.txt')