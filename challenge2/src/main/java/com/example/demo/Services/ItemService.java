package com.example.demo.Services;

import com.example.demo.Adapter.ItemAdapter;
import com.example.demo.Dtos.ItemDto;
import com.example.demo.Entities.Item;
import com.example.demo.Repository.Interfaces.IDao;
import com.example.demo.Services.Interfaces.IItemService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

@Service
@Primary
@Qualifier("itemService")
public class ItemService implements IItemService {

  private final IDao<Item> dao;

  @Autowired
  public ItemService(@Qualifier("itemDao") IDao<Item> dao){
    this.dao = dao;  
  }

  @Override
  public List<ItemDto> getItems() {
    return ItemAdapter.toDtos(this.dao.getAll());
  }

  @Override
  public ItemDto getItemById(long id) {
    return ItemAdapter.toDto(this.dao.get(id));    
  }

  @Override
  public ItemDto createItem(ItemDto dto) {
    return ItemAdapter.toDto(this.dao.save(ItemAdapter.create(dto)));    
  }

  @Override
  public ItemDto updateItem(long id, ItemDto dto) {
    var item = this.dao.get(id);
    if(ItemAdapter.update(item, dto)){
      return ItemAdapter.toDto(this.dao.update(item));
    }
    return dto;
  }

  @Override
  public void deleteItem(long id) {
    this.dao.delete(id);
  }
  
  
}
