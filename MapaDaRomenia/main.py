from Mapa import Mapa
import pprint

if __name__ == '__main__':
  mapa = Mapa()
  #mapa.printMapa()
  solucao = mapa.busca_em_largura('Arad')
  print(solucao)