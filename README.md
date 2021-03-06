# surfs_up
Jupyter and VS Code featuring: SQLAlchemy, SQLite, and Flask

Overview of the statistical analysis:
In this module we utlized powerful new tools Jupyter Notebook and VS Code. These tools were SQLAlchemy, SQLite, and Flask. The purpose of this analysis was to examine a SQLite database and determine the best locale and weather for a beachfront business. In this project, we examine the differences in the weather between the months of June and December in our database. In order to achieve this, we import SQLAlchemy and in order to create an engine ![image](https://user-images.githubusercontent.com/99628763/158084807-a4383fed-6d94-444e-bd1a-fc1220a1820c.png)
, reflect the SQLite database into a new structure ![image](https://user-images.githubusercontent.com/99628763/158084848-1f4a03d3-4d37-4fd5-adcb-1f20437846ca.png)
, and prepare our new tables for reflection and editing: 
![image](https://user-images.githubusercontent.com/99628763/158084898-c6cf8c8d-3138-4723-a95b-a2a226c348e3.png)

We are able to link from Python to our new database by introducing a session link ![image](https://user-images.githubusercontent.com/99628763/158084959-451a7087-349e-4f23-ad6b-1ac73030410b.png). With the above code in place we can take a query of our new tables, add filters, and add other functions such as group_by or order_by, or calculate min/max values with func.min() and func.max(), convert the results to list, and convert that list into a pandas dataframe for further visualization!

Ex. of a session query: ![image](https://user-images.githubusercontent.com/99628763/158085212-81edbbb3-4e7a-442c-9d09-cc792cefd1a1.png)

Using this technique we are able to obtain temperature data for the months of June and December to show 4 key points:
<ul>
  <li>The count of June was over 200 higher than December, possibly showing more activity in the month of June</li>
  <li>the minimum temperature for December was about 8 degress lower than June</li>
  <li>the max temperature for both June and December were about the same 85 vs 83</li>
  <li>the modes of both months were also similar within 5 degrees</li>
</ul>

![image](https://user-images.githubusercontent.com/99628763/158086003-dd3c192a-891d-4895-8819-539c56dd669e.png)

With these results it may be concluded the temperature in this area is overall stable year round. There is a slight decrease in temperature between the summer and winter months, however the lowest temp recorded in December was 56 F vs 64 F in June. This might be cause for concern, as a business that relies on warm weather, 56 F might be a little too low. The aforementioed concern is lessened when we take a look at the mode for the month of December in particular and see that it is 71 F. Even though there may be colder days in December, overall the temperature of the weather is still desirable with many days in the low 70's.

We utlized flask in this project to show our query results for precipitations, total number of stations, temps for the previous year, and min, max, and avg temps for all stations given a range of dates.

Ex.![image](https://user-images.githubusercontent.com/99628763/158086851-df4803dc-ef85-45f4-9366-007329623026.png)


