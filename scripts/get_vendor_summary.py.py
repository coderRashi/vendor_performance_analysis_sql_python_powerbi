import  sqlite3
import pandas as pd
import logging
from ingestion_db import ingest_db

logging.basicConfig(
    filename="logs/get_vendor_summary.log",
    level=logging.DEBUG,
    format = "%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

   
def create_vendor_summary(conn):
    ''' this function will merge the different tables to get the overall vendor summary and adding new colums in the resultant data'''
    vendor_sales_summary = pd.read_sql_query("""WITH FreightSummary As(
    Select
        VendorNumber,
        SUM(Freight) AS FreightCost
    From vendor_invoice
    Group by VendorNumber
    ),
    
    PurchaseSummary AS (
       SELECT 
           P.VendorNumber, 
           P.VendorName,
           P.Brand,
           P.Description,
           P.PurchasePrice,
           pp.Price As ActualPrice,
           pp.Volume,
           SUM(P.Quantity) AS TotalPurchaseQuantity,
           SUM(P.Dollars) AS TotalPurchaseDollars
       From purchases P
       JOIN purchase_prices pp
            ON P.Brand = pp.Brand
       Where P.PurchasePrice > 0 
       Group BY P.VendorNumber , P.VendorName , P.Brand , P.Description , P.PurchasePrice , pp.Price , pp.Volume),
       
       SalesSummary AS (
        SELECT
           VendorNo,
           Brand,
           SUM(SalesQuantity) AS TotalSalesQuantity,
           SUM(SalesDollars) AS TotalSalesDollars,
           SUM(SalesPrice) AS TotalSalesPrice,
           Sum(ExciseTax) AS TotalExciseTax
        FROM sales
        Group by VendorNo, Brand
        )
    
        SELECT
        ps.VendorNumber,
        ps.VendorName,
        ps.Brand,
        ps.Description,
        ps.PurchasePrice,
        ps.ActualPrice,
        ps.Volume,
        ps.TotalPurchaseQuantity,
        ps.TotalPurchaseDollars,
        ss.TotalSalesQuantity,
        ss.TotalSalesDollars,
        ss.TotalSalesPrice,
        ss.TotalExciseTax,
        fs.FreightCost
    From PurchaseSummary ps
    LEFT JOIN SalesSummary ss
         ON ps.VendorNumber = ss.VendorNo
         AND ps.Brand = ss.Brand
    LEFT JOIN FreightSummary fs
         ON ps.VendorNumber = fs.VendorNumber
    ORDER BY ps.TotalpurchaseDollars DESC """,conn) 
    
    return vendor_sales_summary

def clean_data(df):
    '''this function will clean the data'''
    # changing datatype to float
    df['Volume'] = df['Volume'].astype('float')

    # filling missing value with 0
    df.fillna (0,inplace = True)

    # removing spaces from categorial columns
    df['VendorName'] = df['VendorName'].str.strip()
    df['Description'] = df ['Description'].str.strip()


    #  Creating new columns for better analysis
    # df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    # df['ProfitMargin'] = (df['GrossProfit']/df['TotalSalesDollars'])*100
    # df['StockTurnover'] = df['TotalSalesQuantity']/df['TotalPurchaseQuantity']
    # df['StockPurchaseRatio']= df['TotalSalesDollars']/df['TotalPurchaseDollars']

    vendor_sales_summary['GrossProfit'] = vendor_sales_summary['TotalSalesDollars'] - vendor_sales_summary['TotalPurchaseDollars']
    vendor_sales_summary['ProfitMargin'] = (vendor_sales_summary['GrossProfit']/vendor_sales_summary['TotalSalesDollars'])*100
    vendor_sales_summary['StockTurnover'] = vendor_sales_summary['TotalSalesQuantity']/vendor_sales_summary['TotalPurchaseQuantity']
    vendor_sales_summary['StockPurchaseRatio']= vendor_sales_summary['TotalSalesDollars']/vendor_sales_summary['TotalPurchaseDollars']

    return df 

if __name__ == "__main__":

    # import os
    # os.makedirs("logs", exist_ok=True)
    
    conn = sqlite3.connect('inventorys.db')
    
    logging.info ('Creating Vendor Summary Table.....')
    summary_df = create_vendor_summary(conn)
    logging.info(summary_df.head())


    logging.info ('Cleaning Data.....')
    clean_df = clean_data(summary_df)
    logging.info(clean_df.head())

    logging.info('Ingesting data....')
    ingest_db(clean_df,'vendor_sales_summary',conn)
    logging.info('Completed')

    # Read the table into a DataFrame
df = pd.read_sql_query("SELECT * FROM vendor_sales_summary", conn)

print(df.head())   # display first 5 rows

    
    

