package com.example.demo.Repository.Interfaces;

import com.example.demo.Entities.Item;

import java.util.List;

// https://www.baeldung.com/java-dao-pattern

public interface IDao<T> {
    
  T get(long id);
  
  List<T> getAll();
  
  Item save(T t);
  
  Item update(T t);
  
  void delete(long id);
}
