import pandas as pd

file_path = "/content/tabela9515_UF_MG.xlsx"

data = pd.read_excel(file_path, skiprows=3)

data.columns = ["Município", "Índice de Envelhecimento", "Idade Mediana", "Razão de Sexo"]

data = data.dropna(subset=["Município"])

data["Índice de Envelhecimento"] = pd.to_numeric(data["Índice de Envelhecimento"], errors="coerce")

maiores_envelhecimento = data.nlargest(10, "Índice de Envelhecimento")
menores_envelhecimento = data.nsmallest(10, "Índice de Envelhecimento")

maiores_envelhecimento.to_excel("maiores_envelhecimento.xlsx", index=False)
maiores_envelhecimento.to_json("maiores_envelhecimento.json", orient="records", force_ascii=False)

menores_envelhecimento.to_excel("menores_envelhecimento.xlsx", index=False)
menores_envelhecimento.to_json("menores_envelhecimento.json", orient="records", force_ascii=False)

print("Arquivos gerados com sucesso!")