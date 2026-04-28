#!/usr/bin/env python3
# Asistente de Estudio CLI - versión mínima viable (MVP)

from typing import List


def mostrar_menu() -> None:
    print("\n=== Asistente de Estudio ===")
    print("1) Agregar nota")
    print("2) Agregar pregunta")
    print("3) Agregar recordatorio")
    print("4) Ver resumen")
    print("5) Salir")


def agregar_elemento(titulo: str, contenedor: List[str]) -> None:
    texto = input(f"Escribe tu {titulo}: ").strip()
    if not texto:
        print("⚠️ No se guardó nada porque el texto está vacío.")
        return

    contenedor.append(texto)
    print(f"✅ {titulo.capitalize()} guardada(o).")


def imprimir_lista(nombre: str, elementos: List[str]) -> None:
    print(f"\n{nombre}:")
    if not elementos:
        print("- (sin elementos)")
        return

    for indice, item in enumerate(elementos, start=1):
        print(f"{indice}. {item}")


def ver_resumen(notas: List[str], preguntas: List[str], recordatorios: List[str]) -> None:
    print("\n=== Resumen de la sesión ===")
    imprimir_lista("Notas", notas)
    imprimir_lista("Preguntas", preguntas)
    imprimir_lista("Recordatorios", recordatorios)


def ejecutar() -> None:
    notas: List[str] = []
    preguntas: List[str] = []
    recordatorios: List[str] = []

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_elemento("nota", notas)
        elif opcion == "2":
            agregar_elemento("pregunta", preguntas)
        elif opcion == "3":
            agregar_elemento("recordatorio", recordatorios)
        elif opcion == "4":
            ver_resumen(notas, preguntas, recordatorios)
        elif opcion == "5":
            print("\n¡Éxito en tu estudio! Nos vemos.")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo con un número del 1 al 5.")


if __name__ == "__main__":
    ejecutar()
