package pollenrechnung;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class rechnung {

public static PrintWriter wind;
// wind: N(0|1) NO(-1|1) O(-1|0) SO(-1|-1) S(0|-1) SW(1|-1) w(1|0)
public static int ax;
public static int ay;
public static String a = "Nord"; //Eingabe durch Tabelle
	public static void main(String[] args) throws IOException {
		//print
wind = new PrintWriter(new FileWriter ("wind"));
if (a.equals ("Nord")){
	ax = 0;
	ay = 1;
}
else if (a.equals(("Ost"))){
	ax = -1;
	ay = 0;
	
}
else if (a.equals("Süd")){
	ax = 0;
			ay = -1;
}
else if (a.equals("West")){
	ax = 1;
	ay = 0;
}
else if (a.equals("Nordost")){
	ax = -1;
	ay = 1;
}
else if (a.equals("Südost")){
	ax = -1;
	ay = -1;
}
else if (a.equals("Südwest")){
	ax = 1;
	ay = -1;
}
else if (a.equals("Nordwest")){
	ax = 1;
	ay = 1;
}

wind.println(ax);
wind.println(ay);
wind.close ();
}
}