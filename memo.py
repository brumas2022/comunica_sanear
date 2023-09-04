import streamlit as st



st.set_page_config(page_title="Memorando")

def inserir():
  pass
  
st.header("ACESSE UM NUMERO PARA O SEU MEMORANDO")

a0 = st.text_input("Entre com seu nome")

a1 = st.selectbox("SELECIONE O ASSUNTO DO MEMORANDO", ("AQUISICAO", "ORDEM DE SERVIÇO", "AUTORIZAÇÃO DE FORNECIMENTO", "ABERTURA DE PROCESSO LICITATORIO"))


if a1=="AQUISICAO":
  st.image("https://lh3.googleusercontent.com/pw/AIL4fc8um2_bf-evsXVyabYfkgZ4PJFG9h_yCgJpvjiee9D1WvW10hql_u4AkUT7zrKHyBTiOcS90oSBI1o2wfuQRdVJ1V4iKR4uOC3bbpSCckJ41M_sPe-ZaFZYJoW6FilYuLuMgWsnDRj54cSq2H7A4ShWhBEpYPCDxKm1gVIelZCoTfd865ZHvVcU6l2QZLRWXy2DtEZ2aJQaMJGjnfcRBIitJ8DnESt5WVplS8d3kZ7kmpMdRKPVJL7XT3JV4lI6WvfxsClxApup4gl_W1fwV9ylP1i3oxBHJQyxzfyCD3EE-9gVQwy_tRY9wWOdnjK0TdEqS0uQ5wk2U9vRF45d14X2-3HqRj4dL6uxMq2GpVFguiwbl0UrzmE4CM9S35O8fqndHSOmrouTNx56HdN5JCh208UctJurU7bkoyrDz3fM-As7ZllR1nPnR65CNxA0Kda0Glxas6-vGbrjoW-ZJv29R0fTwGAZtYbfTtmdB6rBZwGkGhb-75nDeMaub1WQ-7jmUGFyoXXL6WMm7YG_b5k8ac5sek8HAYMPRfhC5f0UcC_Odq72qiimeLOu3P-jmD9R5e_rCX_6Ez30vIGKvIyaNfVCtb7yW1NYon76EFy8VQrvZ2cPeVyrslEBCZ1jI6NYETkZSEP2aC6c54ZbqdL2cQHjjTSyZToTpcS-Aj_DRvRfNe6SPpaQg2TaqyybTcStUUO-HQkEwNs3VK2EQgBvupH9tgph8qGjoGXlDacIhbEf-UVvddvE7fZXJTFGXAFHvwoSMLssdVKw3J0D4bWLL4dU3ul0dh9qLdvPd3F95cfh5UGCGyUsjGnkNz7TP6I-7AgyDE3_pv1dWsZQabmxgJ06BM1xUbvnHxE-P4h32Wli_gn38XXLDWmxCsfKMuQLLBHaSJyZxhE=w666-h316-s-no?authuser=0")
elif a1=="ORDEM DE SERVIÇO":
  st.image("https://lh3.googleusercontent.com/pw/AIL4fc8tQMTd5Q2JPnrFYRmx-E4ADpJ0W3rQ_BuCjxKX1vB5W3ZAdfosDpRitCEInj1YUSQSUxY1sTjMeckv5GaVDImj7FhEqFMxSZguHoueHduiGHoG06ETRi6Q044qNMpcQrnXQ6uT306ExgCPxF7Ie07AE6zuqZCKUIY74elzvaoR4Kz9NEYzxRXytLhrH9K4fmturJHiAAUfDJkTz6UfJCfsmewd7BwUPznlp-v1tBnGH0GljL6M3oz2iqlk8RqtI76afx621HkksO91blYWTS8SpX-hrDolzTPhuEQ3YtX_D4RmudAca-o3nTOmKba_-SHeuDQg7kKBwD6S2ipygrtkh_fft0kZLWosAzQg7mfHumkZuR7eEJFg6554Y0wzGwNQt7pChj2xojd4oycea2BKst64EoLmgDV1PLwd2mrWpuyeH19Evk7Q0Lk_jCYL9sZQ_8heHxMMRCFn49wc_0dHzXIOsfniP3r4SSCHiGH7Qmzdi7c8qVoydTyOAnyycA2aBHy1DYakrYkvi5Rb0GloCFdujnuEApNdx5dPkHIiwh4pmeH0j2dGfGLtIvJojxM9n3q3v2-Zggpc5q85EJDy4j_CWes5b6XkMCVoJlR5T2ypclEUS-sI5tO70UIxg-TXGrnkTtoGlluF6ZkYB16Vzn97BDq8uSznjKplU2d5dxhRVlca1ac5wzyxZqQVZkt6U30MJVw6ZOS4Wn2BV5caWi1UDTVZrQ7t1JtU3Fb2UhBWrYNhHkNNrLoJ_o7UipE70_WeUZwun6Pm3rcUVqPyuXacBQQzfbnRXCSe5BjFXCJffjrV_UXS-8zm68gIqRa25vR_sUI2Mm9rdwxFX_vb45nmQIho_t8MhhuTV1nG47sXDc4pwGS6agJRxkzEw6QdTdPHwU0zrMc=w219-h463-s-no?authuser=0")
elif a1=="AUTORIZAÇÃO DE FORNECIMENTO":
       try:
          connection = psycopg2.connect(
               host='db.hdhvkseneldllvnlvpgc.supabase.co',
               user='postgres',
               password='Gh2T6ioe2h2b7UD4',
               database='postgres',
               port='5432'
          )
          st.write("conexao exitosa")
          ##cursor = connection.cursor()


          ##comando = """SELECT * FROM saneamento.registro_grandezas WHERE id_amb = 40 and cd_classe = 10  ORDER BY id DESC"""

          ##cursor.execute(comando)
          ##resultado = cursor.fetchone()
          ##print(resultado)
          ##print(entrada + " acessou o bot")
          ##grava(mensagem)
     except Exception as ex:
          print(ex)

st.header(a0)
st.write("A opção selecionado foi", a1)
st.write("O numero do seu memorando é:")
                                                       
st.header("554")

st.write("Melhorando este codigo")
st.write('Mais uma dose de rock')

                                                       
                                                       
