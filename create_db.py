import sqlite3

# Conexão com o banco de dados (cria o arquivo .db se não existir)
conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()

# Criação da tabela de clientes com a coluna de e-mail incluída
cursor.execute('''
CREATE TABLE IF NOT EXISTS table_client (
    id_client INTEGER PRIMARY KEY AUTOINCREMENT,
    name_client TEXT NOT NULL,
    address TEXT,
    city TEXT,
    state TEXT,
    phone TEXT,
    email TEXT
)
''')

# Criação da tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS table_product (
    id_product INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
)
''')

# Criação da tabela de pedidos
cursor.execute('''
CREATE TABLE IF NOT EXISTS table_order (
    id_order INTEGER PRIMARY KEY AUTOINCREMENT,
    id_client INTEGER NOT NULL,
    id_product INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    status TEXT CHECK (status IN ('ok', 'pendent')),
    order_date TEXT DEFAULT CURRENT_DATE,
    FOREIGN KEY (id_client) REFERENCES table_client(id_client),
    FOREIGN KEY (id_product) REFERENCES table_product(id_product)
)
''')

# Inserindo dados na tabela table_client
cursor.executemany('''
INSERT INTO table_client (name_client, address, city, state, phone, email)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ('Alice', '123 Rua das Flores', 'São Paulo', 'SP', '11987654321', 'alice@example.com'),
    ('Bob', '456 Avenida Central', 'Rio de Janeiro', 'RJ', '21987654321', 'bob@example.com'),
    ('Carlos', '789 Rua Nova', 'Curitiba', 'PR', '41987654321', 'carlos@example.com'),
    ('Diana', '1010 Avenida Paulista', 'São Paulo', 'SP', '11991234567', 'diana@example.com'),
    ('Eduardo', '2020 Rua das Palmeiras', 'Belo Horizonte', 'MG', '31987651234', 'eduardo@example.com'),
    ('Fernanda', '3030 Praça da Liberdade', 'Salvador', 'BA', '71987659876', 'fernanda@example.com'),
    ('Gabriela', '4040 Rua do Sol', 'Fortaleza', 'CE', '85987654321', 'gabriela@example.com'),
    ('Henrique', '5050 Avenida do Mar', 'Recife', 'PE', '81987654321', 'henrique@example.com')
])

# Inserindo dados na tabela table_product
cursor.executemany('''
INSERT INTO table_product (description)
VALUES (?)
''', [
    ('Produto A',),
    ('Produto B',),
    ('Produto C',),
    ('Produto D',),
    ('Produto E',),
    ('Produto F',)
])

# Inserindo dados na tabela table_order
cursor.executemany('''
INSERT INTO table_order (id_client, id_product, quantity, price, status)
VALUES (?, ?, ?, ?, ?)
''', [
    (1, 1, 2, 50.00, 'ok'),
    (1, 2, 1, 30.00, 'pendent'),
    (2, 3, 5, 100.00, 'ok'),
    (3, 4, 10, 200.00, 'ok'),
    (4, 5, 3, 45.00, 'pendent'),
    (5, 6, 1, 15.00, 'ok'),
    (6, 1, 7, 70.00, 'pendent'),
    (6, 2, 2, 40.00, 'ok'),
    (6, 3, 5, 125.00, 'ok')
])

# Confirmando as mudanças e fechando a conexão
conn.commit()
conn.close()

print("Banco de dados criado e populado com sucesso!")
