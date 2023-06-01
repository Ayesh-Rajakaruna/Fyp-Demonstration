#define togel_s1 2
#define freez_s1 3
#define togel_s2 4
#define freez_s2 5
#define togel_s3 6
#define freez_s3 7
#define togel_s4 8
#define freez_s4 9

void setup() {
  pinMode(togel_s1,OUTPUT);
  pinMode(freez_s1,OUTPUT);
  pinMode(togel_s2,OUTPUT);
  pinMode(freez_s2,OUTPUT);
  pinMode(togel_s3,OUTPUT);
  pinMode(freez_s3,OUTPUT);
  pinMode(togel_s4,OUTPUT);
  pinMode(freez_s4,OUTPUT);
  // put your setup code here, to run once:
  digitalWrite(freez_s1,HIGH);
  digitalWrite(freez_s2,HIGH);
  digitalWrite(freez_s3,HIGH);
  digitalWrite(freez_s4,HIGH);

}

void loop() {
  digitalWrite(togel_s4,HIGH);
  digitalWrite(freez_s4,LOW);
  delay(400);

  digitalWrite(freez_s4,HIGH);
  delay(2000);

  digitalWrite(togel_s4,LOW);
  digitalWrite(freez_s4,LOW);
  delay(400);

  digitalWrite(freez_s4,HIGH);
  delay(1500);

  // put your main code here, to run repeatedly:

}