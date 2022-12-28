Antes de analizar las relaciones entre dos variables tenemos que ... ¡descubrir cuales están relacionadas! 😛 

Si bien no existe una respuesta taxativa a esta pregunta, una buena primera forma de aproximarse es generar una _matriz de correlación_, que nos dirá el grado en que los cambios de cualquiera de las variables acompañan los cambios de cualquiera de las otras ↔️. Para ello, los `DataFrame`s cuentan con la operación `corr`:

```python
correlaciones = diabetes.corr()
correlaciones
```

Esta matriz mostrará, por cada par de variables, cuán relacionadas están en una escala de -1 a 1, siendo: 

* `1`: altamente correlacionadas y directamente proporcionales. Si una variable crece, la otra también;
* `0`: sin ningún tipo de correlación. Los cambios en una no parecen influir en la otra;
* `-1`: altamente correlacionadas e inveramente propocionales. Si una variable crece, la otra decrece.  

> Generá la matriz de correlación y marcá cuales afirmaciones son correctas.

