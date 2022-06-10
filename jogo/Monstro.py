import sqlite3

# CRIANDO A TABELA MONSTRO

def monstro():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_creat = """
    CREATE TABLE IF NOT EXISTS Monstro(
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        força INT NOT NULL,
        defesa INT NOT NULL,
        vida INT NOT NULL,
        mana TEXT NOT NULL,
        tipo TEXT NOT NULL,
        xp_reconpenca TEXT NOT NULL,
        moedas_reconpensa REAL NOT NULL,
        boss TEXT NOT NULL,
        agressivo TEXT NOT NULL
    )

  """

  cursor.execute(sql_creat)
  con.commit()
  con.close()

#monstro()

# ADICINANDO INTENS NAS TABELAS

def adicinando_monstro(nome, forca, defesa, vida, mana, tipo, xp_reconpensa, moedas_reconpensa, boss, agressivo):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicinando = f"""

    INSERT INTO
    Monstro (nome, força, defesa, vida, mana, tipo, xp_reconpenca, moedas_reconpensa, boss, agressivo)
    VALUES ('{nome}', {forca}, {defesa}, {vida}, '{mana}', '{tipo}', '{xp_reconpensa}', {moedas_reconpensa}, '{boss}', '{agressivo}')


  """

  cursor.execute(sql_adicinando)
  con.commit()
  con.close()

#adicinando_monstro('', 0, 0, 0, '', '', '', 0, '', '')
