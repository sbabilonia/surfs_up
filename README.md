# surfs_up
Jupyter and VS Code featuring: SQLAlchemy, SQLite, and Flask
Overview of the statistical analysis:

The purpose of the analysis is well defined. (3 pt)
Results:

There is a bulleted list that addresses the three key differences in weather between June and December. (6 pt)
Summary:

There is a high-level summary of the results and there are two additional queries to perform to gather more weather data for June and December. (5 pt)


The purpose of this analysis was to 
In this module we utlized powerful new tools Jupyter Notebook and VS Code. These tools were SQLAlchemy, SQLite, and Flask. The purpose of this analysis was to examine a SQLite database and determine the best locale and weather for a beachfront business. In this project, we examine the differences in the weather between the months of June and December in our database. In order to achieve this, we import SQLAlchemy and in order to create an engine ![image](https://user-images.githubusercontent.com/99628763/158084807-a4383fed-6d94-444e-bd1a-fc1220a1820c.png)
, reflect the SQLite database into a new structure ![image](https://user-images.githubusercontent.com/99628763/158084848-1f4a03d3-4d37-4fd5-adcb-1f20437846ca.png)
, and prepare our new tables for reflection and editing ![image](https://user-images.githubusercontent.com/99628763/158084898-c6cf8c8d-3138-4723-a95b-a2a226c348e3.png)
. We are able to link from Python to our new database by introducing a session link ![image](https://user-images.githubusercontent.com/99628763/158084959-451a7087-349e-4f23-ad6b-1ac73030410b.png). With the above code in place we can take a query of our new tables, add filters, and add other functions such as group_by or order_by, or calculate min/max values with func.min() and func.max(), convert the results to list, and convert that list into a pandas dataframe for further visualization!

Ex. of a session query: ![image](https://user-images.githubusercontent.com/99628763/158085212-81edbbb3-4e7a-442c-9d09-cc792cefd1a1.png)

