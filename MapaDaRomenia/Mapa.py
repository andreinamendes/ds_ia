class Mapa:
  def __init__(self):
    self.__mapa = {
      'Arad': {
        'Zernd': 75,
        'Sibiu': 140,
        'Timisoara': 118
      },
      'Zerind': {
        'Arad': 75,
        'Oradea': 71
      },
      'Oradea': {
        'Zerind': 71,
        'Sibiu': 151
      },
      'Timbisoara': {
        'Arad': 118,
        'Lugoj': 111
      },
      'Sibiu': {
        'Fagaras': 99,
        'RimnicuVilcea': 80
      },
      'Lugoj': {
        'Mehadia': 70,
        'Timisoara': 111
      },
      'Mehadia': {
        'Lugoj': 70,
        'Drobeta': 75
      },
      'Drobeta': {
        'Mehadia': 75,
        'Craiova': 120
      },
      'Craioba': {
        'RimnicuVilcea': 146,
        'Pitesti': 138
      },
      'RimnicuVilcea': {
        'Sibiu': 80,
        'Pitesti': 97,
        'Craiova': 146
      },
      'Fagaras': {
        'Sibiu': 99,
        'Bucharest': 211
      },
      'Pitesti': {
        'RimnicuVilcea': 97,
        'Craiova': 138,
        'Bucharest': 101
      },
      'Bucharest': {
        'Pitesti': 101,
        'Fagaras': 211,
        'Giurgiu': 90,
        'Urziceni': 85
      },
      'Giurgiu': {
        'Bucharest': 90
      },
      'Urziceni': {
        'Bucharest': 85,
        'Hirsova': 98,
        'Vaslui': 142
      },
      'Hirsova': {
        'Urziceni': 98,
        'Eforie': 86
      },
      'Eforie': {
        'Hirsova': 86
      },
      'Vaslui': {
        'Urziceni': 142,
        'Iasi': 92
      },
      'Iasi': {
        'Vaslui': 92,
        'Neamt': 87
      },
      'Neamt': {
        'Iasi': 87
      }
    }
    
  def getMapa(self):
    return self.__mapa.items()
  
  def printMapa(self):
    for x, y in self.__mapa.items():
      print('-------------------------------')
      print('Cidade: ' + x + '\nVizinhos:')
      
      for w, z in y.items():
        print('\tCidade: ' + w + '\n\tDistância: ' + str(z))