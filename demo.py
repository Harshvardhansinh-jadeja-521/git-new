import pandas as pd

df = pd.read_csv('purchases.csv')
print("Original DataFrame:")
print(df)

df_en=df.copy()
df_en['Gender']=df_en['Gender'].map({'Male':1, 'Female':0})
df_en['Purchased']=df_en['Purchased'].map({'Yes':1, 'No':0})

print("\nLabel Encoded DataFrame:")
print(df_en)

df_city=df_en.copy()
df_city=pd.get_dummies(df_city, columns=['City'], prefix='City')

print("\nOne-Hot Encode DF (City):")
print(df_city)

df_both=df_en.copy()
df_both=pd.get_dummies(df_both, columns=['City','Gender'], prefix=['City','Gender'])

print("\nOne-Hot Encode DF (City & Gender):")
print(df_both)