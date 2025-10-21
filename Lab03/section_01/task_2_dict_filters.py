#!/usr/bin/env python3
"""
Lab 3 - Task 2: Construir un diccionario con una lista de animales, a partir del diccionario 
originar crear tres diccionarios cuando las palabras contengan: 'a', 'b', y 'y' (case-insensitive).
Autores: Carlos Alberto Vidrios Serrano
         Jorge Saúl Montes Cáceres
"""

animals = [
    "Ferret", "boar", "jaguar", "giraffe", "lizard", "locust", "lion", "wolf",
    "parrot", "raccoon", "butterfly", "jellyfish", "fly", "gnat", "bat", "otter",
    "bear", "polar bear", "oyster", "sheep", "bee", "eagle", "antelope", "spider",
    "squirrel", "tuna", "ostrich", "wasp", "whale", "bison", "buffalo", "owl",
    "donkey", "horse", "goat", "squid", "chameleon", "camel", "crab", "kangaroo",
    "cat", "dog"
]

def build_animals_dict():
    return {name.lower(): name for name in animals}

def filter_by_letter(d, letter):
    letter = letter.lower()
    return {k: v for k, v in d.items() if letter in k}

def main():
    d = build_animals_dict()
    a_dict = filter_by_letter(d, "a")
    b_dict = filter_by_letter(d, "b")
    y_dict = filter_by_letter(d, "y")

    print("Diccionario original:", len(d)," items ->", sorted(d.values()))
    print("Contienen 'a':", len(a_dict), "items ->", sorted(a_dict.values()))
    print("Contienen 'b':", len(b_dict), "items ->", sorted(b_dict.values()))
    print("Contienen 'y':", len(y_dict), "items ->", sorted(y_dict.values()))

if __name__ == "__main__":
    main()
