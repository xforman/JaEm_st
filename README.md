# Empathy Evaluation Framework for Large Language Models

This repository implements a **psychologically grounded evaluation framework for empathy in Large Language Models (LLMs)**. It addresses limitations in current NLP empathy benchmarks, which often rely on loosely defined constructs, leading to reduced dataset validity, weak robustness, and unreliable evaluation. 

Instead of treating empathy as a static label, this framework measures **how model responses change under controlled contextual variation**, enabling a more theoretically sound and fine-grained analysis of empathetic understanding.

This is a repository for the paper "Quantitative Assessment of Intersectional Empathetic Bias and Understanding" on ArXiV https://arxiv.org/abs/2411.05777
---

## 🎯 Project Goals

* Move beyond surface-level empathy scoring
* Evaluate **context-sensitive empathetic reasoning** in LLMs
* Support **bias-aware and cross-lingual evaluation**, including low-resource language families
* Offer a reusable pipeline for **dataset generation and evaluation**

---

## 🧠 Core Idea

Empathy is modeled as **sensitivity to context**, particularly to social and bias-relevant cues.

The framework introduces **systematic variance** into prompts by modifying social and contextual attributes (e.g., group identity, situational framing). LLM responses are then evaluated using:

* Existing **empathy metrics**
* **Emotional valence** measures
* **Variance in model responses** across contextually altered prompts

Rather than focusing only on absolute scores, the framework studies whether models **adjust their reasoning appropriately** when subtle contextual differences are introduced.

---

## 🧪 Evaluation Methodology

1. **Controlled Prompt Generation**
   Prompts are generated from structured templates that encode:

   * Scenario structure
   * Social context variables
   * Bias-relevant attributes

2. **Model Evaluation**
   LLMs are evaluated using:

   * Multiple-choice responses
   * Free-text generation

3. **Scoring and Analysis**
   Responses are analyzed for:

   * Empathy-related scores
   * Emotional valence
   * Variance across context conditions

Even when performance differences are small, changes in reasoning behavior across prompt variants can indicate **context-sensitive empathetic processing**.

---

## 🌍 Cross-Lingual Design

The controlled template-based generation supports **high-quality translation**, making the framework particularly suitable for languages with limited empathy and bias evaluation resources (e.g., Slavic language families).

---

## 📁 Repository Structure

### `/Dataset_generation/`

Main module for constructing the evaluation dataset. Includes logic for:

* Controlled prompt generation
* Contextual and social variation design
* Embedding empathy-related constructs into prompts

---

### `/dataset_generation/templates/`

Prompt templates that define:

* Scenario structures
* Social and contextual parameters
* Bias-related attributes
* Emotional setup

These templates ensure **construct validity** and consistent manipulation of contextual variables.

---

### `/dataset_generation/JaEmSTDataset.py`

Dataset class for assembling generated prompts into a structured evaluation dataset. Handles:

* Instantiating prompts from templates
* Storing metadata about contextual variations
* Formatting data for evaluation pipelines

---

### `/from_epitome/`

Components adapted from the **EPITOME** empathy framework, potentially including:

* Empathy scoring methods
* Feature extraction tools
* Supporting evaluation utilities

This connects prior empathy modeling approaches with the new variance-based evaluation paradigm.

---

### `/results/`

Contains outputs from evaluation runs, such as:

* Model responses (multiple-choice and free generation)
* Empathy and valence scores
* Comparative analyses across contextual conditions

---

## 🔬 Research Context

Initial experiments show limited variance in small samples but reveal that models alter their reasoning chains to accommodate subtle prompt changes. This suggests that:

* Models may be sensitive to nuanced contextual differences
* Larger datasets and refined statistical methods are needed
* The framework provides a strong basis for future empathy evaluation research

---

## 👥 Intended Audience

This repository is designed for researchers working on:

* Empathy modeling in NLP
* Social bias and context sensitivity in LLMs
* Evaluation methodology for socio-emotional capabilities
* Cross-lingual and low-resource language NLP

---

## 📌 Summary

This project provides:

✔ A theory-grounded empathy evaluation framework
✔ A controlled dataset generation pipeline
✔ Tools for measuring response variance under social-context shifts
✔ Support for multilingual and bias-aware evaluation

It serves as both a **dataset construction toolkit** and an **experimental framework** for studying empathetic reasoning in LLMs.

---
