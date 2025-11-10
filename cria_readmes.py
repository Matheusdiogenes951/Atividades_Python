import os

# Caminho da pasta onde estão as atividades
pasta_atividades = "atividades"

# Percorre todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta_atividades):
    if nome_arquivo.endswith(".py"):
        caminho_arquivo = os.path.join(pasta_atividades, nome_arquivo)

        # Tira a extensão
        nome_sem_ext = nome_arquivo.replace(".py", "")

        # Cria o README correspondente
        caminho_readme = os.path.join(pasta_atividades, f"{nome_sem_ext}_README.md")

        conteudo = f"# {nome_sem_ext}\n\n" \
                   f"**Descrição:**\n" \
                   f"Digite aqui o que essa atividade faz.\n\n" \
                   f"**Como executar:**\n" \
                   f"```bash\npython3 {nome_arquivo}\n```"

        with open(caminho_readme, "w", encoding="utf-8") as f:
            f.write(conteudo)

print("✅ Readmes criados com sucesso!")
