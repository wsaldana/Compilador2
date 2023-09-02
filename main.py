import sys
import os
import subprocess

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from antlr4 import InputStream, CommonTokenStream

from compiler.grammar.yaplLexer import yaplLexer
from compiler.grammar.yaplParser import yaplParser
from compiler.utils.errors.Errors import ErrorListener


def main():
    try:
        file = sys.argv[1]
        input_stream = InputStream(file)
    except Exception as e:
        raise Exception("Error with the file", e)

    lexer = yaplLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    error_listener_lexer = ErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener_lexer)

    parser = yaplParser(token_stream)
    error_listener_parser = ErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener_parser)

    parser.program()

    for i in token_stream.tokens:
        if i.type == yaplLexer.ERROR:
            print(f"ERROR: Bad token: {i}")
            continue
        print(i)

    if error_listener_lexer.true or error_listener_parser.true:
        print("\nFile has errors")
        exit(1)

    process = os.popen(
        'antlr4-parse compiler/grammar/yapl.g4 program -gui',
        'w'
    )
    process.write(input_stream.strdata)
    process.close()


if __name__ == '__main__':
    main()


app = FastAPI()

# CORS configuration
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ScriptRequest(BaseModel):
    script_code: str

@app.post("/run-python-script")
async def run_python_script(script_request: ScriptRequest):
    script_code = script_request.script_code
    try:
        # output = subprocess.check_output(['python', '-c', script_code], stderr=subprocess.STDOUT, text=True)
        output = subprocess.check_output(['python', 'main.py', script_code], stderr=subprocess.STDOUT, text=True)
        symtab = subprocess.check_output(['python', 'compiler/symtab.py', script_code], stderr=subprocess.STDOUT, text=True)
        typing = subprocess.check_output(['python', 'compiler/typing.py', script_code], stderr=subprocess.STDOUT, text=True)
        return {"output": output, "symtab": symtab, "typing": typing}
    except subprocess.CalledProcessError as e:
        return {"error": e.output}

