--extracted from https://github.com/NiklasReiche/yapl

class Factorial {
  	var: Int <- 0;
  	
  	factorial(n: Int) : Int {
      {( let f : Int in
      	 if n=0 then f<-0 else
         if n=1 then f<-1 else
        	 f<-n*factorial(n-1)
         fi fi
       );}
    };
  };

class Main inherits IO {
    n: Int <- 4;
  	myFactorial: Factorial;
  
  	main() : SELF_TYPE {
        {
            myFactorial <- new Factorial;
            out_int(myFactorial.factorial(n));
            self;
        }
    };
};