from langchain.utilities import SQLDatabase
import pymysql
from langchain.llms import OpenAI
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st 
load_dotenv()
def sql(USER_INPUT):
    llm = ChatOpenAI(temperature=0)
    host = '######'
    port = '####'
    username = '####'
    password = '#######'
    database_schema = 'chatbot'
    mysql_uri = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database_schema}"

    db = SQLDatabase.from_uri(mysql_uri, sample_rows_in_table_info=2)
    chain = create_sql_query_chain(llm, db)
    response = chain.invoke({"question": USER_INPUT})
    return response 

def main():
    # st.title("SQL Query Generator")
    image = open("SQL.jpg", "rb").read()
    st.image(image,use_column_width=True)
    user_input = st.text_input("Write Your Problem Statement:", "")
    query= sql(user_input)
    if user_input:
        st.write("Your Problem Statement:")
        st.code(query, language='sql')

if __name__ == "__main__":
    main()

        
        
