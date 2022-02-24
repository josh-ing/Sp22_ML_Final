# Kickstarter Success Prediction
## Team 45: Joshua Ng, Kayla Hunt, Minjae Lee, Youngho Lim, Karishma Rana

### Introduction:
Since its inception in 2009, Kickstarter has been a popular way for entrepreneurs and creators to raise funds for their project. Anyone can become a backer for a project, pledging any amount of money and only paying if the project is deemed successful. Success on Kickstarter is defined as reaching the goal pledge amount within a predetermined time frame, at which point funds are collected and given to the creators. If the goal amount is not reached, the project is considered a failure. The current success rate of projects is relatively low, with only 44 percent of Kickstarter projects being considered successful (Yuan et al.). The most important information provided by our dataset is the category of the project, fundraising goal, how long the campaign was open, number of backers, amount pledged, country pledged from, and the outcome of the project.

### Problem Definition:
#### What is our motivation behind this project?
The goal of our project is to predict the future success of a project put on Kickstarter. The motivation for this project is the number of projects that creators try to fund, with low levels of success. If we can accurately predict the success or failure of a project given how well they crowdfund (amount of backers, amount pledged, etc.), we can help creators to decide to pursue the project before the time, effort, and money is expended to create the campaign.

### Our Dataset:
[Kickstarter Projects](https://www.kaggle.com/kemical/kickstarter-projects?select=ks-projects-201801.csv)
#### Data Features:
- Kickstarter ID
- Kickstarter name
- Category
- Main_category
- Currency
- Deadline
- Goal
- Pledged
- State
31 columns total, 12 string features, 8 decimal features, 4 date/time features, and 7 other.

### Methods 
Currently, the algorithms that we have contemplated using to solve this problem are some combination of Naive Bayes, Logistic Regression, and Random Forests. All three of these potential algorithms are designed for supervised learning and classification problems, the type of problem that our dataset falls under. Additionally, we can utilize NLP algorithms like Neural Bag of Words on certain features such as project titles and categories to help predict the projects’ chances of success.  Of course, the chosen algorithms are subject to change in the future, especially since the lectures have yet to cover supervised learning.

### Predicted Results
Ideally, the result would be that the models we create would correctly label the data more than half of the time. That being said, based on the third-party research we conducted we found that previously created models averaged around a 65% to 75% accuracy (Chen et al.) (Greenburg et al.) (Yuan et al.). While it is worth noting that these models utilized different features than the ones our chosen dataset affords us, we still anticipate that creating a model with a similar accuracy will come with its challenges.

### References
- Yuan, Hui, et al. “The Determinants of Crowdfunding Success: A Semantic Text Analytics Approach.” Decision Support Systems, North-Holland, 6 Aug. 2016, https://www.sciencedirect.com/science/article/pii/S0167923616301373. 
- Chen, Kevin, et al. “Courses.cms.caltech.edu.” KickPredict: Predicting Kickstarter Success, http://courses.cms.caltech.edu/cs145/2013/blue.pdf. 
- Greenberg, Michael D, et al. “Crowdfunding Support Tools: Chi '13 Extended Abstracts on Human Factors in Computing Systems.” Crowdfunding Support Tools: Predicting Success &amp; Failure, 1 Apr. 2013, https://dl.acm.org/doi/pdf/10.1145/2468356.2468682. 




