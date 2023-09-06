package com.example.demo.Exception;

import org.springframework.http.HttpStatus;

public class RequestProcessingException extends RuntimeException {

    private final HttpStatus code;

    public RequestProcessingException(HttpStatus code) {
        super();
        this.code = code;
    }

    public RequestProcessingException(String message, Throwable cause, HttpStatus code) {
        super(message, cause);
        this.code = code;
    }

    public RequestProcessingException(String message, HttpStatus code) {
        super(message);
        this.code = code;
    }

    public RequestProcessingException(Throwable cause, HttpStatus code) {
        super(cause);
        this.code = code;
    }

    public HttpStatus getCode(){
      return this.code;
    }

    
}
