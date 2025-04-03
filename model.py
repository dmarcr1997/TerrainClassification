from sklearn import tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def create_and_train_model(X_train, X_test, y_train, y_test):
    """Create and train DecisionTree Classifier given train and test data/labels"""
    model = tree.DecisionTreeClassifier()
    model.fit(X_train, y_train)
    
    ## TESTING EVALUATION

    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    
    return model, accuracy, cm, report