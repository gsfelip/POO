package br.univille.poo.logger;
import java.io.File;
import java.io.FileWriter;

class FileLogger implements Logger {

	@Override
	public void message(String message) {

		try {
			
			File file = new File("log.txt");

			FileWriter writer = new FileWriter(file, true)
			writer.write(message + "\n");
			writer.close();

		} catch (Exception exeption) {

			exeption.printStackTrace();
		}
	}
}