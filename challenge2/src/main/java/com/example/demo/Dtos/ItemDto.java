package com.example.demo.Dtos;


import com.fasterxml.jackson.annotation.JsonProperty;

import javax.validation.constraints.NotEmpty;
import javax.validation.constraints.Size;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ItemDto {
  @JsonProperty("id")
  private Long id;
  
  @JsonProperty("name")
  @NotEmpty
  @Size(min = 5, message = "name should have at least 5 characters")
  private String name;
  
  @JsonProperty("description")
  @NotEmpty
  @Size(min = 5, message = "description should have at least 2 characters")
  private String description;
}
