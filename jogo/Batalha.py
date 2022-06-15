import sqlite3

# CRIANDO A TABELA BATALHA

def batalhas ():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_creat = """
  CREATE TABLE IF NOT EXISTS Batalhas(
      id SERIAL PRIMARY KEY,
      data TEXT NULL,
      hora TEXT NOT NULL,
      heroi_ganhou TEXT NOT NULL,
      multiplicador TEXT NOT NULL
  )

  """

  cursor.execute(sql_creat)
  con.commit()
  con.close()

#batalhas()

# ADICINANDO INTENS NA BATALHA

def adicionando(data, hora, heroi_ganhou, multiplicador):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicinando =f"""

    INSERT INTO
    Batalhas(data, hora, heroi_ganhou, multiplicador)
    VALUES('{data}', '{hora}', '{heroi_ganhou}', '{multiplicador}')

  """


  cursor.execute(sql_adicinando)
  con.commit()
  con.close()

#adicionando('', '', '','')
