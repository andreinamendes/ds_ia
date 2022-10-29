from Mapa import Mapa
import pprint
import time

if __name__ == '__main__':
  mapa = Mapa()
  #mapa.printMapa()
  entradas = ['Neamt','Eforie','Lugoj','Arad','Vaslui','Oradea','Iasi','Timisoara']
 
  
  # print("Busca gulosa")
  # print('-'*10)
  # for i in entradas:
  #   print(i)
  #   start = time.time()
  #   solucao = mapa.busca_a_estrela(origem=i)
  #   end = time.time()
  #   print('Solucao: ')
  #   print(solucao)
  #   print('Tempo: '+str(end-start))
  #   print('-'*10)

  # mapa.busca_a_estrela(origem='Neamt')
  # mapa.busca_a_estrela(origem='Eforie')
  # mapa.busca_a_estrela(origem='Lugoj')
  # mapa.busca_a_estrela(origem='Arad')
  # mapa.busca_a_estrela(origem='Vaslui')
  # mapa.busca_a_estrela(origem='Oradea')
  # mapa.busca_a_estrela(origem='Iasi')
  solucao = mapa.busca_a_estrela(origem='Timisoara')

  # mapa.busca_profundidade(origem='Neamt')
  # mapa.busca_profundidade(origem='Eforie')
  # mapa.busca_profundidade(origem='Lugoj')
  # mapa.busca_profundidade(origem='Arad')
  # mapa.busca_profundidade(origem='Vaslui')
  # mapa.busca_profundidade(origem='Oradea')
  # mapa.busca_profundidade(origem='Iasi')
  # mapa.busca_profundidade(origem='Timisoara')

  # mapa.busca_profundidade(origem='Neamt')
  # mapa.busca_profundidade(origem='Eforie')
  # mapa.busca_profundidade(origem='Lugoj')
  # mapa.busca_profundidade(origem='Arad')
  # mapa.busca_profundidade(origem='Vaslui')
  # mapa.busca_profundidade(origem='Oradea')
  # mapa.busca_profundidade(origem='Iasi')
  # mapa.busca_profundidade(origem='Timisoara')

  # mapa.busca_gulosa(origem='Neamt')
  # mapa.busca_gulosa(origem='Eforie')
  # mapa.busca_gulosa(origem='Lugoj')
  # mapa.busca_gulosa(origem='Arad')
  # mapa.busca_gulosa(origem='Vaslui')
  # mapa.busca_gulosa(origem='Oradea')
  # mapa.busca_gulosa(origem='Iasi')
  # mapa.busca_gulosa(origem='Timisoara')


  # mapa.busca_custo_uniforme(origem='Neamt')
  # mapa.busca_custo_uniforme(origem='Eforie')
  # mapa.busca_custo_uniforme(origem='Lugoj')
  # mapa.busca_custo_uniforme(origem='Arad')
  # mapa.busca_custo_uniforme(origem='Vaslui')
  # mapa.busca_custo_uniforme(origem='Oradea')
  # mapa.busca_custo_uniforme(origem='Iasi')
  # mapa.busca_custo_uniforme(origem='Timisoara')
