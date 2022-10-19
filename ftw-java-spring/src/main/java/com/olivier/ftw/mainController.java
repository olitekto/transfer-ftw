package com.olivier.ftw;

import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.HttpStatusCodeException;
import org.springframework.web.client.RestTemplate;


@RestController
public class mainController {
    
    // @GetMapping("/checkStatus")
    // public Object checkStatus() {

    //     String url = "https://jsonplaceholder.typicode.com/todos/1";
    //     RestTemplate restTemplate = new RestTemplate();
    //     Object result = restTemplate.getForObject(url, Object.class);
    //     return result;
    // }
    @GetMapping("/checkStatus")
    public Object checkStatus(@RequestParam String id)
    {
        try {
            HttpHeaders headers = new HttpHeaders();
            headers.set("Authorization", "Bearer XXXXXX");
            HttpEntity<String> entity = new HttpEntity<String>(headers);
            RestTemplate restTemplate = new RestTemplate();
            ResponseEntity<Object> response = restTemplate.exchange("https://api.flutterwave.com/v3/transfers/"+id,
            HttpMethod.GET,entity, new ParameterizedTypeReference<Object>() {});
            return response.getBody(); 
        } catch(HttpStatusCodeException e) {
            return ResponseEntity.status(e.getRawStatusCode()).headers(e.getResponseHeaders())
                    .body(e.getResponseBodyAsString());
        }
    }

    @PostMapping("/initiateTransfer")
    public Object makeTransfer(@RequestBody String payload) {

       try {
            HttpHeaders headers = new HttpHeaders();
            headers.setContentType(MediaType.APPLICATION_JSON);
            headers.set("Authorization", "Bearer XXXXXX");
            HttpEntity<String> entity = new HttpEntity<String>(payload, headers);
            RestTemplate restTemplate = new RestTemplate();
            ResponseEntity<Object> response = restTemplate.exchange("https://api.flutterwave.com/v3/transfers",
            HttpMethod.POST,entity, new ParameterizedTypeReference<Object>() {});
            return response.getBody(); 
        } catch(HttpStatusCodeException e) {
            return ResponseEntity.status(e.getRawStatusCode()).headers(e.getResponseHeaders())
                    .body(e.getResponseBodyAsString());
        }
    }
}
