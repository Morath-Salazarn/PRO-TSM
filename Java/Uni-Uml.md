```Mermaid
classDiagram

Person <|-- Dozent
Person <|-- Student
Student <|-- PromotionsStudent

class Person{
    -vorname String
    -nachname String
}

class Student{
    -matrikelNr String
}

class PromotionsStudent{
    -doktorVater
}
```