Podemos llevar esta observación a valores concretos, mediante la normalización del RMSE:

RMSE_normalizado = RMSE / (valor máximo - valor mínimo)

De este modo podremos obgener valores entre 0 y 1, donde los valores más cercanos a 0 representan modelos de mejor ajuste.

```python
rmse_normalizado = rmse / (diabetes["response"].max() - diabetes["response"].min())
rmse_normalizado
```