class Pokemon:
    def __init__(self, nombre, numero, tipo):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if not self.root:
            self.root = Node(key, data)
        else:
            self._insert_recursive(self.root, key, data)

    def _insert_recursive(self, node, key, data):
        if key < node.key:
            if node.left:
                self._insert_recursive(node.left, key, data)
            else:
                node.left = Node(key, data)
        elif key > node.key:
            if node.right:
                self._insert_recursive(node.right, key, data)
            else:
                node.right = Node(key, data)

    def find_by_name(self, name):
        return self._find_by_name_recursive(self.root, name)

    def _find_by_name_recursive(self, node, name):
        if not node:
            return None
        if name.lower() in node.data.nombre.lower():
            return node.data
        elif name < node.key:
            return self._find_by_name_recursive(node.left, name)
        else:
            return self._find_by_name_recursive(node.right, name)

    def find_by_number(self, number):
        return self._find_by_number_recursive(self.root, number)

    def _find_by_number_recursive(self, node, number):
        if not node:
            return None
        if number == node.data.numero:
            return node.data
        elif number < node.key:
            return self._find_by_number_recursive(node.left, number)
        else:
            return self._find_by_number_recursive(node.right, number)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, node, result):
        if node:
            self._inorder_traversal_recursive(node.left, result)
            result.append(node.data)
            self._inorder_traversal_recursive(node.right, result)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.data = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, data):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.data = data

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return self._find_words(node)

    def _find_words(self, node):
        results = []
        if node.data:
            results.append(node.data)
        for char, child in node.children.items():
            results.extend(self._find_words(child))
        return results


class TypeNode:
    def __init__(self, type_name):
        self.type_name = type_name
        self.pokemons = []  
        self.children = []


class TypeTree:
    def __init__(self):
        self.root = None

    def insert(self, type_name, pokemon):
        if not self.root:
            self.root = TypeNode(type_name)
        self._insert_recursive(self.root, type_name, pokemon)

    def _insert_recursive(self, node, type_name, pokemon):
        if node.type_name.lower() == type_name.lower():
            node.pokemons.append(pokemon)
        else:
            for child in node.children:
                if child.type_name.lower() == type_name.lower():
                    child.pokemons.append(pokemon)
                    return
            new_child = TypeNode(type_name)
            new_child.pokemons.append(pokemon)
            node.children.append(new_child)

    def get_pokemons_by_type(self, type_name):
        return self._get_pokemons_recursive(self.root, type_name)

    def _get_pokemons_recursive(self, node, type_name):
        if not node:
            return []
        if node.type_name.lower() == type_name.lower():
            return node.pokemons
        else:
            result = []
            for child in node.children:
                result.extend(self._get_pokemons_recursive(child, type_name))
            return result


pokemons = [
    Pokemon("Bulbasaur", 1, "Planta"),
    Pokemon("Charmander", 4, "Fuego"),
    Pokemon("Jolteon", 135, "Eléctrico"),
    Pokemon("Lycanroc", 745, "Roca"),
    Pokemon("Pikachu", 25, "Eléctrico"),
    Pokemon("Tyrantrum", 697, "Roca"),
]

name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = TypeTree()
trie = Trie()

for pokemon in pokemons:
    name_tree.insert(pokemon.nombre.lower(), pokemon)
    number_tree.insert(pokemon.numero, pokemon)
    type_tree.insert(pokemon.tipo, pokemon)
    trie.insert(pokemon.nombre.lower(), pokemon)


def search_pokemon(name, number):
    found_by_name = name_tree.find_by_name(name)
    found_by_number = number_tree.find_by_number(number)
    return found_by_name, found_by_number


def get_pokemons_of_type(type_name):
    pokemons_of_type = type_tree.get_pokemons_by_type(type_name)
    if pokemons_of_type:
        return [pokemon.nombre for pokemon in pokemons_of_type]
    else:
        return None



def get_sorted_pokemons_by_number_and_name():
    return number_tree.inorder_traversal()



def get_specific_pokemons():
    specific_pokemons = []
    for name in ["Jolteon", "Lycanroc", "Tyrantrum"]:
        found_pokemon = name_tree.find_by_name(name.lower())
        if found_pokemon:
            specific_pokemons.append(found_pokemon)
    return specific_pokemons



def count_pokemons_by_type(type_name):
    pokemons_of_type = type_tree.get_pokemons_by_type(type_name)
    if pokemons_of_type:
        return len(pokemons_of_type)
    else:
        return 0


if __name__ == "__main__":
    pokemon_by_name, pokemon_by_number = search_pokemon("bul", 1)
    if pokemon_by_name:
        print("Pokemon encontrado por nombre:", pokemon_by_name.nombre, pokemon_by_name.numero, pokemon_by_name.tipo)
    if pokemon_by_number:
        print("Pokemon encontrado por número:", pokemon_by_number.nombre, pokemon_by_number.numero, pokemon_by_number.tipo)

    tipo_buscado = "Fuego"
    nombres_por_tipo = get_pokemons_of_type(tipo_buscado)
    if nombres_por_tipo:
        print(f"Los nombres de los pokemons de tipo {tipo_buscado} son: {', '.join(nombres_por_tipo)}")
    else:
        print(f"No se encontraron pokemons del tipo {tipo_buscado}")

    pokemons_ordenados = get_sorted_pokemons_by_number_and_name()
    print("Pokemons ordenados por número y nombre:")
    for pokemon in pokemons_ordenados:
        print(pokemon.numero, pokemon.nombre, pokemon.tipo)

    
    pokemons_especificos = get_specific_pokemons()
    print("Datos de los Pokémons Jolteon, Lycanroc y Tyrantrum:")
    for pokemon in pokemons_especificos:
        print(pokemon.nombre, pokemon.numero, pokemon.tipo)

   
    tipo1 = "Eléctrico"
    tipo2 = "Acero"
    cantidad_tipo1 = count_pokemons_by_type(tipo1)
    cantidad_tipo2 = count_pokemons_by_type(tipo2)
    print(f"Hay {cantidad_tipo1} Pokémons de tipo {tipo1}")
    print(f"Hay {cantidad_tipo2} Pokémons de tipo {tipo2}")