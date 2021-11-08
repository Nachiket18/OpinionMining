# OpinionMining
## Contributors: Nachiket Deo, Justin Hong, Aditya Kulkarni, Charitarth Chugh

### Keywords: Opinion Mining, Sentiment Analysis, Bidirectional Encoder Representations from Transformers (BERT), Word Embeddings, Knowledge Graph

Repository for Opinion Mining Framework

## Abstract
This project involves identifying opinions from textual data. This falls under sentiment analysis but goes little deeper into structural understanding of the test. Here, we capture entity, aspect, and opinion words from given review data.  Entities, usually nouns, are the subject of the sentences. An Aspect is a word that further describes the entity, and opinions describe the author’s judgement on both the words. Our work reports the structural understanding found from classifying the data and forming a triplet relation - (entity, aspect, opinion). This structure not only gives an opinion on the entity but also identifies precisely what the opinion is about. The double propagation algorithm is used for identifying the previous structure. Further, we are experimenting with BERT for improving the quality of the model by capturing the implicit opinions and aspects. 


## Double Propagation Algorithm

The algorithm uses a set of rules to identify syntactic patterns. It relies heavily on POS tags which are integral to Natural Language Processing. Once the input text has a pattern that matches one of the rules, the aspect and opinion (specific to that particular rule) gets captured. In the first pass over the sentence, the algorithm attempts to capture some aspects and opinions. Additionally, in the second pass over the same statement, the algorithm tries to find out aspects and opinions based on the aspects and opinions found out in first pass. Detalied algorithm is mentioned in below URL - https://www.mitpressjournals.org/doi/pdf/10.1162/coli_a_00034

## Related Work

As part of the project, we developed the mechanism to connect the entity, aspect and opinions. The double propagation algorithm mentioned in the previous section captures the aspects and opinions but it doesn't provide a specific mechanism to link all these three together. Our mechanism relies on the dependency parse over the sentence and connects the previously captured aspects and opinions along with the entities which are separately captured. In order to get the linkage between these three we traverse the dependency parse tree.


## Data
Justifying recommendations using distantly-labeled reviews and fined-grained aspects
Jianmo Ni, Jiacheng Li, Julian McAuley [link](https://cseweb.ucsd.edu/~jmcauley/pdfs/emnlp19a.pdf)

Empirical Methods in Natural Language Processing (EMNLP), 2019


To test our model, we decide to use Amazon reviews as our dataset for its candidacy and interpretability. The [Review-9-products](http://www.cs.uic.edu/~liub/FBS/Reviews-9-products.rar) available on Professor Bing Liu's website is what we have used.

An issue that drastically weakens the accuracy of our model is spelling mistakes. As our model directly reads in the sentences without or editing the data, spelling errors in the data leads to its non-recognition and occasionally even relationships.

### Knowledge Graph
We decided to feed our algorithm's output into a knowledge graph. Doing so would allow for a clearer depiction of words and their relations between them.

## Results

## Conclusion

## Future Work


---------
[Aditya Kulkarni](https://github.com/adikulkarni11)
[Nachiket Deo](https://github.com/Nachiket18)
[Justin Hong]
[Charitarth Chugh](https://github.com/charitarthchugh)

