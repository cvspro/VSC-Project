import pandas as pd
import numpy as np
# df=pd.DataFrame(np.random.randn(6,4),columns=list("ABCD"),index=[1,2,3,4,5,6])
df=pd.DataFrame({
    "A":pd.Series([3]*4)
})
print(df)