import pandas as pd
import numpy as np
from datetime import timedelta
from sqlalchemy import create_engine
import psycopg2

engine = create_engine('postgresql://id:pw@host/db_name')
df =  pd.read_sql('''SQL-Query''', engine)

print(df)

### Add your Data Frame and edit it as you wish
