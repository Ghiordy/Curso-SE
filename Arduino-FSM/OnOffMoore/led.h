class led{
  private:
    enum estado{s0,s1};
    //estado State;
  public:
    void SetEstado(enum sN){
      estado :: sN;
      }
      
  led(){
    estado :: s0;
    }
  
    enum GetEstado(){
      return estado;
      }
  };
