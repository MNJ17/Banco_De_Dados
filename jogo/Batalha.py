import sqlite3

# CRIANDO A TABELA BATALHA

def batalhas ():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_creat = """
  CREATE TABLE IF NOT EXISTS Batalhas(
      id SERIAL PRIMARY KEY,
      data INT NULL,
      hora TEXT NOT NULL,
      heroi_ganhou TEXT NOT NULL,
      multiplicador INT NOT NULL
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
    VALUES('{data}', {hora}, '{heroi_ganhou}', {multiplicador})

  """


  cursor.execute(sql_adicinando)
  con.commit()
  con.close()


adicionando('2022-01-31', 00.00, 'Ganhou', 500)
adicionando('2020-06-20', 14.20, 'Perdeu', 150)
adicionando('2000-10-28', 8.30, 'Ganhou', 700)
adicionando('2005-05-05', 12.40, 'Perdeu', 100)
adicionando('2019-12-01', 17.00, 'Ganhou', 500)
#adicionando('', 0, '', 0)
