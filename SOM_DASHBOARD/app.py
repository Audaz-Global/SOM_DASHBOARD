from flask import Flask, render_template, request, jsonify
import psycopg2

app = Flask(__name__)

# Conexão com PostgreSQL do Railway
DB_URL = "postgresql://postgres:MopJWitXMvDYDhJnfUFQwZMrTYsPlILK@ballast.proxy.rlwy.net:18110/railway"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tocar-musica', methods=['POST'])
def tocar_musica():
    data = request.get_json()
    nome = data.get("arquivo")

    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comando (arquivo) VALUES (%s)", (nome,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensagem": f"Registrado no banco: {nome}"}), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
