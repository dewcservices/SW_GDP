package com.example.demo.Services;


import com.example.demo.Dtos.ItemDto;
import com.example.demo.Services.Interfaces.IItemService;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Service;

@Service
@Primary
@Qualifier("itemService")
public class ItemServiceMock implements IItemService {

  private List<ItemDto> mockItems;
  public ItemServiceMock(){
    this.mockItems = new ArrayList<>();
    mockItems.add(new ItemDto(1, "item 1", "this is item 1"));
    mockItems.add(new ItemDto(2, "item 2", "this is item 2"));
  }  

  @Override
  public List<ItemDto> getItems() {
    return this.mockItems;
  }

  @Override
  public ItemDto getItemById(int id) {
    return this.mockItems.get(0);
  }

  @Override
  public ItemDto createItem(ItemDto dto) {
    dto.setId(1);
    return dto;
  }

  @Override
  public ItemDto updateItem(ItemDto dto) {
    return dto;
  }

  
}