# Faithfulness / Groundedness (Hallucination Control)

Ensures that the LLM generation is strictly grounded in the retrieved context.

## Architectural Flow
```mermaid
graph TD
    Response[Generated Answer] --> Sentences[Extract Claims]
    Sentences --> Verify[Check against Context]
    Verify --> Grounded[Grounded / Hallucinated Check]
```

## Mechanism
Calculates the fraction of claims made in the answer that can be directly verified from the context.
