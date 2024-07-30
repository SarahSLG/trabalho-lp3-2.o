def cadastro_arquivo():
    with open("Dados/usuarios.csv", mode="r") as usuarios2:
        usuarios = [] 
        for linha in usuarios2: # faz cada linha ser um dicionário
            dados_usuario = linha.strip().split(",") # Tira os espaços antes e depois 
            linha = {
                    "nome": dados_usuario[0],
                    "email": dados_usuario[1], 
                    "senha": dados_usuario[2],
                    "codigo": dados_usuario[3],
                    "admin": dados_usuario[4]
                    }
            usuarios.append(linha)
            return usuarios

def salvar_cadastro(nome, email, senha,codigo, admin):
    with open("Dados/usuarios.csv", "a", encoding="utf8") as usuarios2: 
        usuarios =  f"{nome},{email},{senha},{codigo},{admin}"
        usuarios2.write(f"{usuarios}\n")

def salas_arquivo():
    with open("Dados/salas.csv", mode="r", encoding="utf8") as salas2:
        salas = [] 
        for linha in salas2: # faz cada linha ser um dicionário
            dados_salas = linha.strip().split(",") # Tira os espaços antes e depois 
            linha = {
                        "codigo": dados_salas[0],
                        "tipo": dados_salas[1], 
                        "descricao": dados_salas[2],
                        "capacidade": dados_salas[3],
                        "ativo": dados_salas[4]
                    }
            salas.append(linha)
    return salas
        
def cadastrar_salas(codigo, tipo, descricao, capacidade, ativo):
    with open("Dados/salas.csv", "a", encoding="utf8") as salas2: 
        salas =  f"{codigo},{tipo},{descricao},{capacidade},{ativo}"
        salas2.write(f"{salas}\n")

def reservas_arquivo():
    with open("Dados/reservas.csv", mode="r", encoding="utf8") as reservas2:
        reservas = [] 
        for linha in reservas2: # faz cada linha ser um dicionário
            dados_reservas = linha.strip().split(",") # Tira os espaços antes e depois 
            linha = {
                        "codigo": dados_reservas[0],
                        "sala": dados_reservas[1], 
                        "d_início": dados_reservas[2],
                        "d_fim": dados_reservas[3],
                        "admin": dados_reservas[4],
                        "ativo": dados_reservas[5]
                    }
            reservas.append(linha)
    return reservas

def cadastrar_reserva(codigo, sala, d_inicio, d_fim, admin, ativo):
     with open("Dados/reservas.csv", "a", encoding="utf8") as reservas2: 
        reservas =  f"{codigo},{sala},{d_inicio},{d_fim},{admin},{ativo}"
        reservas2.write(f"{reservas}\n")

