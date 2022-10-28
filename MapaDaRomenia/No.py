class Tree:

    def __init__(self,estado,pai='',custo=0) -> None:
        self.estado=estado
        self.pai=pai
        self.custo=custo
        self.vizinhos = []