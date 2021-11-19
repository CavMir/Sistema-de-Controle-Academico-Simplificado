#Função para registro dos alunos
def alunos(Acesso):
        alunos = {}
    #Adicionar
        if Acesso == 'adicionar':
            arquivo = open('alunos','a')
            while True:
                nome = input('\nPara adicionar um novo aluno, por favor insira o nome do(a) aluno(a): ').title()
                cpf = input('\nInsira o CPF do(a) aluno(a) usando apenas números: ')
                while not cpf.isnumeric() or len(cpf) != 11:
                    cpf = input('\nCPF em formato inválido, por favor insira o CPF utilizando apenas números: ')
    #Reorganizando o CPF para formato padrão
                cpf = list(cpf)
                cpf.insert(9, '-')
                cpf.insert(6, '.')
                cpf.insert(3, '.')
                cpf = ''.join(cpf)
    #Encerrando a operação    
                alunos[cpf] = nome
                fim = input('\nO(a) aluno(a) %s foi adicionado com sucesso, para salvar volte ao menu inicial. Deseja Continuar ou Voltar?: '%alunos[cpf]).lower()
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
            for cpf in alunos:
                arquivo.write('{}:{}\n'.format(cpf,alunos[cpf]))
            arquivo.close()
    #Consultar
        elif Acesso == 'consultar':
            try:
                arquivo = open('alunos','r')
                for linha in arquivo.readlines():
                    cpf,nome = linha.split(':')
                    alunos[cpf] = nome
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhum aluno no registro.\n')
                return
            while True:
                consulta = input('\nVocê deseja procurar através de CPF ou Nome?: ').lower()
                while True:
        #Por nome
                    if consulta == 'nome':
                        consulta = input('\nInsira o nome do(a) aluno(a): ').title()
                        verif = True
                        for cpf in alunos:
                            if consulta == alunos[cpf][:-1]:
                                print('\n>>>{}: {}'.format(cpf,alunos[cpf][:-1]))
                                verif = False
                        if verif:
                            print('\Aluno(a) não encontrado(a).',end=(' '))
                        else: print('\nBusca concluída.',end=(' '))
                        break
        #Por CPF
                    elif consulta == 'cpf':
                        consulta = input(('\nInsira o CPF do(a) aluno(a) no formato 000.000.000-00: '))
                        try:
                            print('\n>>>{}: {}\nBusca concluída.'.format(consulta,alunos[consulta]),end=(' '))
                        except KeyError:
                            print('\nCPF não encontrado.',end=(' '))
                        break
                    else:
                        consulta = input('\nOpção inválida, por favor escolha uma das seguintes opções: CPF ou Nome: ').lower().split()
    #Encerrando a operação
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
    #Atualizar
        elif Acesso == 'atualizar':
            try:
                arquivo = open('alunos','r')
                for linha in arquivo.readlines():
                    cpf,nome = linha.split(':')
                    alunos[cpf] = nome
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhum aluno no registro.\n')
            while True:
                cpf = input('\nInsira o CPF do aluno que você deseja atualizar: ')
                try:
                    print('\n{}{}'.format(alunos[cpf],cpf))
                    alunos[cpf] = '{}\n'.format(input('\nAluno(a) encontrado(a). Insira um novo nome para o(a) aluno(a): ').title())
                    print('\nAlteração realizada com sucesso, para salvar volte ao menu inicial.',end=(' '))
                except KeyError:
                    print('\Aluno(a) não encontrado(a).',end=(' '))
    #Encerrando a operação:
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    arquivo = open('alunos','w')
                    break
            for cpf in alunos:
                arquivo.write('{}:{}'.format(cpf,alunos[cpf]))
            arquivo.close()
    #Deletar
        elif Acesso == 'deletar':
            try:
                arquivo = open('alunos','r')
                for linha in arquivo.readlines():
                    cpf,nome = linha.split(':')
                    alunos[cpf] = nome
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhum aluno no registro.\n')
            verif = False
            while True:
                delete = input('\nInsira o CPF do aluno que você deseja deletar, ou digite 0000 para deletar todo o registro de alunos: ')
                if delete == '0000':
                    delete = input('Tem certeza que deseja deletar todo o registro de alunos? Digite 0000 para continuar ou Cancela para voltar: ')
                    if delete == '0000':
                        from os import remove
                        remove('alunos')
                        print('\nO registro de alunos foi deletado com sucesso.\n')
                    break
                else:
                    try:
                        conf = input('\nTem certeza que deseja deletar o(a) aluno(a) {}, Sim ou Não?: '.format(alunos[delete][:-1]).lower())
                        while conf not in ['sim','não']:
                            conf = input('\nOpção inválida, por favor escolha uma das seguintes opções: Sim ou Não: ')
                        if conf == 'sim':
                            del alunos[delete]
                            print('\nO(A) aluno(a) for deletado(a) com sucesso, para salvar volte ao menu inicial.',end=(' '))
                            verif = True
                        else:
                            print('\nO(A) aluno(a) não foi deletado(a).',end=(' '))
                    except KeyError:
                        print('\Aluno(a) não encontrado(a).',end=(' '))
    #Encerrando a operação
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
            if verif:
                arquivo = open('alunos','w')
                for cpf in alunos:
                    arquivo.write('{}:{}'.format(cpf,alunos[cpf]))
                arquivo.close()
