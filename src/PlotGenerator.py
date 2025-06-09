import matplotlib.pyplot as plt

class PlotGenerator:
    def __init__(self, df_long):
        self.df = df_long

    def plot_gini_over_time_by_state(self, state_name):
        df_state = self.df[self.df["Estado"] == state_name]

        plt.figure(figsize=(10, 5))
        plt.plot(df_state["Ano"], df_state["Gini"], marker='o')
        plt.title(f"Índice de Gini ao longo dos anos - {state_name}")
        plt.xlabel("Ano")
        plt.ylabel("Índice de Gini")
        plt.grid(True)
        plt.show()