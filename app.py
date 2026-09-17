# ============================================================
# MENTAL HEALTH IN TECH SURVEY
# STREAMLIT DASHBOARD - NO HTML / NO CSS
# ============================================================

import streamlit as st
import pandas as pd
import plotly.express as px


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Mental Health in Tech Survey",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    return pd.read_csv("cleaned_mental_health_survey.csv")


df = load_data()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def percentage_yes(data, column):
    if len(data) == 0:
        return 0.0

    return (
        data[column]
        .value_counts(normalize=True)
        .get("Yes", 0) * 100
    )


def chart_style(fig):
    fig.update_layout(
        font=dict(
            family="Arial",
            color="#243B64"
        ),
        title_font=dict(
            size=20,
            color="#173B67"
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(
            l=30,
            r=30,
            t=60,
            b=30
        ),
        legend_title_text=""
    )

    return fig


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧠 Mental Health")
st.sidebar.caption("Tech Survey Dashboard")

st.sidebar.divider()


# ============================================================
# NAVIGATION
# ============================================================

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "👥 Demographics",
        "🧠 Mental Health",
        "🏢 Workplace Support",
        "💊 Treatment Analysis",
        "💡 Insights & Recommendations"
    ]
)


# ============================================================
# FILTERS
# ============================================================

st.sidebar.divider()
st.sidebar.header("🔎 Filters")


country_options = sorted(
    df["Country"]
    .dropna()
    .unique()
)

selected_countries = st.sidebar.multiselect(
    "🌍 Select Country",
    options=country_options,
    placeholder="All Countries"
)


gender_options = sorted(
    df["Gender_Clean"]
    .dropna()
    .unique()
)

selected_gender = st.sidebar.multiselect(
    "👤 Select Gender",
    options=gender_options,
    placeholder="All Genders"
)


treatment_options = sorted(
    df["treatment"]
    .dropna()
    .unique()
)

