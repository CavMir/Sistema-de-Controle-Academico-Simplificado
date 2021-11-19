#Função para registro dos professores
def professores(Acesso):
            professores = {}
    #Adicionar
            if Acesso == 'adicionar':
                arquivo = open('professores','a')
                while True:
                    dados = [input('\nPara adicionar um novo professor, por favor insira o nome do(a) professor(a): ').title(), input('\nInsira o departamento do(a) professor(a): ').title()]
                    cpf = input('\nInsira o CPF do(a) professor(a) usando apenas números: ')
                    while not cpf.isnumeric() or len(cpf) != 11:
                        cpf = input('\nCPF em formato inválido, por favor insira o CPF utilizando apenas números: ')
    #Reorganizando o CPF para formato padrão
                    cpf = list(cpf)
                    cpf.insert(9, '-')
                    cpf.insert(6, '.')
                    cpf.insert(3, '.')
                    cpf = ''.join(cpf)
    #Encerrando a operação 
                    professores[cpf] = dados
                    fim = input('\nProfessor(a) %s adicionado com sucesso, para salvar volte ao menu inicial. Deseja Continuar ou Voltar?: '%professores[cpf][0]).lower()
                    while fim not in ['continuar','voltar']:
                        fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                    if fim == 'voltar':
                        print('')
                        break
                for cpf in professores:
                    arquivo.write('{}:{}:{}\n'.format(cpf,professores[cpf][0],professores[cpf][1]))
                arquivo.close()
    #Consultar
            elif Acesso == 'consultar':
                try:
                    arquivo = open('professores','r')
                    for linha in arquivo.readlines():
                        cpf,nome,dpt = linha.split(':')
                        professores[cpf] = [nome,dpt]
                    arquivo.close()
                except FileNotFoundError:
                    print('\nNão há nenhum professor no registro.\n')
                    return
                while True:
                    consulta = input('\nVocê deseja procurar através de CPF, Nome ou Departamento?: ').lower()
                    while True:
        #Por CPF
                        if consulta == 'cpf':
                            consulta = input('\nInsira o CPF do(a) professor(a) no formato 000.000.000-00: ')
                            try:
                                print('\n>>>{}: Prof. {}, Dpt. de {}\nBusca concluída.'.format(consulta,professores[consulta][0],professores[consulta][1]),end=(' '))
                            except KeyError:
                                print('\nCPF não encontrado.',end=(' '))
                            break
        #Por Nome
                        elif consulta == 'nome':
                            consulta = input('\nInsira o nome do(a) professor(a): ').title()
                            verif = True
                            for cpf in professores:
                                if consulta == professores[cpf][0]:
                                    print('\n>>>{}: Prof. {}, Dpt. de {}'.format(cpf,professores[cpf][0],professores[cpf][1][:-1]))
                                    verif = False
                            if verif:
                                print('\nProfessor não encontrado.',end=(' '))
                            else: print('\nBusca concluída.',end=(' '))
                            break
        #Por Departamento
                        elif consulta == 'departamento':
                            consulta = input('\nInsira o departamento do(a) professor(a): ').title()
                            verif = True
                            for cpf in professores:
                                if consulta == professores[cpf][1][:-1]:
                                    print('\n>>>{}: Prof. {}, Dpt. de {}'.format(cpf,professores[cpf][0],professores[cpf][1][:-1]))
                                    verif = False
                            if verif:
                                print('\nNão há professores neste departamento.',end=(' '))
                            else: print('\nBusca concluída.',end=(' '))
                            break
                        else:
                            consulta = input('\nOpção inválida, por favor escolha uma das seguintes opções: CPF, Nome ou Departamento: ').lower()
    #Encerrando a operação
                    fim = input('Deseja Continuar ou Voltar?: ')
                    while fim not in ['continuar','voltar']:
                       fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                    if fim == 'voltar':
                        print('')
                        break
    #Atuallizar
            elif Acesso == 'atualizar':
                try:
                    arquivo = open('professores','r')
                    for linha in arquivo.readlines():
                        cpf,nome,dpt = linha.split(':')
                        professores[cpf] = [nome,dpt]
                    arquivo.close()
                except FileNotFoundError:
                    print('\nNão há nenhum professor no registro.\n')
                    return
                while True:
                    cpf = input('\nInsira o CPF do(a) professor(a) que você deseja atualizar no formato 000.000.000-00: ')
                    try:
                        print('''
Professor(a): {}
Departamento: {}{}'''.format(professores[cpf][0], professores[cpf][1],cpf))
                        alt = input('\nProfessor(a) encontrado(a). Deseja alterar Nome ou Departamento?: ').lower()
                        while alt not in ['nome','departamento']:
                            alt = input('\nOpção inválida, por favor escolha uma das seguintes opções: Nome ou Departamento: ').lower()
                        if alt == 'nome':
                            professores[cpf][0] = input('\nInsira um novo nome para o(a) professor(a): ').title()
                        elif alt == 'departamento':
                            professores[cpf][1] = '{}\n'.format(input('\nInsira um novo departamento para o(a) professor(a): ').title())
                        print('\nAlteração realizada com sucesso, para salvar volte ao menu inicial.',end=(' '))
                    except KeyError:
                        print('\nCPF não encontrado.',end=(' '))
    #Encerrando a operação
                    fim = input('Deseja Continuar ou Voltar?: ')
                    while fim not in ['continuar','voltar']:
                       fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                    if fim == 'voltar':
                        print('')
                        arquivo = open('professores','w')
                        break
                for cpf in professores:
                    arquivo.write('{}:{}:{}'.format(cpf,professores[cpf][0],professores[cpf][1]))
                arquivo.close()
    #Deletar
            elif Acesso == 'deletar':
                try:
                    arquivo = open('professores','r')
                    for linha in arquivo.readlines():
                        cpf,nome,dpt = linha.split(':')
                        professores[cpf] = [nome,dpt]
                    arquivo.close()
                except FileNotFoundError:
                    print('\nNão há nenhum professor no registro.\n')
                    return
                verif = False
                while True:
                    delete = input('\nInsira o CPF do(a) professor que você deseja deletar no formato 000.000.000-00, ou digite 0000 para deletar todo o registro de professores: ')
                    if delete == '0000':
                        delete = input('Tem certeza que deseja deletar todo o registro de professores? Digite 0000 para continuar ou Cancela para voltar: ')
                        if delete == '0000':
                            from os import remove
                            remove('professores')
                            print('\nO registro de professores foi deletado com sucesso.\n')
                        break
                    else:
                        try:
                            conf = input('\nTem certeza que deseja deletar o(a) Professor(a) {} do Departamento de {}, Sim ou Não?: '.format(professores[delete][0],professores[delete][1][:-1])).lower()
                            while conf not in ['sim','não']:
                                conf = input('\nOpção inválida, por favor escolha uma das seguintes opções: Sim ou Não: ').lower()
                            if conf == 'sim':
                                del professores[delete]
                                print('\nO(A) professor(a) for deletado com sucesso, para salvar volte ao menu inicial.',end=(' '))
                                verif = True
                            else:
                                print('\nO(A) professor(a) não foi deletado(a).',end=(' '))
                        except KeyError:
                            print('\nCPF não encontrado.',end=(' '))
    #Encerrando a operação
                    fim = input('Deseja Continuar ou Voltar?: ')
                    while fim not in ['continuar','voltar']:
                        fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                    if fim == 'voltar':
                        print('')
                        break
                if verif:
                    arquivo = open('professores','w')
                    for cpf in professores:
                        arquivo.write('{}:{}:{}'.format(cpf,professores[cpf][0],professores[cpf][1]))
                    arquivo.close()
