
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

#heroi_1 = Heroi(nome = 'Titan', nivel = 15, forca = 210, defesa = 110, vida = 2500, mana = 1050.00, moeda = 1500, xp = 34010)
#heroi_2 = Heroi(nome = 'Dentas', nivel = 35, forca = 351, defesa = 225, vida = 3100, mana = 1200.00, moeda = 3000, xp = 65125)
#heroi_3 = Heroi(nome = 'Katung', nivel = 23, forca = 275,  defesa = 179, vida = 2850, mana = 1125.00, moeda = 2200, xp = 45784)
#heroi_4 = Heroi(nome = 'Xinguan', nivel = 9, forca  = 112, defesa = 85, vida = 1450, mana = 950.00, moeda = 984, xp = 19874)
#heroi_5 = Heroi(nome = 'Xyra', nivel = 48, forca = 487, defesa = 370, vida = 3890, mana = 1680.00, moeda = 6000, xp = 89837)

#monstro_1 = Monstro(nome = 'DTent', nivel = 10, forca = 45, defesa = 75, vida = 9500, mana = 855, moedas_reconpenca = 125, xp_reconpensa = 1200, boss = 'FALSE', agressivo = 'FALSE', tipo = 'pedra')
#monstro_2 = Monstro(nome = 'Seclar', nivel = 15, forca = 78, defesa = 120, vida = 12500, mana = 985, moedas_reconpenca = 250, xp_reconpensa = 1500,boss = 'FALSE', agressivo = 'FALSE', tipo = 'agua')
#monstro_3 = Monstro(nome = 'OnderBreak', nivel = 47, forca = 215, defesa = 625, vida = 45700, mana = 2500, moedas_reconpenca = 3252, xp_reconpensa = 3520,boss = 'True', agressivo = 'FALSE', tipo = 'fogo')
#monstro_4 = Monstro(nome = 'Decatete', nivel = 99, forca = 3335, defesa = 4444, vida = 85900, mana = 3800, moedas_reconpenca = 7252, xp_reconpensa = 12200, boss = 'True', agressivo = 'TRUE', tipo = 'metal')
#monstro_5 = Monstro(nome = 'OnderBreak', nivel = 22, forca = 124, defesa = 320, vida = 21300, mana = 1204,moedas_reconpenca = 850, xp_reconpensa = 2200, boss = 'False', agressivo = 'TRUE', tipo = 'fantasma')

#batalhas_1 = Batalhas(data = '2022-04-12', hora = '12:33:25', heroi_ganhou = 'TRUE', multiplicador = 1.5)
#batalhas_2 = Batalhas(data = '2022-04-22', hora = '0:47:35', heroi_ganhou = 'TRUE', multiplicador = 1.5)
#batalhas_3 = Batalhas(data = '2022-04-17', hora = '2:25:47', heroi_ganhou = 'TRUE', multiplicador = 1.5)
#batalhas_4 = Batalhas(data = '2022-05-15', hora = '3:10:58', heroi_ganhou = 'TRUE', multiplicador = 1.5)
#batalhas_5 = Batalhas(data = '2022-05-27', hora = '12:41:19', heroi_ganhou = 'TRUE', multiplicador = 1.5)
#batalhas_6 = Batalhas(data = '2022-06-08', hora = '7:22:55', heroi_ganhou = 'FALSE', multiplicador = 1.5)
#batalhas_7 = Batalhas(data = '2022-06-07', hora = '21:39:13', heroi_ganhou = 'TRUE', multiplicador = 1.5)
#batalhas_8 = Batalhas(data = '2022-06-10', hora = '14:44:22', heroi_ganhou = 'FALSE', multiplicador = 1.5)
#batalhas_9 = Batalhas(data = '2022-06-10', hora = '6:17:14', heroi_ganhou = 'FALSE', multiplicador = 1.5)

#poder_1 =  Poder(tipo = 'ataque-basico', dano = 35, custo_mana = 0)
#poder_2 =  Poder(tipo = 'lança-chamas', dano = 115, custo_mana = 50)
#poder_3 =  Poder(tipo = 'congela', dano = 90, custo_mana = 35)
#poder_4 =  Poder(tipo = 'aquatico', dano = 125, custo_mana = 47)
#poder_5 =  Poder(tipo = 'magmante', dano = 200, custo_mana = 150)
#poder_6 =  Poder(tipo = 'confusao', dano = 35, custo_mana = 200)
#poder_7 =  Poder(tipo = 'olha-a-pedra', dano = 55, custo_mana = 10)

#hp_1 = HeroiPoder(heroi_id = 1, poder_id = 7)
#hp_2 = HeroiPoder(heroi_id = 2, poder_id = 6)
#hp_3 = HeroiPoder(heroi_id = 3, poder_id = 4)
#hp_4 = HeroiPoder(heroi_id = 4, poder_id = 2)
#hp_5 = HeroiPoder(heroi_id = 5, poder_id = 5)

#mp1 = MonstroPoder(monstro_id = 1, poder_id = 1)
#mp2 = MonstroPoder(monstro_id = 2, poder_id = 4)
#mp3 = MonstroPoder(monstro_id = 3, poder_id = 3)
#mp4 = MonstroPoder(monstro_id = 4, poder_id = 2)
#mp5 = MonstroPoder(monstro_id = 5, poder_id = 7)

#mpb_1 = MonstroHeroiBatalhas(heroi_id = 4, monstro_id = 1, batalha_id = 1)
#mpb_2 = MonstroHeroiBatalhas(heroi_id = 1, monstro_id = 2, batalha_id = 2)
#mpb_3 = MonstroHeroiBatalhas(heroi_id = 2, monstro_id = 5, batalha_id = 3)
#mpb_4 = MonstroHeroiBatalhas(heroi_id = 4, monstro_id = 5, batalha_id = 4)
#mpb_5 = MonstroHeroiBatalhas(heroi_id = 1, monstro_id = 3, batalha_id = 5)
#mpb_6 = MonstroHeroiBatalhas(heroi_id = 2, monstro_id = 4, batalha_id = 6)


