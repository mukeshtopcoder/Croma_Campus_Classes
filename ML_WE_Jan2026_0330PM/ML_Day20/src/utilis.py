from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def evaluate_model(y_pred,y_test):
    acc = accuracy_score(y_pred,y_test)
    cr  = classification_report(y_pred,y_test)
    cm  = confusion_matrix(y_pred,y_test)
    return acc,cr,cm
