// C++ code
//
int mesafe = 0;

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
  pinMode(3, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop()
{
  mesafe = 0.01723 * readUltrasonicDistance(6, 7);
  if (mesafe > 40) {
    digitalWrite(3, HIGH);
    digitalWrite(2, LOW);
  } else {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    tone(4, 523, 500); // play tone 60 (C5 = 523 Hz)
    delay(500); // Wait for 500 millisecond(s)
    noTone(5);
    delay(500); // Wait for 500 millisecond(s)
  }
}