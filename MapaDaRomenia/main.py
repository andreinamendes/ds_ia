from Mapa import Mapa
import pprint
import time

if __name__ == '__main__':
  mapa = Mapa()
  #mapa.printMapa()
  entradas = ['Neamt','Eforie','Lugoj','Arad','Vaslui','Oradea','Iasi','Timisoara']
 
  print("Busca em profundidade")
  print('-'*10)
  for i in entradas:
    print(i)
    start = time.time()
    solucao = mapa.busca_profundidade(origem=i)
    end = time.time()
    print('Solucao: ')
    print(solucao)
    print('Tempo: '+str(end-start))
    print('-'*10)