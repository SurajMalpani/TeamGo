# TeamGo

File descriptions:
1) Activities.csv : Contains the list of activities and some of the keywords to look for in the event. This file could be updated as and when we get more events.
2) Script.py: Python Script which parses the eventbrite json file (), categorizes the events and gives the output.
3) Output.csv: Output file with events and their respective categories.

Procedure:
1) Collected the data from the [Github repo](https://github.com/go-inc/data-collection-exercise).
2) Developed a python script to parse the json file from the previous step.
3) In the same script, read the activities file for reference on how to categorize the events.
4) Created dummy variables for each event row, based on whether they contained any of the keywords from the activities file.
5) Used these dummy variables to create a category column. Some events could be categorized into two categories. For ex., an event such as 'gather and cook food with friends', would be categorized in 'Cooking' as well as 'Social'. In that case, The categories will be mentioned in the 'Category' column separated by commas.
6) Script outputs the Output.csv. The input file name could be changed as per requirement. 
7) Although this is scalable, I understand this is a Naive approach. However, as the events data grows we could incorporate Machine learning algorithm. It could be as simple as 'Naive Bayes' or 'Random Forests' for better and robust classification. It would not need many changes as I already have created dummy variables in this approach.

