from src.utils import normalizar_preco, normalizar_p_vp, read_csv_file, normalizar_dy

def main(file):
    # Loading the CSV
    df = read_csv_file(file)

    # Applying normalization to the "preco_atual", "p_vp", and "dy_12m_media" columns
    df['preco_atual'] = df['preco_atual'].apply(normalizar_preco)
    df['p_vp'] = df['p_vp'].apply(normalizar_p_vp)
    df['dy_12m_media'] = df['dy_12m_media'].apply(normalizar_dy)

    # Removing rows with null values
    df = df.dropna(subset=['p_vp', 'dy_12m_media'])

    # Creating a new column that represents if each row meets the conditions
    df['conditions_met'] = ((df['p_vp'] > 0.8) & (df['p_vp'] < 1.2) & (df['dy_12m_media'] > 0.95) & (df['dy_12m_media'] < 1.5 ) & (df['quantidade_ativos'] > 0))

    # Filtering the dataset to include only the rows that meet the conditions
    filtered_df = df[df['conditions_met'] == True]

    # Creating a new CSV file with the filtered data
    filtered_df.to_csv('filtered.csv', index=False)

    # TODO: add a classification model to predict if a FII is a good investment or not

if __name__ == "__main__":
    main('planilha-dos-fii.csv')
