
from src.utils import normalizar_preco, normalizar_p_vp


def main(file):
    # Carregando o CSV
    df = read_csv(file)
    
    # Aplicando a normalização na coluna "preco_atuais"
    df['preco_atual'] = df['preco_atual'].apply(normalizar_preco)
    df['p_vp'] = df['p_vp'].apply(normalizar_p_vp)
    
    # Exibindo o DataFrame após a normalização
    print(df['p_vp'].head(50))


if __name__ == "__main__":
    main('planilha-dos-fii.csv')
