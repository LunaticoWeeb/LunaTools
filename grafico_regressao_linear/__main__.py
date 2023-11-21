from . import regressao as rl

# TODO: 
# - [x] resolver problema do interpretador não encontrar o arquivo
# - [x] organizar arquivos da pasta
# - [ ] criar um arquivo de configuração para o programa

if __name__ == '__main__':
    print("Digite o nome (ou localização) do arquivo com os dados do eixo x:")
    arq_eixo_x = input()
    print("Digite o nome (ou localização) do arquivo com os dados do eixo y:")
    arq_eixo_y = input()
    eixo_x, eixo_y = rl.load_dados(arq_eixo_x, arq_eixo_y)
    inclinacao, altura = rl.regressao_linear(eixo_x, eixo_y)

    print("Digite o título do gráfico:")
    titulo = input()
    print("A legenda do eixo x:")
    legenda_x = input()
    print("A legenda do eixo y:")
    legenda_y = input()
    print("Digite o nome do arquivo para salvar o gráfico:")
    nome_arq = input()

    rl.plotar_grafico(eixo_x, eixo_y, inclinacao, altura, titulo, legenda_x, legenda_y, nome_arq)