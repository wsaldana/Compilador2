# Compiler 2

Video Lab 0: https://drive.google.com/file/d/1noVcdKeA1JkZ5xzYrFHc8bpzZnoy_2Vh/view?usp=drive_link

Video Lab 1: https://drive.google.com/file/d/1OecO-50mQEABWLLk28gItcawmP6V9iD8/view?usp=drive_link

## Requirements
Install for python
```
pip install antlr4-tools
pip install antlr4-python3-runtime
```
Install antlr environment
```
cd /usr/local/lib
curl -O https://www.antlr.org/download/antlr-4.13.0-complete.jar
export CLASSPATH=".:/usr/local/lib/antlr-4.13.0-complete.jar:$CLASSPATH"
alias antlr4='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.0-complete.jar:$CLASSPATH" org.antlr.v4.Tool'
alias grun='java -Xmx500M -cp "/usr/local/lib/antlr-4.13.0-complete.jar:$CLASSPATH" org.antlr.v4.gui.TestRig'

```

## Build compiler
```
cd compiler/grammar
antlr4 -Dlanguage=Python3 yapl.g4 -visitor
```

## Run
```
pipenv shell
pipenv install
```

### Start backend
```
uvicorn main:app --reload
```

### Start front
```
cd front
yarn start
```

# Codigo intermedio
#### Asignación
t1 = a

#### Operaciones aritméticas
##### Suma
t1 = a
t2 = b
t3 = t1 + t2
##### Resta
t1 = a
t2 = b
t3 = t1 - t2
##### Multiplicación
t1 = a
t2 = b
t3 = t1 * t2
##### División
t1 = a
t2 = b
t3 = t1 / t2

#### Operaciones booleanas
##### Mayor que
t1 = a
t2 = b
t3 = t1 > t2
##### Menor que
t1 = a
t2 = b
t3 = t1 < t2
##### Igual que
t1 = a
t2 = b
t3 = t1 == t2
##### No igual
t1 = a
t2 = b
t3 = t1 != t2

#### Condicionales
if a > b goto L1
t1 = "a no es mayor que b"
goto L2
L1: t1 = "a es mayor que b"
L2:

#### Funciones
t1 = call FUNC, a, b, ...  # Llama a la función suma con los argumentos a y b

#### Clases
t1 = new CLASS  # Crea una instancia de la clase CLASS
t2 = call t1.obtener_valor  # Llama al método obtener_valor de la instancia

