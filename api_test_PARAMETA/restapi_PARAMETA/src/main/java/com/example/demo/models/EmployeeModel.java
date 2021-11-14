package com.example.demo.models;
import java.time.LocalDate;
import java.util.UUID;

import javax.persistence.*;


@Entity
@Table(name = "Employee")
public class EmployeeModel {

	@Id
	@Column(unique = true, nullable = false)
	private UUID id;
	private String name;
	private String lastName;
	private String documentType;
	private String documentNumber;
	private LocalDate dateofBirth;
	private LocalDate dateOfBonding;
	private String position;
	private Double salary;

    /**
     * @return UUID return the id
     */
    public UUID getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(UUID id) {
        this.id = UUID.randomUUID();
    }

    /**
     * @return String return the name
     */
    public String getName() {
        return name;
    }

    /**
     * @param name the name to set
     */
    public void setName(String name) {
        this.name = name;
    }

    /**
     * @return String return the lastName
     */
    public String getLastName() {
        return lastName;
    }

    /**
     * @param lastName the lastName to set
     */
    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    /**
     * @return String return the documentType
     */
    public String getDocumentType() {
        return documentType;
    }

    /**
     * @param documentType the documentType to set
     */
    public void setDocumentType(String documentType) {
        this.documentType = documentType;
    }

    /**
     * @return String return the documentNumber
     */
    public String getDocumentNumber() {
        return documentNumber;
    }

    /**
     * @param documentNumber the documentNumber to set
     */
    public void setDocumentNumber(String documentNumber) {
        this.documentNumber = documentNumber;
    }

    /**
     * @return LocalDate return the dateofBirth
     */
    public LocalDate getDateofBirth() {
        return dateofBirth;
    }

    /**
     * @param dateofBirth the dateofBirth to set
     */
    public void setDateofBirth(LocalDate dateofBirth) {
        this.dateofBirth = dateofBirth;
    }

    /**
     * @return LocalDate return the dateOfBonding
     */
    public LocalDate getDateOfBonding() {
        return dateOfBonding;
    }

    /**
     * @param dateOfBonding the dateOfBonding to set
     */
    public void setDateOfBonding(LocalDate dateOfBonding) {
        this.dateOfBonding = dateOfBonding;
    }

    /**
     * @return String return the position
     */
    public String getPosition() {
        return position;
    }

    /**
     * @param position the position to set
     */
    public void setPosition(String position) {
        this.position = position;
    }

    /**
     * @return Double return the salary
     */
    public Double getSalary() {
        return salary;
    }

    /**
     * @param salary the salary to set
     */
    public void setSalary(Double salary) {
        this.salary = salary;
    }

}
