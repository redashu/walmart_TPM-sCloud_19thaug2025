# Build vs Buy Decisions

---

## Scenario

Walmart wants to launch a personalized recommendation system for 100M customers before the holiday season. Should the team build it in-house or buy a managed cloud solution?

---

## Build vs Buy Comparison

| Criteria           | Build In-House (ML Engineers + Infra) | Buy/Cloud Service (Vertex AI / Azure Personalizer) |
|--------------------|---------------------------------------|----------------------------------------------------|
| **Time-to-Market**  | 6–12 months (team setup, model training, infra build) | Days–Weeks (ready APIs)                            |
| **Cost**            | High upfront: salaries, GPUs, storage, pipelines | Pay-per-use (subscription / API calls)             |
| **Performance/Accuracy** | Fully customized to Walmart’s data         | Pre-trained, optimized for general retail          |
| **Maintainability** | Ongoing retraining, infra upkeep, model drift | Vendor manages scaling and updates                   |
| **Flexibility/Lock-in** | Full control, customizable                  | Vendor lock-in, less control                         |

---

## Demo: Cloud Buy Option

- Open GCP Vertex AI → Recommendations AI  
- Open Azure Marketplace → Personalizer  

**Show:**  
- Pre-trained solutions for retail personalization  
- API endpoint ready to integrate  
- Pricing is usage-based  

---

## If We Build In-House

- Hire ML engineers, data scientists, and MLOps team  
- Provision GPU clusters, storage, pipelines  
- Collect and clean large datasets  
- Develop and test models over several months  
- Maintain models against drift and evolving data  

---

## Discussion Question

If leadership asks for a working system before the holiday season (3 months away), what would you recommend and why?

---

## Key Takeaway for TPMs

- No option is universally better.  
- TPMs must facilitate structured discussions around time-to-market, cost, performance, and flexibility.  
- Guide leadership and engineering teams to align on priorities, rather than making the technical choice themselves.