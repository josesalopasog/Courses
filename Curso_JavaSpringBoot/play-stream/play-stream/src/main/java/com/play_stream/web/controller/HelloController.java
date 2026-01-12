package com.play_stream.web.controller;


import com.play_stream.domain.services.StreamPlayAiService;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {
    private final String platform;
    private final StreamPlayAiService aiService;

    public HelloController( @Value("${spring.application.name}") String platform, StreamPlayAiService aiService) {
        this.platform = platform;
        this.aiService = aiService;
    }

    @GetMapping("/hi")
    public String hello(){
        return this.aiService.generateGreeting(platform);
    }
}
