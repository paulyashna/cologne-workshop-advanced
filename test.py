from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="http://localhost:12434/engines/v1",
    model="ai/smollm2:360M-Q4_K_M",
    api_key="none"
)

response = llm.invoke("Give me a fact about orcas.")

print(response.content)

# curl http://localhost:12434/engines/v1/chat/completions \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer none" \
#   -d '{
#     "model": "ai/smollm2:360M-Q4_K_M",
#     "messages": [
#       {"role": "user", "content": "Give me a fact about orcas."}
#     ]
#   }'
