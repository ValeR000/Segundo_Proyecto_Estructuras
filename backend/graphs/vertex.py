# Vertice de cada grafo usado tanto en GE como en GM.


class Vertex:  # Un punto del mapa con su posicion su tipo y sus aristas
    def __init__(self, id, x, y, vertex_type=None):
        self.id = id #id que lo identifica
        self.x = x #posicion en x
        self.y = y #posicion en y
        self.vertex_type = vertex_type #tipo de vertice: (base, candidato, transito, helipuerto, entrada o salida) los q habian en el proyecto ps
        self.connections = [] #lista de conexiones del vertice
