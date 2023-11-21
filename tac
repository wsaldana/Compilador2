CLASS  Factorial
Factorial.var = 0
FUNC Factorial.factorial
n = POP
_t1 = n == 0
if _t1 goto _L1
goto _L2
_L1:
f = 0
goto _L3
_L2:
_t2 = n == 1
if _t2 goto _L4
goto _L5
_L4:
f = 1
goto _L6
_L5:
_t3 = n - 1
PUSH _t3
CALL factorial
_t4 = GET 0
_t5 = n * _t4
f = _t5
_L6:
_L3:
RETURN f
END_FUNC

CLASS  Fibonacci
FUNC Fibonacci.fibonacci
n = POP
_t1 = n == 1
if _t1 goto _L1
goto _L2
_L1:
f = 1
goto _L3
_L2:
_t2 = n == 2
if _t2 goto _L4
goto _L5
_L4:
f = 1
goto _L6
_L5:
_t3 = n - 1
PUSH _t3
CALL fibonacci
_t4 = GET 0
_t5 = n - 2
PUSH _t5
CALL fibonacci
_t6 = GET 0
_t7 = _t4 + _t6
f = _t7
_L6:
_L3:
RETURN f
END_FUNC

CLASS  Main
Main.n = 10
Main.facto = NONE
Main.fibo = NONE
FUNC Main.main
_t1 = NEW Factorial
facto = _t1
_t2 = NEW Fibonacci
fibo = _t2
PUSH n
_t3 = CALL fibo.fibonacci
PUSH _t3
CALL out_int
_t4 = GET 0
END_FUNC

