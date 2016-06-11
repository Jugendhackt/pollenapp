package pollenrechnung;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class baumabstand {
public static double l;
public static double b;
public static double h = 450; //VERÄNDERN!!
public static double w = 600;
public static double x;
public static double y;
public static PrintWriter karte;

	public static void main(String[] args) throws IOException {
	
		 BufferedReader in = new BufferedReader(new FileReader("warte.txt"));
		 //dokument l,b
		
karte = new PrintWriter(new FileWriter ("karte"));
     String line1 = in.readLine();
     String line2 = in.readLine();
   


		while(line2 != null)	{
			  l = Double.parseDouble(line1);
     b = Double.parseDouble(line2);
		
		x = (b * h / 180.0) + (h / 2);
				y = (l * w / 360.0) + (w / 2);
			
				karte.println(x);
				karte.println(y);
			line1 = in.readLine();
			line2 = in.readLine();
		}
		karte.close();
	}
}