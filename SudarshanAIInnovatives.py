import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Sudarshan AI Innovatives",
    page_icon="🌟",
    layout="wide",
)

# Title of the app with logo
col1, col2 = st.columns([1, 4])  # Create two columns
with col1:
    st.image(Designer (12).jpeg, width=150)  # Replace with your logo's path
with col2:
    st.title("Sudarshan AI Innovatives")
    st.markdown("<h5 style='text-align: center;'>Empowering Businesses with AI Solutions</h5>", unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.header("Navigation")
options = st.sidebar.selectbox("Choose a page:", ["Home", "Services", "Contact", "About"])

# Home page
if options == "Home":
    st.subheader("Welcome to Sudarshan AI Innovatives")
    st.write(
        "At Sudarshan AI Innovatives, we specialize in providing cutting-edge AI solutions tailored to meet your business needs. "
        "Our mission is to harness the power of artificial intelligence to drive innovation and efficiency."
    )

    st.markdown(
        """
        ### Why Choose Us?
        - **Expert Team**: Our team comprises experienced professionals in AI and software development.
        - **Tailored Solutions**: We provide customized solutions to fit your specific business requirements.
        - **Support & Maintenance**: We offer ongoing support and maintenance for all our products.

        ### Our Approach
        We believe in a collaborative approach, working closely with our clients to understand their needs and deliver solutions that exceed expectations.
        """
    )

    st.write("""We at Sudarshan AI Innovatives can cater to your personalised needs to and provide support as freelancers too.
                As patriotic citizens of our country it is our duty to make affordable AI powered software that could aid the economy,
                and society of Bharat.  
    """)

    # Add a Call to Action
    st.markdown(
        """
        ### Ready to Transform Your Business?
        Contact us today to discuss how we can help you harness the power of AI!
        """)

    # Add a button to navigate to the contact page
    if st.button("Contact Us"):
        st.session_state['selected_option'] = "Contact"  # Change to contact page

# Services page
elif options == "Services":
    st.subheader("Our Services")

    # LearnMate AI section
    col1, col2 = st.columns([1, 3])  # Create two columns for icon and description
    with col1:
        st.image("chemistry.png", width=100)  # Replace with your icon's path
    with col2:
        st.markdown("### LearnMate AI")
        st.write("""
            LearnMate AI is an EduTech app designed to provide personalized learning experiences using AI. 
            It helps students learn at their own pace, providing tailored resources and support.
            LearnMate AI gives student a complete learning experience to overcome any challenges they might face in Academics.
            Key Benefits : AI powered classrooms, Guaranteed Internships (paid), Guaranteed Industry Exposure Programs.
        """)

    # Add a download button for the flyer PDF
    st.markdown("#### Download Flyer")
    with open("LearnMate_Flyer.pdf", "rb") as file:  # Replace with your flyer PDF path
        st.download_button(
            label="Download Flyer",
            data=file,
            file_name="LearnMate_Flyer.pdf",
            mime="application/pdf"
        )

    st.markdown("---")  # Add a horizontal line for separation

    # Other services
    services = {
        "1. AI Solutions for Businesses": "Customized AI solutions that help your business stay ahead.",
        "2. Custom Software Development": "Tailored software to meet your specific requirements.",
        "3. Data Analysis and Visualization": "Transforming data into actionable insights."
    }
    for service, description in services.items():
        st.markdown(f"**{service}**: {description}")


# Contact page
elif options == "Contact":
    st.subheader("Get in Touch")
    st.write("Please fill out the form below to get in touch with us:")
    st.markdown("[Click here to access the contact form](https://docs.google.com/forms/d/e/1FAIpQLSdbkmm5d3WxnUulbMSYW5oxU84oeCaGJztPHdj3QP0Q6Dhx8g/viewform?usp=sf_link)")
    st.write("Feel free to contact us via email, phone, or social media.")
    st.write("📧 Email: sudarshanaiinnovatives@gmail.com")  # Replace with your email
    st.write("📞 Phone: +91-9321701102")  # Replace with your phone number
    st.write("🔗 [Instagram](https://www.instagram.com/sudarshan_ai_innovative)")  # Replace with your Instagram profile
    st.write("Sudarshan AI Innovatives will be very happy to work with you !!!")

# About page
elif options == "About":
    st.subheader("About the Founder")

    # Create two columns for image and text
    col1, col2 = st.columns([1, 3])

    # Display the image in the first column
    with col1:
        st.image("WhatsApp Image 2024-04015 at 2.07.54 AM.jpeg", width=250)  # Replace with your image path

    # Display information about the founder in the second column
    with col2:
        st.write(""" 
        Poornaya Pardeshi is the founder of Sudarshan AI Innovatives. At 17 with a strong background in AI and software development, 
        he has led numerous projects focused on bringing AI-driven innovation to businesses. A visionary in the AI 
        space, Poornaya continues to push boundaries in the field of technology. 
        """)

    # Education Section
    st.subheader("Education")
    st.write(""" 
    - Pursuing B.Eng. in Artificial Intelligence & Machine Learning, SIES GST [2024 - 2028]
        - Key Coursework: Artificial Intelligence, Machine Learning, Data Science, Software Engineering
    - High School (HSC), Don Bosco Senior Secondary School [2024] 
    """)

    # Certifications Section
    st.subheader("Certifications")
    st.write(""" 
    - Microsoft Industry Exposure Program, (2023)
    - AI for Data Scientists, Udemy (2024)
    - Fundamentals of Self Driving Cars, Udemy (2024) 
    """)

    # CV Download Section
    st.subheader("Download CV")
    st.write("You can download a full version of my CV using the link below:")

    # Add a download button for the CV
    with open("Founder_CV.pdf", "rb") as file:
        btn = st.download_button(
            label="Download CV",
            data=file,
            file_name="Founder_CV.pdf",
            mime="application/pdf"
        )

# Footer
st.markdown("<footer style='text-align: center;'>© 2024 Sudarshan AI Innovatives. All rights reserved.</footer>",
            unsafe_allow_html=True)
