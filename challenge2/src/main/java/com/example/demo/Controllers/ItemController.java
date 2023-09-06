package com.example.demo.Controllers;


import com.example.demo.Dtos.ItemDto;
import com.example.demo.Dtos.SuccessDto;
import com.example.demo.Services.Interfaces.IItemService;

import java.util.List;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/items")
public class ItemController {


  private IItemService service;
  @Autowired
  public ItemController(@Qualifier("itemService") IItemService service){
    this.service = service;
  }

  @GetMapping()
  public ResponseEntity<List<ItemDto>> getItems()  {
		return ResponseEntity.ok(service.getItems());
	}

  @GetMapping("/{itemId}")
  public ResponseEntity<ItemDto> getItem(@PathVariable long itemId)  {
		return ResponseEntity.ok(service.getItemById(itemId));
	}

  @PostMapping()
  public ResponseEntity<ItemDto> createItem(@Valid @RequestBody ItemDto dto)  {
		return ResponseEntity.ok(service.createItem(dto));
	}

  @PutMapping("/{itemId}")
  public ResponseEntity<ItemDto> updateItem(@PathVariable long itemId, @Valid @RequestBody ItemDto dto)  {
		return ResponseEntity.ok(service.updateItem(itemId, dto));
	}

  @DeleteMapping("/{itemId}")
  public ResponseEntity<SuccessDto> deleteItem(@PathVariable long itemId)  {
    service.deleteItem(itemId);
		return ResponseEntity.ok(new SuccessDto("Item successfully deleted"));
	}
}
