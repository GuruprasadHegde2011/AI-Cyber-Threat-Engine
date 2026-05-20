# Autonomous Network Intrusion Detection Engine (ANIDE)

An enterprise-grade, unsupervised machine learning pipeline engineered to detect zero-day network anomalies and stealthy cyber threats using isolation dynamics. By establishing a behavioral baseline from telemetry logs, the system bypasses traditional signature-based limitations to isolate multi-vector attacks without prior labeling.

---

## 🛠️ System Architecture & Mechanics

The pipeline is split into two distinct operational phases: synthetic telemetry engineering and mathematical isolation scoring.

### 1. Data Engineering Phase (`generator.py`)
Generates a highly imbalanced dataset containing `2,030` telemetry logs simulating an enterprise network environment:
* **Baseline Traffic (2,000 logs):** Low request rates (5–50 req/min), standard payload sizes (0.1–15 MB), and minimal unauthorized port probes.
* **Anomalous Injections (30 logs):** Mimics multi-vector attack profiles including Distributed Denial of Service (DDoS), Exfiltration (high data transfer volume), and Horizontal Port Scanning.

### 2. Machine Learning Phase (`engine.py`)
Utilizes the **Isolation Forest** algorithm. Instead of modeling profiling metrics of normal data points, the algorithm explicitly isolates anomalies by building random decision trees.

$$s(x, n) = 2^{-\frac{E(h(x))}{c(n)}}$$

Where $h(x)$ is the path length of observation $x$, $c(n)$ is the average path length of an unsuccessful search in a Binary Search Tree, and $n$ is the number of external nodes. Anomalies require significantly fewer splits to isolate, resulting in shorter path lengths and an anomaly score closer to $1.0$.

---

## 📊 Core Feature Matrix

The model evaluates four key network dimensions to compute isolation profiles:

| Feature Variable | Metric | Description |
| :--- | :--- | :--- |
| `request_count_per_min` | Integer | Volume of inbound requests to detect brute-force/DDoS signals. |
| `data_transferred_mb` | Float | Payload size tracking outbound data movement to flag exfiltration. |
| `cpu_utilization_pct` | Float | Server processor load indicating processing stress from exploitation. |
| `unauthorized_ports_touched` | Integer | Count of non-whitelisted ports targeted during exploratory scanning. |

---

## 🔬 Performance Analysis & Validation

The system achieves near-perfect classification on highly imbalanced telemetry arrays, ensuring zero false negatives on catastrophic security threats.

```text
================== 🔬 PERFORMANCE ANALYSIS REPORT ==================
               precision    recall  f1-score   support

           0       1.00      1.00      1.00      2000
           1       0.97      1.00      0.98        30

    accuracy                           1.00      2030
   macro avg       0.98      1.00      0.99      2030
weighted avg       1.00      1.00      1.00      2030
====================================================================
---

## 🚀 Deployment & Local Execution

```bash
python generator.py
python engine.py