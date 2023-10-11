import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_todos(todos)
def del_todo():
    for todo in todos:
        if st.session_state[todo]:
            todos.remove(todo)
            functions.write_todos(todos)
            del st.session_state[todo]




st.title("My Todo App")
st.subheader("This is my todo app.")
st.write('This app is to increase your productivity')



for todo in todos:
    checkbox = st.checkbox(todo,
                           on_change=del_todo, key=todo)


# Clear the input box after hitting enter
st.session_state["new_todo"] = ""
st.text_input(label="", placeholder="Enter a new todo",
              on_change=add_todo, key="new_todo")


st.session_state