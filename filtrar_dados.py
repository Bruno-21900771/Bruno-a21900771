import json

with open("dados.json") as f:
    dados = json.load(f)

modelos_a_excluir = {"auth.permission", "contenttypes.contenttype", "admin.logentry", "sessions.session"}

dados_filtrados = [d for d in dados if d["model"] not in modelos_a_excluir]

with open("dados.json", "w") as f:
    json.dump(dados_filtrados, f)

print(f"Ficheiro filtrado: {len(dados)} → {len(dados_filtrados)} registos")