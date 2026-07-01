# Automated Corporate E-Discovery & Legal Audit Verification

Using retrieval systems to extract evidence or audit files in compliance investigations.

## Architectural Flow
```mermaid
graph TD
    LegalDocs[Legal Documents] --> CrossEncoder[Cross-Encoder Reranker]
    CrossEncoder --> LLM_Auditor[LLM Auditor Agent]
    LLM_Auditor --> Compliant[Verified Evidence Report]
```

## Application Details
Relies heavily on high-recall configurations with verification stages to prevent missed evidence.
