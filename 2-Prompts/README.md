# LangChain Prompts Examples

This directory contains examples demonstrating various prompt engineering techniques using LangChain. It showcases how to create and manage different types of prompts for LLM applications.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Create a `.env` file with your API keys (OpenAI, Google, HuggingFace)
   - Example:
     ```
     OPENAI_API_KEY=your_openai_api_key
     GOOGLE_API_KEY=your_google_api_key
     HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
     ```

## Example Files

### 1. Basic Messaging (`message.py`)
Demonstrates how to use different types of messages (System, Human, AI) with LangChain's message system and OpenAI's API.

Run it:
```bash
python message.py
```

### 2. Chat Prompt Templates (`chat_prompt_template.py`)
Shows how to create and use chat prompt templates with variable substitution.

Run it:
```bash
python chat_prompt_template.py
```

### 3. Interactive Chatbot (`chatbot.py`)
A simple interactive chatbot implementation that maintains conversation history.

Run it:
```bash
python chatbot.py
```

### 4. Message Placeholders (`message_placeholder.py`)
Demonstrates how to use message placeholders to incorporate chat history into new prompts.

Run it:
```bash
python message_placeholder.py
```

## Key Concepts

1. **Message Types**:
   - `SystemMessage`: Instructions for the AI's behavior
   - `HumanMessage`: Represents user input
   - `AIMessage`: Represents AI responses

2. **Chat Prompt Templates**:
   - Structured way to format prompts for chat models
   - Supports variable substitution
   - Can include multiple message types

3. **Messages Placeholder**:
   - Allows inserting a list of messages into a prompt template
   - Useful for incorporating chat history

4. **Chat History Management**:
   - Techniques for maintaining and using conversation context
   - Reading/writing chat history from files

## Models Used

The examples in this directory primarily use OpenAI's models:
- `gpt-4o-mini`: A balanced model offering good performance at a reasonable cost

Other supported models (via installed packages):
- Anthropic Claude models
- Google Gemini models
- Hugging Face models (including local options)

## Further Learning

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Prompt Engineering Guide](https://www.promptingguide.ai)
- [OpenAI Documentation](https://platform.openai.com/docs/introduction)
