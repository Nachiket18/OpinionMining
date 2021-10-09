# OpinionMining
## **Contributors**: Nachiket **Deo**, Justin **Hong**, Aditya **Kulkarni**


Repository for Opinion Mining Framework

## Abstract
This project revolves around identifying opinions in textual data. This falls under sentiment analysis but goes little deeper into structural understand of the test. Structural understanding is done by classifying the data and forming a triplet - (entity,aspect,opinion). Aspect is a word that further describes the entity. This structure not only gives opinion of the entity but also identifies what the opinion is about. The double propogation algorithm is used for identifying the previously structure.


## Double Propagation Algorithm


https://www.mitpressjournals.org/doi/pdf/10.1162/coli_a_00034

## Data
Justifying recommendations using distantly-labeled reviews and fined-grained aspects
Jianmo Ni, Jiacheng Li, Julian McAuley [link](https://cseweb.ucsd.edu/~jmcauley/pdfs/emnlp19a.pdf)

Empirical Methods in Natural Language Processing (EMNLP), 2019


To test our model, we decide to use Amazon reviews as our dataset for its candidacy and interpretability. The [Review-9-products](http://www.cs.uic.edu/~liub/FBS/Reviews-9-products.rar) available of Professor Bing Liu's website is what we have used.



One issue in the review data is that there are spelling mistakes. As our model directly reads in the sentences without checking grammar, issues in the spellings can imply missing the words.

## Method


### Knowledge Graph

We decided to feed our algorithm's output into a knowledge graph. Doing so would allow for a clearer depiction of words and their relations between them.

## Results

### 

## Conclusion

## Future Work

---------
[Aditya Kulkarni](https://github.com/adikulkarni11)
[Nachiket Deo](https://github.com/Nachiket18)
[Justin Hong]
