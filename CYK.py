from itertools import repeat,permutations

# Convertendo o arquivo .txt em map
print("Gramática:")
with open('gramatica.txt', 'r') as f:
    map_gramatica = {}
    for line in f:
        antes, depois = line.split(' => ')
        regra = antes[0]
        gramatica = depois.replace(' ', '').replace('\n', '').split('|')
        map_gramatica[antes] = gramatica
        print(antes,"=>",depois)

# Criando tabela nxn onde n é o número de letras da palavra
def criarTabela(palavra):
  tabela=[]
  tamanho_palavra=len(palavra)
  for i in range(tamanho_palavra):
    tabela.append([None]*(tamanho_palavra))
  return tabela

# Exibindo a tabela no formato que utilizaremos para a exibição dos resultados
def exibirTabela(tabela):
  for r in tabela:
    for e in r:
      print(e,end=" | ")
    print()

# Inserindo elemento em tabela
def inserirElementoTabela(estado):
  aux=set()
  for e in map_gramatica.keys():
    if estado in map_gramatica[e]:
      aux.add(e)
  if(len(aux)):
    return aux
  else:
    return None

# Preenche a tabela na diagonal
def preencherDiagonalTabela(tabela,palavra):
  i=j=0
  for letra in palavra:
    tabela[i][j]=inserirElementoTabela(letra)
    i+=1
    j+=1
  return tabela

# Preenchendo o restante da tabela CYK
def tabelaCyk(tabela,prarlavra):
  passo=1
  for i in range(len(palavra)-1):
    for j in range(len(palavra)-passo):
      concluido=False
      k=j+passo
      count=0
      while(k-count>j):
        a=tabela[j][k-count-1]
        b=tabela[k-count][k]
        if(len(a)<len(b)):
          l=[(list(zip(r, p))) for (r, p) in zip(repeat(a), permutations(b))]    
        else:
          l=[(list(zip(p, r))) for (r, p) in zip(repeat(b), permutations(a))]
        aux=[]
        for e in l:
          for i in e:
            aux.append(("").join(i))
        for z in aux:
          s=inserirElementoTabela(z)
          if(s==None):
            if(not concluido):
              tabela[j][k]=set("ø")
          else:
              x=tabela[j][k]
              if(x==None or x==set("ø")):
                tabela[j][k]=s
              else:
                tabela[j][k]=tabela[j][k]|s
              concluido=True
        count+=1
    passo+=1  
  return tabela  

print("--------------------------")
palavra=input("Digite a palavra: ")
tabela_cyk=criarTabela(palavra)
preencherDiagonalTabela(tabela_cyk,palavra)
tabela_cyk=tabelaCyk(tabela_cyk,palavra)
print("--------------------------")
print("Tabela CYK:")
exibirTabela(tabela_cyk)