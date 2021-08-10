import pandas as pd

class CSVDataHandler:
    """
    An application layer to read in the CSV file as Pandas DataFrame and perform CRUD with it.
    The dataframe is to be used with FastAPI
    """
    def __init__(self, filepath:str):
        self.df = pd.read_csv(filepath,  encoding = "ISO-8859-1")
        self.df['CustomerID'] = self.df['CustomerID'].astype(str)
        self.df['InvoiceNo'] = self.df['InvoiceNo'].astype(str)
        self.df['InvoiceDate'] = self.df['InvoiceDate'].astype(str)

    def get_df_info(self):
        return self.df.info()

    def get_df(self):
        return self.df

    def create_new_customer(self, customer_id: str, country: str):
        # [[np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, customer_id, country]]
        self.df = self.df.append({'CustomerID': customer_id, 'Country': country}, ignore_index=True)
        #fill na values with empty string, else errors will occur when we return the json
        self.df.fillna('', inplace=True)
    
    def get_customer_by_id(self, customer_id: str):
        customer = self.df[self.df['CustomerID']==customer_id]
        customer_dict = customer.to_dict('index')
        return customer_dict
    
    def add_new_invoice_to_customer(self, invoice_no: str, invoice_date: str, customer_id: str):
        self.df = self.df.append({'InvoiceNo': invoice_no, 'InvoiceDate': invoice_date, 'CustomerID': customer_id}, ignore_index=True)
        self.df.fillna('', inplace=True)

    def get_customer_by_invoice(self, invoice_no: str):
        customer = self.df[self.df['InvoiceNo']==invoice_no]
        customer_dict = customer.to_dict('index')
        return customer_dict
    
    def get_invoice_by_customer_id(self, customer_id: str):
        customer = self.df[self.df['CustomerID']==customer_id]
        invoices = customer[['InvoiceNo', 'InvoiceDate']]
        invoices_dict = invoices.to_dict('index')
        return invoices_dict
    
    def get_invoice_by_invoice_no(self, invoice_no: str):
        invoice = self.df[self.df['InvoiceNo'] == invoice_no]
        invoice_dict = invoice.to_dict('index')
        return invoice_dict