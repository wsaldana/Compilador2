
class BooleanIfWhile {
    a: Int;
    b: Bool <- true;

    method1(): Int {{

        while 10 < 30 loop {
            a;
        } pool;


        if b then {
            a;
        } else {
            2;
        } fi;
    }};
};


class Main {
    main(): SELF_TYPE {
        self
    };
};