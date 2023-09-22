# app.py
import streamlit as st
import gradio as gr
import pandas as pd

@st.cache_data  # 👈 Added this line to cache the loaded data
def load_data():
    df_rg = pd.read_pickle('data_rg.pkl')
    return df_rg

# Now, call the function to load the data
df_rg = load_data()

def recommender_artists(artist_name, n_recs):
    if artist_name in df_rg['artists'].values:
        ix = df_rg[df_rg['artists'] == artist_name].index[0]
        ixs = np.argsort(euclidean_matrix[ix, :])[:n_recs]
        recommendations = df_rg['artists'][ixs]
        unique_recommendations = recommendations[~recommendations.isin([artist_name])]
        return unique_recommendations.tolist()
    else:
        return 'Artist not in the dataset'

# Create Gradio Interface
iface = gr.Interface(
    fn=recommender_artists, 
    inputs=[
        gr.Dropdown(
            df_rg['artists'].tolist(), 
            label="Artists that I liked!",
            info="Pick one!"
        ),
        gr.Slider(
            1, 15, 5, step=1,
            label="Number of recommendations"
        )
    ], 
    outputs="text"
)

# Streamlit App
st.title("Artist Recommender")
st.text("This is a Streamlit app with an embedded Gradio Interface to recommend artists.")

# Launch Gradio Interface inline in Streamlit
iface.launch()