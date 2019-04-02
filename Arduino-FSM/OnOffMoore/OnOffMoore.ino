enum State{s0,s1};
enum Input{Unknown,uno,cero};
 
// Variables globales
State currentState;
Input currentInput;

int cuenta = 0; 
/* Acciones de los estados 
 *  y condiciones de transiciones
 *  */
void state0(){
  if (currentInput == Input::cero)
    changeState(State::s0);
  
  if (currentInput == Input::uno)
    changeState(State::s1);}
 
void state1(){
  if (currentInput == Input::cero)
    changeState(State::s1);
    
  if (currentInput == Input::uno)
    changeState(State::s0);}
 
void outputs0(){
  digitalWrite(A0, LOW); 
  cuenta = 0;
  Serial.println("s0");
  }
void outputs1(){
  digitalWrite(A0,HIGH);
  Serial.println("s1");
  }

 
void setup(){
  pinMode(A0,OUTPUT);//LED
  pinMode(3,INPUT);//pulsador 1
  pinMode(2,INPUT);//pulsador 0

  outputs0();
  Serial.begin(9600);
  currentState = s0;
  }
 
void loop(){
  readInput();
  updateStateMachine();}
 
// Actualiza el estado de la maquina
void updateStateMachine(){
  switch (currentState){
    case s0: state0(); break;
    case s1: state1(); break;
    }
}
 
// Lee la entrada por puerto serie
void readInput(){
  currentInput = Input::Unknown;
if(digitalRead(3) == HIGH){
  delay(100);
 if(digitalRead(3) == LOW){
  currentInput = Input::uno;Serial.println("1");delay(100);}}

if(digitalRead(2) == HIGH){
  delay(100);
 if(digitalRead(2) == LOW){
  currentInput = Input::cero;
  Serial.println("0");
  delay(100);
  }
  } 
}
 
// Funcion que cambia el estado y dispara las transiciones
void changeState(int newState)
{
  currentState = newState;
 
  switch (currentState)
  {
    case State::s0: outputs0();   break;
    case State::s1: outputs1();   break;
    default: break;
  }
}
