# FinalProject-DatabaseAutomation
# PROG8850 - Database Automation Project

## Group Members
- **Navneet**
- **Ramanpreet**

## Project Overview
This project implements an automated database management system using **Azure MySQL**, **GitHub Actions**, and **Python**. It focuses on automating database schema changes, data insertion, and query execution, with a focus on performance optimization and monitoring.

---

## GitHub Repository Structure
The repository is structured as follows:

/FinalProject-DatabaseAutomation
  ├── /sql
  │   ├── 1_create_climate_data_table.sql    # SQL to create the ClimateData table
  │   ├── 2_add_humidity_column.sql         # SQL to add the humidity column to the table
  │   ├── 3_seed_climate_data.sql           # SQL to seed climate data
  │   └── 4_validate_climate_data.sql       # SQL to validate inserted data
  ├── /scripts
  │   └── multi_thread_queries.py           # Python script to execute multi-threaded queries
  └── .github
      └── /workflows
          └── ci_cd_pipeline.yml           # GitHub Actions pipeline configuration


---

## Tools and Technologies Required

- **Azure MySQL Database**: A MySQL database hosted on Azure for managing the climate data.
- **Python 3.x**: Required for running the multi-threaded query script.
- **GitHub Actions**: Automates the CI/CD pipeline for deploying schema changes and running queries.
- **Grafana**: For visualizing database performance metrics (optional).
- **Azure Monitor**: For logging and alerting on database metrics.

---

## Prerequisites

1. **Azure Account**: Ensure you have an Azure account to create and manage the MySQL database instance.
2. **GitHub Account**: Required for setting up the GitHub repository and actions.
3. **Python 3.x**: Install Python to run the `multi_thread_queries.py` script for executing concurrent queries.

---

## Repository Secret Setup

To securely store sensitive credentials like database username and password, you need to set up GitHub repository secrets.

1. Go to your repository on GitHub.
2. Click on **Settings** > **Secrets** > **New repository secret**.
3. Add the following secrets:

   - `DB_USERNAME`: MySQL username
   - `DB_PASSWORD`: MySQL password
   - `DB_HOST`: MySQL host (Azure MySQL server)
   - `DB_NAME`: Database name (e.g., `project_db`)

---

## Pipeline Execution

The **CI/CD pipeline** is set up using GitHub Actions to automate the deployment of database schema changes and data seeding.
