from llama_cpp import Llama
import sys

MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

try:
    print(f"Loading model from {MODEL_PATH}...")
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=2048,
        verbose=True
    )
    print("✅ Model loaded successfully!")
    
    print("Testing inference...")
    output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)
    print(output)
    print("✅ Inference worked!")

except Exception as e:
    print(f"❌ Failed to load model: {e}")
    import traceback
    traceback.print_exc()
