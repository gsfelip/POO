package br.univille.poo.logger;

class ConcreteLoggerFactory extends LoggerFactory {

	@Override
	public Logger createConsoleLogger() {

		ConsoleLogger mensagem = new ConsoleLogger();
		return mensagem;

	}

	@Override
	public Logger createFileLogger() {

		FileLogger mensagem = new FileLogger();
		return mensagem;

	}
}