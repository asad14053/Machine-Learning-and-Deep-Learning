from fastapi import FastAPI, Request
import requests
import pandas as pd
import schedule
import time
import uvicorn
import json
import matplotlib.pyplot as plt
import numpy as np
import io
from pydantic import BaseModel

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse 
from fastapi.responses import StreamingResponse

# app = FastAPI(root_path="/myapp")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

#Problem 1: For this assignment, we are going to use the binance crypto currency in last 24 hrs trend price change statistics api (https://binance-docs.github.io/apidocs/spot/en/#24hr-ticker-price-change-statistics) to practice calling external APIs, and using the results
# get the json and save it to a dictionaries in python

result = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
dic= result.json()

#Problem 2: Save 24 hrs cypto trend to a dataframe
df1 = pd.DataFrame(dic)

#Problem 3: find out the most trustworthy gainer coin (symbol) as a seller
# hint: (show the symbols (coin)) who has got highest percentage increase (priceChangePercent) with maximum asking price quantity, lowest weighted avegage, highest (coin) symbol count)
df1['priceChangePercent'] = df1['priceChangePercent'].astype(float)
df1['askPrice'] = df1['askPrice'].astype(float)
df1['weightedAvgPrice'] = df1['weightedAvgPrice'].astype(float)
df1['count'] = df1['count'].astype(float)
df1['priceChange'] = df1['priceChange'].astype(float)
df1['lastPrice'] = df1['lastPrice'].astype(float)

df2 = df1.sort_values(by=['priceChangePercent', 'askPrice', 'weightedAvgPrice', 'count'], ascending = [False, False, True, False])
df21 = df2.iloc[0:1].T

# Problem 4: get the top most name of coin (symbol) info in each price change segment within last 24 hrs
# hint: just find the name of top symbol from each price change with highest previous close price
df3 = df2.sort_values(by =['priceChange', 'lastPrice'], ascending=[False, False]).drop_duplicates(['priceChange'])
df4 = df3[['symbol','priceChange', 'priceChangePercent','lastPrice']]

# Problem 5: show last 24 hrs market trends of crypto coin (symbol) business.
# hint: mask hist plot of postive and negative price change percentage 
n_bins = 50
plt.figure()
heights, bins, _ = plt.hist(df1.priceChangePercent, bins=n_bins) # get positions and heights of bars

bin_width = np.diff(bins)[0]
bin_pos = bins[:-1] + bin_width / 2


mask = (bin_pos >= 0)
plt.title("24 Hrs Market Trend")
# plot data in two steps

plt.bar(bin_pos[mask], heights[mask], width=bin_width, label= 'Price increase', color='C2')
plt.bar(bin_pos[~mask], heights[~mask], width=bin_width, label= 'Price decrease', color='C1')

plt.xlabel("Price Change [%]")
plt.ylabel("Coin Sample")
plt.legend()
plt.axvline(x=0, linestyle='--',linewidth=1, color='black')
# plt.show()
plt.savefig('files/trends.png')

x1 = heights[mask]
x2 = heights[~mask]
y= np.array([45,55])
mylabels = ["Price Increase", "Price Decrease"]
myexplode = [0.2, 0]

plt.figure()
# plt.title("Today Market Trend")
plt.pie(y, labels = mylabels, explode = myexplode, colors= ['C2', "C1"], shadow = False)
plt.savefig('files/pie.png')

df2.to_csv("files/gainer_coin.csv")
df4.to_csv("files/each_price_change_catagory.csv")

app = FastAPI(root_path="/")
# app.mount("/", StaticFiles(directory="/"), name="/")
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/files", StaticFiles(directory="files"), name="files")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
templates = Jinja2Templates(directory="templates")

class Data(BaseModel):
    symbol: str
    priceChangePercent: float
    count: float


# to_predict_dict = df41.to_dict()
# r = requests.post(url, json=to_predict_dict)

#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#return HTMLResponse(content=content)

json_data1 = ""
json_data2 = ""

@app.get('/')
async def home():
    #content = """<body>24 Hrs Coin Base Trends</body>"""
    #return HTMLResponse(content=content)
    #return templates.TemplateResponse("/home.html", {"request": request})
    with open("files/gainer_coin.json", "w") as outfile1:
        json_data1= df21.to_json(orient="index")
        json_data1= json_data1.replace("\'","")
        json.dump(json_data1, outfile1)
    with open("files/each_price_change_catagory.json", "w") as outfile2:
        json_data2= df4.to_json(orient="index")
        json_data2= json_data2.replace("\'","")
        json.dump(json_data2, outfile2)
    return FileResponse('static/home.html')

@app.get('/gainer_coin')
async def trends():
    json_data= df21.to_json(orient="index")
    return json_data

@app.get('/each_price_change_catagory')
async def trends():
    json_data= df4.to_json(orient="index")
    return json_data

@app.get("/gainer_coin_files")
async def get_csv():
    df = df2
    stream = io.StringIO()
    df.to_csv(stream, index = False)
    response = StreamingResponse(iter([stream.getvalue()]),
                            media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=gainer_coin.csv"
    return response

@app.get("/each_price_change_catagory_files")
async def get_csv():
    df = df4
    stream = io.StringIO()
    df.to_csv(stream, index = False)
    response = StreamingResponse(iter([stream.getvalue()]),
                            media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=each_price_change_catagory.csv"
    return response






