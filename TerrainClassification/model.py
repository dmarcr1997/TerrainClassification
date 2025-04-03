from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

def create_and_train_model(X_train, X_test, y_train, y_test):
    """Create and train DecisionTree Classifier given train and test data/labels"""

    # Create model 
    model = tree.DecisionTreeClassifier(
        max_depth=3, # Tree can only split into a max of 3 to help with generalization and stop overfitting
        min_samples_split=10, # Only split tree if node has 10 samples
        min_samples_leaf=5 # No leaf node unless it has 5 samples
    )
    ## MODEL TRAIN

    model.fit(X_train, y_train) # Fit model on training data
    
    ## TESTING EVALUATION

    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    # How well model does on predictions
    # Shows: correctly predicted, and count of false positives / false negatives
    cm = confusion_matrix(y_test, y_pred)
    
    return model, accuracy, cm

def save_model(model, filename='terrain_model.pkl'):
    """Save the model to a pickle file"""
    # Open file to write binary data to
    with open(filename, 'wb') as f: 
        # Save model to file
        pickle.dump(model, f)
    print(f"MODEL SAVED TO: {filename}")

def load_model(filename='terrain_model.pkl'):
    """Load a trained model from a file"""
    try:
        # open file as readable binary
        with open(filename, 'rb') as f:
            # load model
            model = pickle.load(f)
        print(f"MODEL LOADED: {filename}")
        return model
    # If model not found log an error
    except FileNotFoundError:
        print(f"File does not exist: {filename}")
        return None