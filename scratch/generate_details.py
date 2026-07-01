import os

details_dir = r"C:\Users\ishan\Documents\Projects\Awesome-Retrieval-Evaluation-Metrics\details"
os.makedirs(details_dir, exist_ok=True)

pages = [
    {
        "filename": "unranked_set_era.md",
        "title": "The Un-ranked Set Era (Classical Information Retrieval, ~1960s–1990s)",
        "content": """# The Un-ranked Set Era (Classical Information Retrieval, ~1960s–1990s)

During the dawn of computerized document indexing, information retrieval (IR) systems treated search results as unordered sets of documents rather than ranked lists. Users would input Boolean queries, and the system would return a bucket of matching documents.

## Architectural Flow
```mermaid
graph TD
    Query[User Query] --> Engine[Retrieval Engine]
    Engine --> Matches[Unordered Set of Matches]
    Matches --> Relevant[Relevant Docs Group]
    Matches --> Irrelevant[Irrelevant Docs Group]
```

## Detailed Explanation
In this era, systems were evaluated using binary intersections:
- **Precision**: The proportion of retrieved documents that are relevant.
  $$\\text{Precision} = \\frac{|\\text{Relevant} \\cap \\text{Retrieved}|}{|\\text{Retrieved}|}$$
- **Recall**: The proportion of relevant documents that were successfully retrieved.
  $$\\text{Recall} = \\frac{|\\text{Relevant} \\cap \\text{Retrieved}|}{|\\text{Relevant}|}$$

### Key Limitations
- **Rank Blindness**: It treated all retrieved documents as equally positioned. If a perfect document was at index 50, it contributed the same to the score as if it were at index 1.
- **Set Size Dependency**: High variance based on the number of returned items.
"""
    },
    {
        "filename": "rank_sensitive_position_era.md",
        "title": "The Rank-Sensitive Position Era (~1990s–2010s)",
        "content": """# The Rank-Sensitive Position Era (~1990s–2010s)

With the explosion of web search engines (Yahoo, early Google, etc.), user focus shifted heavily towards the top of the search result page. The order in which results were returned became critical.

## Architectural Flow
```mermaid
graph TD
    Query[User Query] --> Ranker[Ranker / Sorting Engine]
    Ranker --> L1[Rank 1: Critical Result]
    Ranker --> L2[Rank 2: Secondary Result]
    Ranker --> L3[Rank 3: Less Relevant Result]
```

## Detailed Explanation
Metrics evolved to track position order:
- **Mean Reciprocal Rank (MRR)**: Focuses on the first relevant result.
- **Mean Average Precision (MAP)**: Averages precision values at each step where a relevant document is retrieved.

### Key Limitations
- **Binary Boundaries**: Still relied on binary relevance (either a document is 100% relevant or 0% relevant).
- **No Graded Utility**: Cannot capture nuances like 'partially relevant' documents.
"""
    },
    {
        "filename": "continuous_relevance_era.md",
        "title": "The Continuous Relevance & Discounted Gain Era (~2000s–2022)",
        "content": """# The Continuous Relevance & Discounted Gain Era (~2000s–2022)

To accommodate graded relevance and position decay, researchers introduced discounted gain matrices, culminating in the widespread adoption of NDCG.

## Architectural Flow
```mermaid
graph TD
    Rank[Result List] --> LogDecay[Logarithmic Discount Function]
    LogDecay --> Normalized[Normalized Score 0-1]
```

## Detailed Explanation
- **Discounted Cumulative Gain (DCG)**: Graded relevance points are discounted logarithmically as rank increases.
- **Normalized Discounted Cumulative Gain (NDCG)**: Normalizes DCG against an Ideal DCG (IDCG).

### Key Significance
Allows search engines to be optimized for highly fine-grained relevance judgements (e.g. scale of 0 to 3).
"""
    },
    {
        "filename": "model_driven_rag_alignment_era.md",
        "title": "The Model-Driven RAG Alignment Era (~2023–Present)",
        "content": """# The Model-Driven RAG Alignment Era (~2023–Present)

Modern RAG pipelines require evaluating the semantic alignment between queries, retrieved contexts, and generated answers. Standard lexical overlap metrics (like ROUGE or BLEU) fail here.

## Architectural Flow
```mermaid
graph LR
    Query --> VectorDB[Vector Database]
    VectorDB --> Context[Retrieved Chunks]
    Context --> LLM[LLM Response Generator]
    LLM --> Judge[LLM-as-a-Judge Eval]
```

## Detailed Explanation
LLM-as-a-Judge metrics (Ragas, TruLens, ARES) evaluate:
- **Context Relevance**
- **Faithfulness / Groundedness**
- **Answer Relevance**
"""
    },
    {
        "filename": "precision_at_k.md",
        "title": "Binary Precision at K (P@K)",
        "content": """# Binary Precision at K (P@K)

Precision at K measures the percentage of relevant documents in the top $K$ results.

## Architectural Flow
```mermaid
graph TD
    TopK[Top K Documents] --> Count[Count Relevant]
    Count --> Divide[Divide by K]
    Divide --> Score[P@K Score]
```

## Formulas & Mechanism
$$\\text{Precision@K} = \\frac{\\text{Relevant Documents in Top K}}{K}$$

### Pros & Cons
- **Pros**: Easy to explain, simple computation.
- **Cons**: Extremely sensitive to the choice of $K$, and rank-blind within the top $K$ list.
"""
    },
    {
        "filename": "mrr.md",
        "title": "Mean Reciprocal Rank (MRR)",
        "content": """# Mean Reciprocal Rank (MRR)

MRR measures the system's ability to return the first correct answer as early as possible.

## Architectural Flow
```mermaid
graph TD
    Query[User Query] --> Results[Ranked List]
    Results --> First[Find First Relevant at Rank k]
    First --> Score[Score = 1/k]
```

## Formulas & Mechanism
$$\\text{MRR} = \\frac{1}{M} \\sum_{i=1}^{M} \\frac{1}{k_i}$$

### Applications
Used in FAQ engines, e-commerce product finders, and QA systems.
"""
    },
    {
        "filename": "ndcg.md",
        "title": "Normalized Discounted Cumulative Gain (NDCG@K)",
        "content": """# Normalized Discounted Cumulative Gain (NDCG@K)

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
$$\\text{DCG@K} = \\sum_{i=1}^{K} \\frac{2^{rel_i} - 1}{\\log_2(i + 1)}$$
$$\\text{NDCG} = \\frac{\\text{DCG}}{\\text{IDCG}}$$
"""
    },
    {
        "filename": "context_relevance.md",
        "title": "Context Relevance (Precision Oversight)",
        "content": """# Context Relevance (Precision Oversight)

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
"""
    },
    {
        "filename": "faithfulness_groundedness.md",
        "title": "Faithfulness / Groundedness (Hallucination Control)",
        "content": """# Faithfulness / Groundedness (Hallucination Control)

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
"""
    },
    {
        "filename": "answer_relevance.md",
        "title": "Answer Relevance (Semantic Alignment)",
        "content": """# Answer Relevance (Semantic Alignment)

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
"""
    },
    {
        "filename": "agentic_llm_eval_cost.md",
        "title": "The High Cost and Latency of Agentic LLM Evaluation",
        "content": """# The High Cost and Latency of Agentic LLM Evaluation

Evaluating millions of production queries using advanced LLMs (like GPT-4) is cost-prohibitive.

## Architectural Flow
```mermaid
graph TD
    Logs[Production Logs] --> DistilledModel[Distilled 8B Judge]
    Logs --> TokenProxies[Bi-Encoder Token Proxies]
    DistilledModel & TokenProxies --> EvalSuite[Evaluation System]
```

## Mitigation
- Using lightweight, domain-specific evaluator models (e.g. Prometheus).
- Real-time heuristic proxies before batch judging.
"""
    },
    {
        "filename": "data_contamination_label_decay.md",
        "title": "The Data Contamination and Static Label Decay Wall",
        "content": """# The Data Contamination and Static Label Decay Wall

Static validation datasets decay rapidly as production data distributions change.

## Architectural Flow
```mermaid
graph TD
    ProdTraffic[Production Traffic] --> SynthGen[Automated Synthetic Test Generator]
    SynthGen --> DynamicMatrix[Updated Evaluation Matrix]
```

## Mitigation
Using synthetic generators to constantly update target evaluation benchmarks dynamically.
"""
    },
    {
        "filename": "mlops_regression_tracking.md",
        "title": "Continuous MLOps Regression Tracking for Enterprise RAG Stacks",
        "content": """# Continuous MLOps Regression Tracking for Enterprise RAG Stacks

Ensures system improvements do not cause regressions in retrieval or generation quality.

## Architectural Flow
```mermaid
graph TD
    Commit[Code / Model Commit] --> CI[CI/CD Eval Harness]
    CI --> TestSuite[NDCG & Ragas Evaluations]
    TestSuite --> Report[Regression Alerts / Approval]
```

## Application Details
Automated evaluation testbeds run during continuous integration to ensure system quality does not decay.
"""
    },
    {
        "filename": "e_discovery_legal_audit.md",
        "title": "Automated Corporate E-Discovery & Legal Audit Verification",
        "content": """# Automated Corporate E-Discovery & Legal Audit Verification

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
"""
    },
    {
        "filename": "healthcare_diagnostic_ir.md",
        "title": "High-Volume Healthcare Diagnostic Information Retrieval",
        "content": """# High-Volume Healthcare Diagnostic Information Retrieval

Assisting clinical personnel by fetching records and pharmacology facts to suggest patient care steps.

## Architectural Flow
```mermaid
graph TD
    PatientData[Patient Records] --> PharmacologyDB[Drug Databases]
    PharmacologyDB --> Guardrails[Groundedness & Faithfulness Audit]
    Guardrails --> Recommendation[Clinician Recommendation]
```

## Application Details
Demands 100% faithfulness scores to prevent medical liability or harm.
"""
    }
]

for page in pages:
    filepath = os.path.join(details_dir, page["filename"])
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(page["content"])

print("Successfully generated all 15 detailed pages.")
