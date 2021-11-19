#Função para registro das disciplinas
def disciplinas(Acesso):
        disciplinas = {}
    #Adicionar
        if Acesso == 'adicionar':
            arquivo = open('disciplinas','a')
            while True:
                nome = input('\nPara adicionar uma nova disciplina, por favor insira o nome da disciplina: ').title()
                cod = input('\nInsira o código da disciplina: ')
                disciplinas[cod] = nome
    #Encerrando a operação
                fim = input('\nDisciplina %s adicionada com sucesso, para salvar volte ao menu inicial. Deseja Continuar ou Voltar?: '%disciplinas[cod]).lower()
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
            for cod in disciplinas:
                arquivo.write('{}:{}\n'.format(cod,disciplinas[cod]))
            arquivo.close()
    #Consultar
        elif Acesso == 'consultar':
            try:
                arquivo = open('disciplinas','r')
                for linha in arquivo.readlines():
                    cod,nome = linha.split(':')
                    disciplinas[cod] = nome
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhuma disciplina no registro.\n')
                return
            while True:
                consulta = input('\nVocê deseja procurar através de Nome ou Código da disciplina?: ').lower().split()
                while True:
        #Por nome
                    if consulta == ['nome']:
                        consulta = input('\nInsira o nome da disciplina: ').title()
                        verif = True
                        for cod in disciplinas:
                            if consulta == disciplinas[cod][:-1]:
                                print('\n>>>{}: Disciplina de {}'.format(cod,disciplinas[cod][:-1]))
                                verif = False
                        if verif:
                            print('\nDisciplina não encontrada.',end=(' '))
                        else: print('\nBusca concluída.',end=(' '))
                        break
        #Por Código da Disciplina
                    elif consulta[0] == 'código':
                        consulta = input('\nInsira o código da disciplina: ').title()
                        try:
                            print('\n>>>{}: Disciplina de {}\nBusca concluída.'.format(consulta,disciplinas[consulta]),end=(' '))
                        except KeyError:
                            print('\nDisciplina não encontrada.',end=(' '))
                        break
                    else:
                        consulta = input('\nOpção inválida, por favor escolha uma das seguintes opções: Nome ou Código: ').lower().split()
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
                arquivo = open('disciplinas','r')
                for linha in arquivo.readlines():
                    cod,nome = linha.split(':')
                    disciplinas[cod] = nome
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhuma disciplina no registro.\n')
                return
            while True:
                cod = input('\nInsira o Código da Disciplina que você deseja atualizar: ')
                try:
                    print('\nDisciplina: {}{}'.format(disciplinas[cod],cod))
                    disciplinas[cod] = '{}\n'.format(input('\nDisciplina encontrada. Insira um novo nome para a disciplina: ').title())
                    print('\nAlteração realizada com sucesso, para salvar volte ao menu inicial.',end=(' '))
                except KeyError:
                    print('\nDisciplina não encontrada.',end=(' '))
    #Encerrando a operação:
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    arquivo = open('disciplinas','w')
                    break
            for cod in disciplinas:
                arquivo.write('{}:{}'.format(cod,disciplinas[cod]))
            arquivo.close()
    #Deletar
        elif Acesso == 'deletar':
            try:
                arquivo = open('disciplinas','r')
                for linha in arquivo.readlines():
                    cod,nome = linha.split(':')
                    disciplinas[cod] = nome
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhuma disciplina no registro.\n')
                return
            verif = False
            while True:
                delete = input('\nInsira o Código da disciplina que você deseja deletar, ou digite 0000 para deletar todo o registro de disciplinas: ')
                if delete == '0000':
                    delete = input('Tem certeza que deseja deletar todo o registro de disciplinas? Digite 0000 para continuar ou Cancela para voltar: ')
                    if delete == '0000':
                        from os import remove
                        remove('disciplinas')
                        print('\nO registro de disciplinas foi deletado com sucesso.\n')
                    break
                else:
                    try:
                        conf = input('\nTem certeza que deseja deletar a Disciplina de {}, Sim ou Não?: '.format(disciplinas[delete][:-1]).lower())
                        while conf not in ['sim','não']:
                            conf = input('\nOpção inválida, por favor escolha uma das seguintes opções: Sim ou Não: ')
                        if conf == 'sim':
                            del disciplinas[delete]
                            print('\nA disciplina for deletado com sucesso, para salvar volte ao menu inicial.',end=(' '))
                            verif = True
                        else:
                            print('\nA disciplina não foi deletada.',end=(' '))
                    except KeyError:
                        print('\nDisciplina não encontrada.',end=(' '))
    #Encerrando a operação
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
            if verif:
                arquivo = open('disciplinas','w')
                for cod in disciplinas:
                    arquivo.write('{}:{}'.format(cod,disciplinas[cod]))
                arquivo.close()
