def ler_logs():
  
    contagem = {"INFO": 0, "ERROR": 0, "WARNING": 0}

 
    with open(r"c:\Users\W10\Downloads\log_exercicio_ip_user_modulo_500_linhas (1).txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            if "[INFO]" in linha:
                contagem["INFO"] += 1
            elif "[ERROR]" in linha:
                contagem["ERROR"] += 1
            elif "[WARNING]" in linha:
                contagem["WARNING"] += 1

    relatorio = (
        f"RELATÓRIO DE LOGS\n"
        f"INFO: {contagem['INFO']}\n"
        f"ERROR: {contagem['ERROR']}\n"
        f"WARNING: {contagem['WARNING']}\n"
    )
#salvando relatorio em arquivo
    with open("relatorio.txt", "w", encoding="utf-8") as arq_rel:
        arq_rel.write(relatorio)

    print(relatorio)
0
ler_logs()