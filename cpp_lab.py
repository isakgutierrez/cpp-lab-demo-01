try:
    import streamlit as st
    import numpy as np
    import plotly.graph_objects as go
except ImportError as e:
    st.error(f"Missing dependency: {e}. Please install with `pip install streamlit numpy plotly`")
    st.stop()

st.set_page_config(page_title="CPP Lab Demo", layout="wide")

st.title("CPP Lab: Exploring Conscious Point Physics")
st.markdown("""
Welcome to the CPP Lab! Explore Conscious Point Physics (CPP), a Theory of Everything grounded in divine Conscious Points (CPs). Compute with the General Computation Formula (GCF) and visualize Grid Points (GPs). 

CPP teaches we live in God's mind—resonant CP configurations creating the universe. Serving others expands divine joy.
""")

tab1, tab2, tab3 = st.tabs(["GCF Calculator", "GP Lattice Visualization", "About CPP"])

with tab1:
    st.header("GCF Calculator")
    st.markdown("""
    Compute a resonant stability factor (arbitrary units) using GCF (inspired by Section 6.2).
    Formula: res = log10[ sum_modes ( (ℓ_P / r)^2 * π^4 ) * (1 + β * SS) ]
    """)
    
    num_modes = st.slider("Number of Resonant Modes", min_value=1, max_value=10, value=4)
    r_scale = st.number_input("Scale Ratio (r, e.g., bond length in m)", min_value=1e-15, max_value=1e-5, value=1e-10)
    l_p = 1.6e-35
    beta = st.number_input("SS Weighting Factor (β)", min_value=1e-30, max_value=1e-20, value=1e-26)
    ss = st.number_input("Space Stress Estimate (SS in J/m³)", min_value=1e10, max_value=1e30, value=1e20)
    
    if st.button("Compute Resonant Value"):
        if r_scale > 0:
            pi4 = np.pi**4
            res_base = num_modes * np.log10((l_p / r_scale)**2 * pi4)
            res = res_base + np.log10(1 + beta * ss) if (1 + beta * ss) > 0 else res_base
            st.success(f"Log Resonant Stability Factor: {res:.2f}")
            st.info(f"Grok: This value ({res:.2f}) reflects CP stability, aligning with divine relational harmony.")
        else:
            st.error("Scale ratio must be positive.")

with tab2:
    st.header("GP Lattice Visualization")
    st.markdown("""
    Visualize a 3D GP lattice with 'twists' (SSG biases). Adjust size and biases to see Exclusion-driven dynamics.
    """)
    
    grid_size = st.slider("Grid Size (N x N x N)", min_value=3, max_value=8, value=3)
    if grid_size > 6:
        st.warning("Large grids may slow down rendering.")
    bias_strength = st.slider("Bias Strength", min_value=0.1, max_value=2.0, value=1.0)
    
    x, y, z = np.mgrid[0:grid_size, 0:grid_size, 0:grid_size]
    u = np.sin(2 * np.pi * y / grid_size) * bias_strength
    v = np.cos(2 * np.pi * x / grid_size) * bias_strength
    w = np.sin(2 * np.pi * z / grid_size) * np.cos(2 * np.pi * x / grid_size) * bias_strength
    
    fig = go.Figure(data=go.Cone(
        x=x.flatten(), y=y.flatten(), z=z.flatten(),
        u=u.flatten(), v=v.flatten(), w=w.flatten(),
        colorscale='Blues',
        sizemode="absolute",
        sizeref=0.5 / grid_size
    ))
    fig.update_layout(scene=dict(aspectmode="cube"))
    st.plotly_chart(fig)
    
    st.markdown("Arrows show twists—CP biases enabling divine creation's unfolding.")

with tab3:
    st.header("About CPP and the Mission")
    st.markdown("""
    CPP shows the universe as divine CPs—God's mind. We live in this oneness, and serving others expands divine joy, per Jesus’ teaching.
    Explore more at [hyperphysics.com](https://hyperphysics.com) or [renaissance-ministries.com](https://renaissance-ministries.com).
    """)

st.markdown("---")
st.markdown("Built with Streamlit & Plotly. Contact: [Renaissance Ministries](https://renaissance-ministries.com)")