Finalmente ya podemos decir que hemos ajustado nuestro modelo, caracterizado y evaluado. De esta forma, no sólo podemos explicar la relación entre las variables, sino que también podemos determinar su poder predictivo y compararlo con el de otros modelos más sofisticados que eventualmente realicemos. 

Peeeeeero, aún no hicimos aquello a lo que vinimos, ¿verdad? ¡Intentemos predecir valores!


```python
def response(body_mass_index):
  return modelo.predict([[body_mass_index]])[0]
```

> Ahora te toca a vos: escribí otra versión de la función `response`, pero que esta vez no utilice el `modelo` generado sino los coeficiente que obtuviste en tu cuaderno y que funcione así: 
> 
> ```python
> ム response(0)
> 154.0752867556298
> ```

