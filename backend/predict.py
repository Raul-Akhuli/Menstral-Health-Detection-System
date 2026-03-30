import sys
from pathlib import Path
import json
import numpy as np
import tensorflow as tf

IMG_SIZE = 224
BASE_DIR = Path(__file__).resolve().parent

# ==========================
# LOAD MODEL
# ==========================
MODEL_PATH = BASE_DIR / "models" / "vgg16_best.keras"

if not MODEL_PATH.exists():
    raise FileNotFoundError("❌ Model not found")

print("✅ Loading model:", MODEL_PATH)
model = tf.keras.models.load_model(MODEL_PATH)

# ==========================
# LOAD CLASS NAMES (FIXED)
# ==========================
CLASS_FILE = BASE_DIR / "models" / "class_names.json"

if CLASS_FILE.exists():
    with open(CLASS_FILE, "r") as f:
        class_names = json.load(f)

else:
    print("⚠️ class_names.json not found, using dataset fallback")

    DATASET_PATH = Path(r"C:\Users\Sibam Das\Downloads\periodic blood image\augmented_highres")

    if not DATASET_PATH.exists():
        raise FileNotFoundError("❌ Dataset path not found")

    class_names = sorted([p.name for p in DATASET_PATH.iterdir() if p.is_dir()])

print("📂 Classes:", class_names)

# ==========================
# PREPROCESS
# ==========================
def preprocess(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img = tf.keras.utils.img_to_array(img) / 255.0
    return np.expand_dims(img, axis=0)

# ==========================
# PREDICT
# ==========================
def predict_image(img_path):
    img = preprocess(str(img_path))
    preds = model.predict(img, verbose=0)[0]

    index = int(np.argmax(preds))
    confidence = float(np.max(preds))

    print("\n📸 Image:", img_path.name)
    print("🔍 Prediction:", class_names[index])
    print(f"📊 Confidence: {confidence * 100:.2f}%")

# ==========================
# MAIN
# ==========================
def main():
    if len(sys.argv) >= 2:
        img_path = Path(sys.argv[1])
    else:
        img_path = Path(input("Enter image path: ").strip('"'))

    img_path = img_path.expanduser().resolve()

    if not img_path.exists():
        raise FileNotFoundError("❌ Image not found")

    predict_image(img_path)

if __name__ == "__main__":
    main()