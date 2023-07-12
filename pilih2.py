# Membuka file sumber.txt
with open('hasil1.txt', 'r') as file:
    # Membaca seluruh konten file
    data = file.read()

# Memisahkan baris-baris
lines = data.split('\n')

# Mencari baris yang mengandung "HTTP/1.1 200 OK -- Server: cloudflare"
filtered_lines = [line for line in lines if 'HTTP/1.1 200 OK -- Server: cloudflare' in line]

# Menghapus kata "HTTP/1.1 200 OK -- Server: cloudflare" dari setiap baris
modified_lines = [line.replace('HTTP/1.1 200 OK -- Server: cloudflare', '') for line in filtered_lines]

# Menyimpan hasil ke dalam file hasil1.txt
with open('hasil2.txt', 'w') as file:
    for line in modified_lines:
        file.write(line + '\n')

print("Disimpan di ->> hasil2.txt")

