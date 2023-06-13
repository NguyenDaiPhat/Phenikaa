public class Person {
    String tensv;
    int tuoi;
    Person(String tensv ){
        this.tensv = tensv;
    }
    Person(int tuoi ){
        this.tuoi = tuoi;
    }
    Person(String tensv,int tuoi ){
        this.tensv = tensv;
        this.tuoi = tuoi;
    }
    Person(Person a ){
        this.tensv=a.tensv;
        this.tuoi = a.tuoi;
    }
}
