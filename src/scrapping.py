'''

Aqui será feito um scrapping de duas paginas de FIIs, para armazenar os dados em uma planilha.

A lista de FIIs pode ser obtida em https://www.fundsexplorer.com.br/funds:

- Nome do fundo
- Label do fundo
- Administrador

em https://fiis.com.br/lista-de-fundos-imobiliarios/ temos:

- tipo
- Patrimônio Líquido

na pagina https://www.fundsexplorer.com.br/funds/<nome do fundo> temos:

- Valor atual
- Valor Patrimonial
- Dividend Yield
- Último Rendimento
- P/VP (Patrimonio / Valor Patrimonial)
- Rentab. no mês

Metricas de dividendos pode ser obtida em: https://fiis.com.br/<nome do fundo>

- Ultimos dividendo


'''


class FilterMainInfosFII():
    pass

class FilterValueAndTypeFII():
    pass

class FilterFIICompanyInfos():
    pass

class FilterDividendMetrics():
    pass