import socket
import httpx
import requests

url = "http://localhost/index.html"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9000))

cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
client.send(cmd)

while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")


client.close()
print("*" * 120)
result = requests.get(url)
print(result.status_code)
print(result.content)

print("*" * 120)
result = httpx.get(url)
print(result.status_code)
print(result.content)
