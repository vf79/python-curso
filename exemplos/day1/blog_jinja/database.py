# 1 conectar com o banco de dados
from sqlite3 import connect

conn = connect("blog.db", check_same_thread=False)
cursor = conn.cursor()


# 2 definir e criar a tabela
conn.execute(
    """\
    CREATE TABLE if not exists posts (
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """
)

# 3 Criamos os posts iniciais para alimentar o banco de dados
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """\
            A linguagem Python foi eleita a linguagem mais popular
            pela revista tech master e segue dominando o mundo.
            """,
        "author": "Satoshi Namamoto"},
    {
        "title": "Como criar um blog utilizando Python",
        "content": """Neste tutorial você aprenderá como criar um blog \
            utilizando Python. <pre> import make_a_blog </pre>""",
        "author": "Guido Van Rossum"},
]

# 4 - Inserimos os posts caso o banco de dados esteja vazio
count = cursor.execute("SELECT * FROM posts;").fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO posts (title, content, author)
        VALUES (:title, :content, :author);
        """,
        posts
    )
    conn.commit()

# 5 - Verificamos que foi realmente inserido
posts = cursor.execute("SELECT * FROM posts;").fetchall()
assert len(posts) >= 2
