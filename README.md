# Banana Equifruit Data Pipeline & Dashboard

This repository documents the end-to-end data preparation and visualization process for Equifruit’s supplier analysis. The goal of this project is to clean, transform, and analyze raw data from various sources, and create an insightful Power BI dashboard to support business decisions.

---

## 🚀 Project Workflow

### 1. **Data Cleaning & Exploration**
- Scripts under `.idea/` perform:
  - Dropping empty or redundant columns
  - Schema generation using inferred data types
  - Exploratory Data Analysis (EDA)

### 2. **Data Preprocessing with Spark**
- Located in `Preprocessing/` folder:
  - Spark notebooks join raw tables and apply business logic
  - Output is a cleaned and consolidated dataset ready for reporting

### 3. **Dashboard Creation**
- Located in `UXUI/` folder:
  - Final `.pbix` file contains the Power BI supplier performance dashboard
  - `.ase` file defines Equifruit brand color palette used for consistent styling
  - Excel metadata file maps dashboard fields to underlying schema

---

## 📊 Output

- **Interactive Power BI Dashboard** for supplier performance monitoring  
- **Documented schema** and metadata for data transparency  
- **Reusable preprocessing scripts** for future updates and automation

---

## 🛠️ Tech Stack

- **Python**: Data cleaning, schema generation, and EDA  
- **PySpark**: Table merging and transformation  
- **Power BI**: Data visualization and dashboard development
- **Microsoft Teams**: Project collaboration and communication  
- **GitHub**: Version control and documentation  

---

## 🤝 Team Collaboration

All team communication, file sharing, and coordination for this project are managed through **Microsoft Teams**.  
- Teams serves as the central hub for:
  - Sharing files (e.g., CSVs, PBIX, Python scripts)
  - Documenting and reviewing meeting notes
  - Maintaining organized project workflows  
- This structure ensures smooth collaboration and visibility across the team.



