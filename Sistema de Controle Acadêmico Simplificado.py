#Preparos para a execução
import prof
import disc
import aluno
import turma
while True:
    try:
#Menu
        Registro = input("Bem vindo ao Sistema de Controle Acadêmico Simplificado, para sair pressione 'ctrl'+'c' a qualquer momento(Algumas operações podem não ser salvas).\nQual registro você deseja acessar: Professores, Disciplinas, Alunos, Turmas ou Sair ?: ").lower()
        while Registro not in ['professores', 'disciplinas', 'alunos', 'turmas', 'sair']:
            Registro = input('\nOpção inválida, por favor escolha uma das seguintes opções: Professores, Disciplinas, Alunos, Turmas ou Sair: ').lower()
        if Registro == 'sair':
            print('Obrigado por usar o Sistema de Controle Acadêmico Simplificado!')
            break
        Acesso = input('\nO que você deseja fazer: Adicionar, Consultar, Atualizar ou Deletar?: ').lower()
        while Acesso not in ['adicionar', 'consultar', 'atualizar', 'deletar']:
            Acesso = input('\nOpção inválida, por favor escolha uma das seguintes opções: Adicionar, Consultar, Atualizar, ou Deletar: ').lower()
        if Registro == 'professores':
            prof.professores(Acesso)
        elif Registro == 'disciplinas':
            disc.disciplinas(Acesso)
        elif Registro == 'alunos':
            aluno.alunos(Acesso)
        elif Registro == 'turmas':
            turma.turmas(Acesso)
    except KeyboardInterrupt:
        print('Obrigado por usar o Sistema de Controle Acadêmico Simplificado!')
        break
    
