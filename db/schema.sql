CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    industry VARCHAR(255),
    ticker VARCHAR(50)
);

CREATE TABLE financial_metrics (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    metric_name VARCHAR(100),
    metric_value NUMERIC,
    fiscal_year INT,
    source_document VARCHAR(255)
);

CREATE TABLE evidence_chunks (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id),
    document_title VARCHAR(255),
    content TEXT NOT NULL,
    embedding vector(1536), -- Tuned for text-embedding-3-small
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Index for hybrid search performance
CREATE INDEX ON evidence_chunks USING hnsw (embedding vector_cosine_ops);
