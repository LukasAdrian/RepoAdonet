import hashlib

def generate_md5(file_path):
    """
    Genera el archivo addons.xml.md5 a partir del addons.xml
    """
    try:
        # Leer el archivo addons.xml
        with open(file_path, 'rb') as file:
            content = file.read()

        # Generar el hash MD5 del contenido de addons.xml
        md5_hash = hashlib.md5(content).hexdigest()

        # Escribir el hash en el archivo addons.xml.md5
        with open(f"{file_path}.md5", 'w') as md5_file:
            md5_file.write(md5_hash)

        print(f"El archivo {file_path}.md5 fue generado exitosamente: {md5_hash}")
    except FileNotFoundError:
        print(f"El archivo {file_path} no existe. Asegúrate de generarlo primero.")
    except Exception as e:
        print(f"Se produjo un error: {e}")

# Especifica el nombre de tu archivo addons.xml
generate_md5('addons.xml')
