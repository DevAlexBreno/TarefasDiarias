# função para aplicar linhas. e menu exemplo: (=====).
def linha():
    print('=' * 75)
# função para mostrar menu e economizar linhas de codigo.
def menu():
    print('''    OPÇÕES
    1- Exercicios.
    2- HTML CSS.
    3- JavaScript.
    4- Ingles.''')


print('=============================TAREFAS DIÁRIAS===============================')
linha()

# lista de tarefas
tarefas = ['exercicios', 'html css', 'javascript', 'Ingles']

nome = 'Alex'
print(f'Olá {nome}, hoje vamos começar o dia para concluir suas tarefas.')
print(f'''{nome}, conforme terminarmos as tarefas elas irão sair da lista,
dessa forma quando acabarmos todas as tarefas iremos concluir as tarefas 
diarias.''')
linha()

# repetição infinita, enquanto a lista de exercicios não for finalizada, ela continua repetindo até terminar todas as tarefas,
# quando atender as condições do exercicio proposto o nomedo exercicio feito é removido da lista. 
while True:
    menu()
    opcao = int(input('Escolha uma das opções acima: '))
    linha()
    if opcao <=0 or opcao > 4:
        print('Erro de digitação. Digite os numeros entre 1 e 4 para fazer sua escolha...')
    else:    
        if opcao == 1:
            print('Para completar a tarefa EXERCICIOS precisamos fazer no minimo 8 exercicios.')
            quantidadeEx = int(input('Quantos exercicios fizemos? '))
            while quantidadeEx < 8:
                print('Parece que a tarefa está incompleta, tenha feito 8 exercicios para completar.')
                quantidadeEx = int(input('Quantos exercicios fizemos? '))
            tarefas.remove('exercicios')       
            print(f'Conseguimos completar a tarefa EXERCICIOS, com {quantidadeEx} exercicios feitos.')
            if len(tarefas) >= 1:
                print(f'''Ainda falta {len(tarefas)} tarefa(s) para fazer, são elas:
                {tarefas}.  NÃO DESANIME.''')
            elif len(tarefas) == 0:
                print(f'Finalizamos as tarefas diarias. PARABENS {nome}, ESTAMOS NO CAMINHO CERTO.')
            linha()
        if opcao == 2:
            print('Para completar a tarefa HTML CSS precisamos ter no minimo 2 horas de estudo.')
            tempo_html_css = int(input('Quantas horas já estudamos HTML CSS? '))
            linha()
            while tempo_html_css < 2:
                print('Parece que não estudamos o tempo necessario para completar esta tarefa.')
                tempo_html_css = int(input('Quantas horas já estudamos HTML CSS? '))
            tarefas.remove('html css')    
            print(f'Conseguimos completar a tarefa HTML CSS, com {tempo_html_css}horas de estudo.')
            if len(tarefas) >= 1:
                print(f'''Ainda falta {len(tarefas)} tarefa(s) para fazer, são elas:
                {tarefas}.  NÃO DESANIME.''')
            elif len(tarefas) == 0:
                print(f'Finalizamos as tarefas diarias. PARABENS {nome}, ESTAMOS NO CAMINHO CERTO.')
            linha()
        elif opcao == 3:
            print('Para completar a tarefa javaScript precisamos ter no minimo 2 horas de estudo.')
            tempo_javaScript = int(input('Quantas horas já estudamos JavaScript? '))
            linha()
            while tempo_javaScript < 2:
                print('Parece que não estudamos o tempo necessário para completar a tarefa.')
                tempo_javaScript = int(input('Quantas horas já estudamos javaScript? '))
            tarefas.remove('javascript')
            linha()
            print(f'Conseguimos completar a tarefa JavaScript, com {tempo_javaScript}horas de estudo.')
            if len(tarefas) >= 1:
                print(f'''Ainda falta {len(tarefas)} tarefa(s) para fazer, são elas:
                {tarefas}.  NÃO DESANIME.''')
            elif len(tarefas) == 0:
                print(f'Finalizamos as tarefas diarias. PARABENS {nome}, ESTAMOS NO CAMINHO CERTO.')    
            linha()
        elif opcao == 4:
            print('''Para completar a tarefa de ingles precisamos ler no minimo 5 paginas de algum 
            artigo em ingles, para melhorar nossa pronuncia.''')
            paginas = int(input('Quantas paginas você ja leu? '))
            while paginas < 5:
                print(f'não conseguimos completar a tarefa, lemos apenas {paginas} paginas.')
                paginas = int(input('Quantas paginas você ja leu? '))    
            tarefas.remove('Ingles')
            linha()
            print(f'Conseguimos completar a tarefa INGLES, lendo {paginas} paginas.')
            if len(tarefas) >= 1:
                print(f'''Ainda falta {len(tarefas)} tarefa(s) para fazer, são elas:
                {tarefas}.  NÃO DESANIME.''')
            elif len(tarefas) == 0:
                print(f'Finalizamos as tarefas diarias. PARABENS {nome}, ESTAMOS NO CAMINHO CERTO.')    
            linha()
    # quando a lista for igual a zero, ou seja não tiver nenhum item dentro dela, o sistema entende 
    # que não temos mais exercicios para fazer e finaliza.    
    if len(tarefas) == 0:
        print('FINALIZANDO O PROGRAMA POR HOJE...')
        break    







