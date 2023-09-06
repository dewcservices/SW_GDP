package com.example.demo.Services.Interfaces;

import com.example.demo.Dtos.ItemDto;

import java.util.List;

public interface IItemService {
  List<ItemDto> getItems();

  ItemDto getItemById(long id);

  ItemDto createItem(ItemDto dto);

  ItemDto updateItem(long id, ItemDto dto);

  void deleteItem(long id);
}
