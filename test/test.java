public class Employee {
    protected String name;
    private String id;
    int grade;
    test2 test = new test2();

    public Employee(String name, String id, int grade) {
        System.out.println("Two argument constructor");
        this.name = name;
        this.id = id;
        this.grade = grade;
    }


    public Employee(){
        System.out.println("Zero argument constructor");
    }
}
