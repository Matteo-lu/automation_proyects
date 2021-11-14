package com.example.demo.services;

import java.util.ArrayList;
import java.util.Optional;

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

	public Optional<EmployeeModel> geteById(Long id){
		return employeeRepository.findById(id);
	}

	public boolean deleteEmployeeById(Long id){
		try{
			employeeRepository.deleteById(id);
			return true;
		}catch(Exception err){
			return false;
		}
	}
}
