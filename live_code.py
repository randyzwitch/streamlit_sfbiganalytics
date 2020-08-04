import streamlit as st

# once "always re-run" enabled, changes made here will be reflected instantly
"# SF Big Analytics - AICamp"

"---"

"## Source code"
# st.echo super helpful for live demos or teaching
with st.echo():
    import streamlit as st

    # markdown supported inline as a string, Streamlit "magics" interpret the script to determine intent
    "---"

    "### 1. Slider example"

    # declaring a slider as simple as giving it a header label and optional bounds
    slider1 = st.slider("Pick a number 1 to 100", 1, 100)

    f"""The number you selected was {slider1}"""

    # moving slider to the sidebar done by adding 'sidebar' to the method name
    slider2 = st.sidebar.slider("Sidebar slider", 1, 100)

    # can pass one slider output to another as default (though, not sure why you might!)
    # slider2 = st.sidebar.slider("Sidebar slider", 1, 100, slider1)

    st.sidebar.markdown(f"Sidebar slider value is {slider2}")

    "---"

    "### 2. Displaying data example"

    # common data science libraries part of "magic"
    import pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.rand(100, 3))
    """ pandas dataframes are auto-recognized just like this markdown statement"""
    df

    """ ## Why are this tables above changing each time anything changes? Because Streamlit re-runs top to bottom on widget change"""

    "---"

    # st.cache works based on memoization...function with the same inputs should always return same output
    # return value from cache instead of re-calculating (potentially expensive) function
    @st.cache()
    def gen_rand_data(cols):
        return pd.DataFrame(np.random.rand(100, cols))

    df2 = gen_rand_data(slider2)

    """ ### 3. Caching example """
    """ only changing the slider in the sidebar will change this table"""
    df2

    f""" This dataframe has a shape of {df2.shape}"""

    " --- "
    """ ### 4. Simple plotting example"""

    offset = st.number_input("Offset", 0, 100, 10, step=5)
    st.bar_chart(
        pd.DataFrame(
            range(1 + offset, 10 + offset), [str(x + offset) for x in range(11, 20)]
        )
    )

    "Several convenience functions for plotting based on Altair. Also have the ability to customize with `st.altair_chart`, `st.pyplot` and many others"
    " --- "
    """ ### To see full set of UI components in Streamlit Core:"""
    "https://docs.streamlit.io/en/stable/api.html"

