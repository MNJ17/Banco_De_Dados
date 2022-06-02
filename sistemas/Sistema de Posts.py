import sqlite3

# CRIANDO TABELAS PARA O BANCO DE DADOS:


def tabelas_usuarios():

  con = sqlite3.connect('banco.sqlite')

  sql_create = """
  CREATE TABLE IF NOT EXISTS usuarios(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  email TEXT NOT NULL,
  username TEXT NOT NULL,
  password TEXT NOT NULL
  ) """

  cursor = con.cursor()
  cursor.execute(sql_create)
  con.commit()
  con.close()

#tabelas_usuarios()

def tabelas_post():

  con = sqlite3.connect('banco.sqlite')

  sql_create = """

  CREATE TABLE IF NOT EXISTS post(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usuarios_id INTEGER NOT NULL,
  titulo TEXT NOT NULL,
  texto TEXT NOT NULL,
  FOREIGN KEY (usuarios_id) REFERENCES usuarios(id)
  )"""

  cursor = con.cursor()
  cursor.execute(sql_create)
  con.commit()
  con.close()

#tabelas_post()

def tabelas_comentarios():

  con = sqlite3.connect('banco.sqlite')

  sql_create = """

  CREATE TABLE IF NOT EXISTS comentario(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  usarios_id INTEGER NOT NULL,
  post_id INTEGER NOT NULL,
  texto TEXT NOT NULL,
  FOREIGN KEY (usarios_id) REFERENCES usuarios(id),
  FOREIGN KEY (post_id) REFERENCES post(id)
 )
  """

  cursor = con.cursor()
  cursor.execute(sql_create)
  con.commit()
  con.close()

#tabelas_comentarios()

# INSERINDO INFORMAÇÕES NAS TABELAS CRIADAS:



def inserir_usuarios(nome, email, username, password):

  con = sqlite3.connect('banco.sqlite')

  sql_inserindo = f"""

      INSERT INTO
      usuarios (nome, email, username, password)
      VALUES
      ('{nome}', '{email}', '{username}', '{password}')
  """

  cursor = con.cursor()
  cursor.execute(sql_inserindo)
  con.commit()
  con.close()

#inserir_usuarios('', '', '', '')

def inserir_post(usuarios_id, titulo, texto):

  con = sqlite3.connect('banco.sqlite')

  sql_inserindo = f"""

      INSERT INTO
      post (usuarios_id, titulo, texto)
      VALUES
      ({usuarios_id}, '{titulo}', '{texto}')
  """

  cursor = con.cursor()
  cursor.execute(sql_inserindo)
  con.commit()
  con.close()

#inserir_post(0, '', '')

def inserir_comentrios(usuarios_id, post_id, texto):

  con = sqlite3.connect('banco.sqlite')

  sql_inserindo = f"""

      INSERT INTO
      comentario (usarios_id, post_id, texto)
      VAlUES
      ({usuarios_id}, {post_id}, '{texto}')
  """

  cursor = con.cursor()
  cursor.execute(sql_inserindo)
  con.commit()
  con.close()

#inserir_comentrios(0, 0, '')

# SELECIONANDO ITENS EXPECIFICOS DO BANCO:


def selecione_usuarios():

  con = sqlite3.connect('banco.sqlite')


  sql_selecionando = """

     SELECT  id, username, email
     FROM usuarios
  """

  cursor = con.cursor()
  cursor.execute(sql_selecionando)
  data = cursor.fetchall()
  print(data)
  print()

  for M in data:
    print(M)

#selecione_usuarios()

def selecione_post():

  con = sqlite3.connect('banco.sqlite')

  sql_selecionando = """

     SELECT titulo, texto
     FROM post

  """

  cursor = con.cursor()
  cursor.execute(sql_selecionando)
  data = cursor.fetchall()
  print(data)
  print()

  for M in data:
   print(M)

#selecione_post()


def selecione_comentarios():

  con = sqlite3.connect('banco.sqlite')

  sql_selecionando = """

    SELECT texto
    FROM comentario

  """

  cursor = con.cursor()
  cursor.execute(sql_selecionando)
  data = cursor.fetchall()
  print(data)
  print()

  for M in data:
    print(M)

#selecione_comentarios()

# EDITANDO INTENS DO BANCO DE DADOS:

def update_usuarios(id, username):

  con = sqlite3.connect('banco.sqlite')

  sql_editando = f"""

     UPDATE usuarios SET username = '{username}'
     WHERE id = {id}
  """

  cursor = con.cursor()
  cursor.execute(sql_editando)
  con.commit()
  con.close()

#update_usuarios(0, '')

def update_post(id, texto):

  con = sqlite3.connect('banco.sqlite')

  sql_editando = f"""

    UPDATE post SET texto  = '{texto}'
    WHERE id = {id}
  """

  cursor = con.cursor()
  cursor.execute(sql_editando)
  con.commit()
  con.close()

#update_post(0, '')

def update_comentarios(id, texto):

  con = sqlite3.connect('banco.sqlite')

  sql_editando = f"""

    UPDATE comentario SET texto = '{texto}'
    WHERE id = {id}
  """

  cursor = con.cursor()
  cursor.execute(sql_editando)
  con.commit()
  con.close()

#update_comentarios(0, '')

# APAGANDO ITENS DO BANCO DE DADOS:

def apagar_usuarios(id):

  con = sqlite3.connect('banco.sqlite')

  sql_apagando = f"""

    DELETE FROM usuarios
    WHERE id = {id}
  """

  cursor = con.cursor()
  cursor.execute(sql_apagando)
  con.commit()
  con.close()

#apagar_usuarios(0)

def apagar_post(id):

  con = sqlite3.connect ('banco.sqlite')

  sql_apaganndo = f"""

      DELETE FROM post
      WHERE id = {id}
  """

  cursor = con.cursor()
  cursor.execute(sql_apaganndo)
  con.commit()
  con.close()

#apagar_post(0)

def apagar_comentarios(id):

  con = sqlite3.connect('banco.sqlite')

  sql_apagando = f"""

     DELETE FROM comentario
     WHERE id = {id}
  """

  cursor = con.cursor()
  cursor.execute(sql_apagando)
  con.commit()
  con.close()

#apagar_comentarios(0)
