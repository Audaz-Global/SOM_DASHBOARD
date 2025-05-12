import psycopg2

# URL do PostgreSQL (Railway)
DB_URL = "postgresql://postgres:MopJWitXMvDYDhJnfUFQwZMrTYsPlILK@ballast.proxy.rlwy.net:18110/railway"

# Conecta no banco
conn = psycopg2.connect(DB_URL)
cursor = conn.cursor()

# Cria a tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS visitas (
    id SERIAL PRIMARY KEY,
    pagina TEXT,
    ip TEXT,
    user_agent TEXT,
    data_acesso TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Salva e fecha
conn.commit()
cursor.close()
conn.close()

print("Tabela 'visitas' criada com sucesso.")
