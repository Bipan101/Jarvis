from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from api.env file
load_dotenv('api.env')

def test_groq_api():
    """Test Groq API connection"""
    groq_api_key = os.getenv('GROQ_API_KEY')
    
    if not groq_api_key or groq_api_key == 'your_groq_api_key_here':
        print("❌ Please add your Groq API key to api.env file")
        print("   Replace 'your_groq_api_key_here' with your actual Groq API key")
        return False
    
    try:
        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        
        # Test with a simple query
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "user", "content": "Say hello in one sentence."}
            ],
            max_tokens=50,
            temperature=0.7
        )
        
        print("✅ Groq API is working!")
        print(f"Test response: {response.choices[0].message.content}")
        return True
        
    except Exception as e:
        print(f"❌ Groq API error: {e}")
        return False

def chat_with_groq():
    """Interactive chat using Groq API"""
    groq_api_key = os.getenv('GROQ_API_KEY')
    
    if not groq_api_key or groq_api_key == 'your_groq_api_key_here':
        print("❌ Please add your Groq API key to api.env file first!")
        return
    
    client = OpenAI(
        api_key=groq_api_key,
        base_url="https://api.groq.com/openai/v1"
    )
    
    print("\n" + "="*50)
    print("🚀 GROQ AI CHAT")
    print("="*50)
    print("Available models:")
    print("1. llama3-8b-8192 (Default - Fast)")
    print("2. mixtral-8x7b-32768 (More capable)")
    print("3. gemma-7b-it")
    print("\nType 'quit' to exit, 'model' to change model")
    print("="*50)
    
    current_model = "llama3-8b-8192"
    print(f"Using model: {current_model}")
    
    while True:
        user_input = input("\n🧑 You: ").strip()
        
        if user_input.lower() in ['quit', 'exit']:
            print("👋 Goodbye!")
            break
        
        if user_input.lower() == 'model':
            print("\nSelect model:")
            print("1. llama3-8b-8192")
            print("2. mixtral-8x7b-32768") 
            print("3. gemma-7b-it")
            choice = input("Enter choice (1-3): ").strip()
            
            models = {
                "1": "llama3-8b-8192",
                "2": "mixtral-8x7b-32768",
                "3": "gemma-7b-it"
            }
            
            if choice in models:
                current_model = models[choice]
                print(f"✅ Switched to: {current_model}")
            else:
                print("❌ Invalid choice")
            continue
        
        if not user_input:
            continue
        
        try:
            print("🤖 AI: ", end="", flush=True)
            
            response = client.chat.completions.create(
                model=current_model,
                messages=[
                    {"role": "user", "content": user_input}
                ],
                max_tokens=1000,
                temperature=0.7,
                stream=True  # Enable streaming for real-time response
            )
            
            # Stream the response
            full_response = ""
            for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    print(content, end="", flush=True)
                    full_response += content
            
            print()  # New line after response
            
        except Exception as e:
            print(f"\n❌ Error: {e}")

def main():
    print("🤖 Groq AI Client")
    print("="*50)
    
    # Test the API first
    print("Testing Groq API connection...")
    
    if test_groq_api():
        print("\n🎉 Setup successful!")
        choice = input("\nStart interactive chat? (y/n): ").strip().lower()
        if choice == 'y':
            chat_with_groq()
    else:
        print("\n📝 Setup Instructions:")
        print("1. Open your api.env file")
        print("2. Replace 'your_groq_api_key_here' with your actual Groq API key")
        print("3. Save the file and run this script again")
        print("\n💡 Your Groq API key should start with 'gsk_'")

if __name__ == "__main__":
    main()
