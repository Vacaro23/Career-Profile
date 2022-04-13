import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt 
 
##########


st.set_page_config(
    page_title= "Dale",
    page_icon= "picture_me.png",
    layout="wide",
    initial_sidebar_state="auto",
)


# my_page = st.sidebar.radio('Page Navigation', ['Career Profile'])


# if my_page == 'Career Profile':
    #####################
    # Header 
st.title('''
John Dale L. Vacaro
#### FIA, CLSSYB, CAEA, CFMP
###### *Career Profile* 
''')

image = Image.open('picture_me.png')
st.image(image, width=250)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- An Inquisitive Leader focused on Data, Innovation and Technology.
- Experienced Data Professional in Financial Services and Consulting Industry specializing Financial Markets, and Revenue Data.
- Exposed in Customer Relationship Management, Sales Operations, Content Operations, Project Management, Knowledge Management, Data Modeling, Data & Quality Management, Data Analysis & Insighting, and Data Visualization & Reporting.
- Expert in streamlining Financial Markets and Revenue data to deliver its best quality to customers and help Senior Leaders generate Strategic Data-Driven Decisions through Research Methods, Exploratory Data Analysis, and Machine Learning Algorithms.
''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/johndalevacaro/" target="_blank">John Dale Vacaro</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#bootcamps-trainings-courses">L&D</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#projects">Projects</a>
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

