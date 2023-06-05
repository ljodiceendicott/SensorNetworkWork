
// ultrasonic tutorial:
// https://howtomechatronics.com/tutorials/arduino/ultrasonic-sensor-hc-sr04/
const int pinTrig = 3;
const int pinEcho = 2;

long duration;
int distance; // measured in cm

void setup() {
  pinMode(pinTrig, OUTPUT);
  pinMode(pinEcho, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(pinTrig, LOW);
  delayMicroseconds(2);

  digitalWrite(pinTrig, HIGH);
  delayMicroseconds(10);
  digitalWrite(pinTrig, LOW);

  duration = pulseIn(pinEcho, HIGH);
  distance = duration * 0.034 / 2;
  //Serial.print("Distance: ");
  Serial.write(distance);
  delay(250);
}
