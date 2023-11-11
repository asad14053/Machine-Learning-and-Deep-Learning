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

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

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

############################################################# Deep Learning Prediction ######################################################
# Reason for taking simple model: To save time when server is running
# Improve latency and processing time for prediction of the data from LSTM model

# Convert the timestamp to datetime
df1['timestamp'] = pd.to_datetime(df1['closeTime'], unit='ms')

# Extract relevant columns for time series prediction
ts_df = df1[['timestamp', 'lastPrice']].rename(columns={'timestamp': 'ds', 'lastPrice': 'y'})

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(ts_df['y'].values.reshape(-1, 1))

# Prepare the data for LSTM
training_data_len = int(np.ceil(len(scaled_data) * .95))

train_data = scaled_data[0:int(training_data_len), :]
x_train = []
y_train = []

for i in range(60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(units=50, return_sequences=False))
model.add(Dense(units=25))
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(x_train, y_train, batch_size=1, epochs=1)

# Test data set
test_data = scaled_data[training_data_len - 60:, :]

x_test = []
y_test = ts_df['y'][training_data_len:].values

for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

x_test = np.array(x_test)

x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# Get the model's predicted price values
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

# Evaluate the model
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(f'Root Mean Squared Error (RMSE): {rmse}')

# Plot the data
train = ts_df[:training_data_len]
valid = ts_df[training_data_len:]
valid['Predictions'] = predictions
df5 = valid[['y', 'Predictions']]

# Visualize the data
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date')
plt.ylabel('Close Price USD ($)')
plt.plot(train['y'])
plt.plot(valid[['y', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.savefig('files/prediction.png')
df5.to_csv("files/prediction.csv")
#plt.show()

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
    return 

@app.get('/prediction')
async def trends():
    json_data= df5.to_json(orient="index")
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
