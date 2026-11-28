# Grafo base no dirigido con lista de adyacencia GE y GM heredan de aqui (para solo tener una clase grafo y q de ahi salga to)

from backend.errors import InvalidDataError, NotFoundError


class Graph:  # Guarda vetices y aristas y permite agregarlos, buscarlos y recorrer vecinos
    def __init__(self):
        self.vertices = {} #vertices (id → Vertex)
        self.edges = {} #edges (id → Edge)



 #Ambos add reciben el objeto ya creado
    def add_vertex(self, vertex):

        if vertex.id in self.vertices:
            raise InvalidDataError(vertex.id)
        
        self.vertices[vertex.id] = vertex

    def add_edge(self, edge):
        """primero valida (id repetido, extremos que existan) y despues guarda
        Mete el mismo objeto en connections de los dos extremos"""

        if edge.id in self.edges:
            raise InvalidDataError(edge.id)
        
        vertex_a = self.get_vertex(edge.a)
        vertex_b = self.get_vertex(edge.b)

        self.edges[edge.id] = edge

        vertex_a.connections.append(edge)
        vertex_b.connections.append(edge)

#Ambos get lanzan NotFoundError si el id no existe
    def get_vertex(self, vertex_id):

        if vertex_id not in self.vertices:
            raise NotFoundError(vertex_id)
        
        return self.vertices[vertex_id]

    def get_edge(self, edge_id):

        if edge_id not in self.edges:
            raise NotFoundError(edge_id)
        
        return self.edges[edge_id]





    def neighbors(self, vertex_id):
        """devuelve tuplas (id_vecino, edge) y salta las aristas con enabled = False 
        osea q no cuenta los puentes destruidos y asi"""

        vertex = self.get_vertex(vertex_id)
        result = []

        for edge in vertex.connections:
            if edge.enabled:
                result.append((edge.other_end(vertex_id), edge))

        return result

#enable y disable solo cambian el booleano La arista nunca sale de la lista por que dice que los puentes destruidos guardan la info
    def enable_edge(self, edge_id):
        self.get_edge(edge_id).enabled = True

    def disable_edge(self, edge_id):
        self.get_edge(edge_id).enabled = False

    #La idea es usar solo una clase grafo que va a tener todos los atributos comunes de los dos grafos y que las clases de cada grafo hereden de esta
