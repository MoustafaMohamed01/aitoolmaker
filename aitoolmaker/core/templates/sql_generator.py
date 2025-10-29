"""
SQL Generator template for AIToolMaker.
"""

SQL_GENERATOR_TEMPLATE = """import streamlit as st
import google.generativeai as genai
from api_key import GEMINI_API_KEY

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('{{ model }}')

def main():
    st.set_page_config(page_title='{{ tool_name }}')
    
    st.markdown(
        \"\"\"
            <div style='text-align: center;'>
                <h1>{{ tool_name }}</h1>
                <h3>I can generate SQL queries for you!</h3>
            </div>
        \"\"\",
        unsafe_allow_html=True
    )
    
    text_input = st.text_area('Enter your Query description here...')
    database_context = st.text_area('Optional: Provide database schema or context (e.g., table names, columns)...')
    dialect = st.selectbox('Optional: Specify SQL dialect', ['Generic SQL', 'PostgreSQL', 'MySQL', 'SQLite'])
    
    submit = st.button('Generate SQL Query')
    
    if submit:
        if not text_input:
            st.warning("Please enter a query description.")
            return
        
        with st.spinner('Generating SQL Query...'):
            try:
                template = f\"\"\"
                    Create a SQL query snippet based on the following description:
                    ```
                    {text_input}
                    ```
                    {'considering the following database context: ' + database_context if database_context else ''}
                    {'Ensure the query is compatible with ' + dialect + '.' if dialect != 'Generic SQL' else ''}
                    I just want the SQL query.
                    \"\"\"
                
                response = model.generate_content(template)
                sql_query = response.text
                sql_query = sql_query.strip().lstrip('```sql').rstrip('```')
                
                expected_output = f\"\"\"
                    What would be the expected response of this SQL Query snippet:
                    ```sql
                    {sql_query}
                    ```
                    Provide a sample tabular response formatted as a Markdown table, with no additional explanation.
                    \"\"\"
                
                output_response = model.generate_content(expected_output)
                output = output_response.text
                
                explanation = f\"\"\"
                    Explain this SQL Query:
                    ```sql
                    {sql_query}
                    ```
                    Please provide a concise explanation.
                    \"\"\"
                
                explanation_response = model.generate_content(explanation)
                explanation_text = explanation_response.text
                
                with st.container():
                    st.success('SQL Query Generated Successfully! Here is your Query Below:')
                    st.code(sql_query, language='sql')
                    
                    st.success('Expected Output of this SQL Query will be:')
                    st.markdown(f"```\\n{output}\\n```")
                    
                    st.success('Explanation of this SQL Query:')
                    st.markdown(explanation_text)
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
"""