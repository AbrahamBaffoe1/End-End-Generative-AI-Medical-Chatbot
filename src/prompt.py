# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
     "You are a helpful assistant for question and answering tasks about medicine. "
     "Use the following pieces of retrieved context to answer the question. "
     "If you don't know the answer, just say that you don't know.\n\n"
     "Context: {context}\n"
     "{context}"
     
)