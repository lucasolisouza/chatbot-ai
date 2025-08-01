from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do chatbot
def setup_chatbot():
    print("Chatbot Terminal com Groq (LLaMA3)")
    print("Digite 'sair' para encerrar\n")
    
    # Configura o modelo 
    llm = ChatGroq(
        temperature=0.7,
        model_name="llama3-8b-8192",
        api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Template de conversa
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é um assistente útil. Responda de forma concisa e clara."),
        ("human", "{input}")
    ])
    
    # Cadeia de processamento
    chain = prompt | llm | StrOutputParser()
    
    return chain

# Loop principal
def run_chat(chain):
    while True:
        try:
            user_input = input("Você: ")
            
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("Chat finalizado!")
                break
                
            if not user_input.strip():
                continue
                
            # Resposta
            print("Bot: ", end="", flush=True)
            for chunk in chain.stream({"input": user_input}):
                print(chunk, end="", flush=True)
            print("\n")
            
        except KeyboardInterrupt:
            print("\nEncerrado pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro: {e}")
            continue

if __name__ == "__main__":
    chatbot = setup_chatbot()
    run_chat(chatbot)