import os
import tensorflow as tf
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# ==========================
# CONFIG
# ==========================
IMG_SIZE = 224
BATCH_SIZE = 32

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ==========================
# DATASET PATH
# ==========================
VAL_DIR = r"C:\Users\Sibam Das\Downloads\periodic blood image\augmented_highres"

if not os.path.exists(VAL_DIR):
    raise FileNotFoundError(f"❌ Dataset not found: {VAL_DIR}")

print("📁 Using dataset:", VAL_DIR)

# ==========================
# LOAD DATASET
# ==========================
try:
    val_ds = tf.keras.utils.image_dataset_from_directory(
        VAL_DIR,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        label_mode="categorical",
        shuffle=False
    )
except Exception as e:
    raise RuntimeError(f"❌ Error loading dataset: {e}")

class_names = val_ds.class_names
print("📂 Classes:", class_names)

# ==========================
# NORMALIZATION
# ==========================
val_ds = val_ds.map(lambda x, y: (tf.cast(x, tf.float32) / 255.0, y))

# ==========================
# MODEL PATH DETECTION
# ==========================
MODEL_PATHS = [
    os.path.join(BASE_DIR, "models", "vgg16_best.keras"),
    os.path.join(BASE_DIR, "vgg16_best.keras"),
]

MODEL_PATH = None
for path in MODEL_PATHS:
    if os.path.exists(path):
        MODEL_PATH = path
        break

if MODEL_PATH is None:
    raise FileNotFoundError(
        "❌ Model not found.\n"
        "👉 Put model in:\n"
        "   models/vgg16_best.keras OR\n"
        "   vgg16_best.keras"
    )

print("✅ Using model:", MODEL_PATH)

# ==========================
# LOAD MODEL
# ==========================
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"❌ Error loading model: {e}")

# ==========================
# EVALUATION
# ==========================
y_true = []
y_pred = []

print("\n🚀 Evaluating model...\n")

for images, labels in val_ds:
    try:
        preds = model.predict(images, verbose=0)

        y_true.extend(np.argmax(labels.numpy(), axis=1))
        y_pred.extend(np.argmax(preds, axis=1))

    except Exception as e:
        print(f"⚠️ Skipping batch due to error: {e}")

# ==========================
# CHECK EMPTY RESULT
# ==========================
if len(y_true) == 0:
    raise RuntimeError("❌ No predictions generated. Check dataset/model.")

# ==========================
# RESULTS
# ==========================
print("\n📊 Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))

print("\n📊 Classification Report:")
print(classification_report(y_true, y_pred, target_names=class_names))