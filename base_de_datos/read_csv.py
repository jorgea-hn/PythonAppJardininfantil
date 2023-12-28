import pandas as pd


df = pd.read_excel("ana.xlsx")


# Tabla de estudiantes-----------------------------------------
df_estudiantes = df[df.columns[0:15]]

for indice, fila in df_estudiantes.iterrows():
    print(f"Fila {indice}:")
    print(fila)

df_grados = df[df.columns[16:]]
df_dt = df_grados[:1]


# for indice, fila in df_dt.iterrows():
#     print(f"Fila {indice}:")
#     print(fila)

docente = df_dt.loc[0,'Docente:']
grupo = df_dt.loc[0,'Grupo:']
ano= int(df_dt.loc[0,'Año:'])
periodo = int(df_dt.loc[0,'Periodo:'])

print(docente)
print(grupo)
print(ano)
print(periodo)