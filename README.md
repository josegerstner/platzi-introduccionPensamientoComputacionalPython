# Platzi - Introduccion al Pensamiento Computacional con Python  
  
## NOTAS  
  
**type(variable)**: me devuelve el tipo de la variable.  
  
**f'{"Hip " * 3} hurra'**: me permite hacer expresiones, en este caso, me devuelve "Hip Hip Hip hurra".  
  
## LAMBDAS  
>Una forma de definir una función en una expresión es utilizando el keyword lambda. lambda tiene la siguiente sintaxis:  
```  
lambda <vars>: <expresion>  
```  
  
## TESTING  
> Para realizar tests se debe importar el módulo **unittest**.  
> Se define la clase donde inlcuiremos todos los test y recibirá como parámetro **_unittest.TestCase_**.  
```  
class xxxTest(unittest.TestCase)
```  
> Definimos los tests. Estos deben empezar con la palabra **test_** y recibir como parámetro a **self**.  
```
def test_xxxx(self):
```
> Por último obtenemos los resultados con **self.**. Ej: self.assertEquals(resultado, True).
  
## MANEJO DE EXCEPCIONES  
  
> Las excepciones se manejan con las palabras: **try, except, catch**.  
> Se pueden utilizar también para ramificar programas.  
> No deben manejarse de manera silenciosa (por ejemplo, con print).  
> Para llamar excepciones propias se usa la palabra **raise**.  
  
