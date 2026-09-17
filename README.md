# 🧠 Mental Health in Tech Survey Dashboard

An interactive **Streamlit dashboard** for exploring mental-health
attitudes, treatment-seeking behaviour, demographic patterns, and
workplace support among professionals in the technology sector.

## 📌 Project Overview

Mental health is an important workplace concern, particularly in
technology environments where employees may experience demanding
workloads, stress, and barriers to discussing mental-health needs.

This project analyzes the **Mental Health in Tech Survey** dataset and
presents the findings through an interactive Streamlit dashboard. The
dashboard helps explore demographic characteristics, treatment
behaviour, family history, work interference, employer support, and
awareness of mental-health resources.

## 🎯 Objectives

The main objectives of this project are to:

-   Analyze mental-health treatment-seeking behaviour among technology
    professionals.
-   Study demographic patterns based on age, gender, and country.
-   Examine the relationship between family history and treatment.
-   Analyze how mental-health conditions interfere with work.
-   Evaluate workplace support through benefits, care options, wellness
    programs, anonymity, leave policies, coworkers, and supervisors.
-   Compare treatment behaviour across demographic and workplace
    factors.
-   Present useful insights and practical workplace recommendations
    through an interactive dashboard.

## ❓ Problem Statement

Although mental-health concerns affect many employees, workplace
awareness and support may vary significantly. Employees may not know
what care options are available, may be uncomfortable discussing mental
health with supervisors or coworkers, or may perceive inadequate
organizational support.

The project therefore explores the survey data to understand:

-   Who seeks mental-health treatment?
-   How does family history relate to treatment behaviour?
-   How does mental health interfere with work?
-   What mental-health support do employers provide?
-   How aware are employees of available care options?
-   How comfortable are employees discussing mental health in the
    workplace?

## 📂 Dataset

The project uses the **Mental Health in Tech Survey** dataset.

The cleaned dataset used by the Streamlit application is:

`cleaned_mental_health_survey.csv`

The cleaned data contains **1,251 respondents** after data
preprocessing.

Important variables analyzed include:

`Age`, `Gender_Clean`, `Country`, `treatment`, `family_history`,
`work_interfere`, `benefits`, `care_options`, `wellness_program`,
`seek_help`, `anonymity`, `leave`, `coworkers`, `supervisor`,
`mental_vs_physical`, `mental_health_consequence`, `remote_work`, and
`no_employees`.

## 🔄 Project Workflow

``` text
Mental Health Survey Dataset
          ↓
Data Understanding
          ↓
Data Cleaning & Preprocessing
          ↓
Exploratory Data Analysis (EDA)
          ↓
Demographic Analysis
          ↓
Mental Health Analysis
          ↓
Workplace Support Analysis
          ↓
Treatment Analysis
          ↓
Business Insights
          ↓
Recommendations
          ↓
Streamlit Dashboard
          ↓
GitHub + Streamlit Deployment
```

## 🏗️ Dashboard Architecture

``` text
CSV Dataset
    ↓
Pandas Data Processing
    ↓
Streamlit Application
    ↓
Sidebar Filters
    ├── Country
    ├── Gender
    └── Treatment Status
    ↓
Interactive Analysis
    ├── Home
    ├── Demographics
    ├── Mental Health
    ├── Workplace Support
    ├── Treatment Analysis
    └── Insights & Recommendations
    ↓
Plotly Visualizations + KPI Metrics
```

## 📊 Dashboard Pages

### 🏠 Home

Provides an overall summary of the survey with key performance
indicators such as total respondents, treatment percentage,
family-history percentage, and number of countries represented.

### 👥 Demographics

Analyzes:

-   Age distribution
-   Gender distribution
-   Age groups
-   Country distribution
-   Gender versus treatment

### 🧠 Mental Health

Explores:

-   Treatment distribution
-   Family history of mental illness
-   Family history versus treatment
-   Work interference versus treatment
-   Age group versus treatment

