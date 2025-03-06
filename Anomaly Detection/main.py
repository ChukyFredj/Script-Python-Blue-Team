import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    # Suppose data is a pandas DataFrame with network traffic data
    clf = IsolationForest(contamination=0.05)  # Set contamination to the proportion of anomalies in the data
    clf.fit(data)
    data['anomaly'] = clf.predict(data)
    anomalies = data[data['anomaly'] == -1]
    return anomalies

if __name__ == "__main__":
    # Example data, replace with actual network traffic data
    data = pd.DataFrame({
        'feature1': [10, 20, 15, 23, 50, 12, 45],
        'feature2': [22, 25, 30, 35, 40, 45, 50]
    })
    anomalies = detect_anomalies(data)
    print("Detected anomalies:")
    print(anomalies)
