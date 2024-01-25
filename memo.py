import streamlit as st
import psycopg2



st.set_page_config(page_title="Memorando")

def inserir():
  pass

st.image("https://static.preparaenem.com/2023/05/ilustracao-de-uma-folha-de-papel-escrita-como-representacao-do-memorando.jpg")  
st.header("ACESSE UM NUMERO DE MEMORANDO")

with st.form(key="novo_memorando"):
  a0 = st.text_input("DIGITE SEU NOME COMPLETO")
  setor1 = st.radio("Selecione a diretoria :", ("GERAL", "ADMINISTRATIVA", "TECNICA", "MANUTENCAO", "JURIDICO"))
  

  a1 = st.selectbox("SELECIONE O ASSUNTO DO MEMORANDO", ("AQUISICAO", "ORDEM DE SERVIÇO", "AUTORIZAÇÃO DE FORNECIMENTO", "ABERTURA DE PROCESSO LICITATORIO"))

  enviar = st.form_submit_button("CONFIRME")
  if enviar:
      try:
          connection = psycopg2.connect(
               host='db.hdhvkseneldllvnlvpgc.supabase.co',
               user='postgres',
               password='Hoje#estamos#fortes#como#geleia',
               database='postgres',
               port='5432'
          )
          ## st.write("conexao exitosa")
          cursor = connection.cursor()
     

          comando = f"""INSERT INTO nmemo(nome, assunto, setor) VALUES ('{a0}','{a1}','{setor1}')"""
          cursor.execute(comando)
          connection.commit()


          comando = """SELECT id, nome FROM nmemo ORDER BY id DESC"""

          cursor.execute(comando)
          resultado = cursor.fetchone()

          st.markdown("Sr. "+resultado[1])
          st.write(str(resultado[1]))
          st.write("Por favor, anote o numero do memorando :  ")
          
          st.title(str(resultado[0]))
          ##print(entrada + " acessou o bot")
          ##grava(mensagem)
      except Exception as ex:
          st.write(ex)

                                                       
                                                       
