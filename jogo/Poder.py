import sqlite3

# CRIANDO A TABELA PODER

def poder ():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_creat = """
    CREATE TABLE IF NOT EXISTS Poder(
      id SERIAL PRIMARY KEY,
      tipo TEXT NOT NULL,
      dano INT NOT NULL,
      custo_mana INT NOT NULL
    )

  """

  cursor.execute(sql_creat)
  con.commit()
  con.close()

#poder()

# ADICIONANDO OS PODERES

def adicinando_poder(tipo, dano, custo_mana):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicionando = f"""

    INSERT INTO
    Poder(tipo, dano, custo_mana)
    VALUES('{tipo}', {dano}, {custo_mana})

  """

  cursor.execute(sql_adicionando)
  con.commit()
  con.close()

#adicinando_poder('', 0, 0)

