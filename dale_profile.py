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


my_page = st.sidebar.radio('Page Navigation', ['Career Profile'])


if my_page == 'Career Profile':
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
    - Exposed in Customer Relationship Management, Content Operations, Business Process Optimization, Projects & Migrations, Data Management, and Business Operations & Sales Enablement.
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
            <a class="nav-link" href="#objective">Education</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#work-experience">Work Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#bootcamps-trainings-courses">L&D</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#skills">Skills</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#social-media">Social Media</a>
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
        
    #####################
    st.markdown('''
    ## Education
    ''')

    txt('**Business Administration Major in Financial Management**, *Pamantasan ng Lungsod ng Maynila*, Philippines',
    '2015 - 2019')
    st.markdown('''
    - GPA: `1.63`
    - Dean's Lister
    - Top Finance Achiever
    - National Finalist of Top Outstanding Finance Students of the Philippines
    ''')

    st.title("")
    
    
    #####################
    st.markdown('''
    ## Work Experience
    ''')

    # txt('`SENIOR ANALYTICS CONSULTANT`',
    # '2021 - Present')
    # txt('Risk Advisory, Deloitte, Philippines', '')
    # st.markdown('''
    # - Collaboratively worked smoothly with AU client stakeholders for business understanding with self-initiated curiosity and with IT Engineers to implement data quality functional services supplementing a detective mindset in every data questions.
    # - Proactively pinpointed data logic issues, creating potential solutions and test cases in order to exceedingly solve client problems and root causes.
    # - Performed 2 Australian Projects focused on Timesheet Digitization in-charge of data integrity using ABBYY FlexiCapture, and achieved an outperforming result with 0 escalation.
    # - Generated ideas and created proposals to Technical Specialists for process and optimization with the goal of improving efficacies of all team members in the project.
    # ''')
    



    txt('`BUSINESS OPERATIONS ANALYST`',
    '2021 - 2021')
    txt('London Stock Exchange Group - Business Operations & Sales Enablement', '')
    st.markdown('''
    - Successfully passed sponsored certification of “Financial Information Associate” (FIA) worth 900 USD and recently granted another sponsorship worth 2,000 USD to expand knowledge in Business Analysis and Data Science, given only to Top 25% outperforming employees in the organization.
    - Lead the performance metric evaluation of 230+ product sellers in Amers, presenting the result to Head of Americas of Business Operations.
    - Developed global data visualization reports and dashboards for pipeline management to forecast sales data for Senior Directors, Managers, and Sales Stakeholders.
    - Drived new logos and white space growth through historical data analysis and forecasting monthly recurring sales for the whole Americas region.
    - Planned sales accelerators to amplify key opportunities, bridged gaps within the sales workflows and to support incentives to excellent sellers.
    - Designed KPI data models to assess seller’s performance and Territory Optimization model to align seller’s book of business for turn of the year.
    - Analyzed sales and retention motions by providing operational guidance to deliver 2021 migrations and strategies, executing revenue synergy pathways and incorporating customer lifecycle framework to key renewals.

    ''')

    
    
    st.title("")
    
    
    txt('`FINANCIAL MARKETS ANALYST II`',
    '2021 - 2021')
    txt('`FINANCIAL MARKETS ANALYST I`',
    '2019 - 2021')
    txt('London Stock Exchange Group - Content Operations & Managed Services', '')
    st.markdown('''
    - Selected as one of the Top 10% Outstanding Employees in the Organization, achieved the highest rating of ‘Leading’ in 2020 Company Year-End Assessment - as a measure of exemplary performance by the following that saved 0.55 FTE:
        - by creation of method of works and documentations,
        - by doing finanical markets data manipulation and analyzation,
        - by stock exchange projects and migration
        - by building 15 excel macros initiatives and
        - by generating automation ideations and proposals
    - Successfully accomplished remarkable performance with 99% data integrity of my daily productions which consistently gave me the award of  ‘Star of the Month’ or ‘Employee of the Month’, within our team - composed of 8 Analysts and 4 Senior Analysts.
    - Successfully planned, supervised and coordinated daily BAU, test new databases and applications release and migrations for new and critical data enhancements in an Agile environment with no supervision from seniors and managers.
    - Performed change management in every projects to improve the transition of the change, collaboration, communication and to create change plans to reduce uncertain issues that avoids client escalations through ServiceNOW.
    - Influenced team members volunteering to new tasks that enhanced adaptability and flexibility for learnings that received zero business critical.
    - Timely published Information, Service and Retrospective Alerts to inform EMEA and SEA clients on changes on products & services with proper Incidenc and Recovery Management of the alerts.
    - Achieved a 10/10 rating from a customer for providing silver bullets that strengthened customer retention, experience and attrition.
    - Identified and pinpointed data inefficiencies and bugs in workstream resolved in JIRA, boosting team performance metrics and data accuracy by ~49% through development and launching of permanent solutions and reinforcement of automations.
    ''')

    st.title("")
    
    #####################
    st.markdown('''
    ## Bootcamps, Trainings, Courses
    ''')

    txt('`DATA SCIENCE FELLOW`',
    '2021 - Present')
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
    '2022 - Present')
    txt('DPhi Tech - Data Science & Machine Learning', '')
    st.markdown('''
    - Accomplished an NLP Modeling Project that predicts if the News Headlines either Sarcastic or Not Sarcastic.
        - Packages: nltk, numpy, seaborn, matplotlib, pandas, contractions, re, string, PIL, wordcloud, sklearn, collections, textblob
        - Methods: Data Pre-Processing, EDA, Text Pre-Processing, Sentiment Analysis, BagOfWords, Logistic Regression, Gradient Boosted Decision Tree, Decision Tree, Random Forest
    - Ongoing -  Explainable AI Bootcamp using LIME, SHAP and other tools
    ''')
    
    st.title("")
        
        
    txt('`DATA SCIENCE & BUSINESS ANALYTICS INTERN`',
    '2022 - Present')
    txt('The Sparks Foundation - Data Science & Machine Learning', '')
    st.markdown('''
    - Started a Project as a Business Manager, to do an Exploratory Data Analysis on a Retail Business dataset in order to identify Business Dilemma and to raise Profit, based on the given data.
    - Created a Decision Tree Modeling Project using Iris Dataset to identify correct classification of Flower based from the given data.
    ''')
    
    st.title("")

    txt('`DATA ENGINEERING SCHOLAR`',
    '2022 - Present')
    txt('Department of Science & Technology - Data Engineer', '')
    st.markdown('''
    - As a Data Engineering Scholar, the scholarship goal is to learn building and managing data workflows, pipelines, ETL processes and platforms.
    - To learn and be responsible for management of the entire data lifecycle: ingestion, processing, surfacing, and storage.
    - To learn and have an in-depth knowledge of programming, databases, data warehousing, and data architecture and pipelining, to use complex tools and techniques to handle data at scale. Also includes machine learning and statistical models in production.
    - The learning pathway includes topics such as: Data Engineering, Operational Analytics, Data Governance, Computing, Data Visualization, Data Analytics Methods and Algorithms, Statistical Techniques, Research Methods, and Domain Knowledge.
    ''')
    
    st.title("")
    
    
    #####################
    st.markdown('''
    ## Skills
    ''')
    txt3('Programming', '`Python`')
    txt3('Data Transformation', '`Advanced Excel`, `VBA`, `Alteryx`, `pandas`, `numpy`, `nltk`')
    txt3('Data Visualization', '`Tableau`, `PowerBI`, `Google Data Studio`, `matplotlib`, `seaborn`, `bokeh`')
    txt3('Machine Learning', '`scikit-learn`, `scipy`, `gensim`, `networkx`')
    txt3('Web Scraping', '`selenium`, `beautifiulsoup`')
    txt3('Model Deployment', '`streamlit`, `Heroku`')
    txt3('Customer Relationship Management', '`Salesforce ServiceCloud`, `Salesforce Trust`, `SalesforceLightning`')
    txt3('Change Management', '`ServiceNOW`')
    txt3('Documentations', '`Confluence`,`Sharepoint`')
    txt3('Issue Tracking & Project Management', '`JIRA`')
    txt3('Fundamental Knowledge', '`Databricks`,`Regular Expression`, `RStudio`')
    
    st.title("")
    
    #####################
    st.markdown('''
    ## Social Media
    ''')
    txt2('LinkedIn', 'https://www.linkedin.com/in/johndalevacaro/')
    txt2('GitHub', 'https://github.com/Vacaro23')
