import socket

def get_ip_address(url):
	try:
		ip_address = socket.gethostbyname(url)
		print(f"Ip Address untuk {url} adalah {ip_address}")
	except socket.gaierror:
		print("Tidak dapat menemukan IP Address. Pastikan website sudah benar.")
		
# Ganti dengan URL website yang ingin Anda cek
website_url = "www.ebay.com"
get_ip_address(website_url)