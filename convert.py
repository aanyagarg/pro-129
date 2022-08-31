import pandas as pd

data = pd.read_csv("pro129/starsDwarf.csv")

data = data.dropna()
print(data.dtypes)


data["Radius"] = 0.102763*  data["Radius"]

data['Mass']=data['Mass'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

data['Mass'] = 0.000954588* data['Mass']

data.to_csv("pro129/conv_data.csv")