def txt5(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

def txt6(a, b):
  col1, col2 = st.columns([2.5,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
    #####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`')
txt3('Data Transformation', '`Advanced Excel`, `Excel VBA`, `Alteryx`, `pandas`, `numpy`, `nltk`')
txt3('Data Visualization', '`AWS Quicksight`,`Tableau`, `PowerBI`, `Google Data Studio`, `Excel`,`matplotlib`, `seaborn`, `bokeh`, `shap & lime`')
txt3('Machine Learning', '`scikit-learn`, `scipy`')
txt3('Web Scraping', '`beautifiulsoup`')
txt3('Process Automation', '`selenium`')
txt3('Model Deployment', '`Streamlit`, `Heroku`')
txt3('Customer Relationship Management', '`Salesforce ServiceCloud`, `Salesforce SalesCloud`')
txt3('Change Management', '`ServiceNOW`')
txt3('Knowledge Management', '`Confluence`,`Sharepoint`')
txt3('Issue Tracking & Project Management', '`JIRA`,`Dataiku`')
txt3('Image Processing', '`ABBYY FlexiCapture`')
txt3('Fundamental Knowledge', '`AWS ML`, `AWS Sagemaker`,`VS Code`,`Gephi`,`Databricks`,`Regular Expression`, `RStudio`')
txt3('2022 Learning Plan', '`DevOps CI/CD`, `AWS Redshift`, `Teradata`, `SAS`, `Microsoft Azure`, `Python Automations`, `Google Cloud Platform`, `Hadoop`, `Spark`')

st.title("")


#####################
st.markdown('''
## Work Experience
''')


txt('`SENIOR ANALYTICS CONSULTANT`',
'2021 - 2022')
txt('Deloitte - Risk Advisory: AU', '')
st.markdown('''
- Pioneered Data Science Team in Deloitte PH - Risk Advisory with other consultants, to create and implement AI solutions to be offered to clients.
    - Constructed a technical framework of Predictive Attrition model for employees with Data Science and Machine Learning Algorithms.
    - Structured a pipeline for Signature Detection using Image Processing and Detection to extract and verified signatures in documents.
    - Contributed to the Voice Detection data gathering in improving Speech Recognition solutions for conduct detection and tagging.
- Lead 2 Australian Projects on Timesheet Digitization of 2 Health Care Companies, in-charge of Data Integrity as Lead Verification Officer:
    - Maintenance of Data Accuracy, Data Completeness, Data Consistency
    - Recognized employees timesheet’s risks and inconsistencies on payout, leaves, and benefits.
- Collaborated smoothly with client stakeholders to define the right business questions with a self-initiated curiosity and with IT Engineers to implement data quality functional services supplementing a detective mindset in every client data.
- Identified risks and data logic issues, creating solutions and use cases in order to exceedingly solve client goals and problems on their data.
- Subject Matter Expert in assessing and generating proposals to the development team to optimize processes and improve efficacies of all members in a project.
     ''')

st.title("")


txt('`BUSINESS OPERATIONS ANALYST`',
'2021 - 2021')
txt('London Stock Exchange Group - Business Operations & Sales Enablement : AMERS', '')
st.markdown('''
- Successfully passed sponsored certification of “Financial Information Associate” (FIA) worth $900 given to Top Outperforming employees.
- Direct Responsible Individual in the performance metric evaluation of 230+ product sellers in the Americas, consistently presented the result to the Head of Sales. Moreover, includes developing seller segmentation in terms of their region, experience, actuals vs quotas & etc.
- Reported to the Head of Sales every month, in summarizing and analyzing monthly business performance trends in terms of Outright, Gross and Net Sales, this includes actual vs quota and the variance, as well as suggesting how and what we can do to improve these numbers.
- Partnered with Head of Enterprise Data Solutions Product and Head of Partners Market along with their Account Directors and Managers to analyze and gain insights, assist, and supervise internal campaigns, reporting analytics, monthly business review and ad-hoc custom reports.
- Developed global data visualization report and dashboard for pipeline management to forecast renewals data for Senior Management.
- Planned sales accelerators to amplify key opportunities, bridged gaps within the sales workflows and to support incentives to excellent sellers.
- Designed new KPI Data Models to assess seller’s performance and Territory Planning Model to align book of business for turn of the year.
- Single Point of Contact that managed and assigned a product seller for new and current clients in Americas respective on their experience and specialist, worked along with Customer Success, Lead Generation and Business Development stakeholders.
- Analyzed sales and retention motions by providing operational guidance to deliver 2021 migrations and strategies, execute revenue synergy pathways and incorporating customer lifecycle framework to key renewals.


''')



st.title("")


txt('`FINANCIAL MARKETS ANALYST II`',
'2021 - 2021')
txt('`FINANCIAL MARKETS ANALYST I`',
'2019 - 2021')
txt('London Stock Exchange Group - Content Operations & Managed Services: EMEA & SEA', '')
st.markdown('''
- Selected as one of the Top 10% Outstanding Employees in the Organization, achieved the highest rating of ‘Leading’ in 2020 Company Year-End Assessment - as a measure of exemplary performance by the following that saved 0.55 FTE:
    - by creation of method of works and documentations,
    - by doing finanical markets data processing and transformation,
    - by stock exchange projects and technical migration
    - by building 15 excel macros initiatives and
    - by generating automation ideations and proposals
- Successfully accomplished remarkable performance with 99% data integrity of my daily productions which consistently gave me the award of  ‘Star of the Month’ or ‘Employee of the Month’, within our team - composed of 8 Analysts and 4 Senior Analysts.
- Successfully planned, supervised and coordinated Financial Markets Master Data (Real-Time Data, Time Series Data, Reference Data) for certain SEA & EMEA markets within the team.
- Conducted database testing, new application releases and migrations for critical data enhancements in an agile environment with no supervision from seniors and received good feedback from Key Strategic Accounts/Clients.
- Performed change management in every projects to improve the transition of the change, collaboration, communication and to create change plans to reduce uncertain issues that avoids client escalations through ServiceNOW
- Point of Contact in raising Information, Service and Retrospective Alerts to inform EMEA and SEA clients on issues and changes on products & services with proper Incident and Recovery Management.
- Challenged status quo of tenured members and influenced them volunteering to new tasks that enhanced adaptability and flexibility for learnings that received zero business critical.
- Implemented business unit wide and team knowledge sharings to increase operations sync, find new ways, and create better collaborations.
- Achieved a 10/10 rating from a customer in Salesforce for providing silver bullets that strengthened customer retention, experience and attrition.
- Identified and pinpointed data inefficiencies and bugs in workstream, boosting team performance metrics and data accuracy by ~49% through development and launching of permanent solutions and reinforcement of automations.

''')

st.title("")

#####################
st.markdown('''
## Bootcamps, Trainings, Courses
''')

txt('`DATA SCIENCE FELLOW`',
'2021 - 2022')
txt('Eskwelabs - Data Science & Machine Learning', '')
st.markdown('''
- Structured Unsupervised Machine Learning Project using 2019 Philippine Electoral Votes land deployed in Streamlit web application.
    - Project Title: An Analysis on Political Spending of 2019 Philippine Senatorial Elections
    - Libraries: Numpy, Pandas, Matplotlib, Seaborn, Sklearn, Scipy 
    - Methods: Data Pre-Processing, EDA, Feature Engineering, KMeans, Silhouettter Score, Hierarchical Clustering, Radar Analysis 
- Worked with a Big Data Credit Card Fraud Project using Supervised Machine Learning techniques, Cloud Infrastructures and Analytics Engine.
    - Project Title: FRAUD-tech Yourself: Eskwebank’s Credit Card Fraud Detection Modeling Project
    - Libraries: Numpy, Pandas, Matplotlib, Seaborn, Sklearn
    - Methods: Data Pre-Processing, EDA, Feature Engineering, Regression, Random Forest, XGBoost, Gradient Boosted Decision Tree, Decision Tree, Metrics Selection, Features Importance, Explainability 
- Created Spotify Recommender Engine using Britney Spears’ Spotify Data in order to strategize in boosting her Streams through Supervised Machine Learning algorithms.
    - Project Title: Hit Me Baby One More Time: Reclaiming the Pop Princess’ Lost Throne
    - Libraries: Numpy, Pandas, Matplotlib, Seaborn, Sklearn, Spotipy, Keyring
    - Methods: Data Pre-Processing, EDA, Feature Engineering, KNN, SVM (linear, poly, radial), Euclidian, Manhattan, Cosine, WebAPI, Classification Algorithm, ROC
- Assembled an NLP Recommender Engine product using Web Scraped Perfume Data to create a product that will feel the perfume based on the user's feelings and emotions.
    - Project Title: Wear Your Memories: Perfume Recommender Engine
    - Libraries: BeautifulSoup, Numpy, Pandas, Matplotlib, Seaborn, Bokeh, Networkx, WordCloud, nltk, gensim, Sklearn, Spacy
    - Methods: Web Scraping, Data Pre-Processing, EDA, Network Analysis, Word Cloud
''')

st.title("")

txt('`DATA SCIENCE TRAINEE`',
'2022 - 2022')
txt('DPhi Tech - Data Science & Machine Learning', '')
st.markdown('''
- Accomplished an NLP Modeling Project that predicts if the News Headlines either Sarcastic or Not Sarcastic.
    - Packages: nltk, numpy, seaborn, matplotlib, pandas, contractions, re, string, PIL, wordcloud, sklearn, collections, textblob
    - Methods: Data Pre-Processing, EDA, Text Pre-Processing, Sentiment Analysis, BagOfWords, Logistic Regression, Gradient Boosted Decision Tree, Decision Tree, Random Forest
- Explainable AI Bootcamp using LIME, SHAP and other tools to increase interpretability and understanding of Machine Learning models while sharing to stakeholders.
''')

st.title("")


txt('`DATA SCIENCE & BUSINESS ANALYTICS INTERN`',
'2022 - 2022')
txt('The Sparks Foundation - Data Science & Machine Learning', '')
st.markdown('''
- Started a Project as a Business Manager, to do an Exploratory Data Analysis on a Retail Business dataset in order to identify Business Dilemma and to raise Profit, based on the given data.
- Created a Decision Tree Modeling Project using Iris Dataset to identify correct classification of Flower based from the given data.
''')

st.title("")


#####################
st.markdown('''
## Education
''')

txt('**Business Administration Major in Financial Management**, *Pamantasan ng Lungsod ng Maynila*, Philippines',
'')
st.markdown('''
- Achievements : Finance Student
    - GPA: `1.63`
    - Dean's Lister  |  Top Finance Achiever
    - National Finalist of Top Outstanding Finance Students of the Philippines
- Organization : Junitor Financial Executives - PLM Chapter
    - Junior Officer
    - Vice President for Publicity and Communication
    - Vice President for External Affairs
''')

st.title("")


#####################
st.markdown('''
## Social Media
''')
txt6('LinkedIn', 'https://www.linkedin.com/in/johndalevacaro/')
txt6('GitHub', 'https://github.com/Vacaro23')

st.title("")


#####################
st.markdown('''
## Projects
''')

txt6('Sarcasm Prediction Modeling','https://github.com/Vacaro23/Projects/blob/main/Sarcasm_Prediction_.ipynb')
st.caption("This Project has been created using News Headlines to predict wether if each news from the dataset is Sarcastic or Not-Sarcastic. The Prediction Modeling might be relevant to All Companies who are relying most of their Decisions on what is happening daily on the Market - knowing which are Truth and False.")

txt6('Breast Cancer Prediction Model with SHAP','https://github.com/Vacaro23/Projects/blob/main/Explainable_AI_.ipynb')
st.caption("A Prediction Modeling with SHAP using the Breast Cancer dataset, the main goal of this project was to have the simplest and most basic explaination of Machine Learning Models in order to make the easiet interpretability while sharing the result to shareholders. This type of interpratiblity enhances stakeholder understanding regarding what is happening and create a direction what are they are representing about.")

txt6('Retail Business EDA','https://github.com/Vacaro23/Projects/blob/main/EDA_Retail_Business_.ipynb')
st.caption("As Business Manager, I need to look for the Business Problems of this Retail Business dataset and create solutions and to make decisions. The situation has been investigated using Top-Down approach; reviewing sales from each region of Americas to Categories and Sub-Category, then validating the Sales, Profit and Discount per State and Cities.")

txt6('Iris Prediction Decision Tree','https://github.com/Vacaro23/Projects/blob/main/Predicion_DecisionTrees_ipynb')
st.caption("Using the Iris dataset, a Prediction Model were created using Decision Tree algorithms in order predict the classification of a flower. This type of a project would be impactful to a company such as Health Care and E-Commerce that would like to predict the classification of a certain disease/illness or a set of product in a easiest and fastest way through Machine Learning.")
