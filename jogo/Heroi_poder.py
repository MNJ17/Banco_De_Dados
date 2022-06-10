import sqlite3

# CRIANDO A TABELA DE PODER DO HERÓI

def heroi_poder():

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_creat = """
   CREATE TABLE IF NOT EXISTS Heroi_poder(
    id SERIAL PRIMARY KEY,
    heroi_id INT NOT NULL,
    poder_id INT NOT NULL,
    FOREIGN KEY(heroi_id) REFERENCES Heroi(id),
    FOREIGN KEY(poder_id) REFERENCES poder(id)
    )
  """

  cursor.execute(sql_creat)
  con.commit()
  con.close()

#heroi_poder()

# ADICIONANDO OS PODERES DOS HEROIS

def adicionando(heroi_id, poder_id):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicionando =f"""

    INSERT INTO
    Heroi_poder (heroi_id, poder_id)
    VALUES ({heroi_id}, {poder_id})

  """

  cursor.execute(sql_adicionando)
  con.commit()
  con.close()

#adicionando(0, 0)
