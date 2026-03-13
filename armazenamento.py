import json
 
def carregar_contas():
    try:
        with open("contas.json", "r") as arquivo:
            contas = json.load(arquivo)
    
    except FileNotFoundError:
        contas = []
    return contas

def salvar_contas(contas):
    with open("contas.json", "w") as arquivo:
        json.dump(contas , arquivo , indent=4)