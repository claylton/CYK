from itertools import repeat,permutations

# Convertendo o arquivo .txt em map
with open('gramatica.txt', 'r') as f:
    map_gramatica = {}
    for line in f:
        antes, depois = line.split(' => ')
        regra = antes[0]
        gramatica = depois.replace(' ', '').replace('\n', '').split('|')
        map_gramatica[antes] = gramatica
        print(antes,"=>",depois)

    print(map_gramatica)

# Criando tabela nxn onde n é o número de letras da palavra
def criarTabela(palavra):
  tabela=[]
  tamanho_palavra=len(palavra)
  for i in range(tamanho_palavra):
    tabela.append([None]*(tamanho_palavra))
  return tabela
print('1)------------------------------------')
print(criarTabela('aba'))

# Exibindo a tabela no formato que utilizaremos para a exibição dos resultados
def exibirTabela(tabela):
  for r in tabela:
    for e in r:
      print(e,end=" | ")
    print()
print('2)------------------------------------')
print(exibirTabela(criarTabela('aba')))

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
  for estado in palavra:
    tabela[i][j]=inserirElementoTabela(estado)
    i+=1
    j+=1
  return tabela
print('2)------------------------------------')
print(preencherDiagonalTabela(criarTabela('aba'),'aba'))

# Preenchendo o restante da tabela CYK
def tabelaCyk(tabela,prarlavra):
  passo=1
  for i in range(len(palavra)-1):
    for j in range(len(palavra)-passo):
      concluido=False
      #k = auxiliares
      k=j+passo
      count=0
      #Enquanto não preencher a diagonal
      while(k-count>j):
        #Diagonal anterior
        a=tabela[j][k-count-1]
        b=tabela[k-count][k]
        print("tamanho a: " + str(len(a)))
        print("valor a: " + str(a))
        print("tamanho b: " + str(len(b)))
        print("valor b: " + str(b))
        print("passo: " + str(passo)+" i: " + str(i)+ " j: "+ str(j))
        if(len(a)<len(b)):
          l=[(list(zip(r, p))) for (r, p) in zip(repeat(a), permutations(b))]
          print("if: " + str(l))          
        else:
          l=[(list(zip(p, r))) for (r, p) in zip(repeat(b), permutations(a))]
          print("else: " + str(l))
        aux=[]
        for e in l:
          for i in e:
            # JUNTA AS TUPLAS EM UM ARRAY
            aux.append(("").join(i))
            print("ççççççççç"+ str(aux))
        for z in aux:
          s=inserirElementoTabela(z)
          #se a chave retornar null
          if(s==None):
            print("S == Noneeeeeeeeeeeeeeee: "+ str(s))
            #Se não tem nenhum elemento na tabela
            if(not concluido):
              tabela[j][k]=set("ø")
          else:
              x=tabela[j][k]
              #Adiciona primeiro elemento no array
              if(x==None or x==set("ø")):
                tabela[j][k]=s
                #Adiciona segundo elemento no array
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
print()
print()
exibirTabela(tabela_cyk)