selected_treatment = st.sidebar.multiselect(
    "💊 Treatment Status",
    options=treatment_options,
    placeholder="All"
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_countries:
    filtered_df = filtered_df[
        filtered_df["Country"].isin(selected_countries)
    ]


if selected_gender:
    filtered_df = filtered_df[
        filtered_df["Gender_Clean"].isin(selected_gender)
    ]


if selected_treatment:
    filtered_df = filtered_df[
        filtered_df["treatment"].isin(selected_treatment)
    ]


# ============================================================
# SIDEBAR INFORMATION
# ============================================================

st.sidebar.divider()

st.sidebar.info(
    """
    💗 **Workplace Well-being**

    Mental-health awareness and accessible support
    can contribute to a healthier workplace.
    """
)


# ============================================================
# COMMON VALUES
# ============================================================

total = len(filtered_df)

countries = filtered_df["Country"].nunique()

treatment_rate = percentage_yes(
    filtered_df,
    "treatment"
)

family_rate = percentage_yes(
    filtered_df,
    "family_history"
)


# ============================================================
# EMPTY DATA CHECK
# ============================================================

if filtered_df.empty:
    st.warning(
        "No records match the selected filters. "
        "Please change the sidebar filters."
    )
    st.stop()


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.title("🧠 Mental Health in Tech Survey Dashboard")

    st.write(
        """
        Exploring mental-health attitudes, treatment-seeking
        behaviour and workplace support among technology
        professionals.
        """
    )

    st.caption(
        "📅 Survey Year: 2014  |  "
        f"👥 Respondents: {total}  |  "
        f"🌍 Countries: {countries}  |  "
        "💻 Focus: Tech Workplace"
    )

    st.divider()


    # ========================================================
    # KPI CARDS
    # ========================================================

    col1, col2, col3, col4 = st.columns(4)


    with col1:
        with st.container(border=True):

            st.subheader("👥 Respondents")

            st.metric(
                "Total Respondents",
                f"{total:,}"
            )

            st.caption(
                f"{countries} countries represented"
            )


    with col2:
        with st.container(border=True):

            st.subheader("💊 Treatment")

            st.metric(
                "Sought Treatment",
                f"{treatment_rate:.1f}%"
            )

            st.caption(
                "Reported seeking mental-health treatment"
            )


    with col3:
        with st.container(border=True):

            st.subheader("❤️ Family History")

            st.metric(
                "Reported",
                f"{family_rate:.1f}%"
            )

            st.caption(
                "Reported a family history of mental illness"
            )


    with col4:
        with st.container(border=True):

            st.subheader("🌍 Coverage")

            st.metric(
                "Countries",
                countries
            )

            st.caption(
                "Geographic participation"
            )


    st.divider()


    # ========================================================
    # MAIN CHARTS
    # ========================================================

    st.header("📊 Survey Overview")

    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # TREATMENT DONUT
    # --------------------------------------------------------

    with col1:

        with st.container(border=True):

            treatment_counts = (
                filtered_df["treatment"]
                .value_counts()
                .reset_index()
            )

            treatment_counts.columns = [
                "Treatment",
                "Count"
            ]


            fig = px.pie(
                treatment_counts,
                names="Treatment",
                values="Count",
                title="Mental Health Treatment Distribution",
                hole=0.55,
                color="Treatment",
                color_discrete_map={
                    "Yes": "#1565C0",
                    "No": "#EC407A"
                }
            )


            fig.update_traces(
                textposition="inside",
                textinfo="percent+label"
            )


            fig = chart_style(fig)


            st.plotly_chart(
                fig,
                use_container_width=True
            )


            st.info(
                f"ℹ️ **{treatment_rate:.1f}%** of respondents "
                "in the current selection reported seeking "
                "treatment for a mental-health condition."
            )


    # --------------------------------------------------------
    # FAMILY HISTORY
    # --------------------------------------------------------

    with col2:

        with st.container(border=True):

            family_counts = (
                filtered_df["family_history"]
                .value_counts()
                .reset_index()
            )

            family_counts.columns = [
                "Family History",
                "Count"
            ]


            fig = px.bar(
                family_counts,
                x="Family History",
                y="Count",
                text="Count",
                title="Family History of Mental Illness",
                color="Family History",
                color_discrete_map={
                    "No": "#7E57C2",
                    "Yes": "#26A69A"
                }
            )


            fig.update_traces(
                textposition="outside"
            )


            fig = chart_style(fig)


            st.plotly_chart(
                fig,
                use_container_width=True
            )


            st.success(
                f"❤️ **{family_rate:.1f}%** of respondents "
                "reported having a family history of "
                "mental illness."
            )


    # ========================================================
    # KEY INSIGHTS
    # ========================================================

    st.header("💡 Key Survey Indicators")


    benefit_rate = percentage_yes(
        filtered_df,
        "benefits"
    )

    care_rate = percentage_yes(
        filtered_df,
        "care_options"
    )

    wellness_rate = percentage_yes(
        filtered_df,
        "wellness_program"
    )


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:
        with st.container(border=True):

            st.write("💊 **Treatment**")

            st.metric(
                "Respondents",
                f"{treatment_rate:.1f}%"
            )

            st.caption(
                "Sought treatment"
            )


    with c2:
        with st.container(border=True):

            st.write("❤️ **Family History**")

            st.metric(
                "Respondents",
                f"{family_rate:.1f}%"
            )

            st.caption(
                "Reported family history"
            )


    with c3:
        with st.container(border=True):

            st.write("🏢 **Benefits**")

            st.metric(
                "Respondents",
                f"{benefit_rate:.1f}%"
            )

            st.caption(
                "Employer provides benefits"
            )


    with c4:
        with st.container(border=True):

            st.write("📖 **Care Options**")

            st.metric(
                "Respondents",
                f"{care_rate:.1f}%"
            )

            st.caption(
                "Know available care options"
            )


    with c5:
        with st.container(border=True):

            st.write("🌱 **Wellness**")

            st.metric(
                "Respondents",
                f"{wellness_rate:.1f}%"
            )

            st.caption(
                "Mental health discussed in wellness programs"
            )


# ============================================================
# DEMOGRAPHICS PAGE
# ============================================================

elif page == "👥 Demographics":

    st.title("👥 Demographic Analysis")

    st.write(
        """
        Explore the demographic characteristics of survey
        respondents including age, gender and geographic
        distribution.
        """
    )

    st.divider()


    # ========================================================
    # AGE + GENDER
    # ========================================================

    col1, col2 = st.columns(2)


    with col1:

        with st.container(border=True):

            fig = px.histogram(
                filtered_df,
                x="Age",
                nbins=20,
                title="Age Distribution",
                color_discrete_sequence=[
                    "#1976D2"
                ]
            )


            fig.update_layout(
                xaxis_title="Age",
                yaxis_title="Number of Respondents"
            )


            fig = chart_style(fig)


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    with col2:

        with st.container(border=True):

            gender_counts = (
                filtered_df["Gender_Clean"]
                .value_counts()
                .reset_index()
            )

            gender_counts.columns = [
                "Gender",
                "Count"
            ]


            fig = px.pie(
                gender_counts,
                names="Gender",
                values="Count",
                title="Gender Distribution",
                hole=0.50,
                color="Gender",
                color_discrete_map={
                    "Male": "#1976D2",
                    "Female": "#EC407A",
                    "Other": "#7E57C2"
                }
            )


            fig.update_traces(
                textinfo="percent+label"
            )


            fig = chart_style(fig)


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # ========================================================
    # AGE GROUP
    # ========================================================

    st.header("📅 Age Group Analysis")


    age_counts = (
        filtered_df["Age_Group"]
        .value_counts()
        .reset_index()
    )

    age_counts.columns = [
        "Age Group",
        "Count"
    ]


    fig = px.bar(
        age_counts,
        x="Age Group",
        y="Count",
        text="Count",
        title="Respondents by Age Group",
        color="Age Group",
        color_discrete_sequence=[
            "#1565C0",
            "#26A69A",
            "#7E57C2",
            "#EC407A",
            "#FF9800",
            "#42A5F5"
        ]
    )


    fig.update_traces(
        textposition="outside"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # COUNTRY ANALYSIS
    # ========================================================

    st.header("🌍 Geographic Analysis")


    country_counts = (
        filtered_df["Country"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    country_counts.columns = [
        "Country",
        "Count"
    ]


    fig = px.bar(
        country_counts,
        x="Count",
        y="Country",
        orientation="h",
        text="Count",
        title="Top 10 Countries by Number of Respondents",
        color="Count",
        color_continuous_scale="Blues"
    )


    fig.update_layout(
        coloraxis_showscale=False
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ========================================================
    # GENDER VS TREATMENT
    # ========================================================

    st.header("👤 Gender and Treatment")


    fig = px.histogram(
        filtered_df,
        x="Gender_Clean",
        color="treatment",
        barmode="group",
        title="Gender vs Mental Health Treatment",
        color_discrete_map={
            "Yes": "#1565C0",
            "No": "#EC407A"
        }
    )


    fig.update_layout(
        xaxis_title="Gender",
        yaxis_title="Number of Respondents"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# MENTAL HEALTH PAGE
# ============================================================

elif page == "🧠 Mental Health":

    st.title("🧠 Mental Health Analysis")

    st.write(
        """
        This section analyzes treatment, family history
        and work interference among survey respondents.
        """
    )

    st.divider()


    col1, col2 = st.columns(2)


    # --------------------------------------------------------
    # TREATMENT
    # --------------------------------------------------------

    with col1:

        with st.container(border=True):

            treatment_counts = (
                filtered_df["treatment"]
                .value_counts()
                .reset_index()
            )

            treatment_counts.columns = [
                "Treatment",
                "Count"
            ]


            fig = px.pie(
                treatment_counts,
                names="Treatment",
                values="Count",
                title="Mental Health Treatment",
                hole=0.5,
                color="Treatment",
                color_discrete_map={
                    "Yes": "#1565C0",
                    "No": "#EC407A"
                }
            )


            fig.update_traces(
                textinfo="percent+label"
            )


            fig = chart_style(fig)


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # FAMILY HISTORY
    # --------------------------------------------------------

    with col2:

        with st.container(border=True):

            family_counts = (
                filtered_df["family_history"]
                .value_counts()
                .reset_index()
            )

            family_counts.columns = [
                "Family History",
                "Count"
            ]


            fig = px.bar(
                family_counts,
                x="Family History",
                y="Count",
                text="Count",
                title="Family History of Mental Illness",
                color="Family History",
                color_discrete_map={
                    "No": "#7E57C2",
                    "Yes": "#26A69A"
                }
            )


            fig.update_traces(
                textposition="outside"
            )


            fig = chart_style(fig)


            st.plotly_chart(
                fig,
                use_container_width=True
            )


    # --------------------------------------------------------
    # FAMILY HISTORY VS TREATMENT
    # --------------------------------------------------------

    st.header("❤️ Family History and Treatment")


    fig = px.histogram(
        filtered_df,
        x="family_history",
        color="treatment",
        barmode="group",
        title="Family History vs Treatment",
        color_discrete_map={
            "Yes": "#1565C0",
            "No": "#EC407A"
        }
    )


    fig.update_layout(
        xaxis_title="Family History",
        yaxis_title="Number of Respondents"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # WORK INTERFERENCE
    # --------------------------------------------------------

    st.header("💼 Work Interference")


    fig = px.histogram(
        filtered_df,
        x="work_interfere",
        color="treatment",
        barmode="group",
        title="Work Interference vs Treatment",
        color_discrete_map={
            "Yes": "#26A69A",
            "No": "#FF9800"
        }
    )


    fig.update_layout(
        xaxis_title="Work Interference",
        yaxis_title="Number of Respondents"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # AGE GROUP VS TREATMENT
    # --------------------------------------------------------

    st.header("📅 Age Group and Treatment")


    fig = px.histogram(
        filtered_df,
        x="Age_Group",
        color="treatment",
        barmode="group",
        title="Age Group vs Treatment",
        color_discrete_map={
            "Yes": "#7E57C2",
            "No": "#42A5F5"
        }
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# WORKPLACE SUPPORT PAGE
# ============================================================

elif page == "🏢 Workplace Support":

    st.title("🏢 Workplace Mental Health Support")

    st.write(
        """
        This section evaluates employer support through
        mental-health benefits, care options, wellness
        programs, resources, anonymity, medical leave
        and workplace communication.
        """
    )

    st.divider()


    factors = {
        "Mental Health Benefits": "benefits",
        "Care Options": "care_options",
        "Wellness Program": "wellness_program",
        "Resources to Seek Help": "seek_help",
        "Anonymity": "anonymity",
        "Medical Leave": "leave",
        "Coworker Discussion": "coworkers",
        "Supervisor Discussion": "supervisor",
        "Mental vs Physical Health": "mental_vs_physical",
        "Mental Health Consequence": "mental_health_consequence"
    }


    factor_label = st.selectbox(
        "Select Workplace Factor",
        options=list(factors.keys())
    )


    workplace_factor = factors[factor_label]


    # --------------------------------------------------------
    # DISTRIBUTION
    # --------------------------------------------------------

    factor_counts = (
        filtered_df[workplace_factor]
        .value_counts()
        .reset_index()
    )

    factor_counts.columns = [
        "Response",
        "Count"
    ]


    fig = px.bar(
        factor_counts,
        x="Response",
        y="Count",
        text="Count",
        color="Response",
        title=factor_label,
        color_discrete_sequence=[
            "#1565C0",
            "#26A69A",
            "#FF9800",
            "#EC407A",
            "#7E57C2"
        ]
    )


    fig.update_traces(
        textposition="outside"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # FACTOR VS TREATMENT
    # --------------------------------------------------------

    st.header(f"💊 {factor_label} vs Treatment")


    fig = px.histogram(
        filtered_df,
        x=workplace_factor,
        color="treatment",
        barmode="group",
        title=f"{factor_label} vs Treatment",
        color_discrete_map={
            "Yes": "#1565C0",
            "No": "#EC407A"
        }
    )


    fig.update_layout(
        xaxis_title=factor_label,
        yaxis_title="Number of Respondents"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # ADDITIONAL WORKPLACE INDICATORS
    # --------------------------------------------------------

    st.header("📊 Workplace Support Overview")


    c1, c2, c3 = st.columns(3)


    with c1:

        st.metric(
            "🏥 Mental Health Benefits",
            f"{percentage_yes(filtered_df, 'benefits'):.1f}%"
        )


    with c2:

        st.metric(
            "📖 Know Care Options",
            f"{percentage_yes(filtered_df, 'care_options'):.1f}%"
        )


    with c3:

        st.metric(
            "🌱 Wellness Programs",
            f"{percentage_yes(filtered_df, 'wellness_program'):.1f}%"
        )


# ============================================================
# TREATMENT ANALYSIS PAGE
# ============================================================

elif page == "💊 Treatment Analysis":

    st.title("💊 Treatment Analysis")

    st.write(
        """
        Compare treatment-seeking behaviour with different
        demographic and workplace factors.
        """
    )

    st.divider()


    variables = {
        "Family History": "family_history",
        "Work Interference": "work_interfere",
        "Mental Health Benefits": "benefits",
        "Care Options": "care_options",
        "Wellness Program": "wellness_program",
        "Gender": "Gender_Clean",
        "Age Group": "Age_Group",
        "Remote Work": "remote_work",
        "Company Size": "no_employees",
        "Supervisor": "supervisor",
        "Coworkers": "coworkers",
        "Seek Help Resources": "seek_help",
        "Anonymity": "anonymity"
    }


    variable_label = st.selectbox(
        "Compare Treatment With",
        options=list(variables.keys())
    )


    variable = variables[variable_label]


    # --------------------------------------------------------
    # CHART
    # --------------------------------------------------------

    fig = px.histogram(
        filtered_df,
        x=variable,
        color="treatment",
        barmode="group",
        title=f"Treatment vs {variable_label}",
        color_discrete_map={
            "Yes": "#1565C0",
            "No": "#EC407A"
        }
    )


    fig.update_layout(
        xaxis_title=variable_label,
        yaxis_title="Number of Respondents"
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # PERCENTAGE TABLE
    # --------------------------------------------------------

    st.header("📋 Treatment Percentage")


    treatment_table = pd.crosstab(
        filtered_df[variable],
        filtered_df["treatment"],
        normalize="index"
    ) * 100


    treatment_table = treatment_table.round(2)


    st.dataframe(
        treatment_table,
        use_container_width=True
    )


    st.caption(
        "Values represent the percentage of respondents "
        "within each selected category."
    )


    # --------------------------------------------------------
    # COMPANY SIZE VS TREATMENT
    # --------------------------------------------------------

    st.header("🏢 Company Size vs Treatment")


    fig = px.histogram(
        filtered_df,
        x="no_employees",
        color="treatment",
        barmode="group",
        title="Company Size vs Treatment",
        color_discrete_map={
            "Yes": "#26A69A",
            "No": "#FF9800"
        }
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # --------------------------------------------------------
    # REMOTE WORK VS TREATMENT
    # --------------------------------------------------------

    st.header("🏠 Remote Work vs Treatment")


    fig = px.histogram(
        filtered_df,
        x="remote_work",
        color="treatment",
        barmode="group",
        title="Remote Work vs Treatment",
        color_discrete_map={
            "Yes": "#7E57C2",
            "No": "#42A5F5"
        }
    )


    fig = chart_style(fig)


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# INSIGHTS & RECOMMENDATIONS PAGE
# ============================================================

elif page == "💡 Insights & Recommendations":

    st.title("💡 Insights & Recommendations")

    st.write(
        """
        Summary of important findings from the Mental Health
        in Tech Survey and practical workplace recommendations.
        """
    )

    st.divider()


    # Use full dataset for overall insights
    treatment_all = percentage_yes(
        df,
        "treatment"
    )

    family_all = percentage_yes(
        df,
        "family_history"
    )

    benefits_all = percentage_yes(
        df,
        "benefits"
    )

    care_all = percentage_yes(
        df,
        "care_options"
    )

    wellness_all = percentage_yes(
        df,
        "wellness_program"
    )


    # ========================================================
    # INDICATORS
    # ========================================================

    st.header("📊 Key Survey Indicators")


    c1, c2, c3, c4, c5 = st.columns(5)


    with c1:
        with st.container(border=True):

            st.write("💊 **Treatment**")

            st.metric(
                "Sought Treatment",
                f"{treatment_all:.1f}%"
            )


    with c2:
        with st.container(border=True):

            st.write("❤️ **Family History**")

            st.metric(
                "Reported",
                f"{family_all:.1f}%"
            )


    with c3:
        with st.container(border=True):

            st.write("🏥 **Benefits**")

            st.metric(
                "Employer Provides",
                f"{benefits_all:.1f}%"
            )


    with c4:
        with st.container(border=True):

            st.write("📖 **Care Options**")

            st.metric(
                "Aware",
                f"{care_all:.1f}%"
            )


    with c5:
        with st.container(border=True):

            st.write("🌱 **Wellness**")

            st.metric(
                "Programs",
                f"{wellness_all:.1f}%"
            )


    # ========================================================
    # KEY BUSINESS INSIGHTS
    # ========================================================

    st.header("🔍 Key Business Insights")


    st.info(
        f"""
        💊 **Treatment Seeking**

        Approximately **{treatment_all:.1f}%** of respondents
        reported seeking treatment for a mental-health
        condition.
        """
    )


    st.success(
        f"""
        ❤️ **Family History**

        Approximately **{family_all:.1f}%** of respondents
        reported having a family history of mental illness.
        """
    )


    st.warning(
        f"""
        🏥 **Employer Mental-Health Benefits**

        Approximately **{benefits_all:.1f}%** of respondents
        reported that their employer provides mental-health
        benefits.
        """
    )


    st.info(
        f"""
        📖 **Awareness of Care Options**

        Approximately **{care_all:.1f}%** of respondents
        reported knowing the mental-health care options
        available through their employer.
        """
    )


    st.warning(
        f"""
        🌱 **Wellness Programs**

        Approximately **{wellness_all:.1f}%** reported that
        mental health had been discussed as part of an
        employee wellness program.
        """
    )


    st.write(
        """
        **💼 Work Interference**

        The survey shows differences in treatment-seeking
        behaviour across levels of reported work interference.
        """
    )


    st.write(
        """
        **🗣️ Workplace Communication**

        Respondents show different levels of willingness to
        discuss mental-health concerns with coworkers and
        supervisors.
        """
    )


    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    st.header("✅ Business Recommendations")


    with st.container(border=True):

        st.subheader(
            "🏥 1. Improve Mental-Health Benefits"
        )

        st.write(
            """
            Organizations should provide accessible
            mental-health benefits and clearly communicate
            the support available to employees.
            """
        )


    with st.container(border=True):

        st.subheader(
            "📢 2. Increase Awareness"
        )

        st.write(
            """
            Employers should clearly communicate available
            mental-health resources and care options.
            """
        )


    with st.container(border=True):

        st.subheader(
            "🌱 3. Strengthen Wellness Programs"
        )

        st.write(
            """
            Mental-health awareness can be included as a
            regular component of employee wellness programs.
            """
        )


    with st.container(border=True):

        st.subheader(
            "🧑‍💼 4. Train Managers and Supervisors"
        )

        st.write(
            """
            Managers can receive mental-health awareness and
            communication training to support appropriate
            workplace conversations.
            """
        )


    with st.container(border=True):

        st.subheader(
            "🔐 5. Communicate Confidentiality"
        )

        st.write(
            """
            Organizations should clearly explain how employee
            privacy and anonymity are protected when
            mental-health resources are used.
            """
        )


    with st.container(border=True):

        st.subheader(
            "📋 6. Conduct Periodic Surveys"
        )

        st.write(
            """
            Anonymous employee surveys can help organizations
            monitor workplace perceptions and identify areas
            where support may need improvement.
            """
        )


    # ========================================================
    # CONCLUSION
    # ========================================================

    st.header("📌 Conclusion")

    st.success(
        """
        The Mental Health in Tech Survey highlights important
        differences in treatment-seeking behaviour, family
        history, work interference and workplace mental-health
        support.

        The findings can help organizations identify gaps in
        awareness, benefits, care options, wellness programs
        and workplace communication.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🧠 Mental Health in Tech Survey | "
    "Exploratory Data Analysis Dashboard | "
    "Survey Data: 2014"
)