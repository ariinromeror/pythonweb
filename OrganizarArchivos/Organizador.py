import os
import shutil

def organizar():
    usuario = os.environ['USERPROFILE']
    ruta = os.path.join(usuario, 'Desktop', 'Descargas')
    
    if not os.path.exists(ruta):
        print("no se encontro la carpeta en el escritorio")
        return

    print("organizando archivos...")
    
    archivos = os.listdir(ruta)
    for nombre in archivos:
        ruta_archivo = os.path.join(ruta, nombre)
        
        if os.path.isfile(ruta_archivo):
            nombre_base, extension = os.path.splitext(nombre)
            ext = extension.lower().strip(".")
            
            if ext and ext not in ["py", "bat"]:
                carpeta_destino = os.path.join(ruta, ext)
                
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                
                shutil.move(ruta_archivo, os.path.join(carpeta_destino, nombre))
                print(f"movido: {nombre} a {ext}")

if __name__ == "__main__":
    organizar()
    print("proceso terminado presiona enter")
    input()