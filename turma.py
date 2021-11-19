#Função para registro das turmas
def turmas(Acesso):
        try:
            professores = {}
            arquivo = open('professores','r')
            for linha in arquivo.readlines():
                cpf,nome,dpt = linha.split(':')
                professores[cpf] = [nome,dpt]
            arquivo.close()
            disciplinas = {}
            arquivo = open('disciplinas','r')
            for linha in arquivo.readlines():
                cod,nome = linha.split(':')
                disciplinas[cod] = nome
            arquivo.close()
            alunos = {}
            arquivo = open('alunos','r')
            for linha in arquivo.readlines():
                cpf,nome = linha.split(':')
                alunos[cpf] = nome
            arquivo.close()
        except FileNotFoundError:
            print('\nPor favor, tenha certeza de adicionar professores, alunos e disciplinas antes de abrir o registro de turmas.\n')
            try:
                from os import remove
                remove('turmas')
                print('O registro de turmas existente estava corrompido e foi deletado.\n')
            except FileNotFoundError:
                return
            return
        turmas = {}
    #Adicionar
        if Acesso == 'adicionar':
            arquivo = open('turmas','a')
            while True:
                cod = input('\nPara adicionar uma nova turma, por favor insira o código da turma: ')
                período = input('\nInsira o período da turma no formato 20xx.x: ')
                while len(período) != 6:
                    período = input('\nFormato incorreto, por favor insira o período da turma no formato 20xx.x: ')
                disc = input('\nInsira o código da disciplina da turma: ')
                prof = []
                while True:
                    cpf = input('\nInsira o CPF do(a) professor(a) da turma usando apenas números: ')
                    while not cpf.isnumeric() or len(cpf) != 11:
                        cpf = input('\nCPF em formato inválido, por favor insira o CPF utilizando apenas números: ')
        #Reorganizando o CPF para formato padrão
                    cpf = list(cpf)
                    cpf.insert(9, '-')
                    cpf.insert(6, '.')
                    cpf.insert(3, '.')
                    cpf = ''.join(cpf)
                    prof.append(cpf)
                    prox = input('\nDeseja adicionar outro professor à turma?: ').lower()
                    while prox not in ['sim','não']:
                        prox = input('Respesta inválida, por favor responda com Sim ou Não: ').lower()
                    if prox == 'não': break
                aluno = []
                while True:
                    cpf = input('\nInsira o CPF do(a) %dº aluno(a) da turma usando apenas números: '%(len(aluno)+1))
                    while not cpf.isnumeric() or len(cpf) != 11:
                        cpf = input('\nCPF em formato inválido, por favor insira o CPF utilizando apenas números: ')
        #Reorganizando o CPF para formato padrão
                    cpf = list(cpf)
                    cpf.insert(9, '-')
                    cpf.insert(6, '.')
                    cpf.insert(3, '.')
                    cpf = ''.join(cpf)
                    aluno.append(cpf)
                    prox = input('\nDeseja adicionar outro aluno à turma?: ').lower()
                    while prox not in ['sim','não']:
                        prox = input('Respesta inválida, por favor responda com Sim ou Não: ').lower()
                    if prox == 'não': break
    #Encerrando a operação
                turmas[cod] = [período,disc,prof,aluno]
                try:
                    fim = input('\nTurma %s de %s adicionada com sucesso, para salvar volte ao menu inicial. Deseja Continuar ou Voltar?: '%(cod,disciplinas[disc][:-1])).lower()
                except KeyError:
                    print('\nDisciplina não encontrada.\n')
                    return
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
            for cod in turmas:
                arquivo.write('{}:{}:{}:{}:{}\n'.format(cod,turmas[cod][0],turmas[cod][1],turmas[cod][2],turmas[cod][3]))
            arquivo.close()
    #Consultar
        elif Acesso == 'consultar':
            try:
                arquivo = open('turmas','r')
                for linha in arquivo.readlines():
                    cod,período,disc,prof,aluno = linha.split(':')
                    prof = prof[2:-2]
                    prof = prof.split("', '")
                    aluno = aluno[2:-3]
                    aluno = aluno.split("', '")
                    turmas[cod] = [período,disc,prof,aluno]
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhuma turma no registro.\n')
                return
        #Inserindo nomes aos alunos e professores
            for cod in turmas:
                for c in range(len(turmas[cod][2])):
                    try:
                        turmas[cod][2][c] = '{}: {}'.format(turmas[cod][2][c],professores[turmas[cod][2][c]][0])
                    except KeyError:
                        turmas[cod][2][c] = '{}: CPF incorreto ou professor não encontrado'.format(turmas[cod][2][c])
                    turmas[cod][2][c] = turmas[cod][2][c].split(':')
                turmas[cod][2] = sorted(turmas[cod][2], key=lambda alfa: alfa[1])
                for c in range(len(turmas[cod][2])):
                    turmas[cod][2][c] = ':'.join(turmas[cod][2][c])
                for c in range(len(turmas[cod][3])):
                    try:
                        turmas[cod][3][c] = '{}: {}'.format(turmas[cod][3][c],alunos[turmas[cod][3][c]][:-1])
                    except KeyError:
                        turmas[cod][3][c] = '{}: CPF incorreto ou aluno não encontrado'.format(turmas[cod][3][c])
                    turmas[cod][3][c] = turmas[cod][3][c].split(':')
                turmas[cod][3] = sorted(turmas[cod][3], key=lambda alfa: alfa[1])
                for c in range(len(turmas[cod][3])):
                    turmas[cod][3][c] = ':'.join(turmas[cod][3][c])
                    
            while True:
                busca = input('\nComo você deseja buscar? Código da turma, Período, Disciplina, Professor(es) ou Aluno(s): ').lower()
                while busca not in ['código','período', 'disciplina', 'professor', 'aluno']:
                    busca = input('\nOpção inválida, por favor escolha uma das seguintes opções: Código, Período, Disciplina, Professor ou Aluno: ').lower()
        #Por código
                if busca == 'código':
                    cod = input('\nInsira o código da turma desejada: ')
                    try:
                        print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}

