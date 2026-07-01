# Context Relevance (Precision Oversight)

Evaluates whether the retrieved context chunks contain only relevant info and exclude noise.

## Architectural Flow
```mermaid
graph TD
    Query & Context --> LLM_Judge[LLM Judge]
    LLM_Judge --> Parse[Identify Key Facts]
    Parse --> Score[Relevance Score]
```

## Mechanism
An LLM analyzes the query and the retrieved context to verify if all retrieved details are useful.
