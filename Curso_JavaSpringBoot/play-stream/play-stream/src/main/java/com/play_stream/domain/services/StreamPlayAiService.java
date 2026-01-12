package com.play_stream.domain.services;

import dev.langchain4j.service.UserMessage;
import dev.langchain4j.service.V;
import dev.langchain4j.service.spring.AiService;

@AiService
public interface StreamPlayAiService {
    @UserMessage("""
            Generate a friendly welcome greeting for the app {{platform}} in English, using fewer than 120 characters.
            """)
    String generateGreeting(@V("platform") String platform);
}