Busca concluída.'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])),end=(' '))
                    except KeyError:
                        print('Turma não encontrada',end=(' '))
        #Por período
                elif busca == 'período':
                    período = input('\nInsira o período da turma desejado no formato 20xx.x: ')
                    verif = True
                    for cod in turmas:
                        if período == turmas[cod][0]:
                            print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                            verif = False
                    if verif:
                        print('\nNão há turmas nesse período.',end=(' '))
                    else: print('\nBusca concluída.',end=(' '))
        #Por disciplina
                elif busca == 'disciplina':
                    disc = input('\nInsira o código da disciplina da turma desejada: ')
                    verif = True
                    for cod in turmas:
                        if disc == turmas[cod][1]:
                            print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                            verif = False
                    if verif:
                        print('\nNão há turmas com essa disciplina.',end=(' '))
                    else: print('\nBusca concluída.',end=(' '))
        #Por professor
                elif busca == 'professor':
                    prof = input('\nInsira o CPF do(a) professor(a) da turma desejado(a) no formato 000.000.000-00: ')
                    try:
                        prof = '{}: {}'.format(prof,professores[prof][0])
                        período = input('\nDigite o período da turma desejado ou digite 0000 para ver todas as turmas deste professor: ')
                    except KeyError:
                        print('\nProfessor não encontrado.',end=(' '))
                        período = False
                        pass
                    verif = True
                    if período == '0000':
                        for cod in turmas:
                            if prof in turmas[cod][2]:
                                print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                                verif = False
                        if verif:
                            print('\nEste(a) professor(a) não está lecionando em nenhuma turma.',end=(' '))
                        else: print('\nBusca concluída.',end=(' '))
                    elif período:
                        for cod in turmas:
                            if prof in turmas[cod][2]:
                                if período == turmas[cod][0]:
                                    print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                                    verif = False
                        if verif:
                            print('\nEste(a) professor(a) não está lecionando em nenhuma turma neste período.',end=(' '))
                        else: print('\nBusca concluída.',end=(' '))
                                    
        #Por aluno
                elif busca == 'aluno':
                    aluno = input('\nInsira o CPF do(a) aluno(a) da turma desejado(a) no formato 000.000.000-00: ')
                    try:
                        aluno = '{}: {}'.format(aluno,alunos[aluno][:-1])
                        período = input('\nDigite o período da turma desejado ou digite 0000 para ver todas as turmas deste aluno: ')
                    except KeyError:
                        print('\nAluno não encontrado.',end=(' '))
                        período = False
                        pass
                    verif = True
                    if período == '0000':
                        for cod in turmas:
                            if aluno in turmas[cod][3]:
                                print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                                verif = False
                        if verif:
                            print('\nEste(a) aluno(a) não está matriculado(a) em nenhuma turma.',end=(' '))
                        else: print('\nBusca concluída.',end=(' '))
                    elif período:
                        for cod in turmas:
                            if aluno in turmas[cod][3]:
                                if período == turmas[cod][0]:
                                    print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                                    verif = False
                        if verif:
                            print('\nEste(a) aluno(a) não está matriculado(a) em nenhuma turma neste período.',end=(' '))
                        else: print('\nBusca concluída.',end=(' '))
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
                arquivo = open('turmas','r')
                for linha in arquivo.readlines():
                    cod,período,disc,prof,aluno = linha.split(':')
                    prof = prof[2:-2]
                    prof = prof.split("', '")
                    aluno = aluno[2:-3]
                    aluno = aluno.split("', '")
                    turmas[cod] = [período,disc,prof,aluno]
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhuma turma no registro.\n')
                return
        #Inserindo nomes aos alunos e professores
            for cod in turmas:
                for c in range(len(turmas[cod][2])):
                    try:
                        turmas[cod][2][c] = '{}: {}'.format(turmas[cod][2][c],professores[turmas[cod][2][c]][0])
                    except KeyError:
                        turmas[cod][2][c] = '{}: CPF incorreto ou professor não encontrado'.format(turmas[cod][2][c])
                    turmas[cod][2][c] = turmas[cod][2][c].split(':')
                turmas[cod][2] = sorted(turmas[cod][2], key=lambda alfa: alfa[1])
                for c in range(len(turmas[cod][2])):
                    turmas[cod][2][c] = ':'.join(turmas[cod][2][c])
                for c in range(len(turmas[cod][3])):
                    try:
                        turmas[cod][3][c] = '{}: {}'.format(turmas[cod][3][c],alunos[turmas[cod][3][c]][:-1])
                    except KeyError:
                        turmas[cod][3][c] = '{}: CPF incorreto ou aluno não encontrado'.format(turmas[cod][3][c])
                    turmas[cod][3][c] = turmas[cod][3][c].split(':')
                turmas[cod][3] = sorted(turmas[cod][3], key=lambda alfa: alfa[1])
                for c in range(len(turmas[cod][3])):
                    turmas[cod][3][c] = ':'.join(turmas[cod][3][c])

            while True:
                cod = input('\nInsira o código da turma que você deseja atualizar: ')
                try:
                    print('''
Turma {} de {} {}:

Professor(es):
{}

Aluno(s):
{}'''.format(cod,disciplinas[turmas[cod][1]][:-1],turmas[cod][0],'\n'.join(turmas[cod][2]),'\n'.join(turmas[cod][3])))
                    alt = input('\nO que você deseja alterar, Professores ou Alunos?: ').lower()
                    while alt not in ['professores','alunos']:
                        alt = input('\nOpção inválida, por favor escolha uma das seguintes opções: Professores ou Alunos: ').lower()
        #Professores
                    if alt == 'professores':
                        alt = input('\nVocê deseja Adicionar ou Remover professores?: ').lower()
                        while alt not in ['adicionar','remover']:
                            alt = input('\nOpção inválida, por favor escolha uma das seguintes opções: adicionar ou remover: ').lower()
                        if alt == 'adicionar':
                            cpf = input('\nInsira o CPF do(a) professor(a) que você deseja adicionar no formato 000.000.000-00: ')
                            try:
                                turmas[cod][2].append('{}: {}'.format(cpf,professores[cpf][0]))
                                print('\nProfessor(a) {} adicionado(a) com sucesso, para salvar volte ao menu inicial.'.format(professores[cpf][0]),end=(' '))
                            except KeyError:
                                print('\nCPF não encontrado ou incorreto.',end=(' '))
                        elif alt == 'remover':
                            cpf = input('\nInsira o CPF do(a) professor(a) que você deseja remover no formato 000.000.000-00: ')
                            verif = True
                            for prof in turmas[cod][2]:
                                if cpf in prof:
                                    turmas[cod][2].remove(prof)
                                    verif = False
                                    print('\nProfessor(a) {} removido(a) com sucesso, para salvar volte ao menu inicial.'.format(professores[cpf][0]),end=(' '))
                                    break
                            if verif:
                                print('\nCPF não encontrado ou incorreto.',end=(' '))
        #Alunos
                    elif alt == 'alunos':
                        alt = input('\nVocê deseja Adicionar ou Remover alunos?: ').lower()
                        while alt not in ['adicionar','remover']:
                            alt = input('\nOpção inválida, por favor escolha uma das seguintes opções: adicionar ou remover: ').lower()
                        if alt == 'adicionar':
                            cpf = input('\nInsira o CPF do(a) aluno(a) que você deseja adicionar no formato 000.000.000-00: ')
                            try:
                                turmas[cod][3].append('{}: {}'.format(cpf,alunos[cpf][:-1]))
                                print('\n{} adicionado(a) com sucesso, para salvar volte ao menu inicial.'.format(alunos[cpf][:-1]),end=(' '))
                            except KeyError:
                                print('\nCPF não encontrado ou incorreto.',end=(' '))
                        elif alt == 'remover':
                            cpf = input('\nInsira o CPF do(a) aluno(a) que você deseja remover no formato 000.000.000-00: ')
                            verif = True
                            for aluno in turmas[cod][3]:
                                if cpf in aluno:
                                    turmas[cod][3].remove(aluno)
                                    verif = False
                                    print('\n{} removido(a) com sucesso, para salvar volte ao menu inicial.'.format(alunos[cpf][:-1]),end=(' '))
                                    break
                            if verif:
                                print('\nCPF não encontrado ou incorreto.',end=(' '))
    #Encerrando a operação
                except KeyError:
                    print('\nTurma não encontrada ou código incorreto.',end=(' '))
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    arquivo = open('turmas','w')
                    break
            for cod in turmas:
                for c in range(len(turmas[cod][2])):
                    turmas[cod][2][c] = turmas[cod][2][c][:15]
                for c in range(len(turmas[cod][3])):
                    turmas[cod][3][c] = turmas[cod][3][c][:15]
                arquivo.write('{}:{}:{}:{}:{}\n'.format(cod,turmas[cod][0],turmas[cod][1],turmas[cod][2],turmas[cod][3]))
            arquivo.close()
    #Deletar
        elif Acesso == 'deletar':
            try:
                arquivo = open('turmas','r')
                for linha in arquivo.readlines():
                    cod,período,disc,prof,aluno = linha.split(':')
                    prof = prof[2:-2]
                    prof = prof.split("', '")
                    aluno = aluno[2:-3]
                    aluno = aluno.split("', '")
                    turmas[cod] = [período,disc,prof,aluno]
                arquivo.close()
            except FileNotFoundError:
                print('\nNão há nenhuma turma no registro.\n')
                return
            verif = False
            while True:
                delete = input('\nInsira o código da turma que você deseja deletar, ou digite 0000 para deletar todo o registro de turmas: ')
                if delete == '0000':
                    delete = input('\nTem certeza que deseja deletar todo o registro de turmas? Digite 0000 para continuar ou Cancela para voltar: ')
                    if delete == '0000':
                        from os import remove
                        remove('turmas')
                        print('\nO registro de turmas foi deletado com sucesso.\n')
                    break
                else:
                    try:
                        conf = input('\nTem certeza que deseja deletar a turma {} de {} {}, Sim ou Não?: '.format(delete,disciplinas[turmas[delete][1]][:-1],turmas[delete][0])).lower()
                        while conf not in ['sim','não']:
                            conf = input('\nOpção inválida, por favor escolha uma das seguintes opções: Sim ou Não: ').lower()
                        if conf == 'sim':
                            del turmas[delete]
                            print('\nA turma for deletada com sucesso, para salvar volte ao menu inicial.',end=(' '))
                            verif = True
                        else:
                            print('\nA turma não foi deletada.',end=(' '))
                    except KeyError:
                        print('\nTurma não encontrada.',end=(' '))
    #Encerrando a operação
                fim = input('Deseja Continuar ou Voltar?: ')
                while fim not in ['continuar','voltar']:
                    fim = input('\nOpção inválida, por favor escolha uma das seguintes opções: Continuar ou Voltar: ').lower()
                if fim == 'voltar':
                    print('')
                    break
            if verif:
                arquivo.open('turmas','w')
                for cod in turmas:
                    arquivo.write('{}:{}:{}:{}:{}\n'.format(cod,turmas[cod][0],turmas[cod][1],turmas[cod][2],turmas[cod][3]))
                arquivo.close()
