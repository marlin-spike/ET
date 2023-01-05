#practical 6
#dataframe
import pandas as pd
# Calling DataFrame constructor
df = pd.DataFrame()
print(df)
# list of strings
lst = ['raj', ' ram', ' rahul', 'aanand','ajay', 'Shreyash', 'Raone']
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print (df)


----------------------------------------------
#to save the file

#practical 6

# importing pandas as pd
import pandas as pd
# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv('file1.csv')

-------------------------------------------------
#to save the file in specific location


#practical 6

# importing pandas as pd
import pandas as pd
# list of name, degree, score
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
# dictionary of lists
dict = {'name': nme, 'degree': deg, 'score': scr}
df = pd.DataFrame(dict)
# saving the dataframe
df.to_csv(r'C:\ET-1\file4.csv', index=False)


--------------------------------------------------
#to read a file from specific location

#practical 6

import pandas
# reading the CSV file
csvFile = pandas.read_csv('file1.csv')
# displaying the contents of the CSV file
print(csvFile)
