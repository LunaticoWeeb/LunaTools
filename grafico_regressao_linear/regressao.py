import numpy as np
import matplotlib.pyplot as plt

def load_dados(arq_eixo_x, arq_eixo_y):
    """Carrega os dados dos arquivos eixo_x e eixo_y"""
    x_data = np.loadtxt(arq_eixo_x)
    y_data = np.loadtxt(arq_eixo_y)
    return x_data, y_data

def regressao_linear(x_data, y_data):
    """Calcula a regressão linear dos dados"""
    a, b = np.polyfit(x_data, y_data, 1)
    return a, b

def plotar_grafico(x_data, y_data, a, b, titulo, legenda_x, legenda_y, nome_arq):
    """Plota o gráfico dos dados e da regressão linear"""
    fig, ax = plt.subplots() # retorna uma tupla com a figura e os eixos
    ax.plot(x_data, y_data, 'or', label='Dados Originais') # plotando os dados
    ax.plot(x_data, a*x_data + b, '-b', label='Regressão Linear') # plotando a reta
      
    # adicionando as legendas
    ax.set_title(titulo) # adicionando o titulo
    ax.set_xlabel(legenda_x) # adicionando o label do eixo x
    ax.set_ylabel(legenda_y) # adicionando o label do eixo y
    ax.legend() # adicionando a legenda
    plt.text(0.72, 0.12, f'inclinação: {a: 0.2f}\n  altura: {b: 0.2f}', 
             transform=plt.gca().transAxes, fontsize=11,
             verticalalignment='top', 
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.5)) # legenda dos coeficientes
      
    # salvando a figura
    fig.savefig(f"{nome_arq}.png", dpi=300) # dpi = resolução da imagem