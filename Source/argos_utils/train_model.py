from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from argos_common import load_config, ARGOS_HOME, ARGOS_CONFIG
import pickle

if __name__ == "__main__":
    config = load_config(ARGOS_CONFIG, "embeddingsExtractor")
    data = pickle.loads(
        open(
            ARGOS_HOME + config["face_embeddings_directory"] + "embeddings.pickle", "rb"
        ).read()
    )

    print("[INFO] encoding lables...")
    label_encoder = LabelEncoder()
    labels = label_encoder.fit_transform(data["names"])

    print("[INFO] training model...")
    recognizer = SVC(C=1.0, kernel="linear", probability=True)
    recognizer.fit(data["embeddings"], labels)

    open(config["face_embeddings_directory"] + "recognizer.pickle", "wb").write(
        pickle.dumps(recognizer)
    ).close()

    open(config["face_embeddings_directory"] + "label_encoder.pickle", "wb").write(
        pickle.dumps(label_encoder)
    ).close()
