import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report

def train_and_detect_threats():
    print("📖 Ingesting telemetry network logs into memory via Pandas...")
    df = pd.read_csv("network_traffic_logs.csv")
    
    features = ['request_count_per_min', 'data_transferred_mb', 'cpu_utilization_pct', 'unauthorized_ports_touched']
    X = df[features]
    y_true = df['is_anomaly'] 
    
    print("🧠 Initializing Unsupervised Isolation Forest Engine...")
    model = IsolationForest(contamination=0.015, random_state=42)
    
    print("🏋️‍♂️ Executing model training matrix calculations...")
    model.fit(X)
    
    print("🎯 Predicting system anomalies...")
    raw_predictions = model.predict(X)
    df['ai_prediction'] = [1 if pred == -1 else 0 for pred in raw_predictions]
    
    print("\n================== 🔬 PERFORMANCE ANALYSIS REPORT ==================")
    print(classification_report(y_true, df['ai_prediction']))
    print("====================================================================")
    
    malicious_discoveries = df[df['ai_prediction'] == 1]
    print(f"\n🚨 AI Alert System flagged {len(malicious_discoveries)} potential malicious threats.")
    print("📋 Sample Matrix of Isolated Suspicious Logs:")
    print(malicious_discoveries[features].head(10))

if __name__ == "__main__":
    train_and_detect_threats()