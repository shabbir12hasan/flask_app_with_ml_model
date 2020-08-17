import pandas as pd
import numpy as np



df = {
    "length":np.random.randint(low=1,high=10, size=10)
    ,"height":np.random.randint(low=1,high=10, size=10)
    ,"width":np.random.randint(low=1,high=10, size=10)
}

df = pd.DataFrame(df)

# test model
from sklearn.linear_model import LogisticRegression
X=df[['length','height']]
y=df['width']
clf = LogisticRegression().fit(X,y)
clf.predict(X)

# storing model
from io import BytesIO
import dill as pickle

bytes = BytesIO()
pickle.dump(clf, bytes)
bytes.seek(0)

with open('bin/logreg_model.pkl','wb') as f:
    f.write(bytes.read())

# reading model
from io import BytesIO
import dill as pickle
log_reg = open('bin/logreg_model.pkl' ,'rb')
model = pickle.load(log_reg)
model.predict([[3,4]])
