from CSVDataHandler import CSVDataHandler


from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.logger import logger

from pydantic import BaseModel
from typing import Optional

app = FastAPI()
data = CSVDataHandler('data.csv')

class Customer(BaseModel):
    customer_id: str
    country: str

class URLLink(BaseModel):
    url: Optional[str] = None

class Invoice(BaseModel):
    invoice_no: str
    invoice_date: str
    customer: Optional[URLLink] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/customer/add")
async def add_customer(item: Customer):
    #extract data from basemodel
    customer_id = item.customer_id
    country = item.country
    #create data in dataframe
    data.create_new_customer(customer_id, country)
    #encode the created customer item if successful into JSON and return state
    json_compatible_item_data = jsonable_encoder(item)
    return JSONResponse(content=json_compatible_item_data, status_code=200)

#get customer by customer_id
@app.get('/customer/id/{customer_id}')
async def get_customer_by_id(customer_id:str):
    customer_dict = data.get_customer_by_id(customer_id)
    if len(customer_dict)>0:
        #encode into JSON
        json_compatible_item_data = jsonable_encoder(customer_dict)
        return JSONResponse(content=json_compatible_item_data, status_code=200)
    else:
        raise HTTPException(status_code=404, detail="Customer Item not found")

#create invoice for customer
@app.post('/customer/{customer_id}/invoice')
async def add_invoice(customer_id: str, invoice: Invoice):
    invoice.customer.url = f'/customer/id/{customer_id}'
    invoice_json = jsonable_encoder(invoice)
    #invoice_json = {'invoice_no': '11111', 'invoice_date': '2020-01-01', 'customer': {'url': '/customer/id/123456'}}
    invoice_no = invoice_json['invoice_no']
    invoice_date = invoice_json['invoice_date']
    #save data to database
    data.add_new_invoice_to_customer(invoice_no, invoice_date, customer_id)
    #read databack from database
    invoice_customer_dict = data.get_customer_by_invoice(invoice_no)
    if len(invoice_customer_dict) > 0:
        invoice_customer_json = jsonable_encoder(invoice_customer_dict)
        return JSONResponse(content=invoice_customer_json, status_code=200)
    else:
        raise HTTPException(status_code=404, detail='Invoice No. not found')

#get all invoices for customer
@app.get('/customer/{customer_id}/invoice')
async def get_invoice_by_customer_id(customer_id: str):
    invoice_dict = data.get_invoice_by_customer_id(customer_id)
    if len(invoice_dict) > 0:
        invoice_json = jsonable_encoder(invoice_dict)
        return JSONResponse(content=invoice_json, status_code=200)
    else:
        raise HTTPException(status_code=404, detail='Invoices not found')

#get all invoices by invoice id
@app.get('/invoice/{invoice_no}')
async def get_invoice_by_invoice_no(invoice_no: str):
    invoice_dict = data.get_invoice_by_invoice_no(invoice_no)
    if len(invoice_dict) > 0:
        invoice_json = jsonable_encoder(invoice_dict)
        return JSONResponse(content=invoice_json, status_code=200)
    else:
        raise HTTPException(status_code=404, detail='Invoices not found')

