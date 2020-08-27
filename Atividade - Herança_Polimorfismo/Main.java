class Main {
  public static void main(String[] args) {
    Progression prog;
    System.out.println("Progressão de Fibonacci com valores iniciais 4 e 6:");
    prog = new Fibonacci(4,6);
    prog.printProgression(10);
  }
}
