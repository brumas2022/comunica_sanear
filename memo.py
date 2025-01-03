import streamlit as st
import psycopg2
import pandas as pd

st.set_page_config(page_title="Memorando ALTERADO", layout="wide")

def inserir():
  pass

##st.image("https://static.preparaenem.com/2023/05/ilustracao-de-uma-folha-de-papel-escrita-como-representacao-do-memorando.jpg")  
st.sidebar.image("blog-aplex-seguranca-documentos-imagens.jpeg", width=300)
st.header("ACESSE UM NUMERO DE MEMORANDO")

with st.form(key="novo_memorando"):
  
  setor1 = st.sidebar.radio("Selecione a diretoria :", ("GERAL", "ALMOXARIFADO", "TECNICA", "MANUTENCAO", "JURIDICO"))

  a1 = st.text_input("QUAL O ASSUNTO DO MEMORANDO ?")

  a0 = st.text_input("DIGITE SEU NOME COMPLETO")

  enviar = st.form_submit_button("CONFIRME")
  if enviar:
      try:
          connection = psycopg2.connect(
               host='aws-0-sa-east-1.pooler.supabase.com',
               user='postgres.hdhvkseneldllvnlvpgc',
               password='Hoje#estamos#fortes#como#geleia',
               database='postgres',
               port='5432'

            
               #host='db.hdhvkseneldllvnlvpgc.supabase.co',
               #user='postgres',
               #password='Hoje#estamos#fortes#como#geleia',
               #database='postgres',
               #port='5432'
          )
          ## st.write("conexao exitosa")
          cursor = connection.cursor()
     
          if setor1=="GERAL":
             comando = f"""INSERT INTO nmemodirgeral(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor, assunto FROM nmemodirgeral ORDER BY id DESC""" 
             cursor.execute(comando1)
             resposta = cursor.fetchall()
             cursor.execute(comando1)
             resultado = cursor.fetchone()
            
          elif setor1=="ALMOXARIFADO":
             comando = f"""INSERT INTO nmemoalmox(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor, assunto FROM nmemoalmox ORDER BY id DESC"""
             cursor.execute(comando1)
             resposta = cursor.fetchall()
             cursor.execute(comando1)
             resultado = cursor.fetchone()

          elif setor1=="TECNICA":
             comando = f"""INSERT INTO nmemodirtec(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor, assunto FROM nmemodirtec ORDER BY id DESC""" 
             cursor.execute(comando1)
             resposta = cursor.fetchall()
             cursor.execute(comando1)
             resultado = cursor.fetchone()

          elif setor1=="MANUTENCAO":
             comando = f"""INSERT INTO nmemodirman(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor, assunto FROM nmemodirman ORDER BY id DESC""" 
             cursor.execute(comando1)
             resposta = cursor.fetchall()
             cursor.execute(comando1)
             resultado = cursor.fetchone()
        

          ##comando = """SELECT id, nome_servidor FROM nmemodirgeral ORDER BY id DESC"""
          ##cursor.execute(comando)
          ##resultado = cursor.fetchone()

          st.markdown("Sr. "+resultado[1])
          
          st.markdown("Por favor, anote o numero do memorando :  ")
          
          st.title(str(resultado[0]))

          st.write("Veja quem solicitou os ultimos memorandos e o respectivo assunto")
          df = pd.DataFrame(resposta)
        
          st.dataframe(df)
          ##print(entrada + " acessou o bot")
          ##grava(mensagem)
      except Exception as ex:
          st.write(ex)

                                                       
                                                       
