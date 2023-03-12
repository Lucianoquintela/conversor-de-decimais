continuar = 'S'
while continuar == 'S':
        
        conversorDeNumerosDecimais = int(input('\nDigite um número decimal:'))

        print(''' Escolha sua opção de conversão:
        [1] Decimal para Binario
        [2] Decimal para Octal
        [3] Decimal para Hexadecimal
        
        [4] Para saber o que significa Binário, Octal e Hexadecimal
        ''')

        opcao = int(input('Digite sua escolha:'))

        if opcao == 4:
                print('''O que você deseja saber?
                [1] O que número Binario?
                [2] O que número Octal?
                [3] O que número Hexadecimal?
                ''')

                pergunta = int(input('Digite sua escolha: '))
                if pergunta == 1:
                        print('''
                        "O sistema binário ou de base 2 é um sistema de numeração posicional em 
                         que todas as quantidades se representam com base em dois números, ou 
                         seja, zero e um. os computadores digitais trabalham internamente com
                         dois níveis de tensão, pelo que o seu sistema de numeração natural é o
                         sistema binário."
                         ''')  
                                               

                elif pergunta == 2:
                        print('''
                        "Sistema octal é um sistema de numeração cuja base é 8, ou seja, utiliza
                        8 símbolos para a representação de quantidade. no ocidente, estes símbo-
                        los são os algarismos arábicos. o octal foi muito utilizado em informá-
                        tica como uma alternativa mais compacta ao binário na programação em                                               linguagem de máquina.    
                        ''')

                elif pergunta == 3:
                        print(''' 
                        "Hexadecimal é sistema numérico de base 16, denotado utilizando os                                                  símbolos 0-9 e A-F(ou a-f). por exemplo, o número decimal 79(cuja                                                  representação binária é 01001111) pode ser escrito como 4f em                                                      hexadecimal(4= 0100,f= 1111) cada dígito hexadecimal consegue                                                      representar 4 bits."
                         ''')

        elif opcao == 1:
                conversor_binario = conversorDeNumerosDecimais
                conversao = bin(conversor_binario)
                print(f'A conversão do seu número decimal {conversorDeNumerosDecimais} para                                        binário é: {conversao [2:]}')

        elif opcao == 2:
                conversor_octal = conversorDeNumerosDecimais
                conversao = oct(conversor_octal)
                print(f'A conversão do seu número decimal {conversorDeNumerosDecimais} para                                        octal é: {conversao [2:]}')

        elif opcao == 3:
                conversor_hexadecimal = conversorDeNumerosDecimais
                conversao = hex(conversor_hexadecimal)
                print(f'A conversão do seu número decimal {conversorDeNumerosDecimais} para                                        hexadecimal é: {conversao.upper() [2:]}')
        else:
                print(f'Você digitou algo errado')

        continuar = str(input('\nDeseja continuar? Digite a letra [s]: ')).upper()
                                 
#                                         ConversionDec
#                                           FuturyTec   