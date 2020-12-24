# Sales-Analysis-of-Adventure-Works-Cycle
Increase the sales of Adventure Work Cycle by targeting specific customers for a mailing  company with the Marketing department.

# dataPreprocessing.py
Exporting the table from the SQL server to preprocess the dataset. Preprocessing phases includes: 1) Handling of NULL values 2) Normalization 3) Discretization (Binning/ Histograms) 4) Calculating Mean/ Median/ Standard Deviation to the Ordinal values 5) Random Sampling 6) Binarization. 

<img src="https://github.com/nikkas27/Sales-Analysis-of-Adventure-Works-Cycle/blob/main/SS16.jpg" width="90%"></img> 

<img src="https://github.com/nikkas27/Sales-Analysis-of-Adventure-Works-Cycle/blob/main/SS8.jpg" width="90%"></img> 

<img src="https://github.com/nikkas27/Sales-Analysis-of-Adventure-Works-Cycle/blob/main/SS_Occu.jpg" width="90%"></img> 



# Similarities.py
Implementation of the Jaccard similarity and creation of custom cosine similarity algorithm on the given Customekey values.

<img src="https://github.com/nikkas27/Sales-Analysis-of-Adventure-Works-Cycle/blob/main/SS14.jpg" width="90%"></img> 

<img src="https://github.com/nikkas27/Sales-Analysis-of-Adventure-Works-Cycle/blob/main/SS15.jpg" width="90%"></img> 

# Prediction System

Prediction System that recognizes a possible buyer for Bikes based on his/her financial conditions, family history, work commutes, etc.
Determining the data preprocessing methods that will be applied to the classifiers. For this section, I have chosen two extra features and converted the data to the one hot encoding for the preprocessing phase. Here, I have chosen the Random Forest classifier and the Decision tree classifier available with the Sklearn library in python.

Decision Tree classifier uses decision trees to learn from the features and then apply it to the test dataset by generating the trees.

Random forest is the type of classifier which selects the data from our dataset randomly and then generates different approaches. Then the best tree that is being generated is being used by the classifier for the prediction. Random forest is a way of averaging multiple deep decision trees, which are trained on different parts of the same dataset with the goal of reducing the variance.

# Accuracy

<img src="https://github.com/nikkas27/Question-Answering-System-for-Webpages-content-Analysis/blob/main/ss1.jpg" width="90%"></img> 

# Results of the Algorithms

<img src="https://github.com/nikkas27/Question-Answering-System-for-Webpages-content-Analysis/blob/main/Results_DecisionTree.png" width="90%"></img> 

<img src="https://github.com/nikkas27/Question-Answering-System-for-Webpages-content-Analysis/blob/main/Results_RandomForest.png" width="90%"></img> 

# Importance of Each features associated by the Random Forest Algorithm

<img src="https://github.com/nikkas27/Question-Answering-System-for-Webpages-content-Analysis/blob/main/ss15.jpg" width="90%"></img> 

