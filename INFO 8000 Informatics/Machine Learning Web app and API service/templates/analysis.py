from fastapi import FastAPI, Request
import requests
import pandas as pd
import schedule

import time
import uvicorn
from pydantic import BaseModel
import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import FileResponse 

# app = FastAPI(root_path="/myapp")

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

def analytical():

    result = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
    dic= result.json()

    df1 = pd.DataFrame(dic)

    df1['priceChangePercent'] = df1['priceChangePercent'].astype(float)
    df1['askPrice'] = df1['askPrice'].astype(float)
    df1['weightedAvgPrice'] = df1['weightedAvgPrice'].astype(float)
    df1['count'] = df1['count'].astype(float)
    df1['priceChange'] = df1['priceChange'].astype(float)
    df1['lastPrice'] = df1['lastPrice'].astype(float)

    df2 = df1.sort_values(by=['priceChangePercent', 'askPrice', 'weightedAvgPrice', 'count'], ascending = [False, False, True, False])
    df21 = df2.iloc[0:1]
    df21

    df3 = df2.sort_values(by =['priceChange', 'lastPrice'], ascending=[False, False]).drop_duplicates(['priceChange'])


    # Problem 5: show last 24 hrs market trends of crypto coin (symbol) business.
    # hint: mask hist plot of postive and negative price change percentage 

    n_bins = 50
    plt.figure()
    heights, bins, _ = plt.hist(df1.priceChangePercent, bins=n_bins) # get positions and heights of bars

    bin_width = np.diff(bins)[0]
    bin_pos = bins[:-1] + bin_width / 2


    mask = (bin_pos >= 0)
    plt.title("Last 24 Hrs Market Trend")
    # plot data in two steps
    plt.bar(bin_pos[mask], heights[mask], width=bin_width, label= 'Price increase', color='C1')
    plt.bar(bin_pos[~mask], heights[~mask], width=bin_width, label= 'Price decrease', color='C0')

    plt.xlabel("Price Change [%]")
    plt.ylabel("Coin Sample")
    plt.legend()
    plt.axvline(x=0, linestyle='--',linewidth=2, color='grey')
    # plt.show()
    plt.savefig('files/trendsx.png')
    print("Hello")
    # return df21.to_html();  

  
schedule.every(1).minutes.do(analytical)
  
while True:
    schedule.run_pending()
    time.sleep(1)