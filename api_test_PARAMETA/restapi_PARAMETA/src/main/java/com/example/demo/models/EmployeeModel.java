package com.example.demo.models;
// import java.time.LocalDate;
// import java.util.UUID;

import java.sql.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
// import javax.validation.constraints.NotEmpty;

import com.fasterxml.jackson.annotation.JsonFormat;

@Entity
@Table(name = "Employee")
public class EmployeeModel {

	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	@Column(unique = true, nullable = false)
	private Long id;

	// @NotEmpty(message="Employee name cannot be empty")
	private String name;

	// @NotEmpty(message="Employee lastName cannot be empty")
	private String lastName;

	// @NotEmpty(message="Employee documentType cannot be empty")
	private String documentType;

	// @NotEmpty(message="Employee documentNumber cannot be empty")
	private String documentNumber;

	// @NotEmpty(message="Employee dateofBirth cannot be empty")
	@JsonFormat(pattern = "yyyy/MM/dd")
	private Date dateofBirth;

	// @NotEmpty(message="Employee dateOfBonding cannot be empty")
	@JsonFormat(pattern = "yyyy/MM/dd")
	private Date dateOfBonding;

	// @NotEmpty(message="Employee position cannot be empty")
	private String position;

	// @NotEmpty(message="Employee salary cannot be empty")
	private Double salary;

    /**
     * @return Long return the id
     */
    public Long getId() {
        return id;
    }

    /**
     * @param id the id to set
     */
    public void setId(Long id) {
        this.id = id;
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
     * @return Date return the dateofBirth
     */
    public Date getDateofBirth() {
        return dateofBirth;
    }

    /**
     * @param dateofBirth the dateofBirth to set
     */
    public void setDateofBirth(Date dateofBirth) {
        this.dateofBirth = dateofBirth;
    }

    /**
     * @return Date return the dateOfBonding
     */
    public Date getDateOfBonding() {
        return dateOfBonding;
    }

    /**
     * @param dateOfBonding the dateOfBonding to set
     */
    public void setDateOfBonding(Date dateOfBonding) {
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
