package com.play_stream;

import dev.langchain4j.service.UserMessage;
import dev.langchain4j.service.spring.AiService;

@AiService
public interface StreamPlayAiService {
    @UserMessage("""
            Generate a friendly welcome greeting for the app StreamPlay in English, using fewer than 120 characters.
            """)
    String generateGreeting();
}
