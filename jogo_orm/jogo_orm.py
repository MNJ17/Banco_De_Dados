
from sqlalchemy import INTEGER, VARCHAR, Column, create_engine, column, INTEGER,ForeignKey, DECIMAL, VARCHAR, BOOLEAN, TIME, DATE
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
password = 'MNJ2004'
host = 'localhost'
port = '5432'
db = 'postgres'
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Heroi(Base):
  __tablename__ = 'Heroi'

  id = Column(INTEGER, primary_key = True)
  nome = Column(VARCHAR(255))
  nivel = Column(INTEGER)
  forca = Column(INTEGER)
  defesa = Column(INTEGER)
  vida = Column(INTEGER)
  mana = Column(DECIMAL(10, 2))
  moeda = Column(DECIMAL(10, 2))
  xp = Column(DECIMAL(10, 2))

  def __repr__(self):
      return f'{self.id} - {self.nome}'

  class Monstro(Base):
     __tablename__ = 'Monstro'

     id = Column(INTEGER, primary_key = True)
     nome = Column(VARCHAR(255))
     nivel = Column(INTEGER)
     forca = Column(INTEGER)
     defesa = Column(INTEGER)
     vida = Column(INTEGER)
     mana = Column(DECIMAL(10, 2))
     tipo = Column(VARCHAR(55))
     moedas_reconpenca = Column(DECIMAL(10, 2))
     xp_reconpensa = Column(DECIMAL(10, 2))
     boss = Column(BOOLEAN)
     agressivo = Column(BOOLEAN)

  class Batalhas(Base):
    __tablename__ = 'Batalhas'

    id = Column(INTEGER, primary_key = True)
    data = Column(DATE)
    hora = Column(TIME)
    heroi_ganhou = Column(BOOLEAN)
    multiplicador = Column(DECIMAL(10, 2))

  class Poder(Base):
   __tablename__ = 'Poder'

   id = Column(INTEGER, primary_key = True)
   tipo = Column(VARCHAR(55))
   dano = Column(INTEGER)
   custo_mana = Column(DECIMAL(10, 2))


  class HeroiPoder(Base):
   __tablename__ = 'Heroi_Poder'

   id = Column(INTEGER, primary_key = True)
   heroi_id  = Column(INTEGER, ForeignKey('Heroi.id'))
   poder_id = Column(INTEGER, ForeignKey('Poder.id'))


  class MonstroPoder(Base):
   __tablename__ = 'Monstro_Poder'

   id = Column(INTEGER, primary_key =  True)
   monstro_id = Column(INTEGER, ForeignKey('Monstro.id'))
   poder_id = Column(INTEGER, ForeignKey('Poder.id'))


  class MonstroHeroiBatalhas(Base):
   __tablename__ = 'Monstro_Heroi_Batalha'

   id = id = Column(INTEGER, primary_key=  True)
   heroi_id  = Column(INTEGER, ForeignKey('Heroi.id'))
   monstro_id = Column(INTEGER, ForeignKey('Monstro.id'))
   batalha_id = Column(INTEGER, ForeignKey('Batalhas.id'))


Base.metadata.create_all(engine)
