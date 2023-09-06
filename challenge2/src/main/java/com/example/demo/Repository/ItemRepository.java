package com.example.demo.Repository;

import com.example.demo.Entities.Item;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;

public interface ItemRepository extends JpaRepository<Item, Long> {
  public Optional<Item> findByName(String name);
}
