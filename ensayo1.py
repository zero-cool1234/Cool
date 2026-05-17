import os
import random
import sys
import time
from tqdm import tqdm

# Limpiar pantalla para mejor estética visual
os.system('clear' if os.name == 'posix' else 'cls')
time.sleep(0.1)

# BANNER: Combinación de Azul (\033[44m o \033[34m) y Blanco (\033[97m o \033[47m)
print("""
\033[97;44m Ƹ̵̡Ӝ̵̨̄ 𝐙𝐄𝐑𝐎𝐂𝐎𝐎𝐋 - 𝐂𝐑𝐄𝐀𝐃𝐎𝐑 𝐃𝐄 𝐂𝐎𝐌𝐁𝐎𝐒 𝐔𝐍𝐈𝐅𝐈𝐂𝐀𝐃𝐎 Ƹ̵̡Ӝ̵̨̄ \033[0m
\033[34m
  ███████╗███████╗██████╗  ██████╗  ██████╗ ██████╗ ██╗     
  ╚══███╔╝██╔════╝██╔══██╗██╔═══██╗██╔════╝██╔═══██╗██║     
    ███╔╝ █████╗  ██████╔╝██║   ██║██║     ██║   ██║██║     
   ███╔╝  ██╔══╝  ██╔══██╗██║   ██║██║     ██║   ██║██║     
  ███████╗███████╗██║  ██║╚██████╔╝╚██████╗╚██████╔╝███████╗
  ╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝
\033[0m
\033[47;34m ─── 𝐄𝐝𝐢𝐭 𝐛𝐲 𝐳𝐞𝐫𝐨𝐜𝐨𝐨𝐥 ─── ⓕⓡⓘⓔⓝⓓⓢ ⓢⓒⓗⓞⓞⓛ ─── \033[0m
""")
time.sleep(0.1)

def main():
    print("\033[1;34m[+] INICIANDO CONFIGURACIÓN DEL COMBO\033[0m\n")
    
    # 1.a Ruta del Archivo de Nombres
    file_path = input("\033[1;97;44m 1.a \033[0m Ruta del Archivo de Nombres (.txt): ").strip()
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            names_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("\n\033[31m[-] Error: Archivo no encontrado. Verifique la ruta.\033[0m")
        return

    # 2.- Nombre que le daremos
    filename = input("\033[1;97;44m 2   \033[0m Nombre que le daremos al archivo de salida: ").strip()

    # 3.- Longitud de las contraseñas
    try:
        longitud_pass = int(input("\033[1;97;44m 3   \033[0m Longitud de las contraseñas (Cantidad de caracteres): "))
        hwm = int(input("\033[1;34m[?] Cantidad de líneas a generar: \033[0m"))
    except ValueError:
        print("\n\033[31m[-] Error: Ingrese un número válido para la longitud/líneas.\033[0m")
        return

    # 4._ El resultado se guardará automáticamente
    print("\n\033[1;47;34m 4._ El resultado se guardará automáticamente \033[0m")
    print(f"\033[34m[i] Líneas base cargadas: {len(names_list)}\033[0m\n")
    
    # Ruta modificada: Se guarda en la misma carpeta donde ejecutas el programa
    output_file_path = f"./{filename}@.txt"
    
    # Barra de progreso personalizada en color azul/celeste
    with open(output_file_path, "a+", encoding="utf-8") as f:
        with tqdm(total=hwm, desc="Procesando", bar_format="{l_bar}\033[34m{bar}\033[0m| {n_fmt}/{total_fmt}", ncols=70) as pbar:
            for _ in range(hwm):
                rname = random.choice(names_list)
                
                # Generación de la contraseña con la longitud exacta requerida
                pass_base = rname
                while len(pass_base) < longitud_pass:
                    pass_base += str(random.randint(0, 9))
                
                password = pass_base[:longitud_pass]
                
                # Escritura directa en formato USER:PASS
                f.write(f"{rname}:{password}\n")
                pbar.update(1)
                time.sleep(0.001)

    print(f"\n\033[1;97;44m [✓] GUARDADO AUTOMÁTICO EXITOSO \033[0m")
    print(f"\033[34mRuta: {os.path.abspath(output_file_path)}\033[0m\n")

if __name__ == "__main__":
    main()
