from flask import Flask, request, jsonify
import sqlite3
from pathlib import Path

app = Flask(__name__)
DB = Path("cupcake_express.db")

def init_db():
    with sqlite3.connect(DB) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT NOT NULL,
            pagamento TEXT NOT NULL,
            subtotal REAL NOT NULL,
            taxa_entrega REAL NOT NULL,
            total REAL NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pedido recebido'
        )
        """)

@app.route("/api/pedidos", methods=["POST"])
def criar_pedido():
    init_db()
    dados = request.get_json(force=True)

    obrigatorios = ["cliente", "telefone", "endereco", "pagamento", "subtotal"]
    faltando = [campo for campo in obrigatorios if not dados.get(campo)]

    if faltando:
        return jsonify({
            "erro": "Campos obrigatórios ausentes",
            "campos": faltando
        }), 400

    subtotal = float(dados["subtotal"])
    taxa_entrega = 8.00
    total = subtotal + taxa_entrega

    with sqlite3.connect(DB) as conn:
        cur = conn.execute(
            """
            INSERT INTO pedidos
            (cliente, telefone, endereco, pagamento, subtotal, taxa_entrega, total)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                dados["cliente"],
                dados["telefone"],
                dados["endereco"],
                dados["pagamento"],
                subtotal,
                taxa_entrega,
                total
            )
        )
        pedido_id = cur.lastrowid

    return jsonify({
        "pedido_id": pedido_id,
        "taxa_entrega": taxa_entrega,
        "total": total,
        "status": "Pedido recebido"
    }), 201

@app.route("/api/pedidos/<int:pedido_id>", methods=["GET"])
def consultar_pedido(pedido_id):
    init_db()

    with sqlite3.connect(DB) as conn:
        row = conn.execute(
            """
            SELECT id, cliente, telefone, endereco, pagamento,
                   subtotal, taxa_entrega, total, status
            FROM pedidos
            WHERE id = ?
            """,
            (pedido_id,)
        ).fetchone()

    if not row:
        return jsonify({"erro": "Pedido não encontrado"}), 404

    return jsonify({
        "id": row[0],
        "cliente": row[1],
        "telefone": row[2],
        "endereco": row[3],
        "pagamento": row[4],
        "subtotal": row[5],
        "taxa_entrega": row[6],
        "total": row[7],
        "status": row[8]
    })

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
