import streamlit as st
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from name_list import clean_name_list
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load and clean the name list
first_scroll, second_scroll = clean_name_list('name_list.txt')

# Initialize ChatGroq
groq_api_key = os.getenv("GROQ_API_KEY")

# Available Groq models
groq_models = [
    "llama-3.2-90b-text-preview",
    "llama-3.1-70b-versatile",
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.2-11b-text-preview",
    "gemma2-9b-it",
    "llama3-8b-8192",
    "llama-3.1-8b-instant",
    "llama-guard-3-8b",
    "gemma-7b-it",
    "llama-3.2-3b-preview",
    "llama-3.2-1b-preview",
]

# Set page configuration to make sidebar closed by default
st.set_page_config(initial_sidebar_state="collapsed", page_title="Star Stable Name Generator", page_icon="🐴")

# Streamlit UI
st.title("🐴✨ Star Stable Online Horse Name Generator 🌟")

# Model selection dropdown
selected_model = st.selectbox("🤖 Select AI Model", groq_models)

# Initialize ChatGroq with selected model
llm = ChatGroq(api_key=groq_api_key, model_name=selected_model)

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["theme", "first_scroll", "second_scroll"],
    template="""Generate 10 unique horse names for Star Stable Online based on the theme: {theme}.
Each name must consist of exactly two words that relate to the theme: {theme}
- The first word MUST be chosen from this list: {first_scroll}
- The second word MUST be chosen from this list: {second_scroll}

Think about words that best represent or are associated with the theme, then choose the closest matches from the provided lists.

Provide the names in the format:
1. FirstWord SecondWord
2. FirstWord SecondWord
...
10. FirstWord SecondWord

Do not include any additional text or explanations."""
)

# Create an LLMChain
name_chain = LLMChain(llm=llm, prompt=prompt_template)

theme = st.text_input("🎨 Enter a theme for your horse names:")

def generate_names(theme, first_scroll, second_scroll):
    response = name_chain.run(
        theme=theme,
        first_scroll=", ".join(first_scroll),
        second_scroll=", ".join(second_scroll)
    )
    
    names = []
    for line in response.split('\n'):
        parts = line.split('. ', 1)
        if len(parts) == 2:
            name = parts[1].strip()
            words = name.split()
            if len(words) == 2 and words[0] in first_scroll and words[1] in second_scroll:
                names.append(name)
    
    # If we don't have 10 valid names, fill the rest with random valid names
    while len(names) < 10:
        random_name = f"{random.choice(first_scroll)} {random.choice(second_scroll)}"
        if random_name not in names:
            names.append(random_name)
    
    return names

if st.button("🎠 Generate Names"):
    if theme:
        with st.spinner(f"🔮 Generating magical names using {selected_model}..."):
            generated_names = generate_names(theme, first_scroll, second_scroll)
        
        st.balloons()
        st.subheader("🏆 Generated Names:")
        for i, name in enumerate(generated_names, 1):
            st.write(f"{i}. {name}")
        
        st.success(f"🎉 Generated using {selected_model}. 🌟")
    else:
        st.warning("🚨 Please enter a theme before generating names.")

# Sidebar content
st.sidebar.title("ℹ️ Information")

# Display name lists in the sidebar
with st.sidebar.expander("📖 About"):
    st.write("This app generates 10 unique horse names for Star Stable Online based on the theme you enter. Each name must consist of exactly two words that relate to the theme. The first word MUST be chosen from the first list of options, and the second word MUST be chosen from the second list of options. The names are generated using a large language model (LLM) from Groq. You can experiment with different models by selecting from the dropdown menu.")
    st.write("This app uses [Groq](https://docs.groq.com/api/) for the LLM, and [Streamlit](https://docs.streamlit.io/) for the UI.")
    st.link_button("🔗 This App's Github", "https://github.com/Arenman7/star-stable-online-horse-name-generator")

st.sidebar.header("🔤 Available Name Options")
with st.sidebar.expander("🔠 First Word Options"):
    st.write(", ".join(first_scroll))   
with st.sidebar.expander("🔡 Second Word Options"):
    st.write(", ".join(second_scroll))
