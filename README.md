# Big-Data-Assignment-03

Big Data Analytics
Assignment-2
Report

Members:
Ibrahim Khurram-22I-1896
Raiha Adnan-22I-1875
Muhammad Afnan-22I-1977

In this assignment, we were required to develop a basic Search Engine using the MapReduce model on Apache Hadoop, focusing on handling the ARTICLE_ID and SECTION_TEXT columns from a subset of the English Wikipedia dump.
 The objectives were to clean the CSV dataset and develop Mapper and Reducer for Document Indexing and Inverse Document Frequency (IDF) calculation.
Firstly, we discussed the assignment and ensured a clear understanding of the objectives and data structure.
Document Indexing:
 We then proceeded to develop the mapper script for document indexing, which reads input data, performs basic text cleaning, and emits words alongside their article IDs.
Term Frequency Calculation:
 Following this, a reducer script was crafted to aggregate word counts per document, laying the groundwork for Term Frequency (TF) calculation.
IDF Calculation:
Next, we tackled IDF calculation by creating another set of mapper and reducer scripts. The mapper emits unique word-article ID pairs, while the reducer calculates the document frequency for each term.
Problems Encountered:
During the Hadoop job executions, we encountered typical issues such as lack of output and errors indicating problems with the mapper or reducer scripts. To address these, we recommended checking job completion, reviewing Hadoop job logs for errors, validating input data format and path, ensuring correct command-line options were used, and debugging the mapper and reducer scripts independently.

Concluded:
This assignment underscored the importance of iterative testing and debugging in developing MapReduce applications and provided practical experience with Hadoop's distributed computing capabilities.
