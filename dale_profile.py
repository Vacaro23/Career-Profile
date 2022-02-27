import streamlit as st
from PIL import Image
import pandas as pd
 
##########


st.set_page_config(
    page_title= "Dale",
    page_icon= "picture_me.png",
    layout="wide",
    initial_sidebar_state="auto",
)


my_page = st.sidebar.radio('Page Navigation', ['Career Profile', 'Project #1: 2019 Senatorial Elections', 'Project #2'])


if my_page == 'Career Profile':
    #####################
    # Header 
    st.title('''
    John Dale L. Vacaro, 
    #### FIA, CLSSYB, CAEA, CFMP
    ###### *Career Profile* 
    ''')

    image = Image.open('picture_me.png')
    st.image(image, width=250)

    st.markdown('## Summary', unsafe_allow_html=True)
    st.info('''
    - An Inquisitive Leader focused on Data, Innovation and Technology.
    - Experienced Data Professional in Financial Services and Consulting Industry specializing Financial Markets, and Revenue Data.
    - Experienced in CustomerRelationship Management, Data Management, Business Operations & Sales Enablement, and Content Operations.
    - Expert in streamlining Financial Markets and Revenue data to deliver its best quality to customers and help senior leaders generate strategic data-driven decisions through Research Methods, Exploratory Data Analysis, and Machine Learning Algorithms.
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
            <a class="nav-link" href="#education">Education</a>
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


    #####################
    st.markdown('''
    ## Work Experience
    ''')

    txt('`SENIOR ANALYTICS CONSULTANT`',
    '2021 - Present')
    txt('Risk Advisory, Deloitte, Philippines', '')
    st.markdown('''
    - Collaboratively worked smoothly with AU client stakeholders for business understanding with self-initiated curiosity and with IT Engineers to implement data quality functional services supplementing a detective mindset in every data questions.
    - Proactively pinpointed data logic issues, creating potential solutions and test cases in order to exceedingly solve client problems and root causes.
    - Performed 2 Australian Projects focused on Timesheet Digitization in-charge of data integrity using ABBYY FlexiCapture, and achieved an outperforming performance with 0 escalation.
    - Generated ideas and created proposals to Technical Specialists to optimize processes and improve efficacies of all members in the project.
    ''')
    



    txt('`BUSINESS OPERATIONS ANALYST`',
    '2021 - 2021')
    txt('Business Operations & Sales Enablement, London Stock Exchange Group, Philippines', '')
    st.markdown('''
    - Successfully passed sponsored certification of “Financial Information Associate” (FIA) worth 900 USD and recently granted another sponsorship worth 2,000 USD to expand knowledge in Business Analysis and Data Science, given only to Top 25% outperforming employees in the organization.
    - Developed global data visualization reports and dashboards for pipeline management to forecast sales data for Senior Sales Leaders.
    - Drived new logos and white space growth through historical data analysis and forecasting monthly recurring sales for the whole Americas region.
    - Planned sales accelerators to amplify key opportunities, bridged gaps within the sales workflows and to support incentives to excellent sellers.
    - Designed KPI data models to assess seller’s performance and Territory Optimization model to align seller’s book of business for turn of the year.
    - Analyzed sales and retention motions by providing operational guidance to deliver 2021 migrations and strategies, executing revenue synergy pathways and incorporating customer lifecycle framework to key renewals.

    ''')

    txt('`FINANCIAL MARKETS ANALYST II`',
    '2021 - 2021')
    txt('`FINANCIAL MARKETS ANALYST I`',
    '2019 - 2021')
    txt('Business Operations & Sales Enablement, London Stock Exchange Group, Philippines', '')
    st.markdown('''
    - Selected as one of the Top 10% Outstanding Employees in the Organization, achieved the highest rating of ‘Leading’ in 2020 Company Year-End Assessment- as a measure of exemplary performance by the following that saved 0.55 FTE:
        - by creation of method of works and documentations,
        - by doing finanical markets data manipulation and analyzation,
        - by stock exchange projects and migration
        - by building 15 excel macros initiatives and
        - by generating automation ideations and proposals
    - Successfully accomplished remarkable performance with 99% data integrity of my daily productions which consistently gave me the award of  ‘Star of the Month’ or ‘Employee of the Month’, within our team - composed of 8 Analysts and 4 Senior Analysts.
    - Successfully planned, supervised and coordinated daily BAU, conducted weekend testings and migrations for new and critical content enhancements on the databases and products with no supervision from seniors and managers.
    - Performed change management in every projects to improve the transition of the change, collaboration, communication and to create change plans to reduce uncertain issues that avoids client escalations through ServiceNOW.
    - Influenced team members volunteering to new tasks that enhanced adaptability and flexibility for learnings that received zero business critical.
    - Achieved a 10/10 rating from a customer for providing silver bullets that strengthened customer retention, experience and attrition.
    - Identified and pinpointed data inefficiencies and bugs in workstream, boosting team performance metrics and data accuracy by ~49% through development and launching of permanent solutions and reinforcement of automations.
    ''')


    #####################
    st.markdown('''
    ## Bootcamps, Trainings, Courses
    ''')

    txt('`DATA SCIENCE FELLOW`',
    '2021 - Present')
    txt('Data Science & Machine Learning, Eskwelabs, Philippines', '')
    st.markdown('''
    - Structured Unsupervised Machine Learning Project using 2019 Philippine Electoral Votes land deployed in Streamlit web application.
        - Project Title: An Analysis on Political Spending of 2019 Philippine Senatorial Elections
        - Packages: Numpy, Pandas, Matplotlib, Seaborn, Sklearn, Scipy 
        - Methods: EDA, Feature Engineering, KMeans, Silhouettter Score, Hierarchical Clustering, Radar Analysis 
    - Worked with a Big Data Credit Card Fraud Project using Supervised Machine Learning techniques, Cloud Infrastructures and Analytics Engine.
        - Project Title: FRAUD-tech Yourself: Eskwebank’s Credit Card Fraud Detection Modeling Project
        - Packages: Numpy, Pandas, Matplotlib, Seaborn, Sklearn
        - Methods: EDA, Feature Engineering, Regression, Random Forest, XGBoost, Gradient Boosted Decision Tree, Decision Tree, Metrics Selection, Features Importance, Explainability 
    - Created Spotify Recommender Engine using Britney Spears’ Spotify Data in order to strategize in boosting her Streams through Supervised Machine Learning algorithms.
        - Project Title: Hit Me Baby One More Time: Reclaiming the Pop Princess’ Lost Throne
        - Packages: Numpy, Pandas, Matplotlib, Seaborn, Sklearn, Spotipy, Keyring
        - Methods: EDA, Feature Engineering, KNN, SVM (linear, poly, radial), Euclidian, Manhattan, Cosine, WebAPI, Classification Algorithm, ROC
    - Assembled an NLP Recommender Engine product using Web Scraped Perfume Data to create a product that will feel the perfume based on the user's feelings and emotions.
        - Project Title: Wear Your Memories: Perfume Recommender Engine
        - Packages: BeautifulSoup, Numpy, Pandas, Matplotlib, Seaborn, Bokeh, Networkx, WordCloud, nltk, gensim, Sklearn, Spacy
        - Methods: Web Scraping, Preprocessing, EDA, Network Analysis, Word Cloud
    ''')


    txt('`DATA SCIENCE & BUSINESS ANALYTICS INTERN`',
    '2022 - Present')
    txt('Data Science & Machine Learning, The Sparks Foundation, Philippines', '')
    st.markdown('''
    - Started a Project as a Business Manager, to do an Exploratory Data Analysis on a Retail Business dataset in order to identify Business Dilemma and to raise Profit, based on the given data.
    - Created and Presented a Decision Tree Modeling Project using Iris Dataset to identify correct classification based from the given data.
    ''')

    txt('`DATA ENGINEERING SCHOLAR`',
    '2022 - Present')
    txt('Data Engineer, Department of Science and Technology, Philippines', '')
    st.markdown('''
    - As a Data Engineering Scholar, the scholarship goal is to learn building and managing data workflows, pipelines, ETL processes and platforms.
    - To learn and be responsible for management of the entire data lifecycle: ingestion, processing, surfacing, and storage.
    - To learn and have an in-depth knowledge of programming, databases, data warehousing, and data architecture and pipelining, to use complex tools and techniques to handle data at scale. Also includes machine learning and statistical models in production.
    - The learning pathway includes topics such as: Data Engineering, Operational Analytics, Data Governance, Computing, Data Visualization, Data Analytics Methods and Algorithms, Statistical Techniques, Research Methods, and Domain Knowledge.
    ''')

    txt('`DATA SCIENCE & BUSINESS ANALYTICS INTERN`',
    '2022 - Present')
    txt('Data Science & Machine Learning, The Sparks Foundation, Philippines', '')
    st.markdown('''
    - Started a Project as a Business Manager, to do an Exploratory Data Analysis on a Retail Business dataset in order to identify Business Dilemma and to raise Profit, based on the given data.
    - Created and Presented a Decision Tree Modeling Project using Iris Dataset to identify correct classification based from the given data.
    ''')

    #####################
    st.markdown('''
    ## Skills
    ''')
    txt3('Programming', '`Python`, `R`')
    txt3('Data Processing/Wrangling', '`Advanced Excel`, `VBA`, `pandas`, `numpy`, `nltk`')
    txt3('Data Visualization', '`Tableau`, `PowerBI`, `Google Data Studio`, `matplotlib`, `seaborn`, `bokeh`')
    txt3('Machine Learning', '`scikit-learn`, `scipy`, `gensim`, `networkx`')
    txt3('Web Scraping', '`selenium`, `beautifiulsoup`')
    txt3('Model Deployment', '`streamlit`, `Heroku`')
    txt3('Customer Relationship Management', '`Salesforce ServiceCloud`, `Salesforce Trust`, `SalesforceLightning`')
    txt3('Change Management', '`ServiceNOW`')
    txt3('Documentations', '`Confluence`,`Sharepoint`')
    txt3('Tech Improvement', '`JIRA`')

    #####################
    st.markdown('''
    ## Social Media
    ''')
    txt2('LinkedIn', 'https://www.linkedin.com/in/johndalevacaro/')
    txt2('GitHub', 'https://github.com/Vacaro23')
    

elif my_page == 'Project #1: 2019 Senatorial Elections':
    #####################
    # Header 
    st.title('''
    Fair Game: An Analysis on Further Equalizing the Philippine Senatorial Elections by their Financial Resources
    
    ##### *Election is one of the biggest manifestations of a democracy.* 
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
            <a class="nav-link" href="#education">Education</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#work-experience">Work Experience</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#bootcamps-trainings-courses">L&D</a>
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
        
    
    image = Image.open('2019_election.jpeg')
    st.image(image, width= 800)
    
    ##################### PROBLEM STATEMENT
    
    st.markdown('## Problem Statement', unsafe_allow_html=True)
    st.info('''
    How can we improve the Philippine Election System in terms of fairness for all candidates?
    ''')
    

    
   ##################### OBJECTIVES

    st.markdown('''
    ## Objective
    ''')
    st.error('''
    To identify strategies on reducing political spending disadvantages in senatorial elections.
    ''')
    
    
    ##################### DATASET
    
    st.markdown('''
    ## Dataset
    ''')
    st.info('''
    1. 2019 Senatorial Votes - candidate name, vote count
    2. 2019 Candidate Campaigns - expenditure breaddown, social media interactions
    ''')
    
    df = pd.read_csv("data_spend-social_df.csv")
    df
    
    
    ##################### DATASET BUTTON
    @st.cache
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    #converting the sample dataframe
    csv = convert_df(df)
    
    #adding a download button to download csv file
    st.download_button( 
        label="Download Dataset",
        data=csv,
        file_name='data_spend-social_df.csv',
        mime='text/csv',
    )

    
    ##################### METHODOLOGY
    
    st.markdown('''
    ## Methodology
    ''')
    st.info('''
    1. Data Preparation - cleaning, merging, error, duplicates, missing
    2. Exploratory Data Analysis - data viz; plotting, correlation
    3. Feature Engineering - features election
    4. Data Modeling - KMeans, Hierarchical Clustering, Euclidian Distance
    5. Cluster Insights - Radar Clustering
    ''')
    
    ##################### EXPLORATORY DATA ANALYSIS
    
    st.markdown('''
    ## Exploratory Data Analysis
    ''')
    
    ### SPENDERS vs NON-SPENDERS
    image = Image.open('eda-1.jpeg')
    st.image(image, width=750)
    st.caption("Out of the 2019 Top Senatorial Winners, **68%** were High Spenders.")
    
    ## Top 10 - List of Winners: Spenders
    image = Image.open('eda-5.jpeg')
    st.image(image, width=750)
    st.caption("**6/10** Top Candidates Spenders were able to win!")
    
    
    image = Image.open('eda-4.jpeg')
    st.image(image, width=750)
    st.caption("**9%** of Senatorial Candidates were Non-Spenders which did not invest on Social Media resulting to low interactions with PH Audience. Hence, in this illustration there was a high correlation between being a non-spender and social media interactions.")
    
    
    
    image = Image.open('eda-6.jpeg')
    st.image(image, width=750)
    st.caption("On the other hand, **91%** of the Top Spender Candidates; had a high investments on their Expenditures with **78%** corr and specifically with **75%** correlation with Political Advertisements.")
    
    
    image = Image.open('eda-2.jpeg')
    st.image(image, width=750)
    st.caption("Looking the Winners Expenditures, **11/12** Senatorial Winners averagely spent **89%** on Political Advertisement.")
    
    
    image = Image.open('eda-3.jpeg')
    st.image(image, width=750)
    txt5("Segment 0","48 Candidates", "2 Won")
    txt5("Segment 1","2 Candidates", "1 Won")
    txt5("Segment 2","12 Candidates", "9 Won")
    st.caption("Looking at the Radar Clustering, Segment 0 are candidates who spent less for the elections relative to the whole group. Segments 1 and 2 are candidates who spent the most - with Segment 1 consisting of candidates whose expenditure are spread throughout all aspects while Segment 2 consisting of candidates whose expenditure are focused on Political Advertisements.")
    
    
    ##################### CONCLUSION
    
    st.markdown('''
    ## Conclusion
    ''')
    
    image = Image.open('con_1.jpeg')
    st.image(image, width=750)
        
    image = Image.open('con_2.jpeg')
    st.image(image, width=750)
    
        

    ##################### RECOMMENDATIONS
    
    st.markdown('''
    ## Recommendations
    ''')
    
    image = Image.open('reco_1.jpeg')
    st.image(image, width=750)
    st.caption("To even the playing field, government funding can be provided to candidates. In Germany, parties receive funding in proportion to the votes they received.")
    st.caption("While this system favor incumbents and can be tweaked further for fairness, the results speak for themselves. Donations comprise barely 10% of the total expenditures whereas in the Philippines, the PCIJ stated candidates are mostly funded by a few backers.")
        
    image = Image.open('reco_2.jpeg')
    st.image(image, width=750)
    st.caption("Ad air time is also partitioned by vote share in Germany. Given that political ads played a factor in the 2019 PH elections, allotting time for candidates should also be considered.")
        
    image = Image.open('reco_3.jpeg')
    st.image(image, width=750)
    st.caption("Competitiveness and reelection rates were reduced in the 2020 Brazil mayoral elections when expenditure limits were put in place. Overall spending was also limited as a result. It is important to watch out for unaccounted funds or dark money however. Thus, limits should be paired with good accounting practices.")
        
    image = Image.open('reco_4.jpeg')
    st.image(image, width=750)
    st.caption("It is important to note that these measures are tailor fitted to these countries. The Philippines has to figure out its own blend of election policies and checks.")
        
        
    image = Image.open('improv.jpeg')
    st.image(image, width=750)
    st.caption("To have more robust analysis, detailed datasets on political ad spending per media, travel, and others could be explored.")
    
    
    
    ##################### REFERENCES
    
    st.markdown('''
    ## References
    ''')
    
    st.caption(
        "Ilagan , Karol, & Simon, Floreen. (n.d.). Covering campaign finance: The Philippine experience. Philippine Center for Investigative Journalism. Retrieved November 26, 2021, from https://pcij.org/article/5377/covering-campaign-finance-philippine-experience.")
    st.caption(
        "Hallam, M. H., & Bateson, I. (n.d.). German election: Party and campaign financing: DW: 09.08.2021. DW.COM. Retrieved November 26, 2021, from https://www.dw.com/en/german-election-party-and-campaign-financing/a-58807353.")
    st.caption(
        "Avis, E., Ferraz, C., Finan, F., & Varjão, C. (2021, July). Money and Politics: The Effects of Campaign Spending Limits on Political Entry and Competition. Econometrics Laboratory, UC Berkeley. Retrieved November 26, 2021, from https://eml.berkeley.edu/~ffinan/Finan_Limits.pdf.")

