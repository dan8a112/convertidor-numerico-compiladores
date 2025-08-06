#Funcion que recibe una ruta o nombre de archivo y retorna cada linea de este archivo
def read_content_txt(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None
    
#Funcion que recibe una entrada, un string y retorna un array de str con las lineas
def split_input(input: str):
    lines = input.split("$") #se separan por delimitador $
    clean_lines = [line.strip() for line in lines] #Se borran los espacios en blanco
    return clean_lines