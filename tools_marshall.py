import requests

print('#----------------------------#')
print('#       AnarchoXploit        #')
print('#  Spam Whatsapp Unlimited   #')
print('#  MarsHall - c0untin9live   #')
print('#----------------------------#')
  
nomor = input('Masukan Nomor => ')
pesan = input('Masukan Pesan => ')
url = 'https://api.chat-api.com/instance#NOMOR-AKUN-ANDA/sendMessage?token=#TOKEN-ANDA&phone={}&body={}'\ # Jika sudah memasukkan Nomor akun dan token hapus tanda (#)
    .format(nomor,pesan)
while True:
    req = requests.post(url)