import pandas as pd
import numpy as np

def create_data(n=100):
    np.random.seed(42)
    experience = np.random.randint(1, 20, n)
    salary = experience * 1500 + np.random.randint(10000, 20000, n)
    df = pd.DataFrame({'experience': experience, 'salary': salary})
    df.to_csv('salary_data.csv', index=False)
    print("salary_data.csv created successfully!")

if __name__ == "__main__":
    create_data()
