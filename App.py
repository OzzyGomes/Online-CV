from pathlib import Path
from platform import platform

import streamlit as st
from PIL import Image

# PATH SETTINGS #
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.PDF"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
page_title = "Digital CV | Ozzy Gomes"
page_icon = ":wave:"
name = "Ozzy Gomes"
description = '''Apaixonado por aprender novas tecnologias e conhecimento em 
geral, Analista de Dados perceptivo e lógico se comunica bem com
profissionais técnicos e usuários finais para identificar e traduzir os
requisitos de negócios. Experiente na condução da precisão e
integridade dos dados para exceder os padrões de qualidade. Cria
e lidera equipes de profissionais talentosos para desenvolver
soluções de processo valiosas e atender aos objetivos de negócios.
'''
email = "ozzygomes@outlook.com"

social_media = {
    "LinkedIn" : "https://linkedin.com/in/ozeasgomes",
    "GitHub" : "https://github.com/OzzyGomes"
}

projects = {
    '🏆 Sales Dashboard with streamlit' : 'https://github.com/OzzyGomes/Dashboard-with-streamlit',
    '🏆 Online Payments Fraud Detection ML Python' : 'https://github.com/OzzyGomes/Online-Payments-Fraud-Detection-ML-Python',
    '🏆 Cadastro Pessoas com Django' : 'https://github.com/OzzyGomes/cadastro-pessoas-django',
    '🏆 YOLO Object Detection Using Opencv with Python' : 'https://github.com/OzzyGomes/YOLO-object-detection-using-Opencv-with-Python',
    '🏆 Renomear PDFs' : 'https://github.com/OzzyGomes/Renomear-PDFs'
}

st.set_page_config(page_title=page_title, page_icon=page_icon)


#--- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

#--- HERO SECTION ---

col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label=' 📄 Download Resume',
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", email)

# --- Social Links ---
st.write('#')
cols = st.columns(len(social_media))

for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f'[{platform}]({link})')

# --- Experience & Qualifications 
st.write('#')
st.subheader('Education')
st.write('''
2015-01 -
2019-12
| **Bachelor of Science: Industrial
Engineering**
- Centro Universitário Fieo - UNIFIEO - Osasco, São Paulo, Brazil
''')

st.subheader('Qualifications')

st.write('''
- 2022-05 | Microsoft Power BI Para Data Science, Data Science Academy

- 2022-02 | Complete SQL Mastery, 2022-02 Code With Mosh
- 2021-06 | Python for Data Science, LinkedIn Learning
- 2020-09 | Data Visualization , Kaggle
- 2020-09 | Pandas , Kaggle

- 2021-06 | Excel 2019: Advanced Formulas and Functions, LinkedIn Learning

- 2021-05 | Big Data Fundamentals: Techniques and Concepts, LinkedIn Learning

- 2021-05 | Data Science Fundamentals: Data Mining, LinkedIn Learning

- 2021-04 | Statistical Fundamentals: Part 1, LinkedIn Learning
- 2021-09 | Intro to Machine Learning, Kaggle
''')

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, VBA, R
- 📊 Data Visulization: PowerBi, MS Excel, Plotly
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MySQL and SQL Server
"""
)

st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Data Analyst | Stefanini, São Paulo**")
st.write("11/2021 - Current")
st.write(
    """
- ► Trabalhando com Python e bibliotecas para trabalhar com dados como: Numpy, Pandas, MatPlotLib, Plotly e Seaborn.
- ► Pesquisou e resolveu problemas relacionados à integridade do fluxo de dados em bancos de dados.
- ► Identificou e documentou regras de negócios detalhadas e casos de uso com base na análise de requisitos.
- ► Padrões de dados extraídos e interpretados para traduzir descobertas em resultados acionáveis.
- ► Garantia de segurança e confidencialidade de documentos e dados dentro da área de responsabilidade.
- ► Desenvolvimento de tables, Views, Stored Procedures e Functions usando SQL.
- ► Algoritioms para a conversão de imagens em texto para automação de processos.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Ecommerce Data Analyst | Chopp Brahma Express, São Paulo**")
st.write("11/2020 - 11/2021")
st.write(
    """
- ► Analisando grandes quantidades de dados com Python, Excel e Power BI
- ► VTEX, Google Analytics, Cadastro de Produtos, Configuração de Preços e Promoções, Plataformas de Transações Bancárias.
- ► Colaborou com os membros da equipe para alcançar os resultados desejados.
- ► Estoque recebido e processado em sistema de gestão de estoque.
- ► Impulsionou melhorias operacionais através de dados que resultaram em economia e melhores margens de lucro.
"""
)

# --- Projects and Links
st.write('#')
st.subheader('Projects & Accomplishment')
st.write('---')
for project, link in projects.items():
    st.write(f'[{project}]({link})')