from app.database import get_db



def output_formatter(results):
    out = []
    for task in results:
        res = {
            "id": task[0],
            "name": task[1],
            "summary": task[2],
            "description": task[3],
            "is_done": task[4]
        }
        out.append(res)
    return out


def scan():
    conn = get_db()
    cursor = conn.cursor()  # Primero creas el cursor desde la conexión
    cursor.execute("SELECT * FROM task")  # Ejecutas la consulta con ese cursor
    results = cursor.fetchall()  # Obtienes los resultados
    cursor.close()  # Cierra el cursor correctamente
    return output_formatter(results)  # Formatea y retorna los resultados


def select_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("SELECT * FROM task WHERE id = ?", (task_id,))
    results = cursor.fetchall()
    if results:
        return output_formatter(results)
    return {}


def insert(task_data):
    task_tuple = (
        task_data["name"],
        task_data["summary"],
        task_data["description"],
        task_data["is_done"],
        task_id
    )

    statement  = """
    UPDATE task 
    SET name = ?, 
        summary = ?, 
        description = ?,
        is_done = ?
    WHERE id = ?
    """

    conn = get_db()
    conn.execute(statement, task_tuple)
    conn.commit()

def update_by_id(task_data, task_id):
    task_tuple = {
        task_data["name"],
        task_data["summary"],
        task_data["description"],
        task_data["is_done"]
    }
    statement  = """
    UPDATE task 
    SET name = ?, 
    summary = ?, 
    description = ?,
    is_done = ?
    WHERE id = ?
    """
    conn = get_db()
    cursor = conn.execute(statement, task_id)
    conn.commit()

def delete_by_id(task_id):
    conn = get_db()
    cursor = conn.execute("DELETE FROM task WHERE id = ?", (task_id,))
    conn.commit()

