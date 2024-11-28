import streamlit as st

# Set the title of the web page
st.title("Chelsea's Biography")

# Editable Section for Personal Information
all_about_me = st.text_area("All About Me", """
- Name: Chelsea Marie D. Cinco
- Sex: Female 
- Birthday: February 20, 2006
- Birthplace: Cebu City
- Address: Purok 3, Brgy. Del Rosario, Tubod, Surigao del Norte
""")
parents = st.text_area("Parents", """
- Mother: Hazel Dagooc De Guzman
- Occupation: OFW 
- Father: Eric Camingue Cinco
- Occupation: OFW 
""")

# Editable Section for Name
name = st.text_input("Enter Your Name", "Chelsea Marie Cinco")

# Editable Section for Introduction Text
about_me = st.text_area("Tell us about yourself", """
   Hi there! My name is Chelsea Marie Cinco. I am 18 years old and I am from Del Rosario, Tubod, Surigao
    del Norte. I  am a first year student taking on Bachelor of Science in Computer Engineering. I am a
    very outgoing person and I like spontaneous activities. I love dancing and playing volleyball. 
""")

# Editable Section for Education
education = st.text_area("Education", """
    - Lourdes Learning Center - Mainit Corporation (2012 - 2015)
    - Gate of Heaven Academy (2015 - 2017)
    - Escuela de Sophia of Caloocan Inc. (2017 - 2022)
    - San Nicolas Academy of Mainit Inc. (2022 - 2024)
    - Surigao del Norte State University (Present)
""")

# Editable Section for Work Experience
work_experience = st.text_area("Work Experience", """
    - NONE
""")

# Editable Section for Skills
skills = st.text_area("Skills", """
    - Public Speaking
    - Computer Literate 
    - Communication Skills 
""")

# Editable Section for Achievements (New Section)
achievements = st.text_area("Achievements", """
    - Outstanding Performance in Athletics
    - Outstanding Performance in Communication Arts 
    - Outstanding Performance in Science
    - Work Immersion Awardee
    - Research Innovation Awardee
""")

links = st.text_area("Connect With Me", """
- Facebook: Chelsea Marie Cinco
- Instagram: @_ccinco
- Email: chelseacinco2006@gmail.com
""")

# Section for Uploading a Profile Picture
st.header("Upload Your Profile Picture")

# File uploader for profile image
image_file = st.file_uploader("Upload your profile image", type=["jpg", "jpeg", "png"])

# If an image is uploaded, display it
if image_file is not None:
    st.image(image_file, caption=f"{name}'s Profile Picture", use_column_width=True)

# Display the editable biography
st.header(f"About {name}")
st.write(about_me)

# All About Me Section
st.header("All About Me")
st.write(all_about_me)

# Parents Section
st.header("Parents")
st.write(parents)

# Education Section
st.header("Education")
st.write(education)

# Work Experience Section
st.header("Work Experience")
st.write(work_experience)

# Skills Section
st.header("Skills")
st.write(skills)

# Achievements Section (New Section)
st.header("Achievements")
st.write("- Outstanding Performance in Athletics\n - Outstanding Performance in Communication Arts\n - Outstanding Performance in Science\n - Work Immersion Awardee\n - Research Innovation Awardee")

# Links Section
st.header("Connect with Me")
st.write(links)

# Button to save changes (Optional)
if st.button("Save Changes"):
    st.success("Your biography has been updated!")