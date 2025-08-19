# 🌐 Decision Tree: When to Use On-Prem, Cloud, or Hybrid

You can frame this with four key trade-offs:

- **Security & Compliance**  
  If data is highly regulated (e.g., payments, healthcare, customer PII), companies often choose **On-Prem** or **Hybrid**.

- **Latency / Proximity**  
  If workloads need ultra-low latency (e.g., POS systems in stores), **On-Prem/Edge** may be better.

- **Cost**  
  Cloud saves CapEx, but long-running predictable workloads may be cheaper **On-Prem** or with **Reserved Instances**.

- **Scalability / Elasticity**  
  Workloads with unpredictable demand (sales spikes, promotions) are best in **Cloud**.

---

## 💡 Decision Framework

| Workload                 | Sensitive Data? | Low Latency? | Highly Variable Demand? | Long-term Predictable? | Best Fit             |
|--------------------------|:--------------:|:------------:|:----------------------:|:---------------------:|----------------------|
|                          |      Yes       |     –        |           –            |          –            | On-Prem/Hybrid       |
|                          |      –         |    Yes       |           –            |          –            | On-Prem/Edge         |
|                          |      –         |     –        |          Yes           |          –            | Cloud                |
|                          |      –         |     –        |           –            |         Yes           | Reserved/Hybrid      |

---

# 💸 Cloud Costs & Pricing Models

### CapEx vs OpEx (Walmart Analogy):

- **CapEx (Capital Expenditure):**  
  Buying physical servers upfront → like Walmart building its own warehouses.

- **OpEx (Operational Expenditure):**  
  Renting cloud → pay monthly for what you use, like renting trucks only during holiday rush.

---

### Pricing Models

#### 1. Pay-as-you-go (On-Demand)
- Flexible, but most expensive per unit.
- **Use:** Short-lived apps, dev/test.

#### 2. Reserved Instances
- Commit for 1–3 years → cheaper.
- **Use:** Predictable workloads like HR, payroll, always-on databases.

#### 3. Spot Instances (Preemptible VMs in GCP)
- Cheapest, but can be terminated anytime.
- **Use:** Non-critical batch jobs (e.g., ML training overnight).

---

## 💰 Price Comparison Overview

### 1. On-Demand (Pay-as-You-Go)

| Cloud Provider | Example Instance          | Cost/Month    |
|----------------|--------------------------|--------------|
| AWS            | t2.nano (1 vCPU, 512MB)  | ~$4.75       |
| Azure          | B2pts-v2 (2 vCPU, 1GB)   | ~$6.13       |
| GCP            | f1-micro (0.2 vCPU, 0.6GB)| ~$5.55       |

> *Note: These are very small VM examples—use for relative comparisons, not direct sizing.*

---

### 2. Reserved / Committed Cost Models

| Provider | Option                    | Discount      | Flexibility/Notes                      |
|----------|---------------------------|--------------|----------------------------------------|
| AWS      | Reserved Instances        | Up to **72%** | Standard (less flexible), Convertible (swappable), Savings Plans (region/family flexibility) |
|          | Savings Plans             | Up to **72%** | Apply to EC2, Fargate, Lambda – very flexible |
| Azure    | Reserved VM Instances     | Up to **72%** | Scope per resource group, subscription or shared; cancellable up to $50k/year |
|          | Azure Hybrid Benefit      | Up to **40%** | If you bring existing Windows/SQL licenses |
| GCP      | Committed Use Discounts   | Up to **70%** | Project or billing account scoped, no cancellations |
|          | Sustained Use Discounts   | Automatic     | Applied for continuous monthly usage; works alongside CUDs |

---

### 3. Spot / Preemptible Instances

| Provider | Example Instance         | Regular Price/hr | Discounted Price/hr | Discount   | Notes        |
|----------|-------------------------|------------------|---------------------|------------|--------------|
| AWS      | p2.xlarge w/ K80 GPU    | $0.90            | $0.27               | Up to 90%  | 2-min warning|
| Azure    | (Low-priority)          | $0.90            | $0.18               | Up to 80%  | Spot VMs     |
| GCP      | e2-standard-4           | $0.663           | $0.424 (custom)     | Varies     | Preemptible  |

---

## 🏷️ Real-World Comparisons & Insights

**Example:** 4-vCPU, 16GB RAM VMs (Linux)

| Provider | Instance        | Cost/Month |
|----------|----------------|------------|
| Azure    | B4ms           | ~$121      |
| AWS      | t3a.xlarge     | ~$109      |
| GCP      | e2-standard-4  | ~$97       |

**Observations:**
- GCP allows fine-tuning specs to further decrease costs.
- Final cost depends on many factors (discounts, usage, flexibility).

---

## 📊 Summary Table

| Pricing Model          | AWS                | Azure                          | GCP                                    |
|-----------------------|--------------------|-------------------------------|----------------------------------------|
| On-Demand             | ~$4.75/mo (nano)   | ~$6.13/mo (small)             | ~$5.55/mo (micro)                      |
| Reserved / Committed  | Up to 72% off; flexible Savings Plans | Up to 72% off; Hybrid Benefit up to 40% | Up to 70% off (CUDs) + automatic Sustained Use |
| Spot / Preemptible    | ~90% off, interruptible | Up to ~80% off for Spot VMs   | Competitive GPU pricing; preemptible discounts |
| Notes                 | Mature tools, flexible Savings Plans | Good for Windows users, flexible reservations | Simple discounts, automatic and committed |

---