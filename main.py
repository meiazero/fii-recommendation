
from src.utils import normalizar_preco, normalizar_p_vp, read_csv_file
from sklearn.neighbors import KNeighborsRegressor


def main(file):
    # Carregando o CSV
    df = read_csv_file(file)

    # Aplicando a normalização na coluna "preco_atuais"
    df['preco_atual'] = df['preco_atual'].apply(normalizar_preco)
    df['p_vp'] = df['p_vp'].apply(normalizar_p_vp)

    # Removendo as linhas que possuem valores nulos
    df = df.dropna(subset=['preco_atual', 'p_vp'])

    # Exibindo o DataFrame após a normalização
    print(df.head())

    # condições: 0.8 < p_vp < 1.2 e dy > 0.95
    # criando um dict para teste e treinamento
    train = data.iloc[:-100]
    test = data.iloc[-100:]

    # criando o modelo de regressão
    model = KNeighborsRegressor(n_neighbors=3)
    model.fit(train[['p_vp']], train['preco_atual'])

    # prevendo os valores
    predictions = model.predict(test[['p_vp']])



if __name__ == "__main__":
    main('planilha-dos-fii.csv')
