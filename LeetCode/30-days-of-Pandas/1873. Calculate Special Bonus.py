import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees
    df['bonus'] = ((df['employee_id'] % 2 != 0) & (~df['name'].str.startswith('M')))*df['salary']
    df = df.sort_values(by='employee_id', ascending=True)
    return df[['employee_id','bonus']]