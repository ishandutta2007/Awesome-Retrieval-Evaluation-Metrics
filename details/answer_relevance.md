# Answer Relevance (Semantic Alignment)

Measures if the generated answer directly addresses the user query.

## Architectural Flow
```mermaid
graph TD
    Query & Answer --> GenQueries[Synthesize Query from Answer]
    GenQueries --> Similarity[Semantic Similarity Check]
    Similarity --> Score[Answer Relevance Score]
```

## Mechanism
LLMs generate hypothetical questions for the answer, and measure similarity to the original query.
