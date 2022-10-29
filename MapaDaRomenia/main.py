from Mapa import Mapa
import pprint
import time

if __name__ == '__main__':
  mapa = Mapa()
  #mapa.printMapa()
  entradas = ['Neamt','Eforie','Lugoj','Arad','Vaslui','Oradea','Iasi','Timisoara']
 
  # print("Busca de custo uniforme")
  # print('-'*10)
  # for i in entradas:
  #   print(i)
  #   start = time.time()
  #   solucao = mapa.busca_custo_uniforme(origem=i)
  #   end = time.time()
  #   print('Solucao: ')
  #   print(solucao)
  #   print('Tempo: '+str(end-start))
  #   print('-'*10)

  # mapa.busca_custo_uniforme(origem='Neamt')
  # mapa.busca_custo_uniforme(origem='Eforie')
  # mapa.busca_custo_uniforme(origem='Lugoj')
  # mapa.busca_custo_uniforme(origem='Arad')
  # mapa.busca_custo_uniforme(origem='Vaslui')
  # mapa.busca_custo_uniforme(origem='Oradea')
  # mapa.busca_custo_uniforme(origem='Iasi')
  mapa.busca_custo_uniforme(origem='Timisoara')


  # print(mapa.busca_custo_uniforme(origem='Arad'))