from pandas import read_csv
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def normalizar_preco(valor):
    if isinstance(valor, str):
        try:
            # Removendo o "R$"
            valor = valor.replace('R$', '')
            # Convertendo para float
            return locale.atof(valor)
        except ValueError:
            return None
    elif isinstance(valor, (int, float)):
        return valor
    else:
        return None


def normalizar_p_vp(valor):
    if isinstance(valor, str):
        try:
            # valor = valor.replace(',', '.')
            return locale.atof(valor)
        except ValueError:
            return None
    elif isinstance(valor, (int, float)):
        return valor
    else:
        return None


def normalizar_dy(valor):
    # recebe um valor em string que representa uma porcentagem e retorna um float
    if isinstance(valor, str):
        try:
            # Removendo o "%"
            valor = valor.replace('%', '')
            # Convertendo para float
            return locale.atof(valor)
        except ValueError:
            return None
    elif isinstance(valor, (int, float)):
        return valor
    else:
        return None


def read_csv_file(file):
    return read_csv(file)
