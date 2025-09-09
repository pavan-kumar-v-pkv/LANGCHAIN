# LANGCHAIN

A comprehensive exploration of the LangChain framework for building LLM-powered applications.

## Project Overview

This repository contains examples and tutorials for working with LangChain, a framework designed to simplify the development of applications using Large Language Models (LLMs). The project is organized into modular sections, each focusing on different aspects of LLM integration and application development.

## Directory Structure

### 1. Models
The `1-Models` directory demonstrates how to work with various LLM providers:

- **1.1-LLMs**: Examples of text completion models
- **1.2-ChatModels**: Examples of various chat models
  - OpenAI GPT models
  - Anthropic Claude models
  - Google Gemini models
  - Hugging Face models (API and local)
- **1.3-EmbeddedModels**: Examples of embedding models and document similarity

### 2. Prompts
The `2-Prompts` directory showcases prompt engineering techniques:

- **Basic Messaging**: How to use different message types (System, Human, AI)
- **Chat Prompt Templates**: Creating and using structured prompt templates
- **Interactive Chatbot**: Building a conversational interface with memory
- **Message Placeholders**: Advanced techniques for incorporating chat history

## Setup

Each directory contains its own `requirements.txt` file for the specific dependencies needed.

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the requirements for the section you're working with:
   ```bash
   cd directory-name
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
   ```

## Key Concepts

- **Model Integration**: Connect to various LLM providers through a unified interface
- **Prompt Engineering**: Structure and optimize inputs to LLMs
- **Chains and Sequences**: Combine models and prompts into reusable components
- **Memory**: Maintain conversation history and context

## Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [LangChain GitHub](https://github.com/langchain-ai/langchain)