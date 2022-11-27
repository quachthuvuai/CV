import streamlit as st
from PIL import Image
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Quach Thu Vu"
PAGE_ICON = ":wave:"
NAME = "Quach Thu Vu - Resume"
DESCRIPTION = """
`CAREER OBJECTIVE:` 

Pursue a successful career in Petroleum Geoscience.
"""
EMAIL = "quachthuvu@gmail.com"


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# # Header 
# st.write('''
# # QUACH THU VU
# '''
# '''
# ##### *Resume* 
# ''')

# image = Image.open('assets/profile-pic.png')
# st.image(image, width=150)


# --- HERO SECTION ---
use_container_width=True
col1, col2 = st.columns(([2.5,1]))

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

with col2:
    st.image(profile_pic, width=200)



#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# sidebar for navigation
with st.sidebar: 
  st.markdown("""
  <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color:#b6dcfa;">
    <a class="navbar-brand" href="/">QUACH THU VU</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="true" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">        
          <a class="nav-link" href="#summary">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#education">Education</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#work-experience">Work Experience</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#competency-skills">Competency and Skills</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#references">References</a>
        </li>
      </ul>
    </div>
  </nav>
  """, unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Summary
''')
st.info('''
A senior geomodeller with 15 years of experience in exploration and development geology. 
- Solid knowledge in geology, geophysics, petrophysics and reservoir engineering and their integration into geological modeling 
- Experienced in new field development, production, exploration, and appraisal 
- Advanced working competencies with complex geological modeling.  
- Self-taught, enthusiastic in the application of data science, deploy machine learning for Geoscience
''')

#####################
st.markdown('''
## Education
''')

txt('**Master of Engineering** (Applied Petroleum Geology), *Ho Chi Minh University of Technology, Vietnam*','2009-2011')

txt('**Bachelor of Engineering** (Geology), *Ho Chi Minh University of Technology, Vietnam*','2002-2007')

#####################
st.markdown('''
## Work Experience
''')

txt('**Senior Geomodeller/Geoscientist**, `JX Nippon Oil & Gas Exploration (Malaysia) Ltd`','`2014-Present`')
st.markdown('''
In charge of G&G evaluation for block SK10 (West Baram province), block SK08 (Central Luconia province), offshore Sarawak, Malaysia & other exploration blocks.                                                   (JX Nippon Oil & Gas Exploration Malaysia Ltd)
-	Lead the geological evaluation and modeling for Helang, Layang and Beryl oil and gas fields (multiple stacked sands with several perched water tables), block SK10, Central Luconia geological province, offshore Sarawak, Malaysia. 
-	Lead seismic interpretation, advanced velocity modeling by integrated seismic velocity and well velocity to correct fault shadow issue, structural uncertainty assessment via multiple velocity methods.
-	Performed core review, quantitative analysis core data, poro-perm transform by HFU, saturation height function from core derived J-function.
-	Generated high resolution stratigraphic correlation with integration of seismic stratigraphic interpretation, detail work on sequence stratigraphic framework for cycle V to cycle VII and depositional environment for Helang, Layang and Beryl fields which was used in full field review study.  
-	Geological conceptual well design for exploration and development wells. Supported geological operating and monitoring for Layang drilling activities and post drilling geological update.
-	Performed regional evaluation of carbonate platform and pinnacle in Central Luconia geological province, offshore Sarawak, Malaysia. Established exploration criteria & guidance for carbonate prospect in Central Luconia province.
-	Lang Lebah prospect evaluation, block SK410B, Central Luconia geological province, offshore Sarawak, Malaysia. Geological risk assessment for HC accommodation, abnormal pressure assessment & pore pressure prediction. 
-	Helang Deep prospect evaluation, block SK10, West Baram geological province, offshore Sarawak, Malaysia. Geological risk assessment for HC accommodation, overpressure assessment & porosity preservation prediction through seismic data. 
-	Matoa prospect evaluation, block SK10, West Baram geological province, offshore Sarawak, Malaysia. Geological evaluation of combination trap type, geological risk assessment and resource assessment.
-	Provided technical support and guidance to team involved in building Beryl geological model and other related G&G work.
-	Reviewer of JX Nippon in JV's with Shell for block SK08 PSC, Central Luconia province, offshore Sarawak, Malaysia.
-	Milestone reviews of Cili Padi gas field, Jintan gas field & Serai gas field 
-	Carried out field review for JX Nippon internal studies which included Cili Padi gas field, Saderi gas field and Serai gas field in comparison with Shell's studies
''')

txt('**Senior Reservoir Geologist**, `PETRONAS Carigali Vietnam Limited (PCVL)`','`2011-2014`')
st.markdown('''
In charge of G&G evaluation for block 01&02 and block 102&106, offshore Vietnam (PETRONAS Carigali Vietnam Limited)
-	Geological evaluation, well planning, geological modeling, RAR & FDP study for Thai Binh gas field, Blocks 102 & 106, Song Hong Basin.
-	Fracture characterization, seismic analysis & geological concept for carbonate fractured modeling. Performed ODP, EDP study and well planning for Ham Rong oil field, Blocks 102 & 106, Song Hong Basin.
-	Geological evaluation, seismic interpretation, velocity modeling, seismic attributes & geobody extraction for depositional concept (DOE) for geological modeling, well planning, FFR study for Pearl field, Blocks 01 & 02, Cuu Long Basin. 
-	Geological modeling for Diamond basement field, Blocks 01 & 02, Cuu Long Basin
-	Reviewer of Petronas in JV's with PVEP on technical review, well proposals, TCM & MCM 
-	Gau Chua, Ca Cho oil field, Blocks 10 & 11, Nam Con Son Basin
-	Thang Long, Dong Do oil field, Blocks 01/97 & 02/97, Cuu Long Basin
''')

txt('**Geomodeller/Geoscientist**, `Roxar (Malaysia) Sdn. Bhd`','`2010-2011`')
st.markdown('''
Reservoir characterization & geological modeling consulting projects (ROXAR)
-	Core description, depositional environment and reservoir architecture interpretation for Dai Nguyet field, Blocks 05-1b & 05-1c, Nam Con Son Basin, Vietnam
-	Full field geological modeling for Nam Rong-Doi Moi fractured basement oil field, Blocks 09-1& 09-3, Cuu Long Basin, Vietnam (for FDP update study).
-	Core description, depositional environment, reservoir architecture interpretation and full field geological modeling for Te Giac Trang oil field, Blocks 16.1, Cuu Long Basin, Vietnam.
-	Member of consulting team of Baram EOR project for Petronas Carigali (more than 1 year), full field geological modeling of a cluster of complex structure, multiple reservoirs (4000+ OWC & GOC, 300+ wells), West Baram province, offshore Sarawak, Malaysia.
-	Full field geological modeling for Lac Da Nau fractured basement oil field (Phu Quy POC), Cuu Long Basin, Vietnam.
-	Full field geological modeling for Anding fractured metamorphic basement oil field (Petronas Carigali), Malay Basin, Malaysia.
-	Full field geological modeling for Ruby fractured basement oil field (Petronas Carigali) Blocks 01&02, Cuu Long Basin, Vietnam
''')
txt('**Geomodeller/Geoscientist**, `Roxar Vietnam Ltd`','`2007-2010`')
st.markdown('''
-	Assisted in updating geological model and resource assessment (Miocene, Oligocene sandstone reservoir & fractured Basement reservoir) of Bach Ho field for Vietsovpetrol, Vietnam.
-	Assisted in building geological model (Miocene sandstone reservoir) of Dong Nam Rong oil field for Vietsovpetro, Vietnam.
-	Assisted in building geological model (Miocene sandstone reservoir) of Rong field for Vietsovpetrol, Vietnam
-	Built structural model (multiple stack sand & complex structure) of Ca Voi, Kim Long and Ac Quy gas field (Malay-Tho Chu basin) for Vietnam Petroleum Institute (VPI) 
-	Built structural model (multiple stacked sand & carbonate with complex structures) of Dai Hung oil field (Nam Con Son basin) for PVEP-Dai Hung
-	Assisted in reviewing geological model of Cendor field (block PM304, Malay basin) for PVEP 
-	Assisted in building complex structural model of Lagomedio oil field (carbonate reservoir, Venezuela) for PVEP
-	Assisted in building Su Tu Den geological model (B10 & C30 reservoir), Cuu Long JOC, Vietnam
-	Assisted in updating geological model (F sequence, Oligocene) for Su Tu Trang gas field (Cuu Long basin) for Cuu Long JOC
-	Assisted in building geological model (carbonate reservoir) for Lan Tay & Lan Do gas field (Nam Con Son basin) for BP Vietnam.
''')

#####################
st.markdown('''
## Competency and Skills
''')

st.markdown('''
`Expertise`
- Geological reservoir modeling of siliciclastic reservoir, carbonate reservoir and fractured reservoirs.  Expertise in fractured reservoir, complex structural and stratigraphy clastic reservoir and carbonate reservoirs modeling with full uncertainty/sensitivity assessments and model selection via assisted streamline simulation.
''')
st.markdown('''
`Advanced`
- Structural geology and fracture characterization in fractured basement & carbonate
-	Sedimentology, sequence stratigraphy and reservoir architecture prediction with integrating of core interpretation, log responses, seismic reflection & production performance for both sandstone and carbonate reservoirs in the understanding of regional geological setting. Exposure in both clastic and carbonate environment and reservoir analog to geological modeling
-	Seismic interpretation, mapping, attributes generation, advanced velocity modeling and time-depth conversion. Integration of QI result into reservoir model
-	Geological analysis with incorporating of well data (core and log data), production data, seismic and regional geology understanding
-	Petroleum geology, prospect generation and evaluation with geological risking and volumetric estimation
-	Sedimentary petrology, facies analysis, rock typing, reservoir quality prediction
-	Resource assessment for undiscovered prospect/ discovered field follow SPE/Petronas/Petrovietnam resource classification
-	Technical studies for RAR, ODP, ADP, FDP and FFR
-	Technical preparation for Peer review, TCM, MCM and other technical workshops to partners & host authority
-	Knowledge in regional geological setting of Central Luconia province, Baram Province and Malay basin, Cuu Long basin, Nam Con Son Basin and Song Hong basin.
''')
st.markdown('''
`Skill `
-	Fault seal analysis
-	Experience in core analysis, capillary pressure, core and log derived saturation height function, subsurface fluids and pressures analysis
-	Experience in field development and reservoir management planning. Carry out data acquisition plan, geological evaluation
-	Well planning for development, exploration and appraisal wells, elaboration of well proposals, monitoring and update while drilling, final geological well report and post drilling review
-	Experience in integrating PLT, DST, MDT, PVT data to enhance geological evaluation and modeling. 
-	Strong background in reservoir engineering, understand fluid properties, rock properties, rock-fluid properties, well strategy and reservoir simulation process. Advise the interaction between static and dynamic modeling to obtain best history matching and prediction.
''')
st.markdown('''
`Knowledge  `
-	4D seismic, petroleum economic, drilling, well completion & production facilities.
''')

st.markdown('''
`programming and database management skills`
- Geoscience softwares:  `Petrel`, `RMS`, `GeoTeric`, `Paleoscan`, `GeoX`, `T-navigator`, `Techlog`, `Attribute Studio`
- Programming, Data science, Machine Learning, Deep Learning, web application:, `Python`, `R`
- Database: `SQL`
''')

st.markdown('''
`Attitude and Ethics`
- Good interpersonal and communication skills
- Integrity, transparency, responsibility, leadership, self-motivation & motivate other with a commitment to team success
- Good at analytical thinking, problem solving capability, system & strategic planning and prioritize the work to obtain project delivery
- Work with passion, keen on taking challenges and different assignment
- Proactive in continuous learning, creativity and applying new ideas and skills
- Knowledge sharing and mentoring skills to junior staff.
''')

#####################
st.markdown('''
## References
''')
txt4('1. DOAN HONG THANG', 'Principal Geologist-Leap Energy, Malaysia', 'email: thangdh73@gmail.com')
txt4('2. Do THI LOAN ', 'Senior Reservoir Engineer-Premier Oil, Vietnam', 'email: dtloan_tb@yahoo.com')

