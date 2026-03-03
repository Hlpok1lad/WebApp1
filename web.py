import streamlit as st
import functions
todos = functions.load_data()
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.save_data()


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This is app for increasing your <b>productivity</b>',unsafe_allow_html=True)
st.text_input(label='Add Todo',placeholder='Add a todo...',on_change=add_todo,key='new_todo')
for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.save_data()
        del st.session_state[todo]
        st.rerun()



