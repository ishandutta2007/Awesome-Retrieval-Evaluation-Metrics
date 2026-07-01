# Normalized Discounted Cumulative Gain (NDCG@K)

NDCG is the gold standard for ranked search evaluation using graded relevance labels.

## Architectural Flow
```mermaid
graph TD
    Relevance[Relevance Scores] --> DCG[Compute DCG]
    Relevance --> Sort[Sort Idealy]
    Sort --> IDCG[Compute IDCG]
    DCG & IDCG --> NDCG[DCG / IDCG]
```

## Formulas & Mechanism
$$\text{DCG@K} = \sum_{i=1}^{K} \frac{2^{rel_i} - 1}{\log_2(i + 1)}$$
$$\text{NDCG} = \frac{\text{DCG}}{\text{IDCG}}$$
