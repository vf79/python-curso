import socket
import httpx
import requests


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("example.com", 80))

cmd = "GET http://example.com/index.html HTTP/1.0\r\n\r\n".encode()
client.send(cmd)

while True:
    data = client.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")


client.close()
print("*" * 120)
result = requests.get("http://example.com/index.html")
print(result.status_code)
print(result.content)

print("*" * 120)
result = httpx.get("http://example.com/index.html")
print(result.status_code)
print(result.content)
