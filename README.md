# Intelligent system for document detection, classification and tokenization

## Background and Objectives

Your mission will be to design and develop a prototype system capable of:

- Extracting and phonetically tokenizing the contents of the file (digital document or image).
- Storing these tokens in a relational database (PostgreSQL) in order to later prepare a powerful search engine for your documents.
- Detecting and classifying any document based on its type using a pre-trained language model (LLM) chosen from the Hugging Face platform:
  - Bill
  - Identity document (passport, identity card, etc.)
  - CONTRACT
  - Functional document, etc.
- The classification will be based on a JSON database describing the different types of documents and their characteristics.

