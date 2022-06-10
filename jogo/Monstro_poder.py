import sqlite3


import sqlite3

from Poder import poder

# CRIANDO A TABELA DE PODER DO MONSTRO

def monstro_poder():

   con = sqlite3.connect('jogo.sqlite')
   cursor = con.cursor()

   sql_creat = """
   CREATE TABLE IF NOT EXISTS Monstro_poder(
    id SERIAL PRIMARY KEY,
    monstro_id INT NOT NULL,
    poder_id INT NOT NULL,
    FOREIGN KEY(monstro_id) REFERENCES Monstro(id),
    FOREIGN KEY(poder_id) REFERENCES Poder(id)
    )
  """

   cursor.execute(sql_creat)
   con.commit()
   con.close()

#monstro_poder()

# ADICINANDO O PODER DOS MONSTROS

def adicinando(monstro_id, poder_id):

   con = sqlite3.connect('jogo.sqlite')
   cursor = con.cursor()

   sql_adiconando =f"""

     INSERT INTO
     Monstro_poder (monstro_id, poder_id)
     VALUES ({monstro_id}, {poder_id})

   """

   cursor.execute(sql_adiconando)
   con.commit()
   con.close()

#adicinando(0, 0)
