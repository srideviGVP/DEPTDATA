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

    # Create a top navigation bar
    selected_section = st.selectbox("Select Section", sections)

    if selected_section:
        st.header(f"{selected_section} Section")

        # Create a submenu for each section
        submenu = st.radio(f"{selected_section} Menu", ["Upload Document", "View Documents"])

        if submenu == "Upload Document":
            st.subheader("Upload a Document")
            uploaded_file = st.file_uploader(f"Choose a document to upload in {selected_section}", type=["pdf", "docx", "txt"])

            if uploaded_file is not None:
                # Save the uploaded document to the specific section's folder
                with open(os.path.join(selected_section, uploaded_file.name), "wb") as f:
                    f.write(uploaded_file.getvalue())
                st.success("Document successfully uploaded!")

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
