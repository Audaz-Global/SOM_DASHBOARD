import psycopg2

# URL do banco PostgreSQL do Railway
DB_URL = "postgresql://postgres:MopJWitXMvDYDhJnfUFQwZMrTYsPlILK@ballast.proxy.rlwy.net:18110/railway"

# Conectar ao banco
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

# Criar a tabela comando, se ainda não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS comando (
    id SERIAL PRIMARY KEY,
    arquivo TEXT,
    data_comando TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Confirmar e encerrar conexão
conn.commit()
cursor.close()
conn.close()

print("✅ Tabela 'comando' criada com sucesso.")
