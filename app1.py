import streamlit as st
import os

# Create a folder to store the uploaded documents
if not os.path.exists("uploads"):
    os.makedirs("uploads")

# Define the Streamlit app
def main():
    st.title("Department Document Manager")

    # Create a menu at the top of the page
    menu = st.radio("Menu", ["Upload Document", "View Documents"])

    if menu == "Upload Document":
        st.header("Upload a Document")
        uploaded_file = st.file_uploader("Choose a document to upload", type=["pdf", "docx", "txt"])

        if uploaded_file is not None:
            # Save the uploaded document
            with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getvalue())
            st.success("Document successfully uploaded!")

    elif menu == "View Documents":
        st.header("List of Documents")
        files = os.listdir("uploads")
        if not files:
            st.info("No documents uploaded yet.")
        else:
            st.write("List of uploaded documents:")
            for file in files:
                st.write(file)

if __name__ == "__main__":
    main()
