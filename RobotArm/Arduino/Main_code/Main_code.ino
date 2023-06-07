#define togel_s1 13
#define freez_s1 12
#define togel_s2 11
#define freez_s2 10
#define togel_s3 9
#define freez_s3 8
#define togel_s4 7
#define freez_s4 6

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
  // digitalWrite(togel_s3,HIGH);
  digitalWrite(freez_s4,HIGH);

}

void loop() {
  digitalWrite(togel_s1,HIGH);
  digitalWrite(freez_s1,LOW);
  delay(2000);
  digitalWrite(freez_s1,HIGH);
  delay(1500);
  
  // servo 2 start
  digitalWrite(freez_s2,LOW);
  digitalWrite(togel_s2,HIGH);
  delay(500);
  digitalWrite(freez_s2,HIGH);
  delay(1500);

  // servo 3 start
  digitalWrite(togel_s3,HIGH);
  digitalWrite(freez_s3,LOW);
  delay(500);

  digitalWrite(freez_s3,HIGH);
  delay(1500);

  //servo 4
  digitalWrite(togel_s4,HIGH);
  digitalWrite(freez_s4,LOW);
  delay(500);


  digitalWrite(freez_s4,HIGH);
  delay(1500);

  
  digitalWrite(togel_s3,LOW);
  digitalWrite(freez_s3,LOW);
  delay(500);
  digitalWrite(freez_s3,HIGH);
  delay(1500);

  digitalWrite(togel_s2,LOW);
  digitalWrite(freez_s2,LOW);
  delay(500);
  digitalWrite(freez_s2,HIGH);
  
  
  delay(1500);
  digitalWrite(togel_s1,LOW);
  digitalWrite(freez_s1,LOW);
  delay(2000);
  digitalWrite(freez_s1,HIGH);
  delay(1500);

  // servo 2 start
  digitalWrite(freez_s2,LOW);
  digitalWrite(togel_s2,HIGH);
  delay(500);
  digitalWrite(freez_s2,HIGH);
  delay(1500);

  // servo 3 start
  digitalWrite(togel_s3,HIGH);
  digitalWrite(freez_s3,LOW);
  delay(500);

  digitalWrite(freez_s3,HIGH);
  delay(1500);
  //servo 4
  digitalWrite(togel_s4,LOW);
  digitalWrite(freez_s4,LOW);
  delay(500);


  digitalWrite(freez_s4,HIGH);
  delay(1500);

  digitalWrite(togel_s3,LOW);
  digitalWrite(freez_s3,LOW);
  delay(500);
  digitalWrite(freez_s3,HIGH);
  delay(1500);

  digitalWrite(togel_s2,LOW);
  digitalWrite(freez_s2,LOW);
  delay(500);
  digitalWrite(freez_s2,HIGH);
  delay(1500);
}