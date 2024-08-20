import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Pad sequences to ensure uniform length
max_length = max(len(seq) for seq in data_dict['data'])

def pad_sequence(seq, max_length):
    return seq + [0] * (max_length - len(seq))

data_padded = [pad_sequence(seq, max_length) for seq in data_dict['data']]

# Convert to numpy arrays
data = np.asarray(data_padded, dtype=np.float32)
labels = np.asarray(data_dict['labels'])

# Split the data
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize and train the model
model = RandomForestClassifier()
model.fit(x_train, y_train)

# Predict and evaluate
y_predict = model.predict(x_test)
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly!'.format(score * 100))

# Predict probabilities for the test set
y_probabilities = model.predict_proba(x_test)

# Print example probabilities for the first test sample
print('Probabilities for the first test sample:', y_probabilities[0])

# Save the model
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)
