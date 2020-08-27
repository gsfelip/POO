public class Fibonacci extends Progression{
  long prev; 

  Fibonacci(){
    this(0, 1);
  }

  Fibonacci(long value1, long value2){
    first = value1;
    prev = value2 - value1;
  }

  protected long nextValue(){
    long temp = prev;
    prev = cur;
    cur += temp;
    return cur;

  }
}
