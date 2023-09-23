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
t2 = a
t3 = b
if t2 [bool_op] t3 goto L1
t1 = ...
goto L2
L1: t1 = ...
L2:

#### Funciones
```
L1: 
    FUNC t2, t3, ...:
        [func def]
        t1 = ...
        goto L2
L2:
    t1 = call FUNC a, b, ...
        t2 = a
        t3 = b
        goto L1
```

#### Clases
t1 = new CLASS  # Crea una instancia de la clase CLASS
t2 = call t1.obtener_valor  # Llama al método obtener_valor de la instancia

