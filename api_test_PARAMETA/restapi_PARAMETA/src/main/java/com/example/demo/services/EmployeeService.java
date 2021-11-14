package com.example.demo.services;

import java.util.ArrayList;

import com.example.demo.models.EmployeeModel;
import com.example.demo.repositories.EmployeeRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class EmployeeService {
	@Autowired
	EmployeeRepository employeeRepository;

	public ArrayList<EmployeeModel> getEmployees(){
		return (ArrayList<EmployeeModel>) employeeRepository.findAll();
	}

	public EmployeeModel saveEmployee(EmployeeModel employee){
		return employeeRepository.save(employee);
	}
}
