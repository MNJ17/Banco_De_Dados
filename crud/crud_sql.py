import sqlite3
def create_table():

  con = sqlite3.connect('crud.sqlite')
  cursor = con.cursor()

  sql_creat = """

      CREATE TABLE IF NOT EXISTS MovimentaçãoFinanceira(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      data TEXT NOT NULL,
      nome TEXT NOT NULL,
      tipo TEXT NOT NULL,
      valor REAL NOT NULL
      )
  """
  cursor.execute(sql_creat)
  con.commit()
  con.close()

create_table()

def insert(data, nome, tipo, valor):

   con = sqlite3.connect('crud.sqlite')
   cursor = con.cursor()

   sql_add = f"""

      INSERT INTO
      MovimentaçãoFinanceira(data, nome, tipo, valor)
      VALUES
      ('{data}', '{nome}', '{tipo}', {valor})

   """

   cursor.execute(sql_add)
   con.commit()
   con.close()

#insert('', '', '', 0 )

def select(id):

  con = sqlite3.connect('crud.sqlite')
  cursor = con.cursor()

  sql_select = f"""

    SELECT  id, data
    FROM MovimentaçãoFinanceira
    WHERE id = {id}
  """
  cursor.execute(sql_select)
  printando = cursor.fetchall()
  print(printando[0])

#select(0)

def select_list():

    con =  sqlite3.connect('crud.sqlite')
    cursor = con.cursor()

    sql_select = """

        SELECT id, nome, tipo, valor
        FROM MovimentaçãoFinanceira

    """

    cursor.execute(sql_select)
    printando = cursor.fetchall()

    for M in printando:
        print (M)

#select_list()

def update(id, data):

  con = sqlite3.connect('crud.sqlite')
  cursor = con.cursor()

  sql_update = f"""

     UPDATE MovimentaçãoFinanceira set data = '{data}'
     WHERE id = {id}
  """

  cursor.execute(sql_update)
  con.commit()
  con.close()

#update(0,'2022-02-03')

def delete(id):

  con = sqlite3.connect('crud.sqlite')
  cursor = con.cursor()

  sql_delet =f"""

     DELETE FROM MovimentaçãoFinanceira
     WHERE id = {id}
  """

  cursor.execute(sql_delet)
  con.commit()
  con.close()

#delete(0)

def entradas():

  con = sqlite3.connect('crud.sqlite')
  cursor = con.cursor()

  sql_entrada = """

    SELECT data, nome, tipo
    FROM MovimentaçãoFinanceira
    WHERE tipo = 'Entrada'
  """

  cursor.execute(sql_entrada)
  printando = cursor.fetchall()
  print(printando)

#entradas()

def saidas():

   con = sqlite3.connect('crud.sqlite')
   cursor = con.cursor()

   sql_saida = """

      SELECT data, nome, tipo
      FROM MovimentaçãoFinanceira
      WHERE tipo = 'Saida'
   """

   cursor.execute(sql_saida)
   printando = cursor.fetchall()
   print(printando)

saidas()

if __name__ == "__main__":
    pass
