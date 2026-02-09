import pandas as pd


df = pd.read_csv(r'C:\coding\leetcode-company-wise-problems\1-code\leetcode_problems_by_type_and_company.csv')
df.drop(columns=['Company_List', "Link"], inplace=True)
df.to_csv(r'C:\coding\leetcode-company-wise-problems\1-code\leetcode_problems_by_type_and_company.csv')