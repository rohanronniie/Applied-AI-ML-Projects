import streamlit as st
import joblib

movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity.pkl")

st.title("Movie Recommendation System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Select a movie", movie_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[index]))
    movies_list = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]
    
    return [movies.iloc[i[0]].title for i in movies_list]

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    
    for movie in recommendations:
        st.write(movie)