import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")
db_host = os.environ.get("DB_HOST", "db")
db_port = os.environ.get("DB_PORT", "5432")

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    status = db.Column(db.String(20), nullable=False, default="ToDo")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
        }


@app.before_request
def create_tables():
    if not hasattr(app, 'tables_created'):
        db.create_all()
        app.tables_created = True


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([t.to_dict() for t in tasks])


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")
    description = data.get("description", "")
    status = data.get("status", "ToDo")

    if not title:
        return {"error": "title es requerido"}, 400

    if status not in ["ToDo", "Doing", "Done"]:
        return {"error": "status inválido"}, 400

    task = Task(title=title, description=description, status=status)
    db.session.add(task)
    db.session.commit()
    return task.to_dict(), 201


@app.route("/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get(id)
    if not task:
        return {"error": "tarea no encontrada"}, 404

    data = request.get_json()

    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    status = data.get("status", task.status)

    if status not in ["ToDo", "Doing", "Done"]:
        return {"error": "status inválido"}, 400

    task.status = status

    db.session.commit()
    return task.to_dict()


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return {"error": "tarea no encontrada"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "tarea eliminada"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
