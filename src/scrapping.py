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

from fncs import FilterCardsInfos, FilterCardName, FilterCardSymbol, FilterCardAdmin

BASE_URL = 'https://www.fundsexplorer.com.br/funds'


class FilterMainInfosFII():
    error = []

    def __init__(self) -> None:
        self.run()

    def run(self, url: str = BASE_URL, get=None) -> list:
        cards: list = FilterCardsInfos(url, card_class='fund-card')

        names: list = FilterCardName(cards)
        symbols: list = FilterCardSymbol(cards)
        admins: list = FilterCardAdmin(cards)

        if get == 'names':
            print(f'FIIs Names has listed \n {names} \n')
            return names
        elif get == 'symbol':
            print(f'FIIs Symbols has listed \n {symbols} \n')
            return symbols
        elif get == 'admins':
            print(f'FIIs Admins has listed \n {admins} \n')
            return admins
        else:
            return self.error


class FilterValueAndTypeFII():
    pass


class FilterFIICompanyInfos():
    pass


class FilterDividendMetrics():
    pass


if __name__ == '__main__':
    FilterMainInfosFII().run(get='symbol')
