import streamlit as st
import psycopg2



st.set_page_config(page_title="Memorando ALTERADO")

def inserir():
  pass

##st.image("https://static.preparaenem.com/2023/05/ilustracao-de-uma-folha-de-papel-escrita-como-representacao-do-memorando.jpg")  
st.image("blog-aplex-seguranca-documentos-imagens.jpeg")
st.header("ACESSE UM NUMERO DE MEMORANDO")

with st.form(key="novo_memorando"):
  a0 = st.text_input("DIGITE SEU NOME COMPLETO")
  setor1 = st.sidebar.radio("Selecione a diretoria :", ("GERAL", "ADMINISTRATIVA", "TECNICA", "MANUTENCAO", "JURIDICO"))

  a0 = st.text_input("DIGITE SEU NOME COMPLETO")

  a1 = st.radio("SELECIONE O ASSUNTO DO MEMORANDO", ("AQUISICAO", "ORDEM DE SERVIÇO", "AUTORIZAÇÃO DE FORNECIMENTO", "ABERTURA DE PROCESSO LICITATORIO", "OUTROS"))

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
             comando1 = """SELECT id, nome_servidor FROM nmemodirgeral ORDER BY id DESC""" 
             cursor.execute(comando1)
             resultado = cursor.fetchone()
            
          elif setor1=="ADMINISTRATIVA":
             comando = f"""INSERT INTO nmemodiradm(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor FROM nmemodiradm ORDER BY id DESC""" 
             cursor.execute(comando1)
             resultado = cursor.fetchone()

          elif setor1=="TECNICA":
             comando = f"""INSERT INTO nmemodirtec(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor FROM nmemodirtec ORDER BY id DESC""" 
             cursor.execute(comando1)
             resultado = cursor.fetchone()

          elif setor1=="MANUTENCAO":
             comando = f"""INSERT INTO nmemodirman(nome_servidor, assunto) VALUES ('{a0}','{a1}')"""
             cursor.execute(comando)
             connection.commit()
             comando1 = """SELECT id, nome_servidor FROM nmemodirman ORDER BY id DESC""" 
             cursor.execute(comando1)
             resultado = cursor.fetchone()
        

          ##comando = """SELECT id, nome_servidor FROM nmemodirgeral ORDER BY id DESC"""
          ##cursor.execute(comando)
          ##resultado = cursor.fetchone()

          st.markdown("Sr. "+resultado[1])
          
          st.markdown("Por favor, anote o numero do memorando :  ")
          
          st.title(str(resultado[0]))
          ##print(entrada + " acessou o bot")
          ##grava(mensagem)
      except Exception as ex:
          st.write(ex)

                                                       
                                                       
