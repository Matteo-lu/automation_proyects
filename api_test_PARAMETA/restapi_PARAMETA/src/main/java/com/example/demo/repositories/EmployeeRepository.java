package com.example.demo.repositories;

import java.util.UUID;

import com.example.demo.models.EmployeeModel;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EmployeeRepository extends CrudRepository<EmployeeModel, UUID> {

}
