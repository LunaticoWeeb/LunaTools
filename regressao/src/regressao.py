import numpy as np
import matplotlib.pyplot as plt

def load_dados(arq_eixo_x, arq_eixo_y):
    """Carrega os dados dos arquivos eixo_x e eixo_y"""
    x_data = np.loadtxt(arq_eixo_x)
    y_data = np.loadtxt(arq_eixo_y)
    return x_data, y_data

def regressao(x_data, y_data, grau):
    """Calcula a regressão linear dos dados"""
    coef = np.polyfit(x_data, y_data, grau)
    linha_x = np.linspace(min(x_data), max(x_data), 1000)

    print(f'Coeficientes da regressão: {coef}')

    linha_y = np.zeros(len(linha_x))

    for i in range(grau+1):
        j = grau - i
        linha_y += coef[j]*linha_x**i
        
    return linha_x, linha_y


def plotar_grafico(config, graph_options):
    """Plota o gráfico dos dados e da regressão"""

    # Carregando os dados
    arq_eixo_x = config['arquivos']['coord_x']
    arq_eixo_y = config['arquivos']['coord_y']
    eixo_x, eixo_y = load_dados(arq_eixo_x, arq_eixo_y)

    # Calculando a regressão
    grau = config['grau']['grau']
    coeficientes = regressao(eixo_x, eixo_y, grau)

    # Informações do gráfico
    titulo = config['legendas']['titulo']
    legenda_x = config['legendas']['eixo_x']
    legenda_y = config['legendas']['eixo_y']
    nome_arq = config['alvo']['pasta'] + config['alvo']['nome']

    # Estilo do gráfico
    plt.style.use(graph_options['styles'][config['estilo']['estilo']])
    dados_estilo = (graph_options['markers'][config['estilo']['tipo_marca']] 
                    + graph_options['colors'][config['estilo']['cor_dados']])
    linha_estilo = (graph_options['colors'][config['estilo']['cor_linha']]
                    + graph_options['linestyles'][config['estilo']['tipo_linha']])

    # Plotando o gráfico
    fig, ax = plt.subplots() # retorna uma tupla com a figura e os eixos
    ax.plot(eixo_x, eixo_y, dados_estilo, label='Dados') # plotando os dados
    ax.plot(coeficientes[0], coeficientes[1], linha_estilo, label='Regressão') # plotando a reta
      
    # adicionando as legendas
    ax.set_title(titulo) # adicionando o titulo
    ax.set_xlabel(legenda_x) # adicionando o label do eixo x
    ax.set_ylabel(legenda_y) # adicionando o label do eixo y
    ax.legend() # adicionando a legendas
      
    # salvando a figura
    fig.savefig(f"{nome_arq}.png", dpi=300) # dpi = resolução da imagem