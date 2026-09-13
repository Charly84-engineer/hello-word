import argparse
import json
from pathlib import Path


ARCHIVO_TAREAS = Path(__file__).with_name("tareas.json")


def cargar_tareas():
	if not ARCHIVO_TAREAS.exists():
		return []

	with ARCHIVO_TAREAS.open("r", encoding="utf-8") as archivo:
		return json.load(archivo)


def guardar_tareas(tareas):
	with ARCHIVO_TAREAS.open("w", encoding="utf-8") as archivo:
		json.dump(tareas, archivo, ensure_ascii=False, indent=2)


def mostrar_tareas(tareas):
	if not tareas:
		print("No tienes tareas pendientes.")
		return

	for tarea in tareas:
		estado = "x" if tarea["completada"] else " "
		print(f"{tarea['id']}. [{estado}] {tarea['texto']}")


def crear_parser():
	parser = argparse.ArgumentParser(description="Lista de tareas sencilla")
	subcomandos = parser.add_subparsers(dest="comando", required=True)

	subcomandos.add_parser("listar", help="Muestra todas las tareas")

	agregar = subcomandos.add_parser("agregar", help="Crea una tarea nueva")
	agregar.add_argument("texto", help="Texto de la tarea")

	completar = subcomandos.add_parser("completar", help="Marca una tarea como completada")
	completar.add_argument("id", type=int, help="Identificador de la tarea")

	eliminar = subcomandos.add_parser("eliminar", help="Elimina una tarea")
	eliminar.add_argument("id", type=int, help="Identificador de la tarea")

	return parser


def main():
	argumentos = crear_parser().parse_args()
	tareas = cargar_tareas()

	if argumentos.comando == "listar":
		mostrar_tareas(tareas)
		return

	if argumentos.comando == "agregar":
		siguiente_id = max((tarea["id"] for tarea in tareas), default=0) + 1
		tareas.append({"id": siguiente_id, "texto": argumentos.texto, "completada": False})
		guardar_tareas(tareas)
		print(f"Tarea {siguiente_id} agregada.")
		return

	tarea = next((tarea for tarea in tareas if tarea["id"] == argumentos.id), None)
	if tarea is None:
		print(f"No existe una tarea con el id {argumentos.id}.")
		return

	if argumentos.comando == "completar":
		tarea["completada"] = True
		print(f"Tarea {argumentos.id} completada.")
	else:
		tareas.remove(tarea)
		print(f"Tarea {argumentos.id} eliminada.")

	guardar_tareas(tareas)


if __name__ == "__main__":
	main()