from pathlib import Path

import streamlit as st
from PIL import Image
from dateparser.data.date_translation_data import to

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "CV.pdf"



# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Akash Deep Yadav"
PAGE_ICON = ":wave:"
NAME = "Akash Deep Yadav"
DESCRIPTION = """
Tech Enthusiast.
"""
EMAIL = "Akashdeepyadavji@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/akash-deep-yadav-615a21183/",
    "GitHub": "https://github.com/AkashDeepYadavji",
   
}
PROJECTS = {
    "🏆 Android Malware Attacks And Its Prevention -Researched on vulnerabilities and Malware Attacks And Preventions" : "#",
    "🏆 CryptoDashboard - Displaying Real Time Values of Cryptocurrencies using Web Scrapping ": "https://github.com/AkashDeepYadavji/CryptoDashboard/",
    "🏆 Movie Recommender System -Recommended movies on basis of a user previous movies watched": "https://github.com/AkashDeepYadavji/Movie-Recommender",

}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()



# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")


with col1:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python,C++,MatLab
- 📊 Data Visulization: MS Excel
- 📚 Modeling: Logistic regression, linear regression, decision trees
- 🗄️ Databases: MySQL
-    Cloud: Amazon Web Services


"""
)

st.write('\n')
st.subheader("Education")
st.write("---")

# --- JOB 1
st.write( "📚","**Birla Institute of Technology, Mesra **")
st.write("08/2021 - Present |   Masters in Computer Applications")
st.write(
    """
- ► Sgpa: 8.10
"""
)

st.write( "📚","**Vivekananda Institute Of Professional Studies**")
st.write("08/2017 - 10/2020  |   Bachelors in Computer Applications")
st.write(
    """
- ► Percentage: 70.90%
"""
)

st.write( "📚","**Vidya Bharti School **")
st.write("04/2015 - 04/2016  |   All India Senior School Certificate Examination")
st.write(
    """
- ► Percentage: 56.16%
"""
)
st.write( "📚","**Ryan International School **")
st.write("04/2013 - 04/2014  |   Secondary School Examination Certificate")
st.write(
    """
- ► CGPA: 7.0
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Team Member DX | FIS Global Business Solutions**")
st.write("12/2020 - 08/2021")
st.write(
    """
- ► Worked With Vodafone UK 
- ►  Interacted And Handled  Customers With the Technical Difficulties
"""
)

st.write('\n')
st.subheader("Roles and Responsibility")
st.write(
    """
- ✔️ Event Organiser(YPSOMED SELFCARE SOLUTIONS) (03/2018 - 03/2018)
- ✔️Event Organiser(Bharat Uday Foundation , Sewa Bharat NGO , 
Youth For Sewa Organization , ITOWE
Development Foundation) (01/2019 - 01/2019)
"""
)
st.write('\n')
st.subheader("Research Paper")
st.write("---")


st.write( "**Blockchain AR (Evolution)**")
st.write("(05/2018 - 05/2018)")
st.write(
    """
- ► Presented A Research paper at Information security Risks - 
Techno Legal Management (TeLMISR - 2018) | International Conference - TeLMISR- 2018
""")
st.write('\n')
st.subheader("Certifications")
st.write(
    """- ✔️National Students Convention 2018
Spilled Ink , Tongue-Tied , Abhivyakti Event Was Organized In
Vivekananda Institute of Professional Studies
- ✔️Vivekananda Club - The CSR Society
The Certificate Is Awarded For the Active Participation in the Social
Welfare Activities Organized By The CSR Society.

- ✔️British Council Spoken English

Spoken English Upper Intermediate Module 2 Is a Course Organized By
the British Council Of India Which Educates the Student to reach the
Global Standard in Spoken English And Help the Student to Prepare for
Group Discussions and Public Speaking.
- ✔️Security Analyst By Microsoft
Aggregate: 73.0 / 100.0 Subjects: Security Fundamentals ( 73.0 / 100.0 )
Key Skills: Ethical Hacking
"""

)





# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
