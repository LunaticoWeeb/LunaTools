from .src import regressao as rl
import toml
import os

def main():

    # Acha o diretório do script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Criando o caminho para o arquivo de configuração e opções de gráfico
    config_path = os.path.join(script_dir, 'config/config.toml')
    graph_options_path = os.path.join(script_dir, 'config/graph_options.toml')

    # Carregando o arquivo de configuração
    config = toml.load(config_path) 
    graph_options = toml.load(graph_options_path)

    # Realizando a regressão e plotando o gráfico
    rl.plotar_grafico(config, graph_options)

if __name__ == '__main__':
    main()