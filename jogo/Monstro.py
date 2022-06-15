import sqlite3

# CRIANDO A TABELA MONSTRO

def monstro():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_creat = """
    CREATE TABLE IF NOT EXISTS Monstro(
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        nivel INT NOT NULL,
        força INT NOT NULL,
        defesa INT NOT NULL,
        vida INT NOT NULL,
        mana INT NOT NULL,
        xp_reconpenca INT NOT NULL,
        moedas_reconpensa INT NOT NULL,
        boss TEXT NOT NULL,
        agressivo TEXT NOT NULL,
        tipo TEXT NOT NULL
    )

  """

  cursor.execute(sql_creat)
  con.commit()
  con.close()

#monstro()

# ADICINANDO INTENS NAS TABELAS

def adicinando_monstro(nome, nivel, forca, defesa, vida, mana, xp_reconpensa, moedas_reconpensa, boss, agressivo, tipo):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicinando = f"""

    INSERT INTO
    Monstro (nome, nivel, força, defesa, vida, mana, moedas_reconpensa, xp_reconpenca, boss, agressivo, tipo)
    VALUES ('{nome}', {nivel}, {forca}, {defesa}, {vida}, {mana}, {moedas_reconpensa}, {xp_reconpensa}, '{boss}', '{agressivo}','{tipo}')


  """

  cursor.execute(sql_adicinando)
  con.commit()
  con.close()

#adicinando_monstro('', 0, 0, 0, '', '', '', 0, '', '')


