En efecto, el coeficiente de Person nos arrojó `0.58645...`, que coincide con el valor obtenido mediante `corr()`. El motivo es simple: `corr()` utiliza por defecto el método de Pearson...

```python
# esta línea ...
diabates.corr()
# ... es equivalente a 
diabates.corr('pearson')
```

Pero bien se podría usar otro método, como por ejemplo el coeficiente de correlación de Spearman: 

```
ム diabetes.corr("spearman")['response']
age                          0.197822
sex                          0.037401
body_mass_index              0.561382
average blood pressure       0.416241
total_serum_cholesterol      0.232429
low_density_lipoproteins     0.195834
high_density_lipoproteins   -0.410022
total_cholesterol            0.448931
blood_sugar_level            0.350792
response                     1.000000







```python
Coeficiente de correlación de Pearson: 0.5864501344746887
P-value: 3.4660064451654114e-42
```