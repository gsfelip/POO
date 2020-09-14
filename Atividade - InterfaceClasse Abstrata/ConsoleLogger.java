package br.univille.poo.logger;

class ConsoleLogger implements Logger{

    public void message(String message){

        System.out.println(message);
   
    }
    
}