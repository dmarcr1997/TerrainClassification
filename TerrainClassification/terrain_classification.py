from dataset_gen import generate_terrain_dataset
from sklearn.model_selection import train_test_split # Split data 
from model import create_and_train_model, save_model

def main():
    """Generates data to train model, splits it into data/labels, does a train test split for model traing, creates and trains model, and then saves model to pkl file"""
    dataset = generate_terrain_dataset() # Get dataset
    data = [item["data"] for item in dataset] # Retrieve data from dataset
    labels = [item["label"] for item in dataset] # Get labels from dataset
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2) # Split into train test data. 20% of data will be test data
    # print(f"X SIZES - Train: {len(X_train)} | Test: {len(X_test)}")
    # print(f"Y SIZES - Train: {len(y_train)} | Test: {len(y_test)}")
    model, accuracy, cm = create_and_train_model(X_train, X_test, y_train, y_test)

    print(f"Accuracy: {accuracy}")
    print("\nConfusion Matrix:")
    print(cm)
    save_model(model, 'terrain_classification.pkl')

# File entry point to run main function
if __name__ == "__main__":
    main()
    