
# vendor Performance Analysis - Retail Inventory and Sales

Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisiona using SQL,
Python SQLite3 and Power BI.

---

#Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-problem">Business Problem</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools and Technologies</a>
- <a href="#project-Structure">Project Structure</a>
- <a href="#data-cleaning--preparation">Data Cleaning and Preparation</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis(EDA)</a>
- <a href="#research-questions--key-findings">Research Question and Key Findings</a>
- <a href="#dashboard">Dashboard</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#final-recommendation">Final Recommendations</a>
- <a href="#author--contact">Author and Contact</a>

---
<h2><a class="anchor" id ="overview"></a>Overview</h2>

This Project evaluates vendor performance and retail inventory dynamics to drive strategic 
insights for purchasing , pricing and inventory optimization. A complete data pipeline was
built using SQL for ETL, Python for analysis and hypothesis testing , and Power BI
for visualization.

---
<h2><a class="anchor" id ="business-problem"></a>Business Problem</h2>

Effective inventory and Sales management are critical in the retail sector. This Project aims to:
- Identify underperforming brands needing pricing or promotional adjustments
- Determine vendor contributions to sales and profits
- Analyze the cost-benefits of bulk purchasing 
- Investigate inventory turnover inefficiencies
- Statistically validate differences in vendor profitability

---
<h2><a class="anchor" id ="dataset"></a>Dataset</h2>

- Multiple CSV files located in '/data/' folder (sales,vendors,inventory)
- Summary table created from ingested data and used for analysis

---
<h2><a class="anchor" id ="tools--technologies"></a>Tools and Technologies</h2>

-SQl (common Table Expressions , Joins , Filtering)
-Python (Pandas ,Matplotlib,Seaborn , Scipy)
-Power BI (Interactive visualization)
-GitHub

--
<h2><a class="anchor" id ="project-structure"></a>Project Structure</h2>

'''
vendor-performance-analysis/
│
├── README.md
├── .gitignore
├── requirements.txt
├── Vendor Performance Report.pdf
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   ├── vendor_performance_analysis.ipynb
│
├── scripts/
│   ├── ingestion_db.py
│   ├── get_vendor_summary.py
│
├── dashboard/
│   ├── vendor_performance_dashboard.pbix
'''


---
<h2><a class="anchor" id ="data-cleaning--preparation"></a>Data Cleaning and Preparation</h2>

-Removed transaction with:
-Gross Profit <=0
-Profit Margin <=0
-Sales Quantity =0
-Created Summary tables with vendor-level metrics
-Converted data types, handled outliers , merged lookup tables

---
<h2><a class="anchor" id ="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>
**Negative or Zero Values Detected :**
-Gross Profit :Min -52,002.78(loss-making sales)
-Profit Margin: (Sales at zero or below cost)
-Unsold Inventory:Indicating slow-moving stock

**Outliers Identified :**
-High Frieght Costs(up to 257K)
-Large Purchase /Actual prices

**Correlation Analysis:**
-Waek between Purchse Price and Profit 
-Strong between Purchase QTY and Sales Qty(0.999)
-Negative between Profit Margin and Sales Price(-0.179)

---
<h2><a class="anchor" id ="research-questions--key-findings"></a>Research Questions and Key Findings</h2>

1. **Brand for Promotions**: 198 brands with low sales but high profit Margins
2. **Top Vendors**:Top 10 Vendors = 65.69% of purchase - risk of over -reliance 
3.**Bulk Purchasing Impact**: 72% cost savings per unit in large orders

4.**Inventory Turnover**: $2.71M worth of unsold inventory

5.**Vendor Profitability**:
– High Vendors: Mean Margin = 31.17%
– Low Vendors: Mean Margin = 41.55%

6.**Hypothesis Testing**: Statistically significant difference in profit margins ▯ distinct vendor strategies



---
<h2><a class="anchor" id ="dashboard"></a>Dashboard</h2>
-Power BI Dashboard shows:
-Vendor-wise Sales and Margins
-Inventory turnover
-Bulk Purchase Savings
-Performance Heatmap

![Vendor Performance Dashboard](images/dashboard.png)

---
<h2><a class="anchor" id ="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:https://github.com/coderRashi/vendor_performance_analysis_sql_python_powerbi.git
''' bash 
git  Clone
'''
2.Load the CSVs and ingest into database:
'''bash 
pyhton 
'''
3.Create vendor summary table:
''' bash
python
'''
4.Open and run notebooks:
-'notebook
-
5.Open Power BI Dashboard:
-

---
<h2><a class="anchor" id ="final-recommendations"></a>Final Recommendations</h2>
-Diversify vendor base to reduce risk
-Optimize bulk order strategies
-Reprice slow-moving , high - margin brands
-Clear unsold inventory strategically 
-improve marketing for underperforming vendors

---
<h2><a class="anchor" id ="author--contact"></a>Author and Contact</h2>
**Rashi Bongirwar
Data Analyst
Email: bongirwarrashi@gmail.common
Linkeddin: https://www.linkedin.com/in/rashi-bongirwar/
