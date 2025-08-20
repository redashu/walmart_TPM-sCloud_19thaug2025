# Compute Services (GCE, App Engine)


## Learning Objective
TPMs will understand the trade-offs between VMs and Managed Services regarding:
- Delivery timelines
- Cost implications
- Scalability options

## GCE (Google Compute Engine)
### Overview
- Functions like a virtual data center with raw VM capabilities
- **TPM Focus**: Ideal for lift & shift workloads
    - Provides greater control
    - Longer setup time
    - Higher operational overhead

### Use Case
> Example: Migrating Walmart's legacy on-premises ERP system - GCE provides easier migration path compared to complete rewrite

## GCP App Engine
### Overview
- Fully managed Platform-as-a-Service (PaaS)
- Code-centric deployment model
- Automatic scaling capabilities
    - Handles Black Friday traffic spikes
    - Scales down during low-traffic periods

### TPM Benefits
- Faster time-to-market
- Reduced operational overhead
- Limited customization options

## Azure Equivalents
| GCP Service | Azure Equivalent |
|-------------|-----------------|
| GCE | Azure VM |
| App Engine | Azure App Service |