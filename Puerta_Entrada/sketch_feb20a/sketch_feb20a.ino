int add(int* a,int* b){
  int c = *a + *b;
  return c;
}

/*int add(int a,int b){
  int c = a+b;  
  return c;
}*/
void setup() {

}

void loop() {
int a =2,b=3;
int c = add(&a,&b);
}
