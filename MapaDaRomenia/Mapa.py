import heapq as hq

class Mapa:
  def __init__(self):
    self.__mapa = {'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Fagaras': 99, 'RimnicuVilcea': 80, 'Oradea': 151, 'Arad': 140},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'RimnicuVilcea': 146, 'Pitesti': 138, 'Drobeta': 120},
    'RimnicuVilcea': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'RimnicuVilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Pitesti': 101, 'Fagaras': 211, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}}

  def busca_em_largura(self,origem, destino='Bucharest'):
    borda = []
    explorados = []
    no = {
      'estado':origem,
      'pai':'',
      'custo':0
    }
    borda.append(no)
    custo_total = 0
    arvore = {}
    arvore[no['estado']]=no
    
    while len(borda):
      no = borda.pop(0)
      explorados.append(no['estado'])
      arvore[no['estado']]=no

      cidade_atual = no['estado']
      
      for vizinho, custo in self.__mapa[cidade_atual].items():
        
        filho = {
          'estado':vizinho,
          'pai':cidade_atual,
          'custo':custo+no['custo']
        }
        
        if (not filho['estado'] in explorados) and (not filho['estado']  in [x['estado'] if x['estado']== filho['estado'] else '' for x in borda]):
          if filho['estado'] == destino:
            
            #return sol ([],int)
            solucao = [filho['estado']]
            pai = filho['pai']
            
            while pai != '':
              solucao.append(arvore[pai]['estado'])
              pai = arvore[pai]['pai']
            solucao.reverse()
            return (solucao, filho['custo'])

          borda.append(filho)
      
    else:
      return 'falha'

  def busca_custo_uniforme(self, origem='Arad', destino='Hirsova'):
    explorados = []
    no = {
      'estado':origem,
      'pai':'',
      'custo':0
    }
    # guarda a tupla (custo, no) na fila de prioridade
    borda = [(0, no)]
    hq.heapify(borda)
    

    while True:
      if len(borda)==0:
        return 'Falha'
      
      #recupera o no
      no = hq.heappop(borda)[1]

      if no['estado'] == destino:
        #print(borda)
        #percorre os pais e soma os custos
        solucao = [no['estado']]
        pai = no['pai']
        #procura o no na fila
        custo = no['custo']
        
        while True:
          if pai=='':
            break
          #print(no['estado'])
          solucao.append(no['pai'])
          #custo+=no['custo']
          def pega_pai(a):
            for k in borda:
              if k[1]['estado'] == pai:
                return k[1] #! == {estado:pipip, pai:pipipi, custo:0}
                
          no = pega_pai(borda)
          try:
            pai = no['pai']
          except:
            pai = ''
        solucao.reverse()
        return (solucao, custo)
        
      
      explorados.append(no['estado'])
      
      for vizinho, custo in self.__mapa[no['estado']].items():
        filho = {
          'estado':vizinho,
          'pai': no['estado'],
          'custo': custo+no['custo']
        }
        #print(filho)
        def estado_com_maior_custo(fila):
          for f in fila:
            if f[1]['estado']==filho['estado'] and f[0]>filho['custo']:
              return True
          return False
        
        borda_aux = [i[1]['estado'] for i in borda]
        
        if (not filho['estado'] in explorados) or (not filho['estado'] in borda_aux):
          hq.heappush(borda, (filho['custo'], filho))
        
        #adiciona à fila o nome da cidade que está sendo procurada se o seu custo for maior que o custo atual
        #elif filho['estado'] in [i[1]['estado'] if i[1]['custo']>filho['custo'] else '' for i in borda]:
        elif estado_com_maior_custo(borda):
          #remove da fila a cidade igual a filho['estado']
          def f(borda_):
            res = []
            for i in borda_:
              #print(borda_)
              if i[1]['estado']!=filho['estado']:
                res.append((i[1]['custo'], i[1]))
            return res

          borda = f(borda)
          hq.heapify(borda)
          hq.heappush(borda,(filho['custo'], filho))

  def busca_profundidade(self, origem='Arad', destino='Bucharest'):
    #pilha = ultimo que entra, primeiro que sai
    explorados = {}
    no = {
      'estado':origem,
      'pai':'',
      'custo':0
    }
    borda = [no]
    solucao = []

    while True:
      if len(borda)==0:
        return 'Falha'
      
      no = borda.pop()
      solucao.append(no['estado'])
      explorados[no['estado']]=no
      
      for vizinho, custo in self.__mapa[no['estado']].items():
        filho = {
          'estado':vizinho,
          'pai': no['estado'],
          'custo': custo+no['custo']
        }
        
        if (not filho['estado'] in explorados) and (not filho['estado'] in [x['estado'] for x in borda]):
          
          if filho['estado']==destino:
            return (solucao, filho['custo'])
          borda.append(filho)

  @property
  def mapa(self):
    return self.__mapa.items()
  
  @mapa.setter
  def mapa(self, mapa:'Mapa'):
    self.__mapa = mapa
  
  def print_mapa(self):
    for x, y in self.__mapa.items():
      print('-------------------------------')
      print('Cidade: ' + x + '\nVizinhos:')
      
      for w, z in y.items():
        print('\tCidade: ' + w + '\n\tDistância: ' + str(z))
    print('-------------------------------')