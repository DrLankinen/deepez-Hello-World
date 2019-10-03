import pandas as pd
import requests
import os

df = pd.read_csv('test.csv')
data = df.to_dict('index')
req = requests.post(url="https://api.deepez.com/model/use",json={
    "authorization": os.environ['my deepez token'],
    "model_name": "Hello World",
    "multi": data
},verify=False)
preds = eval(req.json())

preds_new = []
for i in range(1461,2920):
    pred = preds[i-1461]['prediction']
    preds_new.append([i,pred])

pd.DataFrame(preds_new,columns=['Id','SalePrice']).to_csv('preds.csv',index=False)
