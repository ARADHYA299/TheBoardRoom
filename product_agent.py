def product_agent(llm , context):
  prompt = f"""
  You are a Product Manager.
  
  Analyze this:
  {context}
  
  
  Give:
  Product Insights / Key product issues
  Suggestions for improvement
  
  """
  
  
  return llm(prompt)

