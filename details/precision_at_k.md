# Binary Precision at K (P@K)

Precision at K measures the percentage of relevant documents in the top $K$ results.

## Architectural Flow
```mermaid
graph TD
    TopK[Top K Documents] --> Count[Count Relevant]
    Count --> Divide[Divide by K]
    Divide --> Score[P@K Score]
```

## Formulas & Mechanism
$$\text{Precision@K} = \frac{\text{Relevant Documents in Top K}}{K}$$

### Pros & Cons
- **Pros**: Easy to explain, simple computation.
- **Cons**: Extremely sensitive to the choice of $K$, and rank-blind within the top $K$ list.
