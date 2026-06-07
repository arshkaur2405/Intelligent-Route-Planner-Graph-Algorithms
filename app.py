import streamlit as st
import pandas as pd

from src.graph import Graph
from src.router import Router
from src.visualizer import Visualizer


# -----------------------------------
# CREATE CITY GRAPH
# -----------------------------------

@st.cache_resource
def load_city_network():

    city = Graph()

    city.add_node("Airport", 12.9716, 77.5946)
    city.add_node("Tech Park", 12.9785, 77.6408)
    city.add_node("Downtown", 12.9592, 77.5913)
    city.add_node("Metro Station", 12.9423, 77.5684)
    city.add_node("Suburb East", 12.9912, 77.6821)
    city.add_node("Harbor Area", 12.9105, 77.6254)
    city.add_node("Industrial Zone", 12.9012, 77.5212)
    city.add_node("Central Hospital", 12.9644, 77.5344)

    city.add_edge("Airport", "Tech Park", 15, 80)
    city.add_edge("Airport", "Central Hospital", 12.5, 60)

    city.add_edge("Tech Park", "Suburb East", 5.2, 40)
    city.add_edge("Tech Park", "Downtown", 8, 50)

    city.add_edge("Central Hospital", "Downtown", 6.4, 40)
    city.add_edge("Central Hospital", "Industrial Zone", 9.8, 50)

    city.add_edge("Downtown", "Metro Station", 4.5, 35)
    city.add_edge("Downtown", "Harbor Area", 11.2, 60)

    city.add_edge("Metro Station", "Industrial Zone", 5, 40)

    city.add_edge("Harbor Area", "Suburb East", 18.5, 70)
    city.add_edge("Harbor Area", "Industrial Zone", 14, 60)

    return city


city = load_city_network()

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Intelligent Route Planner",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ Intelligent Route Planner")
st.markdown(
    "### Dijkstra Algorithm + Graph Data Structures"
)

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("Route Settings")

locations = list(city.nodes.keys())

source = st.sidebar.selectbox(
    "Select Source",
    locations
)

destination = st.sidebar.selectbox(
    "Select Destination",
    locations,
    index=1
)

optimization = st.sidebar.radio(
    "Optimization Type",
    ["distance", "time"]
)

# -----------------------------------
# FIND ROUTE
# -----------------------------------

if st.sidebar.button("Find Best Route"):

    path, cost = Router.shortest_path(
        city,
        source,
        destination,
        optimization
    )

    if path is None:

        st.error("No route found")

    else:

        summary = Router.route_summary(
            city,
            path,
            optimization
        )

        st.success("Route Found Successfully")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Distance (km)",
                summary["distance"]
            )

        with col2:
            st.metric(
                "Travel Time (min)",
                summary["time"]
            )

        with col3:
            st.metric(
                "Stops",
                len(path)
            )

        st.subheader("Optimized Route")

        st.write(
            " ➜ ".join(path)
        )

        route_df = pd.DataFrame({
            "Step": range(1, len(path)+1),
            "Location": path
        })

        st.dataframe(
            route_df,
            use_container_width=True
        )

        st.session_state["path"] = path

# -----------------------------------
# GRAPH INFO
# -----------------------------------

st.subheader("Road Network")

edge_data = []

for source_node in city.adjacency_list:

    for neighbor, distance, speed in city.get_neighbors(source_node):

        edge_data.append([
            source_node,
            neighbor,
            distance,
            speed
        ])

df = pd.DataFrame(
    edge_data,
    columns=[
        "Source",
        "Destination",
        "Distance",
        "Speed Limit"
    ]
)

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------------
# VISUALIZATION
# -----------------------------------

st.subheader("Graph Visualization")

if st.button("Visualize Network"):

    current_path = st.session_state.get(
        "path",
        None
    )

    fig = Visualizer.draw(
        city,
        current_path,
        return_figure=True
    )

    st.pyplot(fig)