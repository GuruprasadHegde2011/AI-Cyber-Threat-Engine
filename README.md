# AI-Cyber-Threat-Engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

An unsupervised machine learning pipeline designed for real-time anomaly detection and zero-day network attack mitigation[cite: 1]. By moving away from rigid, signature-based detection systems, this engine models baseline network behavior to isolate unknown structural threats before signatures are published[cite: 1].

---

## 🚀 Features

* **Unsupervised Threat Isolation:** Utilizes non-linear isolation structures to catch zero-day exploits without prior training labels[cite: 1].
* **High-Dimensional Feature Engineering:** Extracts dynamic network metrics including packet length variance, inter-arrival times, and TCP flag entropy.
* **Modular Pipeline Architecture:** Built with a strict separation of concerns between data ingestion, preprocessing, modeling, and alerting.

---

## 📐 Mathematical Framework

The core engine leverages an **Isolation Forest** ensemble architecture[cite: 1]. Unlike traditional anomaly detection techniques that attempt to construct a profile of "normal" data points and flag variations, this model explicitly isolates anomalies based on their inherent geometric property: **they are few and different.**

### 1. Path Length and Anomaly Scoring

Anomalies require fewer random splits to isolate in a binary tree structure compared to normal data points. The engine evaluates data instances using a normalized anomaly score $s(x, n)$:

$$s(x, n) = 2^{-\frac{E(h(x))}{c(n)}}$$

Where:
* $h(x)$ is the path length of observation $x$ (the number of edges $x$ traverses from the root node to an external terminating node).
* $E(h(x))$ is the expected value of $h(x)$ across an ensemble of isolation trees.
* $c(n)$ is the average path length of an unsuccessful search in a Binary Search Tree (BST) built over $n$ instances, acting as the normalization factor:

$$c(n) = 2 \ln(n - 1) + 0.5772156649 - \frac{2(n - 1)}{n}$$

### 2. Decision Boundaries
* If the score $s \to 1$, the instance exhibits a significantly short path length across the ensemble and is flagged as an active network threat.
* If $s \ll 0.5$, the observation is deeply integrated into dense clusters, representing safe, baseline network traffic.

---

## 📁 Repository Structure

```text
AI-Cyber-Threat-Engine/
│
├── data/                  # Sample PCAP logs or network traffic datasets
├── src/                   # Core engine source code
│   ├── __init__.py
│   ├── preprocessing.py   # Feature extraction and packet cleaning
│   ├── model.py           # Isolation Forest framework initialization
│   └── main.py            # Execution entry point
├── tests/                 # Automated unit tests
│   └── test_model.py
├── requirements.txt       # Software dependencies
└── README.md              # Project documentation
