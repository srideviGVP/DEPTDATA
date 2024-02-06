import streamlit as st
import os

# Create a folder to store the uploaded documents for each section
sections = ["Research", "API", "ChatGPT", "Safety", "Company"]

for section in sections:
    if not os.path.exists(section):
        os.makedirs(section)

# Define the Streamlit app
def main():
    st.title("Document Manager")

    # Create a horizontal menu with styled buttons
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("Research", key="ResearchButton"):
            selected_section = "Research"

    with col2:
        if st.button("API", key="APIButton"):
            selected_section = "API"

    with col3:
        if st.button("ChatGPT", key="ChatGPTButton"):
            selected_section = "ChatGPT"

    with col4:
        if st.button("Safety", key="SafetyButton"):
            selected_section = "Safety"

    with col5:
        if st.button("Company", key="CompanyButton"):
            selected_section = "Company"

    if "selected_section" not in locals():
        st.stop()

    st.header(f"{selected_section} Section")

    # Create a submenu for each section with sample text
    submenu = st.radio(f"{selected_section} Menu", ["Upload Document", "View Documents"])

    if submenu == "Upload Document":
        st.subheader("Upload a Document")
        uploaded_file = st.file_uploader(f"Choose a document to upload in {selected_section}", type=["pdf", "docx", "txt"])

        if uploaded_file is not None:
            # Save the uploaded document to the specific section's folder
            with open(os.path.join(selected_section, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success("Document successfully uploaded!")

        st.write("You can upload documents related to this section.")

    elif submenu == "View Documents":
        st.subheader(f"List of Documents in {selected_section}")
        files = os.listdir(selected_section)
        if not files:
            st.info(f"No documents uploaded yet in {selected_section}.")
        else:
            st.write(f"List of uploaded documents in {selected_section}:")
            for file in files:
                st.write(file)

if __name__ == "__main__":
    main()
