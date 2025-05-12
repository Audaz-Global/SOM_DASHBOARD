import psycopg2
import time
import os

# Conexão com PostgreSQL do Railway
DB_URL = "postgresql://postgres:MopJWitXMvDYDhJnfUFQwZMrTYsPlILK@ballast.proxy.rlwy.net:18110/railway"

# Pasta local onde estão os arquivos MP3
CAMINHO = "C:/Users/CS2/OneDrive - AUDAZ GLOBAL/Área de Trabalho/SOM_DASHBOARD/static"

# Armazena o ID do último comando executado
ultimo_id = None

def tocar_musica(arquivo):
    caminho = os.path.join(CAMINHO, arquivo)
    if os.path.exists(caminho):
        print(f"🔊 Tocando: {arquivo}")
        os.system(f'start "" "{caminho}"')
    else:
        print(f"⚠️ Arquivo não encontrado: {arquivo}")

while True:
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT id, arquivo FROM comando
            ORDER BY data_comando DESC
            LIMIT 1
        """)
        resultado = cursor.fetchone()

        if resultado:
            id_comando, nome_arquivo = resultado
            if id_comando != ultimo_id:
                tocar_musica(nome_arquivo)
                ultimo_id = id_comando

        cursor.close()
        conn.close()

    except Exception as e:
        print("❌ Erro ao consultar banco:", e)

    time.sleep(1)  # Consulta a cada 1 segundo
