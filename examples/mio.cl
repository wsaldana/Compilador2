class Main inherits IO {
    x: Int <- 1;
    y: Int <- 2;
    main(x:Int): Int {
        {(let y: Int in 2 + 1);}
    };
};