#!/usr/bin/env python3
"""
Task 2 - Diccionarios y filtros con animales
Autores: Carlos Alberto Vidrios Serrano
         Jorge Saúl Montes Cáceres
"""

def crear_diccionario_animales():
    """Crea el diccionario inicial con los animales proporcionados"""
    animales_texto = "Ferret, boar, jaguar, giraffe, lizard, locust, lion, wolf, parrot, raccoon, butterfly, jellyfish, fly, gnat, bat, otter, bear, polar bear, oyster, sheep, bee, eagle, antelope, spider, squirrel, tuna, ostrich, wasp, whale, bison, buffalo, owl, donkey, horse, goat, squid, chameleon, camel, crab, kangaroo, cat, dog"
    
    # Convertir a lista y limpiar espacios
    lista_animales = [animal.strip() for animal in animales_texto.split(",")]
    
    # Crear diccionario con clave en minúsculas y valor original
    diccionario_animales = {}
    for animal in lista_animales:
        clave = animal.lower()
        diccionario_animales[clave] = f"animal definicion-{animal}"
    
    return diccionario_animales

def filtrar_por_letra(diccionario, letra):
    """Filtra animales que contienen una letra específica"""
    return {clave: valor for clave, valor in diccionario.items() if letra in clave}

def main():
    print("=== Task 2 - Diccionarios de animales ===")
    
    # Crear diccionario principal
    animales_dict = crear_diccionario_animales()
    
    print(f"Total de animales en el diccionario: {len(animales_dict)}")
    print("Diccionario animales completos:")
    for clave, valor in sorted(animales_dict.items()):
        print(f"  {clave} -> {valor}")
    
    # Filtrar por letras específicas
    print("\n--- Filtros por letra ---")
    
    # a. Animales con la letra "a"
    animales_con_a = filtrar_por_letra(animales_dict, "a")
    print(f"\na) Animales con 'a' ({len(animales_con_a)} encontrados):")
    for clave, valor in sorted(animales_con_a.items()):
        print(f"  {clave} -> {valor}")
    
    # b. Animales con la letra "b"
    animales_con_b = filtrar_por_letra(animales_dict, "b")
    print(f"\nb) Animales con 'b' ({len(animales_con_b)} encontrados):")
    for clave, valor in sorted(animales_con_b.items()):
        print(f"  {clave} -> {valor}")
    
    # c. Animales con la letra "y"
    animales_con_y = filtrar_por_letra(animales_dict, "y")
    print(f"\nc) Animales con 'y' ({len(animales_con_y)} encontrados):")
    for clave, valor in sorted(animales_con_y.items()):
        print(f"  {clave} -> {valor}")
    
    # Size de los diccionarios
    print("\n--- Datos de los diccionarios ---")
    print(f"Total de animales únicos: {len(animales_dict)}")
    print(f"Animales con 'a': {len(animales_con_a)}")
    print(f"Animales con 'b': {len(animales_con_b)}")
    print(f"Animales con 'y': {len(animales_con_y)}")

if __name__ == "__main__":
    main()