import pandas as pd
import numpy as np
# df=pd.DataFrame(np.random.randn(6,4),columns=list("ABCD"),index=[1,2,3,4,5,6])
df=pd.DataFrame({
    "A":np.array([3]*4),
<<<<<<< HEAD
    "B":pd.Series(1,index=list(range(4)),dtype='float32')
=======
    "B":pd.Series(1,index=list(range(4)),dtype='float32'),
    "C":pd.Timestamp("20230102"),
    "D":pd.Categorical(['I','LOVE','YOU','LOTS'])
>>>>>>> 22a02a5b7537422dd02c59421652fb843961be36
})
print(df)
