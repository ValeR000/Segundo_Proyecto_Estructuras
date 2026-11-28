# Grafo del laberinto (GM): corredores por donde avanza el convoy

import math

from backend.errors import InvalidDataError, InvalidOperationError, NotFoundError
from backend.graphs.graph import Graph

VERTEX_TYPES = ("entrance", "exit", None)


def _is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


class MazeGraph(Graph):  # Graph con las reglas de GM: una entrada, una salida y corredores válidos.
    def __init__(self):
        super().__init__()
        self.entrance_id = None
        self.exit_id = None

    def add_vertex(self, vertex):

        if not (_is_number(vertex.x) and _is_number(vertex.y)): # q el vertice sea valido
            raise InvalidDataError(vertex.id)
        
        if vertex.vertex_type not in VERTEX_TYPES:
            raise InvalidDataError(vertex.id)
        
        if vertex.vertex_type == "entrance" and self.entrance_id is not None: #solo puede habe 1 entrada 1 salida y 1 base
            raise InvalidOperationError(vertex.id)

        if vertex.vertex_type == "exit" and self.exit_id is not None:
            raise InvalidOperationError(vertex.id)
        
        super().add_vertex(vertex)


        if vertex.vertex_type == "entrance":
            self.entrance_id = vertex.id

        elif vertex.vertex_type == "exit":
            self.exit_id = vertex.id

    def add_edge(self, edge):

        for value in (edge.length, edge.speed):

            if not _is_number(value) or value <= 0:
                raise InvalidDataError(edge.id)
            
        super().add_edge(edge)

    def get_entrance(self):

        if self.entrance_id is None:
            raise NotFoundError("entrance")
        
        return self.vertices[self.entrance_id]

    def get_exit(self):

        if self.exit_id is None:
            raise NotFoundError("exit")
        
        return self.vertices[self.exit_id]
