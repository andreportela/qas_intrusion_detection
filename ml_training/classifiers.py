import sklearn.feature_selection as fs
import sklearn as sk
import pandas as pd

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression

DATASET = "data_collection/labeled_dataset.tab"
LABEL_NAME = "label"
DATE_NAME = "Date"
TIME_NAME = "Time"

def evaluate_classifier(
    X_train, X_test, y_train, y_test, results, classifier_name, classifier_model
):
    classifier_model.fit(X_train, y_train)
    y_pred = classifier_model.predict(X_test)

    # Classifier Evaluation
    return {
        "confusion matrix": sk.metrics.confusion_matrix(y_test, y_pred),
        "accuracy": str(sk.metrics.accuracy_score(y_test, y_pred)),
        "f1 score": str(sk.metrics.f1_score(y_test, y_pred, pos_label="attack")),
        "f2 score": str(
            sk.metrics.fbeta_score(y_test, y_pred, beta=2, pos_label="attack")
        ),
        "mcc": str(sk.metrics.matthews_corrcoef(y_test, y_pred)),
    }


def start():
    # Loading Dataset
    df = pd.read_csv(DATASET, sep=" ")
    print("Dataset loaded: " + str(len(df.index)) + " items")
    y = df[LABEL_NAME]
    y_bin = y

    # Basic Pre-Processing
    attack_labels = df[LABEL_NAME].unique()
    normal_frame = df.loc[df[LABEL_NAME] == "normal"]
    print("Normal data points: " + str(len(normal_frame.index)) + " items ")

    X = df.drop(columns=[LABEL_NAME, DATE_NAME, TIME_NAME])
    X_no_cat = X.select_dtypes(exclude=["object"])
    index_with_nan = X_no_cat.index[df.isnull().any(axis=1)]
    X_no_cat.drop(index_with_nan, 0, inplace=True)
    # Features Ranking
    features_no_cat = X_no_cat.columns
    chi_rank = fs.chi2(X_no_cat, y)
    rank_df = pd.DataFrame({"label": features_no_cat, "rank": chi_rank[0]})
    rank_df = rank_df.sort_values(by=["rank"], ascending=False)

    # Reduced feature set with the best 10 features according to chi2 - based feature selection
    selector = fs.SelectKBest(fs.chi2, k=10)
    selector.fit_transform(X_no_cat, y)
    X_red = X_no_cat.iloc[:, selector.get_support(indices=True)]

    # Training/Testing Classifiers
    X_train, X_test, y_train, y_test = sk.model_selection.train_test_split(
        X_no_cat, y_bin, test_size=0.5, shuffle=True
    )
    classifiers = {
        "RandomForest": RandomForestClassifier(),
        "DecisionTree": DecisionTreeClassifier(),
        "NaiveBayes": GaussianNB(),
        "LDA": LinearDiscriminantAnalysis(),
        "Logistic Regression": LogisticRegression(),
        "kNN": KNeighborsClassifier(n_neighbors=3),
        "AdaBoost": AdaBoostClassifier()
    }

    results = dict()
    for classifier_name, classifier_model in classifiers.items():
        results[classifier_name] = evaluate_classifier(
            X_train, X_test, y_train, y_test, results, classifier_name, classifier_model
        )

    for name, scores in results.items():
        print("---------------------")
        print_metric(name, scores)
    print("---------------------")

def print_metric(name, scores):
    accuracy = "accuracy"
    f1_score = "f1 score"
    f2_score = "f2 score"
    mcc = "mcc"
    confusion_matrix = "confusion matrix"
    score_result = scores[accuracy]
    print(f"{name} {accuracy} {score_result}")
    score_result = scores[f1_score]
    print(f"{name} {f1_score} {score_result}")
    score_result = scores[f2_score]
    print(f"{name} {f2_score} {score_result}")
    score_result = scores[mcc]
    print(f"{name} {mcc} {score_result}")
    score_result = scores[confusion_matrix]
    print(f"{name} {confusion_matrix}")
    print(f"{score_result}")
