class vehiculo{
  private:
    String color;
    float cilindraje;
  
  public:
    void SetColor(String COLOR){
      color = COLOR;
      }
    void SetCilindraje(float CILINDRAJE){
      cilindraje = CILINDRAJE;
      }

  vehiculo(){
    color = "blanco";
    cilindraje = 0;
    }
  
  public:
    String GetColor(){
      return color;
      }
    float GetCilindraje(){
      return cilindraje;
      }
  };
