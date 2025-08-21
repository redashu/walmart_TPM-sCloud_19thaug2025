# CAP Theorem in Cloud (Azure & GCP Examples)

The CAP theorem says that in a distributed system, you can only strongly guarantee two out of three:

- Consistency
- Availability
- Partition Tolerance

Since cloud systems are distributed across regions/zones, Partition Tolerance (P) is a must → so you're usually choosing between C and A.

## Azure & GCP Mapping

| CAP Property | What It Means | Azure Example | GCP Example | When It's Used |
|--------------|---------------|---------------|-------------|----------------|
| Consistency (C) | All users see the same data immediately, no stale reads. | Azure Cosmos DB (Strong Consistency mode) | Cloud Spanner (Strong mode) | Financial apps, banking, inventory mgmt (no tolerance for stale data). |
| Availability (A) | System always responds, even if some data may be slightly outdated. | Azure Cosmos DB (Eventual Consistency mode) | Cloud Datastore / Firestore (Eventual Consistency) | Social media feeds, messaging apps, analytics dashboards. |
| Partition Tolerance (P) | System continues working despite network splits or region failures. | Built into Cosmos DB Global Distribution | Built into Spanner / Bigtable with multi-region setup | Always needed for cloud systems spanning zones/regions. |



===>
🔸 Real-World TPM-Level Explanation

If you pick Consistency + Partition Tolerance (CP) → During a failure, the system may reject requests to avoid stale data. (e.g., a payment transaction system).

If you pick Availability + Partition Tolerance (AP) → The system will always serve requests, but users might see slightly stale data. (e.g., user profile updates in a social network).