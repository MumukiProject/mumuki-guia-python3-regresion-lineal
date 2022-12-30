Ya podemos decir que hemos ajustado nuestro modelo, caracterizado y evaluado. De esta forma, no sólo podemos explicar la relación entre las variables, sino que también podemos determinar su poder predictivo y compararlo con el de otros modelos más sofisticados que eventualmente realicemos. ¡Lo logramos! 🥲

Peeeeeero, aún no hicimos aquello a lo que vinimos, ¿verdad? ¡Intentemos predecir valores! :tada: Primero, definamos una función para hacer más sencillo el uso del `modelo`:

```python
def predecir_respuesta(body_mass_index):
  return modelo.predict([[body_mass_index]])[0]
```

Y ahora probemos con un índice de masa corporal ["normal" según la OMS](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal): 

```python
ム predecir_respuesta(20)
1881.9868473136542
```

¿Qué, qué? ¡Esto no puede estar bien! El máximo valor de `response` era de aproximadamente 300:

```python
max(diabetes["response"])
346.0
```

¿Qué pasó entonces?




x * 92.78055277 + 26.375791855203694
> Ahora te toca a vos: escribí otra versión de la función `predecir_respuesta`, pero que esta vez no utilice el `modelo` generado sino los coeficiente que obtuviste en tu cuaderno y que funcione así: 
> 
> ```python
> ム response(0)
> 154.0752867556298
> ```

