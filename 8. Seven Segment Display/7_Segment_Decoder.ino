//int a=2,b=3,c=4,d=5,e=6,f=7,g=8;
int a[7] = {2,3,4,5,6,7,8}; 

void setup()
{
  for(int i=0;i<7;i++){
    pinMode(a[i],OUTPUT);
  }
}

void loop()
{
  for(int i=0;i<=10;i++){ // 0 1 2 3 4 5 6 7 8 9 | 10 (no number found ERROR TEST) |
    display_segment(String(i));
    delay(500);
  }
}

void display_segment(String v){
  int ch[7];

  if (v == "0") {
      ch[0] = 1;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 1;
      ch[4] = 1;
      ch[5] = 1;
      ch[6] = 0;
  }
  

  else if (v == "1") {
      ch[0] = 0;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 0;
      ch[4] = 0;
      ch[5] = 0;
      ch[6] = 0;
  }
  

  else if (v == "2") {
      ch[0] = 1;
      ch[1] = 1;
      ch[2] = 0;
      ch[3] = 1;
      ch[4] = 1;
      ch[5] = 0;
      ch[6] = 1;
  }
  

  else if (v == "3") {
      ch[0] = 1;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 1;
      ch[4] = 0;
      ch[5] = 0;
      ch[6] = 1;
  }
  

  else if (v == "4") {
      ch[0] = 0;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 0;
      ch[4] = 0;
      ch[5] = 1;
      ch[6] = 1;
  }
  

  else if (v == "5") {
      ch[0] = 1;
      ch[1] = 0;
      ch[2] = 1;
      ch[3] = 1;
      ch[4] = 0;
      ch[5] = 1;
      ch[6] = 1;
  }
  

  else if (v == "6") {
      ch[0] = 0;
      ch[1] = 0;
      ch[2] = 1;
      ch[3] = 1;
      ch[4] = 1;
      ch[5] = 1;
      ch[6] = 1;
  }
  

  else if (v == "7") {
      ch[0] = 1;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 0;
      ch[4] = 0;
      ch[5] = 0;
      ch[6] = 0;
  }
  

  else if (v == "8") {
      ch[0] = 1;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 1;
      ch[4] = 1;
      ch[5] = 1;
      ch[6] = 1;
  }
  

  else if (v == "9") {
      ch[0] = 1;
      ch[1] = 1;
      ch[2] = 1;
      ch[3] = 0;
      ch[4] = 0;
      ch[5] = 1;
      ch[6] = 1;
  }

  else{
    for(int i=0;i<6;i++){
      ch[i] = 0;
    }
    ch[6] = 1;

    // "-" => no symbol found
  }


  for(int i=0;i<7;i++){
    digitalWrite(a[i],ch[i]);
  }
}