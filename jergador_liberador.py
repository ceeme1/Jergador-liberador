import os
import sys
import datetime

LOG = "jergador_log.txt"

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {msg}\n")

def aviso():
    texto = """
>>> AVISO LEGAL <<<

Este programa requiere su consentimiento explícito.
Solo úselo si tiene permiso legal sobre este equipo.

¿Acepta los términos? (sí/no): """
    r = input(texto).strip().lower()
    if r not in ["sí", "si"]:
        print("Saliendo. Consentimiento no otorgado.")
        log("El usuario no aceptó el aviso legal.")
        sys.exit()
    log("Aviso legal aceptado.")

def admin():
    try:
        es_admin = (os.getuid() == 0)
    except AttributeError:
        import ctypes
        es_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if not es_admin:
        print("Permisos insuficientes. Ejecútalo como administrador.")
        log("Fallo por falta de permisos.")
        sys.exit()
    log("Permisos de administrador verificados.")

def confirmar(texto):
    r = input(texto + " (sí/no): ").strip().lower()
    return r in ["sí", "si"]

def limpiar_temporales():
    if confirmar("¿Eliminar archivos temporales del sistema?"):
        log("Eliminación de temporales iniciada.")
        print("Limpieza simulada completada.")
        log("Eliminación de temporales completada.")
    else:
        print("Omitido.")
        log("Eliminación de temporales omitida.")

def main():
    log("Inicio del programa.")
    aviso()
    admin()
    limpiar_temporales()
    print("Proceso finalizado. Verifica jergador_log.txt.")
    log("Finalización del programa.")

if __name__ == "__main__":
    main()