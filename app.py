"""
SmartHire AI — Public Demo
A self-contained showcase of the SmartHire AI resume screening platform.
Uses pre-loaded sample data (no live backend, no API keys, no risk).
Deploy free on https://share.streamlit.io
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SmartHire AI — Resume Screening Demo",
    page_icon="🤖",
    layout="wide",
)

# ──────────────────────────────────────────────────────────────────────────
# SAMPLE DATA — 6 jobs, 6 resumes, pre-computed AI-style scores
# ──────────────────────────────────────────────────────────────────────────

JOBS = [
    {
        "id": 1,
        "title": "Senior Java Backend Developer",
        "company": "Google India",
        "location": "Bangalore",
        "skills": ["Java", "Spring Boot", "Kafka", "Elasticsearch", "AWS", "MongoDB", "Microservices", "Docker"],
        "exp": "3-7 years",
        "salary": "₹25L - ₹45L",
    },
    {
        "id": 2,
        "title": "Data Engineer",
        "company": "Flipkart",
        "location": "Bangalore",
        "skills": ["Python", "Spark", "Kafka", "Airflow", "SQL", "AWS", "Hadoop"],
        "exp": "2-5 years",
        "salary": "₹18L - ₹32L",
    },
    {
        "id": 3,
        "title": "Frontend Engineer (React)",
        "company": "Razorpay",
        "location": "Remote",
        "skills": ["React", "TypeScript", "JavaScript", "CSS", "REST API", "Redux"],
        "exp": "1-4 years",
        "salary": "₹12L - ₹24L",
    },
    {
        "id": 4,
        "title": "DevOps Engineer",
        "company": "Microsoft India",
        "location": "Hyderabad",
        "skills": ["Kubernetes", "Docker", "AWS", "Terraform", "CI/CD", "Jenkins", "Linux"],
        "exp": "3-6 years",
        "salary": "₹22L - ₹38L",
    },
    {
        "id": 5,
        "title": "Machine Learning Engineer",
        "company": "Swiggy",
        "location": "Bangalore",
        "skills": ["Python", "TensorFlow", "PyTorch", "MLOps", "SQL", "AWS Sagemaker"],
        "exp": "2-5 years",
        "salary": "₹20L - ₹36L",
    },
    {
        "id": 6,
        "title": "QA Automation Engineer",
        "company": "Infosys",
        "location": "Pune",
        "skills": ["Selenium", "Java", "TestNG", "API Testing", "CI/CD", "Cucumber"],
        "exp": "2-5 years",
        "salary": "₹10L - ₹18L",
    },
]

RESUMES = [
    {
        "id": "r1",
        "name": "Ravi Sharma",
        "role": "Senior Backend Developer",
        "exp_years": 5,
        "skills": ["Java", "Spring Boot", "Apache Kafka", "MongoDB", "MySQL", "REST APIs",
                    "Microservices", "Docker", "Kubernetes", "AWS EC2", "S3", "Elasticsearch", "CI/CD"],
        "education": "B.Tech Computer Science",
        "matched_job_id": 1,
        "score": 98,
        "summary": "Seasoned Senior Backend Developer with 5 years of experience in Java, Spring Boot, "
                    "and cloud technologies. Proven expertise in building scalable backend systems, "
                    "messaging, and search engines.",
    },
    {
        "id": "r2",
        "name": "Priya Nair",
        "role": "Data Engineer",
        "exp_years": 4,
        "skills": ["Python", "Apache Spark", "Kafka", "Airflow", "SQL", "AWS Glue", "Hadoop", "Redshift"],
        "education": "M.Tech Data Science",
        "matched_job_id": 2,
        "score": 94,
        "summary": "Strong data engineering background with hands-on Spark and Kafka pipeline experience "
                    "at scale. Excellent fit for high-throughput data infrastructure roles.",
    },
    {
        "id": "r3",
        "name": "Arjun Mehta",
        "role": "Frontend Developer",
        "exp_years": 2,
        "skills": ["React", "JavaScript", "HTML", "CSS", "Redux", "REST API"],
        "education": "B.Tech Information Technology",
        "matched_job_id": 3,
        "score": 81,
        "summary": "Solid React fundamentals with production experience. Missing TypeScript exposure, "
                    "which is a stated requirement — worth probing in interview.",
    },
    {
        "id": "r4",
        "name": "Sneha Iyer",
        "role": "DevOps Engineer",
        "exp_years": 6,
        "skills": ["Kubernetes", "Docker", "AWS", "Terraform", "Jenkins", "CI/CD", "Linux", "Ansible"],
        "education": "B.E Computer Engineering",
        "matched_job_id": 4,
        "score": 96,
        "summary": "Excellent infrastructure-as-code and container orchestration background. "
                    "Directly matches all core requirements for the DevOps role.",
    },
    {
        "id": "r5",
        "name": "Karthik Rajan",
        "role": "ML Engineer",
        "exp_years": 3,
        "skills": ["Python", "TensorFlow", "Scikit-learn", "SQL", "Pandas", "AWS"],
        "education": "M.Sc Artificial Intelligence",
        "matched_job_id": 5,
        "score": 78,
        "summary": "Good ML fundamentals and Python depth, but limited production MLOps and PyTorch "
                    "exposure relative to the job's requirements.",
    },
    {
        "id": "r6",
        "name": "Ananya Gupta",
        "role": "QA Engineer",
        "exp_years": 3,
        "skills": ["Selenium", "Java", "TestNG", "API Testing", "Postman", "Jenkins"],
        "education": "B.Tech Computer Science",
        "matched_job_id": 6,
        "score": 88,
        "summary": "Strong automation testing background with relevant tooling experience. "
                    "Cucumber/BDD experience not explicitly listed — confirm in screening.",
    },
]


def rank_category(score: int) -> str:
    if score >= 90:
        return "EXCELLENT"
    if score >= 75:
        return "GOOD"
    if score >= 60:
        return "AVERAGE"
    return "POOR"


def rank_color(category: str) -> str:
    return {
        "EXCELLENT": "#16a34a",
        "GOOD": "#2563eb",
        "AVERAGE": "#d97706",
        "POOR": "#dc2626",
    }[category]


# ──────────────────────────────────────────────────────────────────────────
# HEADER
# ──────────────────────────────────────────────────────────────────────────

st.title("🤖 SmartHire AI")
st.subheader("Intelligent Resume Screening & Job Matching Platform")
st.caption(
    "Built with Java Spring Boot · Apache Kafka · MongoDB · MySQL · Elasticsearch · "
    "Google Gemini AI · Apache NiFi"
)
st.info(
    "📌 **This is a public showcase using pre-loaded sample data.** "
    "The real system (shown architecture below) runs the full AI pipeline live. "
    "[View source on GitHub](#) to see the complete working code.",
    icon="ℹ️",
)

st.divider()

# ──────────────────────────────────────────────────────────────────────────
# TABS
# ──────────────────────────────────────────────────────────────────────────

tab1, tab2, tab3 = st.tabs(["🏆 Candidate Rankings", "📋 Job Postings", "📊 Analytics Dashboard"])

# ──────────────────────────────────────────────────────────────────────────
# TAB 1 — RANKINGS (the centerpiece)
# ──────────────────────────────────────────────────────────────────────────

with tab1:
    st.markdown("### Select a job to see AI-ranked candidates")

    job_titles = {j["id"]: f"{j['title']} — {j['company']}" for j in JOBS}
    selected_job_id = st.selectbox(
        "Job Posting", options=list(job_titles.keys()), format_func=lambda x: job_titles[x]
    )
    selected_job = next(j for j in JOBS if j["id"] == selected_job_id)

    st.markdown(
        f"**{selected_job['title']}** · {selected_job['company']} · {selected_job['location']} · "
        f"{selected_job['exp']} · {selected_job['salary']}"
    )
    st.markdown("**Required skills:** " + ", ".join(selected_job["skills"]))
    st.markdown("")

    matched = sorted(
        [r for r in RESUMES if r["matched_job_id"] == selected_job_id],
        key=lambda r: -r["score"],
    )

    if not matched:
        st.warning("No sample candidates pre-loaded for this job. Try 'Senior Java Backend Developer'.")
    else:
        for rank, candidate in enumerate(matched, start=1):
            category = rank_category(candidate["score"])
            color = rank_color(category)
            matched_skills = [s for s in candidate["skills"] if s in selected_job["skills"]]

            with st.container(border=True):
                col1, col2, col3 = st.columns([0.5, 3, 1.2])
                with col1:
                    st.markdown(f"### #{rank}")
                with col2:
                    st.markdown(f"**{candidate['name']}** — {candidate['role']}")
                    st.caption(f"{candidate['exp_years']} years experience · {candidate['education']}")
                    st.markdown(
                        f"<span style='color:{color}; font-weight:600;'>● {category}</span>"
                        f" &nbsp;|&nbsp; Skill match: {len(matched_skills)}/{len(selected_job['skills'])}",
                        unsafe_allow_html=True,
                    )
                with col3:
                    st.metric("Match Score", f"{candidate['score']}/100")

                st.progress(candidate["score"] / 100)
                st.markdown(f"💬 *{candidate['summary']}*")

                with st.expander("View extracted skills"):
                    st.write(", ".join(candidate["skills"]))

# ──────────────────────────────────────────────────────────────────────────
# TAB 2 — JOB POSTINGS
# ──────────────────────────────────────────────────────────────────────────

with tab2:
    st.markdown("### Sample Job Postings")
    st.caption("In the live system, HR creates these via POST /api/jobs — AI scoring kicks in the moment a resume is uploaded against one.")

    for job in JOBS:
        with st.container(border=True):
            c1, c2 = st.columns([3, 1])
            with c1:
                st.markdown(f"**{job['title']}**")
                st.caption(f"{job['company']} · {job['location']} · {job['exp']} · {job['salary']}")
                st.write(", ".join(job["skills"]))
            with c2:
                count = len([r for r in RESUMES if r["matched_job_id"] == job["id"]])
                st.metric("Candidates", count)

# ──────────────────────────────────────────────────────────────────────────
# TAB 3 — ANALYTICS
# ──────────────────────────────────────────────────────────────────────────

with tab3:
    st.markdown("### Dashboard Overview")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Resumes", len(RESUMES))
    c2.metric("Total Jobs", len(JOBS))
    avg_score = sum(r["score"] for r in RESUMES) / len(RESUMES)
    c3.metric("Average Match Score", f"{avg_score:.0f}/100")
    excellent = len([r for r in RESUMES if r["score"] >= 90])
    c4.metric("Excellent Matches", excellent)

    st.markdown("#### Score Distribution")
    buckets = {"EXCELLENT (90-100)": 0, "GOOD (75-89)": 0, "AVERAGE (60-74)": 0, "POOR (<60)": 0}
    for r in RESUMES:
        cat = rank_category(r["score"])
        if cat == "EXCELLENT":
            buckets["EXCELLENT (90-100)"] += 1
        elif cat == "GOOD":
            buckets["GOOD (75-89)"] += 1
        elif cat == "AVERAGE":
            buckets["AVERAGE (60-74)"] += 1
        else:
            buckets["POOR (<60)"] += 1
    st.bar_chart(pd.Series(buckets))

    st.markdown("#### Candidates by Match Score")
    df = pd.DataFrame(
        [
            {
                "Candidate": r["name"],
                "Role": r["role"],
                "Job Applied": next(j["title"] for j in JOBS if j["id"] == r["matched_job_id"]),
                "Score": r["score"],
                "Category": rank_category(r["score"]),
                "Experience (yrs)": r["exp_years"],
            }
            for r in sorted(RESUMES, key=lambda r: -r["score"])
        ]
    )
    st.dataframe(df, use_container_width=True, hide_index=True)

# ──────────────────────────────────────────────────────────────────────────
# FOOTER
# ──────────────────────────────────────────────────────────────────────────

st.divider()
st.markdown(
    "**Architecture:** Resume upload → Spring Boot API → Kafka event → AI scoring "
    "(Google Gemini) → parallel write to MongoDB (resume data), Elasticsearch (search index), "
    "and MySQL (rankings) → real-time dashboard."
)
st.caption("Built as a portfolio project demonstrating event-driven architecture, polyglot persistence, and AI integration.")
