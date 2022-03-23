import streamlit as st
import pandas as pd
import numpy as np

t = np.arange(0.00, 10*np.pi, 0.05)
data = pd.DataFrame({
  "rand": np.random.rand(1, len(t))[0] + 5,
  "sin": np.random.rand(1, len(t))[0] + 3*np.sin(t) - 2*np.sin(0.5*t) + np.sin(0.25*t)
})
st.line_chart(data)
