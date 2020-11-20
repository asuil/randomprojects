const int servo_pin = 6;
char servo_angle;
#include <Servo.h>
Servo servo;

void setup() {
    Serial.begin(9600);
    servo.attach(servo_pin);
}

void loop() {
    if (Serial.available() > 0) {
        servo_angle = Serial.read();
        Serial.println(servo_angle);
        servo.write(servo_angle);
    }
}
