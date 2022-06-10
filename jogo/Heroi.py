import sqlite3

# CRIANDO A TABELA DE HERÓIS

def herois():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_create = """
    CREATE TABLE IF NOT EXISTS Heroi (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        nível INT NOT NULL,
        força INT NOT NULL,
        defesa INT NOT NULL,
        vida INT NOT NULL,
        mana TEXT NOT NULL,
        modelos TEXT NOT NULL,
        xp TEXT NOT NULL
   )
"""

  cursor.execute(sql_create)
  con.commit()
  con.close()

#herois()

# ADICIONANDO ITENS NA TABELA

def adicionando_herois(nome, nivel, forca, defesa, vida, mana, modelos, xp):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicionando = f"""

     INSERT INTO
     Heroi(nome, nível, força, defesa, vida, mana, modelos, xp)
     VALUES ('{nome}', {nivel}, {forca}, {defesa}, {vida}, '{mana}', '{modelos}', '{xp}')

  """

  cursor.execute(sql_adicionando)
  con.commit()
  con.close()

#adicionando_herois('', 0, 0, 0, 0, '', '', '')
