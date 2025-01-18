import os

# Definir la ruta donde se creará la carpeta "build"
build_directory = os.path.join(os.getcwd(), "build")

# Crear la carpeta "build" si no existe
os.makedirs(build_directory, exist_ok=True)

# Ruta completa para el archivo "build.py"
build_file_path = os.path.join(build_directory, "build.py")

# Crear y escribir el archivo "build.py"
with open(build_file_path, "w") as build_file:
    build_file.write('print("build.py")')

print(f"Build completed. Created: {build_file_path}")
