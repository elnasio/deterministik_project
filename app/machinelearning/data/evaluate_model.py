import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

from app.core.constants import *
from dataset_builder import generate_dataset
from ml_model import SimpleMLP
from train_model import pad_sequence, load_feedback_dataset, LABELS

label_to_index = {label: i for i, label in enumerate(LABELS)}


def prepare_eval_data():
    raw_data = generate_dataset() + load_feedback_dataset()
    X, y_true = [], []
    for item in raw_data:
        padded = pad_sequence(item[SEQUENCE_LABEL])
        label = item["label"]
        if label not in label_to_index:
            continue
        X.append(padded)
        y_true.append(label_to_index[label])
    return np.array(X), np.array(y_true)


def evaluate():
    X, y_true = prepare_eval_data()
    model = SimpleMLP(input_size=6, output_size=len(LABELS))
    model.load("model_weights.npz")
    probs = model.predict(X)
    y_pred = np.argmax(probs, axis=1)
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=LABELS))


if __name__ == "__main__":
    evaluate()
