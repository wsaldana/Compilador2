class Main {

    method1(): Int {
        1
    };

    method2(param1: String, param2: Int) : String {
        param1
    };

    method3(): SELF_TYPE {{
        method1();

        method2("a", 1);

        self;
    }};

    main(): SELF_TYPE{
        self
    };
};