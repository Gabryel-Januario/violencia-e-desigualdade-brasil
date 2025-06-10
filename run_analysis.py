def main():
    import sys
    import os
    import pandas as pd
    from src.Data_handler import Data_handler
    from src.PlotGenerator import PlotGenerator
    from src.utils.Utils import Utils

    sys.path.append(os.path.abspath('..')) 

    mortes_violentas_csv_path = os.path.join('datas', 'mortes-violentas.csv' )
    indice_gini_csv_path = os.path.join('datas', 'ipeadata[05-06-2025-04-16].csv' )

    dh_mv = Data_handler(mortes_violentas_csv_path)
    dh_gini = Data_handler(indice_gini_csv_path)

    df_mv = dh_mv.load_csv()
    df_gini = dh_gini.load_csv(skiprows=1)

    df_mv = dh_mv.clean_data()
    df_gini = dh_gini.clean_data()

    for i in range(2012, 2023):
        df_gini[str(i)] = df_gini[str(i)].str.replace(',', '.').astype(float)

    df_gini_long = dh_gini.gini_df_to_long(df=df_gini)
    df_gini_long = df_gini_long.rename(columns={'Sigla': 'UF', 'Ano': 'ano'})

    df_mv_filtrado = df_mv[(df_mv['periodo'] >= 2012) & (df_mv['periodo'] <= 2022)]
    df_mv_filtrado = df_mv_filtrado.rename(columns={'nome': 'UF', 'periodo': 'ano'})

    utils = Utils()
    utils.column_type_converter(df=df_mv_filtrado, column_name='ano', type=int)
    utils.column_type_converter(df=df_mv_filtrado, column_name='valor', type=int)
    utils.column_type_converter(df=df_gini_long, column_name='ano', type=int)

    # Geração de gráficos
    plt_gini = PlotGenerator(df_gini_long)
    plt_gini.plot_gini_over_time_by_state(['SP', 'RJ', 'PB', 'BH', 'RS', 'MG'])

    plt_mv = PlotGenerator(df=df_mv_filtrado)
    plt_mv.plot_violence_over_time_by_state(['SP', 'RJ', 'PB', 'BH', 'RS', 'MG'])

    df_combined = utils.merge_dataframes(df_gini=df_gini_long, df_mv=df_mv_filtrado)
    plt_df_combined = PlotGenerator(df_combined)
    plt_df_combined.ratio_over_time_by_state('MG')

    plt_df_combined.plot_correlation_heatmap(["SP", "RJ", "MG", "PB", "RS", "BA", "GO", "SC", "ES", "MT", "AC" ])

if __name__ == '__main__':
    main()