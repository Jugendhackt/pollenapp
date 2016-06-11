package pollenrechnung;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class wetterwarte {
public static double l = 16.4;
public static double b = 48;
public static double h = 450;
public static double w = 600;
public static double x;
public static double y;
public static PrintWriter warten;

	public static void main(String[] args) throws IOException {
		warten = new PrintWriter(new FileWriter ("warten"));
		
		 BufferedReader in = new BufferedReader(new FileReader("warte.txt")); 
		 // dokunemt l,b 
			      String line1 = in.readLine();
		      String line2 = in.readLine();
		    
		 		while(line2 != null)	{
		 			  l = Double.parseDouble(line1);
		      b = Double.parseDouble(line2);
		 		
		 		x = (b * h / 180.0) + (h / 2);
		 				y = (l * w / 360.0) + (w / 2);
		 			
		 				warten.println(x);
		 				warten.println(y);
		 			line1 = in.readLine();
		 			line2 = in.readLine();
		 		}
		 		
		warten.close();
		
	
	}
}

