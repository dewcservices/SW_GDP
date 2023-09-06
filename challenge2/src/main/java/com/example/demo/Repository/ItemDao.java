package com.example.demo.Repository;

import com.example.demo.Entities.Item;
import com.example.demo.Exception.RequestProcessingException;
import com.example.demo.Repository.Interfaces.IDao;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

@Service
@Primary
@Qualifier("itemDao")
public class ItemDao implements IDao<Item>{

  private final ItemRepository repository;

  @Autowired
  public ItemDao(ItemRepository repository){
    this.repository = repository;
  }

  private Item find(long id) throws RequestProcessingException{
    var temp = this.repository.findById(id);
    if(temp.isEmpty()){
      throw new RequestProcessingException("Item could not be found", HttpStatus.NOT_FOUND);
    }
    return temp.get();
  }

  @Override
  public Item get(long id) throws RequestProcessingException {
    return find(id);
  }

  @Override
  public List<Item> getAll() {
    return this.repository.findAll();
  }

  @Override
  public Item save(Item item) {
    var temp = this.repository.findByName(item.getName());
    if(temp.isPresent()){
      throw new RequestProcessingException("Item with matching name already exists.", HttpStatus.BAD_REQUEST);
    }
    return this.repository.save(item);
  }

  @Override
  public Item update(Item item) throws RequestProcessingException {
    return this.repository.save(item);

  }

  @Override
  public void delete(long id) {
    var item = find(id);
    this.repository.delete(item);
  }
  
}
