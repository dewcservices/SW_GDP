package com.example.demo.Dtos;

import com.example.demo.Exception.LowerCaseClassNameResolver;
import com.fasterxml.jackson.annotation.JsonTypeInfo;
import com.fasterxml.jackson.databind.annotation.JsonTypeIdResolver;

import org.springframework.http.HttpStatus;
import lombok.Data;

@Data
@JsonTypeInfo(include = JsonTypeInfo.As.WRAPPER_OBJECT, use = JsonTypeInfo.Id.CUSTOM, property = "error", visible = true)
@JsonTypeIdResolver(LowerCaseClassNameResolver.class)
public class ApiErrorDto {
  private HttpStatus code;
  private String message;
  private String debugMessage;

  public ApiErrorDto(HttpStatus code){
    this.code = code;
  }

  public ApiErrorDto(HttpStatus code, Throwable ex){
    this.code = code;
    this.message = "Unexpected error";
    this.debugMessage = ex.getLocalizedMessage();
  }

  public ApiErrorDto(HttpStatus code, String message, Throwable ex){
    this.code = code;
    this.message = message;
    this.debugMessage = ex.getLocalizedMessage();
  }
}
