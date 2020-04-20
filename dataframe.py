import pandas as pd


web_xys={"Days":[1,2,3,4,5],"Visitor":[123,258,369,789,456],"Bounce_rate":[12,36,12,32,14]}


df=pd.DataFrame(web_xys)
print(df)
