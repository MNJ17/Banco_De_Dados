import sqlite3

# CRIANDO A TABEA MONTRO_HERÓI_BATALHA

def monstro_heroi_batalha():

   con = sqlite3.connect('jogo.sqlite')
   cursor = con.cursor()

   sql_creat = """
     CREATE TABLE IF NOT EXISTS Monstro_Heroi_Batalha(
      id SERIAL PRIMARY KEY,
      heroi_id INT NOT NULL,
      monstro_id INT NOT NULL,
      batalha_id INT NOT NULL,
      FOREIGN KEY(heroi_id) REFERENCES Heroi(id),
      FOREIGN KEY(monstro_id) REFERENCES Monstro(id),
      FOREIGN KEY(batalha_id) REFERENCES Batalhas(id)
   )

   """

   cursor.execute(sql_creat)
   con.commit()
   con.close()

#monstro_heroi_batalha()

# ADICINANDO ITENS NA TABELA MONSTRO_HEROI_BATALHA

def adicinando(heroi_id, monstro_id, batalha_id):

  con = sqlite3.connect('jogo.sqlite')
  cursor = con.cursor()

  sql_adicinando =f"""

  INSERT INTO
  Monstro_Heroi_Batalha(heroi_id, monstro_id, batalha_id)
  VALUES({heroi_id}, {monstro_id}, {batalha_id})
  """

  cursor.execute(sql_adicinando)
  con.commit()
  con.close()

#adicinando()
