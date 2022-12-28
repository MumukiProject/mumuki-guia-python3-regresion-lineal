Primero, necesitaremos importar algunas bibliotecas:

```python
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

plt.rcParams['image.cmap'] = "bwr"
plt.rcParams['savefig.bbox'] = "tight"
plt.style.use('ggplot')
```

Luego, procederemos a cargar el lote de datos que nos interesa. En este caso, utilizaremos uno de ejemplo provisto por la propia biblioteca `scikit-learn`...

```python
from sklearn import datasets

diabetes = datasets.load_diabetes(as_frame=True)
print(diabetes['DESCR']) 
```

... y haremos realizaremos algunos ajustes a su estructura para que sea un poco más _tratable_: 

```python
diabetes = pd.concat((diabetes['data'], diabetes['target']), axis='columns')
diabetes = diabetes.rename(columns={
    'bmi':'body_mass_index',
    'bp':'average blood pressure',
    's1':'total_serum_cholesterol',
    's2':'low_density_lipoproteins',
    's3':'high_density_lipoproteins',
    's4':'total_cholesterol',
    's6':'blood_sugar_level',
    'target': 'response'})
del diabetes['s5']

diabetes
```

> ¡Ahora te toca a vos!: ejecutá el código anterior en un nuevo cuaderno y luego continuá al siguiente ejercicio. 