package com.example.demo.controllers;

import java.util.ArrayList;
import java.util.Optional;

import javax.validation.Valid;

import com.example.demo.models.EmployeeModel;
import com.example.demo.services.EmployeeService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/employee")
public class EmployeeController{
	@Autowired
	EmployeeService employeeService;

	@GetMapping
	public ArrayList<EmployeeModel> getEmployees(){
		return employeeService.getEmployees();
	}

	@PostMapping()
	public EmployeeModel saveEmployee(@Valid @RequestBody EmployeeModel employee){
		System.out.println(employee);
		return this.employeeService.saveEmployee(employee);
	}

	@GetMapping(path = "/{id}")
	public Optional<EmployeeModel> getEmployeeById(@PathVariable("id") Long id){
		return this.employeeService.geteById(id);
	}


	@DeleteMapping(path = "/{id}")
	public String deleteById(@PathVariable("id") Long id){
		boolean ok = this.employeeService.deleteEmployeeById(id);
		if (ok){
			return String.format("User id %d was deleted ", id);
		}else{
			return String.format("Could not delete user with id %d ", id);
		}
	}
}
