package com.example.demo.Adapter;

import com.example.demo.Dtos.ItemDto;
import com.example.demo.Entities.Item;

import java.util.ArrayList;
import java.util.List;

public class ItemAdapter {
  
  protected ItemAdapter(){}

  public static Item create(ItemDto dto){
    var newItem = new Item();
    update(newItem, dto);
    return newItem;
  }

  public static boolean update(Item currentItem, ItemDto updatedItem){

    var updated = false;
    if(!currentItem.getName().equals(updatedItem.getName())){
      currentItem.setName(updatedItem.getName());
      updated = true;
    }

    if(!currentItem.getDescription().equals(updatedItem.getDescription())){
      currentItem.setDescription(updatedItem.getDescription());
      updated = true;
    }

    return updated;
  }

  public static ItemDto toDto(Item item){
    return new ItemDto(item.getId(), item.getName(), item.getDescription());
  }

  public static List<ItemDto> toDtos(List<Item> items){
    List<ItemDto> dtos = new ArrayList<>();
    for( var item: items){
      dtos.add(toDto(item));
    }
    return dtos;
  }
}
