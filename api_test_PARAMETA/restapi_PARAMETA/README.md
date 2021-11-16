# Spring Boot Employee test project for PARAMETA company

This is a example Java / Spring Boot (version 2.5.6) application built as interview test for PARAMETA company.

## How to Run

This application was created through https://start.spring.io and to run it make sure of the following.

* Clone this repository
* Make sure you are using JDK 11.0.11
* Run the sql script ```setup_mysql_databse.sql``` to create a database with the name springboot
* Update the file ```restapi_PARAMETA/src/main/resources/application.properties``` with an user name and password with the permissions to access the database.

Once the application runs you should see something like this

```
2021-11-15 21:00:50.171  INFO 16017 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8080 (http) with context path ''
2021-11-15 21:00:50.182  INFO 16017 --- [           main] com.example.demo.DemoApplication         : Started DemoApplication in 4.433 seconds (JVM running for 4.918)
```

## About the Service

The service is just a simple Employee REST service. It uses a mySQL database to store the data.  If your database connection properties work, you can call some REST endpoints through localhost on **port 80800**.

Here are the endpoints you can call:

### Get all employees

```
GET
http://localhost:8080/employee
Response: HTTP 200 (OK)
```

### Get specific employee

```
GET
http://localhost:8080/employee/<id>
Response: HTTP 200 (OK)
```
### Delete specific employee

```
DELETE
http://localhost:8080/employee/<id>
Response: HTTP 200 (OK) User id <id> was deleted
```
### Create specific employee

```
POST
{
    "name": <String>,
    "lastName": <String>,
    "documentType": <String>,
    "documentNumber": <String>,
    "dateOfBirth": <LocalDate> "dd/MM/yyyy",
    "dateOfBonding": <LocalDate> "dd/MM/yyyy",
    "position": <String>,
    "salary": <Double>
}

http://localhost:8080/employee
Response: HTTP 200 (OK)
```

### Update specific employee

```
POST
{
    "id": <Integer>
    "name": <String>,
    "lastName": <String>,
    "documentType": <String>,
    "documentNumber": <String>,
    "dateOfBirth": <LocalDate> "dd/MM/yyyy",
    "dateOfBonding": <LocalDate> "dd/MM/yyyy",
    "position": <String>,
    "salary": <Double>
}

http://localhost:8080/employee
Response: HTTP 200 (OK)
```

# Questions and Comments: mateolondono.u@gmail.com
