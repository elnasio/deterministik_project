from datetime import datetime

import numpy as np

from app.core.constants import *
from dataset_builder import generate_dataset
from ml_model import SimpleMLP

# Label encoding
LABELS = [
    "arithmetic",
    "geometric",
    "fibonacci",
    "second_order",
    "factorial",
    "cubic",
    "odd",
    "even",
    "digit_repetition"
]
label_to_index = {label: i for i, label in enumerate(LABELS)}


def pad_sequence(seq, length=6):
    return seq + [0] * (length - len(seq)) if len(seq) < length else seq[:length]


def prepare_data():
    raw_data = generate_dataset() + load_feedback_dataset()
    X, y = [], []
    for item in raw_data:
        padded = pad_sequence(item[SEQUENCE_LABEL])
        label = item["label"]
        if label not in label_to_index:
            continue  # skip data tidak valid
        one_hot = [0] * len(LABELS)
        one_hot[label_to_index[label]] = 1
        X.append(padded)
        y.append(one_hot)
    return np.array(X), np.array(y)


def train():
    X, y = prepare_data()
    model = SimpleMLP(input_size=6, output_size=len(LABELS))
    model.train(X, y, epochs=1000, lr=0.1)
    version = datetime.now().strftime("%Y%m%d%H%M")
    model.save(f"model_weights_{version}.npz")
    model.save("model_weights.npz")  # juga simpan versi latest
    print(f"Model trained and saved as model_weights_{version}.npz")


def load_feedback_dataset():
    import json
    from pathlib import Path
    path = Path("dataset_feedback.json")
    if path.exists():
        with open(path) as f:
            return json.load(f)
    return []


if __name__ == "__main__":
    train()
