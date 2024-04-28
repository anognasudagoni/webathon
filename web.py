import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pickle
cast_data = pd.read_csv("C:/Users/anogn/OneDrive/Desktop/webathon/Cast.csv")
bottle_data = pd.read_csv("C:/Users/anogn/OneDrive/Desktop/webathon/Bottle.csv", encoding='ISO-8859-1')
merged_df = pd.merge(bottle_data, cast_data, on='Cst_Cnt', how='inner')

# Define target variable
merged_df['oceanographic_condition'] = ((merged_df['Salnty'] >= 33) & (merged_df['Salnty'] <= 35) &
                                        (merged_df['T_degC'] >= 10) & (merged_df['T_degC'] <= 20) &
                                        (merged_df['R_Depth'] <= 25)).astype(int)

# Features and target
X = merged_df[['R_Depth', 'Salnty', 'Lat_Dec', 'Lon_Dec']]
y = merged_df['oceanographic_condition']

# Train-test split (optional)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Train Random Forest classifier
classifier = RandomForestClassifier(n_estimators=100, random_state=60)
classifier.fit(X, y)

# Save the trained model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(classifier, model_file)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

model.predict([[1,1,11,1]])