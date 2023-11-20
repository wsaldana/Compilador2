class CastBoolInt {
    a: Int;
    b: Bool;

    method1(): Int {{
        b <- 0; -- se esta asignando un bool a un int y la funcion retorna 'b' cuando deberia retornar un int pero hay casteo implicito
    }};

    method2(param1: Int, param2: Bool): Int {
        false
    };

    method3(): Bool {{
        self.method2(true, 5); -- se esta usando self para acceder a un metodo de la clase al igual que se hace casteo implicito de tipos de la funcion

        method2(false, 0); -- se esta llamando a un metodo de la clase sin usar self y hay casteo implicito. Se retorna tipo int de 'method2' cuando la funcion devuelve Bool
    }};
};


class Main {
    main(): SELF_TYPE {
        self
    };
};