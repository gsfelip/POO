package br.univille.poo.logger;

class Main {

	public static void main(final String[] args) {

		Logger log = LoggerFactory.getInstance().createConsoleLogger();
		Logger txt = LoggerFactory.getInstance().createFileLogger();

        log.message("Teste log");
        txt.message("Teste log");
        
	}

}