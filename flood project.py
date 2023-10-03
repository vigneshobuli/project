// C++ code
//
int level = 0;

long readUltrasonicDistance(int triggerPin, int echoPin)
{
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}

void setup()
{
  pinMode(5, OUTPUT);
  Serial.begin(9600);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
}

void loop()
{
  level = 0.01723 * readUltrasonicDistance(2, 3);
  if (level <= 40) {
    tone(5, 523, 1000); // play tone 60 (C5 = 523 Hz)
    Serial.println("Evacuate ");
    digitalWrite(6, HIGH);
    digitalWrite(7, LOW);
  }
  if (level > 40) {
    digitalWrite(6, LOW);
    digitalWrite(7, HIGH);
    Serial.println("Normal");
  }

  1 > 40;
  delay(10); // Delay a little bit to improve simulation performance
}