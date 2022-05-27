import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt

array = [[53863,325,234],
         [149,1116,0],
         [104,0,1161]]
    
df_cm = pd.DataFrame(array, pd.DataFrame(array, index=["O","BS", "ES"], columns=["O","BS", "ES"]))
sn.set(font_scale=1.4)#for label size
sn.heatmap(df_cm, annot=True,annot_kws={"size": 16})# font size



In these tables, the highest accuracy values for precision, recall, F1 measure are averaged and are specified in bold font.
We compare our results with base line results and with the one related CRF-based method used for SBD on speech transcripts texts. 

Confusion matrices are actually normalized by its values to avoid the skewed 'O' tag distortion for compact presentation of matrices. 
These confusion matrices for English and French SBD tasks are shown in Table 7 for the submitted results. 
The average precision of 'BS' and 'ES' tags are comparatively less when compared to the average recall of these tags as these tags are often predicted as 'O' tag as shown in Fig 7.
We also observe that bothe 'BS' and 'ES' tags in English shared task were not confused with each other as they were with 'O' tag. Same is seen in case of improved results' confusion matrices as shown in Figure 9.
In the case of French SBD task, The average precision of 'BS' and 'ES tags are comrpatively more when compared to the average recall as these tags were mostly confused with 'O' tag as shown in the Figure 8.






nd ES sentences were not confused as much with each other as they were with others. This may be an artifact of the latter being the majority class. 
When Others were misclassified, they were more likely to be labelled as ES, suggesting that the vocabulary employed in the two
classes of claims is similar.

We manually examined those setences that are misclassified as BS and found that they contained a relatively high proportion of personal pronouns, wh-questions, and negations. While these vocabulary
terms are typically associated with other sentences.

By contrast, when ES tagged sentences were misclassified as BS, we found that they tend
to contain several distinct propositions or clauses, only one of which was ES in nature. Properly
handling these type of sentences would require modelling them with better features using non linear chain CRF methods.


We also present the normalized confusion matrices for the improved results post submission in the Table 8.











