import pandas as pd
from sklearn import preprocessing

data = pd.read_csv("shopping_data.csv")
df = pd.DataFrame(data)

# Normalisasi Tanpa Library
df["Age"] = df["Age"] / df["Age"].max()
df["Annual_Income"] = df["Annual_Income"] / df["Annual_Income"].max()

# Min-Max
df_normalized_minmax_umur = df["Age"] = (df["Age"] - df["Age"].min()) / (df["Age"].max() - df["Age"].min())
df_normalized_minmax_gaji = df["Annual_Income"] = (df["Annual_Income"] - df["Annual_Income"].min()) / (df["Annual_Income"].max() - df["Annual_Income"].min())

print(df_normalized_minmax_umur)
print(df_normalized_minmax_gaji)

#Z-Score
df_normalized_zscore_umur = df["Age"] = (df["Age"] - df["Age"].mean()) / df["Age"].std()
df_normalized_zscore_gaji = df["Annual_Income"] = (df["Annual_Income"] - df["Annual_Income"].mean()) / df["Annual_Income"].std()

print(df_normalized_zscore_umur)
print(df_normalized_zscore_gaji)


#Menggunakan Library
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("shopping_data.csv")
df = pd.DataFrame(data)

gender = LabelEncoder()
df['Genre'] = gender.fit_transform(df['Genre'])

df = pd.get_dummies(df, columns=['Genre'])

min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(df)
df_normalized = pd.DataFrame(np_scaled, columns=df.columns)

print(df_normalized)

