#*******************************************************************************
#Autor: Vivian Martins Moura
#Componente Curricular: MI-Algoritmos 
#Concluido em: 01/06/2025
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************
import pickle

#classe criada para a criação dos clientes
class Cliente:
    def __init__(self,nome,categoria,cashback):
        self.nome=nome
        self.categoria=categoria
        self.cashback=cashback
    def __str__(self):
        return f'Cliente: {self.nome}, Categoria: {self.categoria}, Cashback: R$ {self.cashback:.2f}'

#classe criada para a criação dos dicionários das bases e dos complementos    
class bebida:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco

#função que verifica se o nome já está cadastrado ou não
def ver_se_existe(nome):
    try:
        with open('registro.dat','rb') as arq:
            registro=pickle.load(arq)
    except (EOFError, FileNotFoundError):
        print('Não há cliente cadastrado ainda')
        return False
    if nome in registro:
        return True
    else:
        print('Usuário não cadastrado')
        return False


        