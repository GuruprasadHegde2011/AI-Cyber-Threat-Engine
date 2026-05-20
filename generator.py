import pandas as pd
import numpy as np

def generate_network_data():
    np.random.seed(42)
    print("📈 Fabricating 2,000 benign baseline network traffic rows...")
    normal_data = {
        'request_count_per_min': np.random.randint(5, 50, 2000),
        'data_transferred_mb': np.random.uniform(0.1, 15.0, 2000),
        'cpu_utilization_pct': np.random.uniform(2.0, 35.0, 2000),
        'unauthorized_ports_touched': np.random.randint(0, 2, 2000),
        'is_anomaly': 0
    }
    df_normal = pd.DataFrame(normal_data)

    print("🚨 Injecting 30 highly stealthy cyber attack records...")
    attack_1 = {
        'request_count_per_min': np.random.randint(10, 30, 10),
        'data_transferred_mb': np.random.uniform(500.0, 2500.0, 10),
        'cpu_utilization_pct': np.random.uniform(10.0, 40.0, 10),
        'unauthorized_ports_touched': np.zeros(10, dtype=int),
        'is_anomaly': 1
    }
    attack_2 = {
        'request_count_per_min': np.random.randint(800, 1500, 10),
        'data_transferred_mb': np.random.uniform(1.0, 5.0, 10),
        'cpu_utilization_pct': np.random.uniform(40.0, 70.0, 10),
        'unauthorized_ports_touched': np.random.randint(15, 50, 10),
        'is_anomaly': 1
    }
    attack_3 = {
        'request_count_per_min': np.random.randint(500, 1200, 10),
        'data_transferred_mb': np.random.uniform(100.0, 300.0, 10),
        'cpu_utilization_pct': np.random.uniform(90.0, 100.0, 10),
        'unauthorized_ports_touched': np.random.randint(2, 8, 10),
        'is_anomaly': 1
    }

    df_attack = pd.concat([pd.DataFrame(attack_1), pd.DataFrame(attack_2), pd.DataFrame(attack_3)], ignore_index=True)
    final_dataset = pd.concat([df_normal, df_attack], ignore_index=True).sample(frac=1).reset_index(drop=True)
    
    final_dataset.to_csv("network_traffic_logs.csv", index=False)
    print("💾 Dataset exported successfully as 'network_traffic_logs.csv'!")

if __name__ == "__main__":
    generate_network_data()