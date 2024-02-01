# carregar os dados
dados = [
    {"nome": "Python", "cidade": "Curitiba"},
    {"nome": "Java", "cidade": "Nova York"},
]

# processar
template = """\
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>First Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <ul>
        <li> Nome: {dados[nome]}
        <li> Cidade: {dados[cidade]}
    </ul>
</body>
</html>
"""

# renderizar
for item in dados:
    print(template.format(dados=item))
