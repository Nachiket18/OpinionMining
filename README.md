# OpinionMining

Repository for Opinion Mining Framework

## Abstract
This project revolves around identifying opinions in textual data. This falls under sentiment analysis but goes little deeper into structural understand of the test. Structural understanding is done by classifying the data and forming a triplet - (entity,aspect,opinion). Aspect is a word that further describes the entity. This structure not only gives opinion of the entity but also identifies what the opinion is about. The double propogation algorithm is used for identifying the previously structure.


## Double Propagation Algorithm

The algorithm uses set of rules to identify syntatical patterns. It relies heavily on POS tags which are integral to Natural Language Processing. Once the input text has a pattern that matches to one of the rules, the aspect and opinion (specific to that particular rule) gets captured. In first pass over the sentence, algorithm attempts to capture some aspects and opinions and in second pass over the same statement, algorithm tries to find out aspects and opinions based on the aspects and opinions found out in first pass. Detalied algorithm is mentioned in below URL - https://www.mitpressjournals.org/doi/pdf/10.1162/coli_a_00034

## Related Work

As the part of the project, we developed the mechanism to connect the entity, aspect and opinions. The double propagation algorithm mentioned in previous section captures the aspects and opinions but it doesn't provide a specific mechanism to link all these three together. Our mechanism relies on the dependency parse over the sentence and connects the previously captured aspects and opinions along with the entities which are seperately captured. In order to get the linkage between these three we traverse the dependency parse tree.


## Data
Justifying recommendations using distantly-labeled reviews and fined-grained aspects
Jianmo Ni, Jiacheng Li, Julian McAuley
Empirical Methods in Natural Language Processing (EMNLP), 2019




### Knowledge Graph

## Results

## Conclusion

## Future Work
