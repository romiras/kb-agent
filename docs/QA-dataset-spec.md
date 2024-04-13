# Specification of dataset for Q&A

A file in GitHub flavored Markdown syntax contains a series of sections. Each section consists of a pair of a question and an answer. Here's a more detailed breakdown:

- **Question (Q):** The line of the question starts with `Q:`. This is where the question is written and it can be in multiple lines.
- **End of Question:** The end of the question body is indicated by a line with `---`.
- **Answer (A):** The line of the answer starts with `A:`. This is where the answer to the corresponding question is written and it can be in multiple lines.
- **End of Answer:** The end of the answer body is indicated by a line with `-----`. This also designates the end of a Q&A pair.

Here's an example for better understanding:

```
Q: What is the capital of France?
---
A: The capital of France is Paris.
-----
```
