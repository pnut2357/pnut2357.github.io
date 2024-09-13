---
title: "Interview Preparation1"
excerpt: "Interview Questions"
categories:
  - interview
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  Interview / Algorithms
---

# Interview Preparation1

## 1. MLOps vs. LLMOps:

MLOps: Focuses on automating and managing the lifecycle of traditional machine learning models (e.g., image classification, regression).

LLMOps: Tailored to the specific challenges of deploying and managing Large Language Models, emphasizing:

Data & Model Size: Handling massive datasets and model parameters.
Prompt Engineering: Optimizing input prompts for desired outputs.
Continuous Learning & Adaptation: LLMs constantly evolve with new data and feedback.
Explainability & Bias Mitigation: Addressing the "black box" nature of LLMs and ensuring ethical use.

Resources:

## 2. Prompt Engineering:

Definition: The art and science of crafting effective prompts to elicit desired responses from LLMs.
Key Techniques:
Instruction Following: Providing clear instructions within the prompt.
Few-Shot Learning: Providing a few examples to guide the LLM.
Prompt Formatting: Using delimiters, keywords, and structure to enhance clarity.

Resources:
[Prompt Engineering Guide](https://www.promptingguide.ai/)

## 3. Retrieval Augmented Generation (RAG):

Concept: Enhancing LLM responses by retrieving relevant information from external knowledge sources.
Components:
Document Retriever: Finds relevant documents based on the query.
Contextualizer: Extracts relevant passages from the retrieved documents.
LLM Generator: Uses the retrieved context to generate an informed response.

Resources:
Blog: RAG: [A Comprehensive Guide](https://www.pinecone.io/learn/retrieval-augmented-generation/)
## 4. Chunking Strategies:

Challenge: LLMs have limited input context windows.
Solution: Chunking large texts into smaller segments for processing.
Strategies:
Sentence/Paragraph-Based: Dividing text based on natural boundaries.
Sliding Window: Moving a fixed-size window across the text with overlaps.
Meaning-Based: Using semantic segmentation to create cohesive chunks.
Resources:
Blog: Text Chunking for Large Language Models
Library: LangChain (provides chunking utilities)
## 5. Embedding Models:

Purpose: Converting text into numerical vectors, capturing semantic meaning and relationships.
Popular Models:
Word2Vec, GloVe: Word-level embeddings.
SentenceTransformers: Sentence/paragraph-level embeddings.
Applications:
Semantic Search: Finding similar documents based on meaning.
Clustering: Grouping related documents together.
Input Representation for LLMs: Transforming text into a format LLMs understand.
Resources:
Blog: Understanding Embeddings
## 6. Internal Working of Vector Databases:

Purpose: Efficient storage and retrieval of high-dimensional vectors (e.g., text embeddings).
Key Concepts:
Approximate Nearest Neighbor (ANN) Search: Quickly finding vectors closest to a query vector.
Index Structures: Optimizing search speed (e.g., k-d trees, ball trees, HNSW).
Popular Databases:
Pinecone: Managed service with high scalability.
Faiss (Facebook AI Similarity Search): Open-source library for efficient similarity search.
Resources:
Blog: Vector Databases Explained
## 7. Advanced Search Algorithms:

Relevance: Retrieving the most pertinent information from massive datasets.
Algorithms:
BM25: A probabilistic model considering term frequency and document length.
TF-IDF: Statistical measure of word importance in a document collection.
Learning-to-Rank (LTR): Training models to rank documents based on relevance.
Resources:
Blog: Search Relevance Algorithms: BM25 vs. TF-IDF

## 8. Supervised Fine-tuning of LLMs:

Goal: Adapting pre-trained LLMs to specific downstream tasks and improving performance.
Techniques:
Instruction Tuning: Training on examples of desired input-output pairs.
Parameter-Efficient Fine-tuning (PEFT): Updating a small subset of model parameters for resource efficiency.
Prompt Tuning: Optimizing the prompt itself as learnable parameters.
Resources:
Paper: [Finetuned Language Models Are Zero-Shot Learners](https://arxiv.org/abs/2109.01652)
Library: Hugging Face Transformers

## 9. Evaluation of LLMs:

Challenges: Evaluating LLMs goes beyond traditional metrics like accuracy.
Evaluation Metrics:
Perplexity: Measures how well the model predicts the next token in a sequence (lower is better).
BLEU, ROUGE: Evaluate the similarity between generated text and reference text.
Human Evaluation: Assessing aspects like fluency, coherence, and factual accuracy.
Resources:
Paper: Beyond Accuracy: [Behavioral Testing of NLP Models with CheckList](https://arxiv.org/abs/2005.04118)
Library: Hugging Face Evaluate
## 10. Deployment of LLMs:

Considerations:
Infrastructure: LLMs require powerful hardware (GPUs/TPUs) and efficient deployment frameworks.
Latency: Optimizing response times for real-time applications.
Scalability: Handling large user volumes and requests.
Monitoring & Maintenance: Ensuring model performance and addressing issues.
Resources:
Platform: Hugging Face Spaces
Framework: Ray (for distributed computing)
Blog: [Deploying Large Language Models](https://www.anyscale.com/blog)

## 11. Agent-based Systems:

Concept: Building intelligent agents that interact with their environment and make decisions.
LLM's Role: Powering agents with natural language understanding and generation capabilities.
Applications:
Chatbots: Engaging in natural conversations with users.
Task-Oriented Agents: Completing tasks based on user instructions.
Resources:
Framework: LangChain (for building agent-based systems with LLMs)
Blog: Building LLM-Powered Agents


[//]: # (<center>)

[//]: # (<img src="" height="0" width="0" >)
[//]: # (</center>)
[//]: # (<caption><center>  <font color='purple'> Figure 1 </font> Cat or Dog Classification </center></caption>)

