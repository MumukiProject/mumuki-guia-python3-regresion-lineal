En efecto, el coeficiente de Person nos arrojó `0.58645...`, que coincide con el valor obtenido mediante `corr()`. El motivo es simple: `corr()` utiliza por defecto el método de Pearson...

```python
# esta línea ...
diabates.corr()
# ... es equivalente a 
diabates.corr('pearson')
```

Pero bien se podría usar otro método, como por ejemplo el coeficiente de correlación de Spearman: 

```
diabetes.corr("spearman")['response']





```python
Coeficiente de correlación de Pearson: 0.5864501344746887
P-value: 3.4660064451654114e-42
```