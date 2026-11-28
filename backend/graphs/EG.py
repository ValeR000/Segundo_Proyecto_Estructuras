# Grafo elevado (GE): caminos y puentes de los soldados, donde van las torres

#Ambas clases hijos que heredan de la padre de graph hacen sus propias valudaciones
#si todo bien entonces llaman a graph que revisa id repetido y vertices existentes
#solo si graph agrego el vertice entonces deciden el tipo de arista
#si cualquier validación falla, el grafo queda exactamente como estaba 

#QUE ES LA BASE:
#Un vértice de GE con vertex_type = "base", y hay solo uno.
#El punto de partida: ahí aparecen los soldados comprados, y desde ahí se calculan el MST y las distancias para elegir las torres.
#El punto de regreso de los soldados que el helicóptero no pudo dejar en ninguna torre.

import math

from backend.errors import InvalidDataError, InvalidOperationError, NotFoundError
from backend.graphs.graph import Graph

VERTEX_TYPES = ("base", "tower_candidate", "transit", "helipad") #tupla de tipos de vertice


def _is_number(value):
    """# Revisa que el valor sea un número real y finito: 
    isinstance acepta solo enteros o decimales (rechaza texto y None), 
    excluye True/False  e isfinite rechaza infinito y NaN."""

    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


class ElevatedGraph(Graph):  # Graph con las reglas de GE: una sola base, tiempos y puentes validos
    def __init__(self):
        super().__init__() #super() significa "llama a la version del padre" osea llama a graph
        #GE revisa lo propio de GE 
        # y despues, con super().add_vertex(vertex), le pasa el vertice al padre para que haga lo general (id repetido y guardarlo)

    def add_vertex(self, vertex):
        if not (_is_number(vertex.x) and _is_number(vertex.y)) or vertex.x <= 0 or vertex.y <= 0: #la posicion en x y y son numeros (valida con isnumber)? y luego pregunta que si alguna es negativa, si lo es saca error Con solo isnumber x = -5 pasaria
            raise InvalidDataError(vertex.id)
        
        if vertex.vertex_type not in VERTEX_TYPES:# si el tipo no esta en la lista de tipos, lanza error
            raise InvalidDataError(vertex.id)
        
        if vertex.vertex_type == "base" and self.base_id is not None: #si ya existe la base pues saca error
            raise InvalidOperationError(vertex.id)
        
        super().add_vertex(vertex) #le pasa el vertice a clase graph y este revisa q no sea repetido y asi

        if vertex.vertex_type == "base": #si no hay base todo bien
            self.base_id = vertex.id

    def add_edge(self, edge):
        for time in (edge.walk_time, edge.moto_time): #Revisa todos los walk time y moto time uno x uno

            if time is not None and (not _is_number(time) or time <= 0): #si no hay tiempo o no es valido el num saca error
                raise InvalidDataError(edge.id)
            
        if edge.is_bridge: #si hay puente mira la resustencia 
            resistance = edge.max_resistance

            if not isinstance(resistance, int) or isinstance(resistance, bool) or resistance <= 0:
                raise InvalidDataError(edge.id) #y valida que sea entero (no puede ser decimal, T/F, texto o none) tiene q ser >0 si no error
            
        super().add_edge(edge) # si todo bn le pasa la arista al padre graph 

    def get_base(self):

        if self.base_id is None:
            raise NotFoundError("base")
        
        return self.vertices[self.base_id]

#ambos get revisan el diccionario de vertices, le extraen los valores con .values 
    def get_candidates(self): #esta es la vaina de propuesta de distribucion de torres
        candidates = []
        for vertex in self.vertices.values():
            if vertex.vertex_type == "tower_candidate":
                candidates.append(vertex)
        return candidates

    def get_helipads(self):
        helipads = []
        for vertex in self.vertices.values():
            if vertex.vertex_type == "helipad":
                helipads.append(vertex)
        return helipads
