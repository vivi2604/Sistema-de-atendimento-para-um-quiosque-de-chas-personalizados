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
from secundário import *

#dicionário com as bases e com os complementos
bases={1:bebida('Leite', 4.35),2:bebida('Maracujá',4.60),3:bebida('Rosa',5.85),4:bebida('Manga',5.47)}
complementos={1:bebida('Boba',0.50),2:bebida('Lichia',0.75),3:bebida('Geleia',0.65),4:bebida('Taro',1.00),5:bebida('Chia',0.35)}

#carrega o registro de clientes já existentes
try:
    with open('registro.dat', 'rb') as arq:
        registro = pickle.load(arq)
except (EOFError, FileNotFoundError):
    registro = {}

#loop perguntando se o atendente deseja continuar atendendo ou não
encerrar=1
while encerrar !=2:
    while True:
        try:
            encerrar=int(input('Deseja atender um cliente ? Digite 1 pra sim e 2 pra não:'))
            if encerrar!=1 and encerrar!=2:
                print('Digite apenas 1 ou 2!')
            else:
                break
        except ValueError:
            print('Digite apenas números válidos')
    if encerrar==1:
        valor=0
        adicionais=[]
        nome=input('Nome do(a) cliente:').upper()

#Caso a pessoa já possua cadastro aparecerá na tela as informações dessa pessoa
        if ver_se_existe(nome)==True:
            with open('registro.dat', 'rb') as arq:
                registro = pickle.load(arq)
            cliente = registro[nome]
            print(f"Informações sobre {cliente.nome}: Sua categoria é {cliente.categoria} e seu cashback atual é R$ {cliente.cashback:.2f}")

#parte do código onde o cliente que ainda não está no sistema é cadastrado
        else:
            categoria = 0
            while categoria != 1 and categoria != 2:
                try:
                    categoria = int(input('Digite 1 para estudante e 2 para funcionário:'))
                    if categoria != 1 and categoria != 2:
                        print('Digite apenas 1 ou 2!')
                    else:
                        break
                except ValueError:
                    print('Digite apenas números válidos')
            cliente = Cliente(nome, categoria, 0.0)
            registro[cliente.nome] = cliente

#parte do código onde o cliente monta o seu pedido
        while True:
            try:
                print('1=Leite / 2=Maracujá / 3=Rosa / 4=Manga')
                base=int(input('Qual a base do chá? Digite apenas uma opção:'))
                if base<1 or base>4:
                    print('Digite apenas um dos números entre as opções')
                else:
                    valor+=bases[base].preco
                    break
            except ValueError:
                print('Digite apenas números válidos')
        while True:
            try:
                print('1=Boba / 2=Lichia / 3=Geleia / 4=Taro / 5=Chia')
                quantidade=int(input('Digite quantos complementos você irá querer, no máximo 5:'))
                if quantidade < 0 or quantidade > 5:
                    print('Digite apenas um número entre 0 e 5!')
                else:
                    break
            except ValueError:
                print('Digite apenas números válidos')
        for i in range(quantidade):
            while True:
                try:
                    print('1=Boba / 2=Lichia / 3=Geleia / 4=Taro / 5=Chia')
                    complemento = int(input(f'Digite qual complemento o cliente deseja:'))
                    if complemento < 1 or complemento > 5:
                        print('Digite apenas um dos números entre as opções!')
                    else:
                        valor+=complementos[complemento].preco
                        adicionais.append(complementos[complemento].nome)
                        break  
                except ValueError:
                    print('Digite apenas números válidos')

#parte do resumo do pedido
        print('RESUMO DO PEDIDO:')
        print(f'Cliente: {nome}')
        print(f'Base: {bases[base].nome}')
        print(f'Adicionais:{adicionais}')
        
        if cliente.categoria ==1:
            print('Cliente com desconto especial de estudante')
            valortotal=valor-0.25*valor
        elif cliente.categoria ==2:
            print('Cliente com desconto especial de professor')
            valortotal=valor-1

        if cliente.cashback > 0: 
            while True:
                try:
                    desc_extra = int(input(f'O cliente deseja utilizar o valor de R$ {cliente.cashback:.2f} do seu saldo de cashback? 1=sim / 2=não: '))
                    if desc_extra == 1 or desc_extra == 2:
                        break
                    else:
                        print('Digite apenas 1 ou 2!')
                except ValueError:
                    print('Entrada inválida, digite um número válido')
        else:
            desc_extra = 2

        if desc_extra==1:
            valortotal-=cliente.cashback
            print(f'Valor total: R$ {valortotal:.2f}')
            print('Cashback utilizado')
            saldocash=0.10*valortotal
            cliente.cashback=saldocash
            print(f'Saldo de cashback: R$ {saldocash:.2f}')

        elif desc_extra==2:
            print(f'Valor total: R$ {valortotal:.2f}')
            print('Cashback não utilizado')
            saldocash=0.10*valortotal
            cliente.cashback+=saldocash
            print(f'Saldo de cashback: R$ {cliente.cashback:.2f}') 
            
        # Atualiza o arquivo
        registro[cliente.nome] = cliente
        with open('registro.dat', 'wb') as arq:
            pickle.dump(registro, arq)