#Membuka file sumber.txt
with open('1sumber.txt', 'r') as file:
    # Membaca seluruh konten file
    data = file.read()

# Memisahkan baris-baris
lines = data.split('\n')

# Mencari baris yang mengandung "HTTP/1.1 200 OK -- Server: cloudflare"
filtered_lines = [line for line in lines if 'HTTP/1.1 200 OK -- Server: cloudflare' in line]

# Menyimpan hasil ke dalam file hasil1.txt
with open('hasil1.txt', 'w') as file:
    for line in filtered_lines:
        file.write(line + '\n')
        
print("Disimpan di ->> hasil.txt")