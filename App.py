from pathlib import Path

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
Description = '''Apaixonado por aprender novas tecnologias e conhecimento em
geral, Analista de Dados perceptivo e lógico se comunica bem com
profissionais técnicos e usuários finais para identificar e traduzir os
requisitos de negócios. Experiente na condução da precisão e
integridade dos dados para exceder os padrões de qualidade. Cria
e lidera equipes de profissionais talentosos para desenvolver
soluções de processo valiosas e atender aos objetivos de negócios.
'''
email = "ozzygomes@outlook.com"

social_media = {
    "LinkedIn" : "linkedin.com/in/ozeasgomes",
    "GitHub" : "https://github.com/OzzyGomes"
}

projects = {
    'Sales Dashboard with streamlit' : 'https://github.com/OzzyGomes/Dashboard-with-streamlit',
    'Online Payments Fraud Detection ML Python' : 'https://github.com/OzzyGomes/Online-Payments-Fraud-Detection-ML-Python',
    'Cadastro Pessoas com Django' : 'https://github.com/OzzyGomes/cadastro-pessoas-django',
    'YOLO Object Detection Using Opencv with Python' : 'https://github.com/OzzyGomes/YOLO-object-detection-using-Opencv-with-Python',
    'Renomear PDFs' : 'https://github.com/OzzyGomes/Renomear-PDFs'
}

