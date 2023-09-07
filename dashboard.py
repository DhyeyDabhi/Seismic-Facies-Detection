import streamlit as st
from streamlit_carousel import carousel
import time

st.set_page_config(layout='wide')

st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            text-align: justify;
            font-size: 150px;
        } 

        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: justify;
            vertial-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
)

st.title('Seismic Facies Identification')

with st.container():
    st.subheader('What are Seismic Facies?')
    col1, col2 = st.columns((2,1))
    with col1:
        st.write("Seismic facies are distinct geological units or zones in the Earth's subsurface identified through the analysis of seismic data. These units share similar seismic characteristics, such as reflection amplitudes, frequency, and waveform attributes. Seismic facies analysis helps geologists and geophysicists understand the composition and structure of the subsurface, making it valuable for various applications, including locating oil and gas reservoirs, assessing geological features, and planning infrastructure projects.")
        '''
        Seismic waves are sent into the ground, and their reflections are recorded.Raw data is processed to improve quality and remove noise.Geologists analyze data for patterns in attributes like reflection amplitudes, frequencies, and continuity. Mathematical representations of data (e.g., amplitude maps) highlight specific features. Similar patterns are grouped into seismic facies. Geological Correlation: Facies are validated using known geological data. Facies are visually represented for a clear understanding. Properties like lithology and porosity may be determined.
        '''
    with col2:
        st.image('Seismic-Facies.jpg')

with st.container():
    col3, col4 = st.columns((1,2))

    with col4:
        st.subheader("Data Preprocessing")
        st.write("The shape of the provided data was (1006,450,500), where the first dimension represents the depth, and other two dimensions represent measurements in horizontal direction. The data cuboid is sliced along horizontal dimensions i.e. (2nd and 3rd) dimensions. And the obtained slices are squeezed to shape of (512,256). Hence, after data processing the shape of the data is (512,256,950). This data is splitted into training and testing dataset.")

    with col3:
        ''', , https://drive.google.com/file/d/1DDONnFyjJ4TIbKmbtBrfc0cf1e32oJkZ/view?usp=sharing, https://drive.google.com/file/d/1OO9FgDAt03KCSKyEZSBWM-ETKSQ9BDv9/view?usp=sharing, https://drive.google.com/file/d/1P7w2mingVFECNyK0o8c2C0T_w2Mi9xQE/view?usp=sharing, https://drive.google.com/file/d/1iobHqCjZ8CRp-13GG5fHFqnQ8UG0dNOQ/view?usp=sharing, https://drive.google.com/file/d/1jXukNtPn7uBQuFaqQmCTAT1YaT4Z1TPz/view?usp=sharing, https://drive.google.com/file/d/1qUSribkY4xRRz9AFSVkSVDLcUVK8sw0K/view?usp=sharing
        '''
        items=[
            dict(
                title='Training Data1',
                text='Type 1',
                img='https://drive.google.com/file/d/1Cc4g0yL1JeOjO8BH6pg5oiPEGFn7rh_C/preview'
            ),
            dict(
                title='Training Data2',
                text='Type 2',
                img='https://drive.google.com/file/d/1DDONnFyjJ4TIbKmbtBrfc0cf1e32oJkZ/preview'
            )
        ]
        carousel(items=items,width=1)



    