# Arista no dirigida usada tanto en GE como en GM


class Edge:  # Une dos vertices: guarda tiempos (GE), puente (GE) o largo y velocidad (GM)
    def __init__(self, id, a, b, walk_time=None, moto_time=None, is_bridge=False,
                 max_resistance=None, length=None, speed=None):
        
        self.id = id
        self.a = a #a y b son los ids de los extremos
        self.b = b
        self.enabled = True #osea que la arista esta activa o el puente no esta destruido ps
        #ambos grafos comparten esos 4 atributos

        #ATRIBUTOS GRAFO GE
        self.walk_time = walk_time
        self.moto_time = moto_time
        self.is_bridge = is_bridge
        self.max_resistance = max_resistance #esto es pa calcular si el puente esta bien o q
        self.current_resistance = max_resistance

        #ATRIBUTOS GRAFO GM
        self.length = length
        self.speed = speed

    def travel_time(self): 
        """es el tiempo que tarda el convoy en recorrer un corredor: t= longitud / velocidad
            Solo lo tiene GM. En GE los tiempos ya estan en walk_time y moto_timey asi"""
        return self.length / self.speed

    def other_end(self, vertex_id):
        """si le das un extremo, te devuelve el otro. 
        Hace falta porque la arista no tiene dirección: 
        desde A el vecino es B, y desde B es A."""
        if vertex_id == self.a:
            return self.b
        return self.a

    #La idea es usar solo una clase arista que va a tener todos los atributos de los dos grafos y que cuando se elija uno
    #solo van a quedar en algun valor o !=None los atributos que corresponden a ese grafo y el resto en none
