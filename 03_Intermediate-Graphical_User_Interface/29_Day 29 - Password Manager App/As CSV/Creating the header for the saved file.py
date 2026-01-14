import pandas as pd
dataset = pd.DataFrame(None, columns = ["Website", "Email", "Password"])
dataset.to_csv("Password record.csv")