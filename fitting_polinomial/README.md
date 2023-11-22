# Fitting Polinomial

Programa que realiza o ajuste de uma função polinomial de grau n a um conjunto de dados e plota o gráfico da função ajustada.

## Como usar

### Requisitos

Para executar o programa, é necessário ter instalado o [Python](https://www.python.org/), os pacotes [NumPy](https://numpy.org/), [Matplotlib](https://matplotlib.org/) e [TOML](https://github.com/uiri/toml).

### Execução

A forma mais direta de utilizar o programa é alterar o arquivo `config/config.toml` nas linhas:

```toml
[arquivos]
pasta = ".../LunaTools/fitting_polinomial/arquivos/" # Pasta onde estão os arquivos
arq_coord_x = "coord_x.txt" # Arquivo com as coordenadas x
arq_coord_y = "coord_y.txt" # Arquivo com as coordenadas y

[grau]
grau = 2 # Grau do polinômio

.
.
.

[legendas] # Alterar as legendas do gráfico
titulo = "Gráfico Linear"
eixo_x = "Eixo X"
eixo_y = "Eixo Y"
dados = "Dados"
linha = "Regressão"
```



E executar o programa, basta executar o _script_ `fitting_polinomial.sh` com o comando:

```bash
bash fitting_polinomial.sh
```

O programa irá gerar um arquivo `arquivos/gráfico.png` com o gráfico da função ajustada e imprimir os coeficientes do polinômio ajustado.

### Configuração

Outras opções de configuração podem ser feitas no arquivo `config/config.toml`, como a localização e nome do arquivo de saída:

```toml
[alvo]
pasta = "~/Projetos/LunaTools/fitting_polinomial/arquivos/"
nome = "gráfico"
```

E também o estilo do gráfico:

```toml
[estilo]
cor_dados = "red"
tipo_marca = "circle"
cor_linha = "blue"
tipo_linha = "solid"
estilo = "classic"
```
As opções de estilo estão em `config/graph_options.toml`.
