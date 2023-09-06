package com.example.demo.Repository;

import com.example.demo.Entities.Item;
import com.example.demo.Repository.Interfaces.IDao;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

@Service
@Qualifier("itemDao")
public class ItemDaoMock implements IDao<Item> {

  private List<Item> mockItems;

  public ItemDaoMock(){
    this.mockItems = new ArrayList<>();
  }

  private Item find(long id){
    for (var item : mockItems) {
      if(item.getId() == id){
        return item;
      }
    }
    return null;
  }

  
  @Override
  public Item get(long id) {
    return find(id);
  }

  @Override
  public Item save(Item item) {
    item.setId((long)(mockItems.size() + 1));
    mockItems.add(item);
    return item;
  }

  @Override
  public void delete(long id) {
    var item = find(id);
    if(item != null){
      mockItems.remove(item);
    }
  }

  @Override
  public List<Item> getAll() {
    return this.mockItems;
  }

  @Override
  public Item update(Item item) {
    var currentItem = find(item.getId());
    if(currentItem != null){
      mockItems.remove(currentItem);
      mockItems.add(item);
      return item;
    }
    return null;
  }
  
}
