/*  Muxall Active IR Detector Arduino Sketch Example.
 *   
 *  This sketch reads the output from the IRD
 *  and lights the LED on the Arduino board.
 *  
 *  Flashig LED indicates weak detection and objects
 *  far away.  Solid LED indicates good detection and
 *  objects close up.
 *  
 *  Depending on your application, you may need
 *  to add debounce code or capacitor.
 *  
 */

//Initialize some globals.
int ttlPin = 51;          // 5v TTL from IRD output. 
int vsPin  = 53;          // 5v power for IRD
//  gndPin = 55           // The ground.
int ledPin = 13;          // The LED connected to digital pin 13

int val       = HIGH;     // Start with val HIGH which is "no detection event".
int led       = LOW;      // Start with the LED OFF.


//Setup Arduino and initialize the io pins
void setup()
{  
  Serial.begin(9600);           // Initialize serial port:

  pinMode(ttlPin, INPUT);       // Set the digital pin as input.
  pinMode(vsPin, OUTPUT);       // Set the digital pin as output.
  pinMode(ledPin, OUTPUT);      // Set the digital pin as output.
  
  digitalWrite(ledPin, LOW);    // Initialize the LED to OFF.
  
  Serial.print("Powering on the IRD...");
  digitalWrite(vsPin, HIGH);     //Turn on the IRD.
  Serial.println("Done");
  
}

//Run the program.
void loop()
{
  val = digitalRead(ttlPin);                        // Read the TTL pin value.
  led = digitalRead(ledPin);                        // Read the LED pin value.
    
  if (val == LOW)                                   // If val is LOW then the IRD has a detection event.
  {
    if (led == LOW)                                 // If the LED is OFF we need to turn it ON.
    {
      digitalWrite(ledPin, HIGH);                   // Turn ON the LED.                    
      Serial.println("IR Detector Triggered!");     // Tell someone.
    }
            
  } else                                            // Otherwise, val is HIGH and the IRD has NO detection event.
  {       
    if (led == HIGH)                                // If the LED is ON we need to turn it OFF.
    {
      digitalWrite(ledPin, LOW);                    // Turn OFF the LED..
      Serial.println("End of IR Detector Event.\n");  // Tell someone.
    }
  }
}


