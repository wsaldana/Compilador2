# Compiler 2

Video testing: https://drive.google.com/file/d/1noVcdKeA1JkZ5xzYrFHc8bpzZnoy_2Vh/view?usp=drive_link

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
python main.py <input file>
```