### 🏢 Workplace Support

Examines employer and workplace factors including:

-   Mental-health benefits
-   Care options
-   Wellness programs
-   Resources for seeking help
-   Anonymity
-   Medical leave
-   Coworker communication
-   Supervisor communication
-   Mental versus physical health support
-   Perceived mental-health consequences

### 💊 Treatment Analysis

Provides interactive comparison of treatment behaviour with:

-   Family history
-   Work interference
-   Benefits
-   Care options
-   Wellness programs
-   Gender
-   Age group
-   Remote work
-   Company size
-   Supervisor support
-   Coworker support
-   Help resources
-   Anonymity

A percentage table is also provided for easier comparison.

### 💡 Insights & Recommendations

Summarizes the major findings from the survey and provides practical
recommendations for improving workplace mental-health awareness and
support.

## 🔍 Key Business Insights

The cleaned dataset used in the dashboard shows:

-   Approximately **50.5%** of respondents reported seeking
    mental-health treatment.
-   Approximately **39.1%** reported a family history of mental illness.
-   Approximately **37.8%** reported that their employer provides
    mental-health benefits.
-   Approximately **35.1%** reported awareness of employer-provided
    mental-health care options.
-   Approximately **18.1%** reported that mental health had been
    discussed as part of an employee wellness program.
-   Treatment-seeking behaviour differs across family-history and
    work-interference groups.
-   Employees report varying levels of comfort discussing mental health
    with coworkers and supervisors.

These findings describe associations and survey responses; they should
not be interpreted as proving causal relationships.

## ✅ Recommendations

Organizations can use the survey findings to guide workplace initiatives
such as:

1.  Improve awareness of available mental-health benefits and services.
2.  Clearly communicate mental-health care options to employees.
3.  Strengthen employee wellness and mental-health awareness programs.
4.  Provide appropriate mental-health awareness training for managers
    and supervisors.
5.  Clearly communicate confidentiality and anonymity policies.
6.  Develop supportive medical-leave and workplace policies.
7.  Encourage a workplace culture where employees can seek support
    without unnecessary stigma.
8.  Conduct periodic anonymous surveys to monitor employee perceptions
    and support needs.

## 🛠️ Technologies Used

-   **Python**
-   **Pandas** --- data manipulation and analysis
-   **Plotly** --- interactive data visualization
-   **Streamlit** --- dashboard development
-   **GitHub** --- source-code hosting and version control
-   **Streamlit Community Cloud** --- application deployment

## 📁 Project Structure

``` text
Mental-Health-in-Tech-Survey/
│
├── app.py
├── cleaned_mental_health_survey.csv
├── requirements.txt
└── README.md
```

## 📦 Requirements

The `requirements.txt` file contains:

``` text
streamlit
pandas
plotly
```

Install the required packages using:

``` bash
pip install -r requirements.txt
```

## ▶️ Run the Project Locally

Clone or download the repository, open a terminal in the project
directory, and run:

``` bash
streamlit run app.py
```

Streamlit will open the dashboard in your web browser.

## 🚀 Deployment

The application can be deployed using **Streamlit Community Cloud**:

1.  Upload the project files to a GitHub repository.
2.  Sign in to Streamlit Community Cloud using GitHub.
3.  Select the project repository.
4.  Set the main file path to `app.py`.
5.  Deploy the application.

## 🌐 Live Application

**Streamlit App:** [https://mental-health-in-tech-survey.streamlit.app/]

## 📌 Conclusion

This project transforms the Mental Health in Tech Survey into an
interactive analytical dashboard. It provides a clear view of treatment
behaviour, demographic patterns, work interference, and workplace
mental-health support. The dashboard can help communicate survey
findings and identify areas where organizations may strengthen
mental-health awareness, accessibility, and employee support.

------------------------------------------------------------------------

### 🧠 Mental Health in Tech Survey

**Exploratory Data Analysis and Interactive Streamlit Dashboard**
