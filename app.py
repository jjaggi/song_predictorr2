import streamlit as st



# MAIN PAGE

# import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
# st.components.v1.iframe("https://prophet.streamlit.app/")
# heading

st.header("SONG POPULARITY PREDICTOR:")



  
st.write(f'''
    <a target="_self" href="https://prophet.streamlit.app/">
        <button>
            Agree T&C
        </button>
    </a>
    ''',
    unsafe_allow_html=True
)
# # display of popularity meter and number


# # widgets for user to select values for features

st.text('')
st.text('Created by Jaskaran Singh Jaggi')
# SIDE BAR
st.sidebar.title('Info & Glossary')

st.sidebar.markdown(
    'This tool predicts Spotify popularity on a scale of 0 to 100. As defined in the '
    '[Spotify API Reference](https://developer.spotify.com/documentation/web-api/reference/tracks/get-track/), the '
    'popularity of a track is algorithmically calculated, and is a combination of how many plays a track has and how '
    'recent those plays are. This project was made by Stephen Kaplan over a 2-week span in July 2020 as a project for '
    'the [Metis](https://www.thisismetis.com/) data science program.'
)


st.sidebar.subheader('Technical Details')
st.sidebar.markdown(
    'The model was trained on Spotify audio features and other data defined below, using a Lasso linear model. The '
    'R2 score is `0.58` and it has a RMSE is `13.82`. The code is located '
    '[here](https://github.com/stephenjkaplan/song-popularity-predictor) and the blog post about it is '
    '[here](https://stephenjkaplan.github.io/).'
)

st.sidebar.subheader('Feature Glossary')
st.sidebar.markdown(
    '_Most of the definitions below can be attributed to the '
    '[Spotify API Docs](https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/)._'
)
st.sidebar.markdown("**# of Spotify Followers** is the number of Spotify users following a track's artist. This tool "
                    "only allows for up to 1 million followers, but artists such as Beyonce have 20+ million "
                    "followers.")
st.sidebar.markdown('**Danceability** describes how suitable a track is for dancing based on a combination of musical '
                    'elements including tempo, rhythm stability, beat strength, and overall regularity.')
st.sidebar.markdown('**Energy** represents a perceptual measure of intensity and activity.')
st.sidebar.markdown('**Speechiness** represents the presence of spoken words in a track.')
st.sidebar.markdown('**Valence** describes the musical positiveness/happiness/cheerfulness conveyed by a '
                    'track.')
st.sidebar.markdown('**Mode** determines if the song is in a major or minor key.')
