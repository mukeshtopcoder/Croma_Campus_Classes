from sklearn.svm import SVC

def train_model(X,y,C,kernel):
    model = SVC(C=C , kernel=kernel)
    model.fit(X,y)
    return model
