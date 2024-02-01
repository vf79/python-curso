#!/usr/bin/env python
import cgi


form = cgi.FieldStorage()
nome = form.getvalue("nome")
mensagem = form.getvalue("mensagem")

print("Content-type:text/html\r\n\r\n")
print("<!DOCTYPE html>")
print('<html lang="pt-BR">')
print('<head>')
print('<meta charset="UTF-8">')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('<title>Enviado</title>')
print('<link rel="stylesheet" href="style.css">')
print('</head>')
print('<body>')
print('<h1>Enviado com sucesso</h1>')
print(f"<h1>{nome} - {mensagem}</h1>")
print('</body>')
print('</html>')
