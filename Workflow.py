from llama_index.llms.openai import OpenAI
import os
import nest_asyncio

if __name__ == '__main__':
    nest_asyncio.apply()

    os.environ["OPENAI_API_KEY"] = "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" # Get your API key from https://platform.openai.com/account/api-keys
    os.environ["LLAMA_CLOUD_API_KEY"] = "llx-ulskyur4sbyH90bJrcJSAzP4BdY6WqtxljOL4zPiXR2WvuVi" # Get your API key from https://cloud.llamaindex.ai/api-key

    llm = OpenAI(model='gpt-4o-mini')