# Core Pkgs
import streamlit as st 

# EDA Pkgs
import pandas as pd 
import numpy as np 

# Data Viz Pkg
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use("Agg")
import seaborn as sns 
import warnings

# Suppress PyplotGlobalUseWarning
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    """Semi Automated ML App with Streamlit """

    activities = ["EDA", "Plots"]    
    choice = st.sidebar.selectbox("Select Activities", activities)

    if choice == 'EDA':
        st.subheader("Exploratory Data Analysis")

        data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
        if data is not None:
            try:
                df = pd.read_csv(data)
                st.dataframe(df.head())

                st.write("### Description:")
                st.write("This dataset contains various columns and records. Explore the data using the options below.")

                if st.checkbox("Show Shape"):
                    st.write("### Summary:")
                    st.write("Displays the number of rows and columns in the dataset.")
                    st.write(df.shape)

                if st.checkbox("Show Columns"):
                    st.write("### Summary:")
                    st.write("Displays the names of all columns in the dataset.")
                    all_columns = df.columns.to_list()
                    st.write(all_columns)

                if st.checkbox("Summary"):
                    st.write("### Summary:")
                    st.write("Displays a statistical summary of the numerical columns in the dataset.")
                    st.write(df.describe(include='all'))  # Include all data types

                if st.checkbox("Show Selected Columns"):
                    st.write("### Summary:")
                    st.write("Displays a new dataframe with only the selected columns.")
                    selected_columns = st.multiselect("Select Columns", all_columns)
                    if selected_columns:
                        new_df = df[selected_columns]
                        st.dataframe(new_df)

                if st.checkbox("Show Value Counts"):
                    st.write("### Summary:")
                    st.write("Displays the counts of unique values in the last column of the dataset.")
                    last_column = df.columns[-1]
                    st.write(df[last_column].value_counts())

                if st.checkbox("Correlation Plot (Matplotlib)"):
                    st.write("### Summary:")
                    st.write("Displays a correlation matrix heatmap using Matplotlib.")
                    num_df = df.select_dtypes(include=[np.number])  # Select only numerical columns
                    if not num_df.empty:
                        fig, ax = plt.subplots()
                        corr = num_df.corr()
                        cax = ax.matshow(corr, cmap='coolwarm')
                        plt.colorbar(cax)
                        st.pyplot(fig)
                    else:
                        st.warning("No numerical columns available for correlation plot.")

                if st.checkbox("Correlation Plot (Seaborn)"):
                    st.write("### Summary:")
                    st.write("Displays a correlation matrix heatmap using Seaborn.")
                    num_df = df.select_dtypes(include=[np.number])  # Select only numerical columns
                    if not num_df.empty:
                        fig, ax = plt.subplots()
                        sns.heatmap(num_df.corr(), annot=True, ax=ax, cmap='coolwarm')
                        st.pyplot(fig)
                    else:
                        st.warning("No numerical columns available for correlation plot.")

                if st.checkbox("Pie Plot"):
                    st.write("### Summary:")
                    st.write("Displays a pie chart of the selected column's value counts.")
                    all_columns = df.columns.to_list()
                    column_to_plot = st.selectbox("Select 1 Column", all_columns)
                    
                    if column_to_plot:
                        fig, ax = plt.subplots()
                        try:
                            # Convert the column to string to avoid type issues
                            df[column_to_plot] = df[column_to_plot].astype(str)
                            # Count values
                            value_counts = df[column_to_plot].value_counts()
                            
                            if value_counts.empty:
                                st.warning("The selected column has no data to plot.")
                            else:
                                # Plot pie chart
                                value_counts.plot.pie(autopct="%1.1f%%", ax=ax, startangle=90)
                                st.pyplot(fig)
                        except Exception as e:
                            st.error(f"Error generating pie plot: {e}")

            except Exception as e:
                st.error(f"Error loading data: {e}")

    elif choice == 'Plots':
        st.subheader("Data Visualization")
        data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
        if data is not None:
            try:
                if data.name.endswith('.xlsx'):
                    df = pd.read_excel(data)
                else:
                    df = pd.read_csv(data)
                st.dataframe(df.head())

                if st.checkbox("Show Value Counts"):
                    st.write("### Summary:")
                    st.write("Displays a bar plot of the value counts in the last column of the dataset.")
                    fig, ax = plt.subplots()
                    try:
                        df.iloc[:, -1].value_counts().plot(kind='bar', ax=ax)
                        st.pyplot(fig)
                    except Exception as e:
                        st.error(f"Error generating bar plot: {e}")
            
                # Customizable Plot
                all_columns_names = df.columns.tolist()
                type_of_plot = st.selectbox("Select Type of Plot", ["area", "bar", "line", "hist", "box", "kde"])
                selected_columns_names = st.multiselect("Select Columns To Plot", all_columns_names)

                if st.button("Generate Plot"):
                    st.success("Generating Customizable Plot of {} for {}".format(type_of_plot, selected_columns_names))

                    if type_of_plot == 'area':
                        cust_data = df[selected_columns_names]
                        st.area_chart(cust_data)

                    elif type_of_plot == 'bar':
                        cust_data = df[selected_columns_names]
                        st.bar_chart(cust_data)

                    elif type_of_plot == 'line':
                        cust_data = df[selected_columns_names]
                        st.line_chart(cust_data)

                    elif type_of_plot in ['hist', 'box', 'kde']:
                        if len(selected_columns_names) == 0:
                            st.warning("Please select columns to plot.")
                            return
                        
                        num_df = df[selected_columns_names].select_dtypes(include=[np.number])  # Handle only numerical data
                        if num_df.empty:
                            st.warning("Selected columns do not contain numerical data for this plot type.")
                            return

                        fig, ax = plt.subplots()
                        if type_of_plot == 'hist':
                            num_df.hist(ax=ax)
                        elif type_of_plot == 'box':
                            num_df.plot.box(ax=ax)
                        elif type_of_plot == 'kde':
                            num_df.plot.kde(ax=ax)

                        st.pyplot(fig)

            except Exception as e:
                st.error(f"Error loading data or generating plot: {e}")

if __name__ == '__main__':
    main()
