from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np

class OutlierTrans(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=1.5):
        self.threshold = threshold
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_new = X.copy()
        for col in X_new.columns:
            first_q = X_new[col].quantile(0.25)
            third_q = X_new[col].quantile(0.75)
            interquartile_range = self.threshold * (third_q - first_q)
            outlier_high = interquartile_range + third_q
            outlier_low = first_q - interquartile_range
            X_new.loc[(X_new[col] > outlier_high) | (X_new[col] < outlier_low), col] = np.nan  
        return X_new.values
    
class MakeOrdinal(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_new = X.copy()
        for col in X_new.columns:
            cats = np.sort(X_new[col].unique())
            X_new[col] = X_new.apply(lambda x: int(np.where(cats == x[col])[0]), axis=1)
        return X_new.values
    
class ReplaceVals(BaseEstimator, TransformerMixin):
    def __init__(self, repdict):
        self.repdict = repdict
                                     
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        X_new = X.copy().replace(self.repdict)
        return X_new.values