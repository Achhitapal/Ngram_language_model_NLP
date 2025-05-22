# N-Gram Based Language Modeling for Predictive Text and Autocorrect

## 1. Objective

The goal of this case study is to demonstrate how unigram, bigram, and trigram language models can be used to perform next-word prediction and autocorrect, using a compact dataset of natural conversational sentences.

---

## 2. Dataset Description

A manually curated mini-dataset of 50 sentences was created using common daily conversations. This dataset includes simple sentence structures, making it ideal for calculating and interpreting N-gram probabilities.

- **Total Sentences**: 50  
- **Total Unique Words**: X  
- **Vocabulary Size**: X (including start/end tokens if used)  
- **Average Sentence Length**: X words  
*(Fill in "X" after data analysis.)*

---

## 3. Methodology

### 3.1 Preprocessing

- Tokenization  
- Lowercasing  
- Optional: Start (`<s>`) and end (`</s>`) tokens added  

### 3.2 Model Building

- **Unigram Model**:  
  `P(w) = Count(w) / Total Words`

- **Bigram Model**:  
  `P(w2|w1) = Count(w1 w2) / Count(w1)`

- **Trigram Model**:  
  `P(w3|w1 w2) = Count(w1 w2 w3) / Count(w1 w2)`

### 3.3 Applications

- **Next-word prediction**:  
  Example: Input: “how are” → Output: “you”

- **Autocorrect**:  
  Example: Input typo: “i am cmoing” → Suggest “coming” using trigram context

---

## 4. Sample Results

### 4.1 Predictions

| Input Phrase | Predicted Word (Bigram/Trigram) |
|--------------|----------------------------------|
| how are      | you                              |
| i am         | doing / coming                   |
| do you       | want / have                      |

### 4.2 Autocorrect Examples

| Incorrect Input    | Corrected Output | Reason (Trigram Context)               |
|--------------------|------------------|----------------------------------------|
| i am cmoing        | i am coming      | “i am coming” is more likely           |
| lets ge to cafe    | lets go to cafe  | Common bigram: “go to”                 |

---

## 5. Observations

- Trigram models perform better at context-sensitive predictions but require more data.  
- Bigrams offer a balance between accuracy and computational simplicity.  
- Unigrams are too general but useful as fallbacks in sparse contexts.

---

## 6. Limitations

- Small dataset size limits generalizability.  
- No smoothing applied (can cause zero probabilities).  
- Context errors with rare or unseen phrases.

---

## 7. Future Work

- Apply smoothing techniques (Laplace/Kneser-Ney).  
- Extend dataset to include diverse sentence structures.  
- Compare with neural language models (e.g., RNN, BERT).

---

## 8. Conclusion

This case study illustrates how simple N-gram models can be effectively used for predictive text and autocorrect applications, especially in resource-constrained or explainable AI systems.
